# ================================
# Imports
# ================================

from decimal import Decimal

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db import transaction
from django.db.models import Sum, F

from .models import BankAccount, Transaction, Profile, UserActivity
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    TransferForm,
    DepositWithdrawForm,
)

# ================================
# Home
# ================================

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')


# ================================
# Register
# ================================

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            Profile.objects.get_or_create(
                user=user,
                defaults={'phone': form.cleaned_data.get('phone')}
            )

            BankAccount.objects.get_or_create(
                user=user,
                defaults={
                    'account_number': f"ACC{user.id:04d}",
                    'balance': Decimal("0.00")
                }
            )

            messages.success(request, "Account created successfully")
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'banking/register.html', {'form': form})


# ================================
# Login
# ================================

def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            UserActivity.objects.create(
                user=user,
                activity_type="Login"
            )

            return redirect('dashboard')

        messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


# ================================
# Logout
# ================================

def user_logout(request):

    if request.user.is_authenticated:

        UserActivity.objects.create(
            user=request.user,
            activity_type="Logout"
        )

        logout(request)

    return redirect('login')


# ================================
# Profile
# ================================

@login_required
def profile(request):

    profile_instance, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile_instance
        )

        if u_form.is_valid() and p_form.is_valid():

            u_form.save()
            p_form.save()

            messages.success(request, "Profile updated")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile_instance)

    return render(request, "banking/profile.html", {
        'u_form': u_form,
        'p_form': p_form
    })


# ================================
# Dashboard
# ================================

@login_required
def dashboard(request):

    account, created = BankAccount.objects.get_or_create(
        user=request.user,
        defaults={
            'account_number': f"ACC{request.user.id:04d}",
            'balance': Decimal("0.00")
        }
    )

    transactions = Transaction.objects.filter(
        account=account
    ).order_by('-date')[:5]

    activities = UserActivity.objects.filter(
        user=request.user
    ).order_by('-timestamp')[:5]

    total_deposits = Transaction.objects.filter(
        account=account,
        transaction_type='Deposit'
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal("0")

    total_withdrawals = Transaction.objects.filter(
        account=account,
        transaction_type='Withdraw'
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal("0")

    return render(request, "banking/dashboard.html", {
        'account': account,
        'transactions': transactions,
        'activities': activities,
        'total_deposits': total_deposits,
        'total_withdrawals': total_withdrawals
    })


# ================================
# Deposit
# ================================

@login_required
def deposit(request):

    form = DepositWithdrawForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        amount = form.cleaned_data['amount']
        account = request.user.bank_account

        if amount <= 0:
            messages.error(request, "Deposit amount must be greater than zero.")
            return render(request, 'banking/deposit.html', {'form': form})

        with transaction.atomic():
            BankAccount.objects.filter(pk=account.pk).update(
                balance=F('balance') + amount
            )
            Transaction.objects.create(
                account=account,
                amount=amount,
                transaction_type='Deposit'
            )

        messages.success(request, f"Successfully deposited ${amount:.2f} to your account.")
        return redirect('dashboard')

    return render(request, 'banking/deposit.html', {'form': form})


# ================================
# Withdraw
# ================================

@login_required
def withdraw(request):

    form = DepositWithdrawForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        amount = form.cleaned_data['amount']

        if amount <= 0:
            messages.error(request, "Withdrawal amount must be greater than zero.")
            return render(request, 'banking/withdraw.html', {'form': form})

        with transaction.atomic():
            # Re-read balance inside atomic block to prevent race conditions
            account = BankAccount.objects.select_for_update().get(
                user=request.user
            )

            if account.balance < amount:
                messages.error(request, f"Insufficient balance. Your balance is ${account.balance:.2f}.")
                return render(request, 'banking/withdraw.html', {'form': form})

            account.balance -= amount
            account.save(update_fields=['balance'])

            Transaction.objects.create(
                account=account,
                amount=amount,
                transaction_type='Withdraw'
            )

        messages.success(request, f"Successfully withdrew ${amount:.2f} from your account.")
        return redirect('dashboard')

    return render(request, 'banking/withdraw.html', {'form': form})


# ================================
# Transfer (BEST VERSION)
# ================================

@login_required
def transfer(request):

    form = TransferForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        to_account_number = form.cleaned_data['to_account']
        amount = form.cleaned_data['amount']
        remarks = form.cleaned_data.get('remarks', '')

        # Validate recipient exists
        try:
            receiver_account = BankAccount.objects.get(
                account_number=to_account_number
            )
        except BankAccount.DoesNotExist:
            messages.error(request, "Recipient account not found. Please check the account number.")
            return render(request, "banking/transfer.html", {"form": form})

        with transaction.atomic():
            # Re-read sender balance inside atomic block to prevent race conditions
            sender_account = BankAccount.objects.select_for_update().get(
                user=request.user
            )

            if sender_account.account_number == to_account_number:
                messages.error(request, "You cannot transfer money to your own account.")
                return render(request, "banking/transfer.html", {"form": form})

            if amount <= 0:
                messages.error(request, "Transfer amount must be greater than zero.")
                return render(request, "banking/transfer.html", {"form": form})

            if sender_account.balance < amount:
                messages.error(
                    request,
                    f"Insufficient balance. Your current balance is ${sender_account.balance:.2f}."
                )
                return render(request, "banking/transfer.html", {"form": form})

            # Deduct from sender
            sender_account.balance -= amount
            sender_account.save(update_fields=['balance'])

            # Credit to receiver (also lock for update)
            receiver_account = BankAccount.objects.select_for_update().get(
                pk=receiver_account.pk
            )
            receiver_account.balance += amount
            receiver_account.save(update_fields=['balance'])

            # Record outgoing transaction for sender
            Transaction.objects.create(
                account=sender_account,
                to_account=receiver_account,
                amount=amount,
                transaction_type="Transfer",
                remarks=remarks or f"Transfer to {receiver_account.account_number}"
            )

            # Record incoming transaction for receiver
            Transaction.objects.create(
                account=receiver_account,
                amount=amount,
                transaction_type="Deposit",
                remarks=f"Received from {sender_account.account_number}"
            )

        messages.success(
            request,
            f"Successfully transferred ${amount:.2f} to account {receiver_account.account_number}."
        )
        return redirect('dashboard')

    return render(request, "banking/transfer.html", {"form": form})
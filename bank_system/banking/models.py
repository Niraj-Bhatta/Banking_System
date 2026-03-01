from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Profile(models.Model):
    """
    Stores additional user information.
    Automatically linked to Django's User via OneToOneField.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class BankAccount(models.Model):
    """
    Stores user's bank account details.
    Each user has one account with unique account number.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='bank_account'
    )
    account_number = models.CharField(max_length=12, unique=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Ensure unique 12-digit account number
        if not self.account_number:
            while True:
                account_number = get_random_string(12, '0123456789')
                if not BankAccount.objects.filter(account_number=account_number).exists():
                    self.account_number = account_number
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

    class Meta:
        verbose_name = "Bank Account"
        verbose_name_plural = "Bank Accounts"

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=10, choices=[('Login','Login'),('Logout','Logout')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} at {self.timestamp}"
class Transaction(models.Model):
    """
    Stores transactions for each bank account.
    Supports Deposit, Withdraw, and Transfer.
    """
    TRANSACTION_CHOICES = [
        ('Deposit', 'Deposit'),
        ('Withdraw', 'Withdraw'),
        ('Transfer', 'Transfer'),
    ]

    account = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=100, blank=True)
    to_account = models.ForeignKey(
        BankAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='received_transactions'
    )

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.account.account_number}"

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['-date']  # most recent first
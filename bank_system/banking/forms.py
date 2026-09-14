from decimal import Decimal
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']

class TransferForm(forms.Form):
    to_account = forms.CharField(
        max_length=12,
        label="Recipient Account Number",
        widget=forms.TextInput(attrs={'placeholder': 'Enter 12-digit account number'})
    )
    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=Decimal('0.01'),
        label="Amount"
    )
    remarks = forms.CharField(
        max_length=100,
        required=False,
        label="Remarks (optional)",
        widget=forms.TextInput(attrs={'placeholder': 'Optional note'})
    )


class DepositWithdrawForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=Decimal('0.01'),
        label="Amount",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter amount', 'step': '0.01', 'min': '0.01'})
    )
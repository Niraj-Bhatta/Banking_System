from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, BankAccount
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import UserActivity

@receiver(post_save, sender=User)
def create_profile_and_account(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        BankAccount.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile_and_account(sender, instance, **kwargs):
    instance.profile.save()
    instance.bank_account.save()


from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import UserActivity

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    UserActivity.objects.create(user=user, activity_type='Login')

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    UserActivity.objects.create(user=user, activity_type='Logout')
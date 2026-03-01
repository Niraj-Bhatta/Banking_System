from django.contrib import admin
from .models import Profile, BankAccount, Transaction

admin.site.register(Profile)
admin.site.register(BankAccount)
admin.site.register(Transaction)
#registration of models to admin site
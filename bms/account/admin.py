from django.contrib import admin
from .models import SavingAccount, CheckingAccount

# Register your models here.
admin.site.register(SavingAccount)
admin.site.register(CheckingAccount)

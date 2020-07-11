from django.db import models
from branch.models import Branch
from customer.models import Customer
from djmoney.models.fields import MoneyField


# Create your models here.
class Account(models.Model):
    balance = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')
    date_opened = models.DateField(auto_now_add=True)
    branch = models.ForeignKey(Branch, related_name='%(class)ss', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='%(class)ss', on_delete=models.PROTECT)

    class Meta:
        abstract = True


class SavingAccount(Account):
    currency_type = models.CharField(max_length=16)
    interest_rate = models.FloatField()


class CheckingAccount(Account):
    overdraft = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')

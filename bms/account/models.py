from django.db import models
from branch.models import Branch, Staff
from customer.models import Customer
from djmoney.models.fields import MoneyField
from django.db.models import UniqueConstraint
import datetime


# Create your models here.
class Account(models.Model):
    balance = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')
    date_opened = models.DateField(default=datetime.date.today, blank=True)
    branch = models.ForeignKey(Branch, related_name='%(class)ss', on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, related_name='%(class)ss', on_delete=models.PROTECT)
    manager = models.ForeignKey(Staff, related_name='managed_%(class)ss', on_delete=models.PROTECT, null=True)

    class Meta:
        abstract = True
        constraints = [
            UniqueConstraint(
                fields=['customer', 'branch'],
                name='unique_branch_customer_%(class)s',
            ),
        ]


class SavingAccount(Account):
    interest_rate = models.FloatField()


class CheckingAccount(Account):
    overdraft = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')

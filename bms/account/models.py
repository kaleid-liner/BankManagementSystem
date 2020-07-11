from django.db import models
from branch.models import Branch
from customer.models import Customer


# Create your models here.
class Account(models.Model):
    balance = models.FloatField()
    date_opened = models.DateField(auto_now_add=True)
    branch = models.ForeignKey(Branch, related_name='%(class)ss', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='%(class)ss', on_delete=models.PROTECT)

    class Meta:
        abstract = True


class SavingAccount(Account):
    currency_type = models.CharField(max_length=16)
    interest_rate = models.FloatField()


class CheckingAccount(Account):
    overdraft = models.FloatField()

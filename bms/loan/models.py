from django.db import models
from branch.models import Branch
from djmoney.models.fields import MoneyField


# Create your models here.
class Loan(models.Model):
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class LoanPayment(models.Model):
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')
    date = models.DateField(auto_now_add=True)
    loan = models.ForeignKey(Loan, related_name='payments', on_delete=models.CASCADE)

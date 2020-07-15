from django.db import models
from branch.models import Branch
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from customer.models import Customer
import datetime


# Create your models here.
class Loan(models.Model):
    amount = MoneyField(
        max_digits=19,
        decimal_places=4,
        default_currency='CNY',
        validators=[
            MinMoneyValidator(0),
        ]
    )
    branch = models.ForeignKey(Branch, related_name='loans', on_delete=models.CASCADE)
    customers = models.ManyToManyField(Customer, related_name='loans')

    @property
    def status(self):
        released = self.released
        if released == 0:
            return 'empty'
        elif released >= self.amount:
            return 'full'
        else:
            return 'half'

    @property
    def released(self):
        return sum(payment.amount for payment in self.payments.all())

    @property
    def remained(self):
        released = self.released
        if released == 0:
            return self.amount
        else:
            return self.amount - released


class LoanPayment(models.Model):
    amount = MoneyField(
        max_digits=19,
        decimal_places=4,
        default_currency='CNY',
        validators=[
            MinMoneyValidator(0),
        ]
    )
    date = models.DateField(default=datetime.date.today, blank=True)
    loan = models.ForeignKey(Loan, related_name='payments', on_delete=models.CASCADE)

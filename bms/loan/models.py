from django.db import models
from branch.models import Branch
from djmoney.models.fields import MoneyField
from customer.models import Customer


# Create your models here.
class Loan(models.Model):
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
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


class LoanPayment(models.Model):
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY')
    date = models.DateField(auto_now_add=True)
    loan = models.ForeignKey(Loan, related_name='payments', on_delete=models.CASCADE)

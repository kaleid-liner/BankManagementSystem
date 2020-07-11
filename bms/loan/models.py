from django.db import models
from branch.models import Branch


# Create your models here.
class Loan(models.Model):
    amount = models.FloatField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class LoanPayment(models.Model):
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    loan = models.ForeignKey(Loan, related_name='payments', on_delete=models.CASCADE)

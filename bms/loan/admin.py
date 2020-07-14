from django.contrib import admin
from .models import Loan, LoanPayment

# Register your models here.
admin.site.register(Loan)
admin.site.register(LoanPayment)

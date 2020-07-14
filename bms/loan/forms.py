from django import forms
from .models import Loan, LoanPayment


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = [
            'amount',
            'branch',
            'customers',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class LoanPaymentForm(forms.ModelForm):
    class Meta:
        model = LoanPayment
        fields = [
            'amount',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })

from django import forms
from . import models


class CheckingAccountForm(forms.ModelForm):
    class Meta:
        model = models.CheckingAccount
        fields = [
            'balance',
            'branch',
            'manager',
            'overdraft',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class SavingAccountForm(forms.ModelForm):
    class Meta:
        model = models.SavingAccount
        fields = [
            'balance',
            'branch',
            'manager',
            'interest_rate',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })

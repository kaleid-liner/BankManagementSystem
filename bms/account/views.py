from django.shortcuts import render
from .models import SavingAccount, CheckingAccount
from django.views import generic
from customer.models import Customer
from django.urls import reverse, reverse_lazy


# Create your views here.
class AccountListView(generic.TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saving_account_list'] = SavingAccount.objects.all()
        context['checking_account_list'] = CheckingAccount.objects.all()
        return context


class BaseAccountCreateView(generic.CreateView):
    template_name = 'account/create.html'
    fields = [
        'balance',
        'branch',
        'manager',
    ]
    account_type = None

    def dispatch(self, request, *args, **kwargs):
        self.customer = Customer.objects.get(pk=self.kwargs['customer_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_type'] = self.account_type
        context['customer'] = self.customer

        return context

    def form_valid(self, form):
        customer = self.customer
        form.instance.customer = customer
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:update', args=(self.customer.pk,))


class CheckingAccountCreateView(BaseAccountCreateView):
    model = CheckingAccount
    fields = [
        'balance',
        'branch',
        'manager',
        'overdraft',
    ]
    account_type = 'checking'


class SavingAccountCreateView(BaseAccountCreateView):
    model = SavingAccount
    fields = [
        'balance',
        'branch',
        'manager',
        'interest_rate',
    ]
    account_type = 'saving'


class SavingAccountDeleteView(generic.DeleteView):
    model = SavingAccount
    success_url = reverse_lazy('account:index')
    template_name = 'account/delete.html'


class CheckingAccountDeleteView(generic.DeleteView):
    model = CheckingAccount
    success_url = reverse_lazy('account:index')
    template_name = 'account/delete.html'


class AccountUpdateView(generic.UpdateView):
    template_name = 'account/create.html'
    account_type = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['account_type'] = self.account_type
        return context

    def get_success_url(self):
        return self.request.path


class SavingAccountUpdateView(AccountUpdateView):
    model = SavingAccount
    fields = [
        'balance',
        'branch',
        'manager',
        'interest_rate',
    ]
    account_type = 'saving'


class CheckingAccountUpdateView(AccountUpdateView):
    model = CheckingAccount
    fields = [
        'balance',
        'branch',
        'manager',
        'overdraft',
    ]
    account_type = 'checking'

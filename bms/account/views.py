from django.shortcuts import render
from .models import SavingAccount, CheckingAccount
from django.views import generic
from customer.models import Customer
from django.urls import reverse, reverse_lazy
from .forms import CheckingAccountForm, SavingAccountForm
from chartjs.views.lines import BaseLineChartView
from django.db.models import Sum
from branch.models import Branch


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
    account_type = 'checking'
    form_class = CheckingAccountForm


class SavingAccountCreateView(BaseAccountCreateView):
    account_type = 'saving'
    form_class = SavingAccountForm


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
    form_class = SavingAccountForm
    account_type = 'saving'


class CheckingAccountUpdateView(AccountUpdateView):
    model = CheckingAccount
    form_class = CheckingAccountForm
    account_type = 'checking'


class SavingAccountChartView(BaseLineChartView):
    def dispatch(self, request, *args, **kwargs):
        self.step = self.request.GET.get('step', default='year')
        self.type = self.request.GET.get('type', default='amount')
        self.accounts = SavingAccount.objects.all()
        self.branches = Branch.objects.all()

        min_year = SavingAccount.objects.earliest('date_opened').date_opened.year
        max_year = SavingAccount.objects.latest('date_opened').date_opened.year
        self.years = list(range(min_year, max_year + 1))

        return super().dispatch(request, *args, **kwargs)

    def get_labels(self):
        if self.step == 'month':
            return [
                '一月',
                '二月',
                '三月',
                '四月',
                '五月',
                '六月',
                '七月',
                '八月',
                '九月',
                '十月',
                '十一月',
                '十二月',
            ]
        elif self.step == 'season':
            return [
                '第一季度',
                '第二季度',
                '第三季度',
                '第四季度',
            ]
        else:
            return self.years

    def get_providers(self):
        return [branch.name for branch in self.branches]

    def get_data_for_branch(self, branch):
        queryset = branch.savingaccounts
        raw_data_list = []
        if self.step == 'month':
            for month in range(1, 13):
                raw_data = queryset.filter(date_opened__month=month)
                raw_data_list.append(raw_data)
        elif self.step == 'season':
            seasons = [
                (1, 3),
                (4, 6),
                (7, 9),
                (10, 12),
            ]
            for min_month, max_month in seasons:
                raw_data = queryset.filter(date_opened__month__gte=min_month,
                                           date_opened__month__lte=max_month)
                raw_data_list.append(raw_data)
        else:
            for year in self.years:
                raw_data = queryset.filter(date_opened__year=year)
                raw_data_list.append(raw_data)

        data = []
        for raw_data in raw_data_list:
            if self.type == 'amount':
                amount = raw_data.aggregate(Sum('balance'))
                data.append(amount['balance__sum'] or 0)
            else:
                count = raw_data.count()
                data.append(count)

        return data

    def get_data(self):
        data = []
        for branch in self.branches:
            data.append(self.get_data_for_branch(branch))
        return data

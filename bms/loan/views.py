from django.shortcuts import render
from .models import Loan, LoanPayment
from django.views import generic
from django.urls import reverse
from .forms import LoanForm, LoanPaymentForm
from chartjs.views.lines import BaseLineChartView
from branch.models import Branch
from django.db.models import Sum


# Create your views here.
class LoanListCreateView(generic.CreateView):
    form_class = LoanForm
    template_name = 'loan/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loan_list'] = Loan.objects.all()
        return context

    def get_success_url(self):
        return reverse('loan:index')


class LoanDeleteView(generic.DeleteView):
    model = Loan
    template_name = 'loan/delete.html'

    def get_success_url(self):
        return reverse('loan:index')


class LoanPaymentCreateView(generic.CreateView):
    form_class = LoanPaymentForm

    def get_success_url(self):
        return reverse('loan:index')


class LoanDetailPayView(generic.CreateView):
    form_class = LoanPaymentForm
    template_name = 'loan/detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.loan = Loan.objects.get(pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loan'] = self.loan

        return context

    def form_valid(self, form):
        loan = self.loan
        form.instance.loan = loan
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('loan:detail', args=(self.loan.pk,))


class LoanChartView(BaseLineChartView):
    def dispatch(self, request, *args, **kwargs):
        self.step = self.request.GET.get('step', default='year')
        self.type = self.request.GET.get('type', default='amount')
        self.loans = Loan.objects.all()
        self.branches = Branch.objects.all()

        try:
            min_year = LoanPayment.objects.earliest('date').date.year
            max_year = LoanPayment.objects.latest('date').date.year
        except:
            min_year = max_year = 0
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
        queryset = LoanPayment.objects.filter(loan__branch=branch)
        raw_data_list = []
        if self.step == 'month':
            for month in range(1, 13):
                raw_data = queryset.filter(date__month=month)
                raw_data_list.append(raw_data)
        elif self.step == 'season':
            seasons = [
                (1, 3),
                (4, 6),
                (7, 9),
                (10, 12),
            ]
            for min_month, max_month in seasons:
                raw_data = queryset.filter(date__month__gte=min_month,
                                           date__month__lte=max_month)
                raw_data_list.append(raw_data)
        else:
            for year in self.years:
                raw_data = queryset.filter(date__year=year)
                raw_data_list.append(raw_data)

        data = []
        for raw_data in raw_data_list:
            if self.type == 'amount':
                amount = raw_data.aggregate(Sum('amount'))
                data.append(amount['amount__sum'] or 0)
            else:
                count = raw_data.count()
                data.append(count)

        return data

    def get_data(self):
        data = []
        for branch in self.branches:
            data.append(self.get_data_for_branch(branch))
        return data

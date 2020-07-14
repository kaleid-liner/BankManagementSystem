from django.shortcuts import render
from .models import Loan, LoanPayment
from django.views import generic
from django.urls import reverse
from .forms import LoanForm, LoanPaymentForm


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

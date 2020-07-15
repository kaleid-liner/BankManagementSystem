from django.shortcuts import render
from django.views import generic
from .models import Customer
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest


# Create your views here.
class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'customer/index.html'


class CustomerCreateView(generic.CreateView):
    model = Customer
    template_name = 'customer/create.html'
    fields = [
        'card_id',
        'name',
        'phone_number',
        'address',
        'contact_name',
        'contact_phone_number',
        'contact_email',
        'contact_relationship',
    ]
    success_url = reverse_lazy('customer:index')


class CustomerDeleteView(generic.DeleteView):
    model = Customer
    template_name = 'customer/delete.html'
    success_url = reverse_lazy('customer:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == 'locked':
            return HttpResponseBadRequest('你不能删除此账户')
        return super().delete(request, *args, **kwargs)


class CustomerUpdateView(generic.UpdateView):
    model = Customer
    template_name = 'customer/create.html'
    fields = [
        'card_id',
        'name',
        'phone_number',
        'address',
        'contact_name',
        'contact_phone_number',
        'contact_email',
        'contact_relationship',
    ]
    success_url = reverse_lazy('customer:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['saving_account_list'] = self.object.savingaccounts.all()
        context['checking_account_list'] = self.object.checkingaccounts.all()
        context['loan_list'] = self.object.loans.all()

        return context

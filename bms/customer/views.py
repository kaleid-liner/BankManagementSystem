from django.shortcuts import render
from django.views import generic
from .models import Customer
from django.urls import reverse_lazy


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

    def clean_card_id(self):
        return self.initial['card_id']

    def clean_name(self):
        return self.initial['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context

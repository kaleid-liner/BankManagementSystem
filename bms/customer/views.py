from django.shortcuts import render
from django.views import generic
from .models import Customer


# Create your views here.
class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'customer/index.html'

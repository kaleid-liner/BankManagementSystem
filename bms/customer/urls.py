from django.urls import path, include
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='index'),
    path('create', views.CustomerCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.CustomerDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='update'),
]

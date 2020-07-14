from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.AccountListView.as_view(), name='index'),
    path('checking/create/<int:customer_id>', views.CheckingAccountCreateView.as_view(), name='checking_create'),
    path('saving/create/<int:customer_id>', views.SavingAccountCreateView.as_view(), name='saving_create'),
    path('checking/delete/<int:pk>', views.CheckingAccountDeleteView.as_view(), name='checking_delete'),
    path('saving/delete/<int:pk>', views.SavingAccountDeleteView.as_view(), name='saving_delete'),
    path('checking/update/<int:pk>', views.CheckingAccountUpdateView.as_view(), name='checking_update'),
    path('saving/update/<int:pk>', views.SavingAccountUpdateView.as_view(), name='saving_update'),
    path('saving/chartjs', views.SavingAccountChartView.as_view(), name='saving_chart')
]

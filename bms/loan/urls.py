from django.urls import path
from . import views

app_name = 'loan'

urlpatterns = [
    path('', views.LoanListCreateView.as_view(), name='index'),
    path('delete/<int:pk>', views.LoanDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', views.LoanDetailPayView.as_view(), name='detail'),
]

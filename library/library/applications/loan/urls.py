from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('loans/',views.LoanRegister.as_view(), name="loans"),
    path('loans/multiple-add',views.MultipleAddLoan.as_view(), name="multiple_loans"),

]
# Django
from django.urls import include, re_path, path

# Local
from . import views

app_name = 'sale_app'

urlpatterns = [
    path(
        'api/sale/report',
        views.SalesReportList.as_view(),
        name='sale-report'
    ),
    path(
        'api/sale/create',
        views.SaleRegister.as_view(),
        name='sale-register'
    ),
    path(
        'api/sale/add',
        views.SaleRegister2.as_view(),
        name='sale-add'
    ),
]

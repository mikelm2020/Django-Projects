# Django
from django.urls import include, re_path, path

# Local
from . import views

app_name='product_app'

urlpatterns = [
    path(
        'api/product/by-user/',
        views.ListProductUser.as_view(),
        name='product-product_by_user'
    ),
    path(
        'api/product/with-stock/',
        views.ListProductsStock.as_view(),
        name='product-product_with_stock'
    ),
    path(
        'api/product/by-gender/<gender>/',
        views.ListProductGender.as_view(),
        name='product-product_by_gender'
    ),
    path(
        'api/product/filter/',
        views.FilterProducts.as_view(),
        name='product-filter'
    ),
]

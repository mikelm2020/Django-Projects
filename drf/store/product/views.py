from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import render
from .serializers import ProductSerializer

from .models import Product


class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # recuperating user
        user = self.request.user
        return Product.objects.products_by_user(user)


class ListProductsStock(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Product.objects.products_with_stock()


class ListProductGender(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        gender_param = self.kwargs["gender"]

        return Product.objects.products_by_gender(gender_param)


class FilterProducts(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        male_param = self.request.query_params.get("man", None)
        female_param = self.request.query_params.get("woman", None)
        name_param = self.request.query_params.get("name", None)

        return Product.objects.filter_products(
            man=male_param, woman=female_param, name=name_param
        )

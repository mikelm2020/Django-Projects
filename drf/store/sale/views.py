from django.shortcuts import render
from django.utils import timezone

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from .models import Sale, SaleDetail, Product

from .serializers import (
    SaleReportSerializer,
    SaleProcessSerializer,
    SaleProcessSerializer2,
)


class SalesReportList(ListAPIView):
    serializer_class = SaleReportSerializer

    def get_queryset(self):
        return Sale.objects.all()


class SaleRegister(CreateAPIView):
    serializer_class = SaleProcessSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = SaleProcessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sale = Sale.objects.create(
            date_sale=timezone.now(),
            amount=0,
            count=0,
            type_invoce=serializer.validated_data["type_invoce"],
            type_payment=serializer.validated_data["type_payment"],
            adreese_send=serializer.validated_data["adreese_send"],
            user=self.request.user,
        )
        # Variables for sales
        amount = 0  # Total amount of the sale
        count = 0

        # We recuperate products of rhe sale
        products = serializer.validated_data["products"]
        sales_detail = []
        for product in products:
            prod = Product.objects.get(id=product["pk"])
            sale_detail = SaleDetail(
                sale=sale,
                product=prod,
                count=product["count"],
                price_purchase=prod.price_purchase,
                price_sale=prod.price_sale,
            )
            amount += prod.price_sale * product["count"]
            count += product["count"]
            sales_detail.append(sale_detail)

        sale.amount = amount
        sale.count = count
        sale.save()

        SaleDetail.objects.bulk_create(sales_detail)

        return Response({"msj": "Venta exitosa"})


class SaleRegister2(CreateAPIView):
    serializer_class = SaleProcessSerializer2
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = SaleProcessSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)

        sale_object = Sale.objects.create(
            date_sale=timezone.now(),
            amount=0,
            count=0,
            type_invoce=serializer.validated_data["type_invoce"],
            type_payment=serializer.validated_data["type_payment"],
            adreese_send=serializer.validated_data["adreese_send"],
            user=self.request.user,
        )
        # Variables for sales
        total_amount = 0  # Total amount of the sale
        total_count = 0

        # We recuperate products of rhe sale
        products_list = Product.objects.filter(
            id__in=serializer.validated_data["products"]
        )

        counts_list = serializer.validated_data["counts"]
        sales_detail = []
        for product_element, count_element in zip(products_list, counts_list):
            sale_detail = SaleDetail(
                sale=sale_object,
                product=product_element,
                count=count_element,
                price_purchase=product_element.price_purchase,
                price_sale=product_element.price_sale,
            )
            total_amount += product_element.price_sale * count_element
            total_count += count_element
            sales_detail.append(sale_detail)

        sale_object.amount = total_amount
        sale_object.count = total_count
        sale_object.save()

        SaleDetail.objects.bulk_create(sales_detail)

        return Response({"msj": "Venta exitosa"})

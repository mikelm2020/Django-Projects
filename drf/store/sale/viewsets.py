from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.utils import timezone
from django.shortcuts import get_object_or_404

from product.models import Product
from .serializers import SaleProcessSerializer2, SaleReportSerializer

from .models import Sale, SaleDetail


class SalesViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    queryset = Sale.objects.all()

    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve' :
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all()

        serializer = SaleReportSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
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

    def retrieve(self, request, pk=None):
        sale_object = get_object_or_404(Sale.objects.all(), pk=pk)
        serializer = SaleReportSerializer(sale_object)
        return Response(serializer.data)

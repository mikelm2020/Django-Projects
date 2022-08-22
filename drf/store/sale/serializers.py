from itertools import product
from rest_framework import serializers
from .models import Sale, SaleDetail, Product


class SaleReportSerializer(serializers.ModelSerializer):
    """Serializer for see the sales in detail"""

    products = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            "id",
            "date_sale",
            "amount",
            "count",
            "type_invoce",
            "cancelado",
            "type_payment",
            "state",
            "adreese_send",
            "anulate",
            "user",
            "products",
        )

    def get_products(self, obj):
        query = SaleDetail.objects.products_by_sale(obj.id)
        products_serializered = SaleDetailProductSerializer(query, many=True).data
        return products_serializered


class SaleDetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = ("id", "sale", "product", "count", "price_purchase", "price_sale")


class ProductDetailSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class SaleProcessSerializer(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    products = ProductDetailSerializer(many=True)


class SaleProcessSerializer2(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    products = ArrayIntegerSerializer()
    counts = ArrayIntegerSerializer()

    def validate(self, data):
        if data["type_payment"] not in ("0", "1", "2"):
            raise serializers.ValidationError("Ingrese un tipo de pago correcto")

        return data

    def validate_type_invoce(self, value):
        if value not in ("0", "3", "4"):
            raise serializers.ValidationError("Ingrese un valor correcto")

        return value

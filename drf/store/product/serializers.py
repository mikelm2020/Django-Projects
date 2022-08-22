from rest_framework import serializers, pagination
from rest_framework.response import Response

from .models import Product, Colors


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ("color",)


class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "man",
            "woman",
            "weight",
            "price_purchase",
            "price_sale",
            "main_image",
            "image1",
            "image2",
            "image3",
            "colors",
            "video",
            "stok",
            "num_sales",
            "user_created",
        )


class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 50


class ProductSerializerViewSet(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    
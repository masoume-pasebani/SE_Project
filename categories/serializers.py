from rest_framework import serializers
from categories.models import Category
from product.serializers import ProductSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    category_detail = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = ['id', 'name', 'category_detail']


class CategorySerializer(serializers.ModelSerializer):
    category_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name','is_active', 'category_products']


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'is_active']
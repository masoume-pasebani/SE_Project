from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filters import ProductFilter
from .models import Product, Brand
from .pagination import Pagination
from .seializers import ProductDetailSerializer, BrandListSerializer, BrandDetailSerializer, ProductListSerializer


class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['flag', 'brand','price']
    ordering_fields = ['price']
    filterset_class = ProductFilter


class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()


class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
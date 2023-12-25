from rest_framework import generics
from rest_framework.permissions import AllowAny

from categories.models import Category
from categories.serializers import CategorySerializer, CategoryCreateSerializer, CategoryListSerializer
from rest_framework import status


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryListSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [AllowAny]


class CategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

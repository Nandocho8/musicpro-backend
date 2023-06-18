from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class Type_Viewset(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Type_Serializers

class Category_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Category_Serializers

class Subcategory_Viewset(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Subcategory_Serializers


class Brand_Viewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Brand_Serializers

class Product_Viewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Product_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'subcategory__name', 'subcategory__category__name','subcategory__category__type__name']
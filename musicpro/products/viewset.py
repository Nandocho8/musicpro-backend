from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import Product_Filter


class Type_Viewset(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Type_Serializers
    http_method_names = ['get', 'head']


class Category_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Category_Serializers
    http_method_names = ['get', 'head']


class Subcategory_Viewset(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Subcategory_Serializers
    http_method_names = ['get', 'head']


class Brand_Viewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Brand_Serializers
    http_method_names = ['get', 'head']


class Product_Viewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Product_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = Product_Filter
    http_method_names = ['get', 'head']


class Stock_Viewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Stock_Serializers

class Product_Stock_Viewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Product_Stock_Serializers
from rest_framework import viewsets, permissions

from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from .filters import Order_Filter


class Payment_method_Viewset(viewsets.ModelViewSet):
    queryset = Payment_method.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Payment_method_Serializers


class Payment_Viewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Payment_Serializers


class Order_Viewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Order_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = Order_Filter


class Detail_Order_Viewset(viewsets.ModelViewSet):
    queryset = Detail_Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Detail_Order_Serializers


class Sale_Viewset(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Sale_Serializers



from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import Comuna_Filter


class User_Viewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers
    http_method_names = ['get', 'post', 'patch', 'head']


class Region_Viewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Region_Serializers
    http_method_names = ['get']


class Comuna_Viewset(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Comuna_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = Comuna_Filter
    http_method_names = ['get']


class Store_Viewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Store_Serializers
    http_method_names = ['get']

# class Client_Viewset(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = Client_Serializers


# class Admin_Viewset(viewsets.ModelViewSet):
#     queryset = Admin.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = Admin_Serializers

# class Grocer_Viewset(viewsets.ModelViewSet):
#     queryset = Grocer.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = Grocer_Serializers


# class Salesman_Viewset(viewsets.ModelViewSet):
#     queryset = Salesman.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = Salesman_Serializers
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class User_Viewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers
    http_method_names = ['get', 'post', 'put', 'patch', 'head']


class Region_Viewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Region_Serializers


class Comuna_Viewset(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Comuna_Serializers


class Store_Viewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Store_Serializers

class Client_Viewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Client_Serializers


class Admin_Viewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Admin_Serializers

class Grocer_Viewset(viewsets.ModelViewSet):
    queryset = Grocer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Grocer_Serializers


class Salesman_Viewset(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Salesman_Serializers
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
    serializer_class = Region_Serializer


class Comuna_Viewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Comuna_Serializer


class Store_Viewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Store_Serializer

from rest_framework import viewsets, permissions
from .models import Type
from .serializers import Type_Serializers

class Type_Viewset(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Type_Serializers
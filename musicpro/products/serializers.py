from rest_framework import serializers
from .models import Type, Category, Subcategory

class Type_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = "__all__"
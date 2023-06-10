from rest_framework import serializers
from .models import *

class Type_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = "__all__"


class Category_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class Subcategory_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = "__all__"


class Brand_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class Product_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

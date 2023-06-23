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

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'category': instance.category.name,
            'type': instance.category.type.name
        }


class Brand_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class Product_Serializers(serializers.ModelSerializer):
    pass

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'price': instance.price,
            "image": instance.image,
            "subcategory": instance.subcategory.name,
            "category": instance.subcategory.category.name,
            "type": instance.subcategory.category.type.name,
            "brand": instance.brand.name
        }


class Stock_Serializers(serializers.ModelSerializer):

    # store = serializers.StringRelatedField()

    class Meta:
        model = Stock
        fields = ['store', 'quantity']


class Product_Stock_Serializers(serializers.ModelSerializer):

    stocks = Stock_Serializers(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'image', 'subcategory', 'brand', 'stocks']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_name = instance.subcategory.category.name
        representation['category'] = category_name
        stocks = self.get_stocks(instance)
        representation['stocks'] = stocks
        subcategory_name = instance.subcategory.name
        representation['subcategory'] = subcategory_name
        brand_name = instance.brand.name
        representation['brand'] = brand_name
        return representation

    def get_stocks(self, obj):
        stocks = Stock.objects.filter(product=obj)
        return Stock_Serializers(stocks, many=True).data

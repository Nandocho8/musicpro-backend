from rest_framework import serializers
from .models import *


class Payment_method_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Payment_method
        fields = '__all__'


class Payment_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class Sale_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class Order_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Detail_Order_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Detail_Order
        fields = '__all__'

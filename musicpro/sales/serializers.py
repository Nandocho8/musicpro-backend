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


class Detail_Order_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Detail_Order
        fields = '__all__'

    def to_representation(self,instance):
        return {
            "id": instance.id,
            "product_id": instance.product.id,
            "product_name": instance.product.name,
            "store" : instance.store.name_store,
            "quantity" : instance.quantity
        }


class Order_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class Order_With_Details_Serializers(serializers.ModelSerializer):
    detail_order  = Detail_Order_Serializers(many=True)

    class Meta:
        model = Order
        fields = ['id', 'total_order', 'status' , 'detail_order']

    def to_representation(self,instance):
        representation = super().to_representation(instance)
        detail_order  = self.get_detail_order(instance)
        representation['detail_order'] = detail_order 
        total_order = instance.total_order
        formatted_total = "{:,.0f}".format(total_order).replace(",", ".")
        representation['total'] = f"CLP {formatted_total}"

        return representation

    def get_detail_order(self, obj):
        detail_order  = Detail_Order.objects.filter(order=obj)
        return Detail_Order_Serializers(detail_order , many=True).data


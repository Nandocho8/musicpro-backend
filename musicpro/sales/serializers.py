from  rest_framework import serializer
from  .models import *


class Region_Serializers(serializer.ModelSerializer):
    class Meta:
        model = Region
        field = '__all__'

class Comuna_Serializers(serializer.ModelSerializer):
    class Meta:
        model = Comuna
        field = '__all__'

class Store_Serializers(serializer.ModelSerializer):
    class Meta:
        model = Store
        field = '__all__'
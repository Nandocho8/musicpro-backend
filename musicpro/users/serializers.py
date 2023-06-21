from rest_framework import serializers
from .models import *


class User_Serializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',
                  'type_user', 'name_user', 'last_name_user')
        read_only_fields = ('id', )

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['username'],
            username=validated_data['username'],
            type_user=validated_data['type_user'],
            name_user=validated_data['name_user'],
            last_name_user=validated_data['last_name_user'],
            is_active=1,
        )
        user.set_password(validated_data['password'])
        user.save()

        return User

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class Region_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = "__all__"


class Comuna_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Comuna
        fields = "__all__"


class Store_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = "__all__"

from rest_framework import serializers
from .models import *

from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut[:-1])))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11



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


class Client_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('user_main_id', )

class Admin_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = '__all__'
        read_only_fields = ('user_main_id', )

class Salesman_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Salesman
        fields = '__all__'
        read_only_fields = ('user_main_id', )

class Grocer_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Grocer
        fields = '__all__'
        read_only_fields = ('user_main_id', )
class User_Serializers(serializers.ModelSerializer):
    client = Client_Serializers(required=False)
    admin = Admin_Serializers(required=False)
    salesman = Salesman_Serializers(required=False)
    grocer = Grocer_Serializers(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'rut', 'email', 'password', 'type_user', 'name_user', 'last_name_user', 'client','admin', 'salesman', 'grocer')
        read_only_fields = ('id', )

    def create(self, validated_data):
        # Funcion para crear usuario con las especificaciones dadas
        def create_user(email , username , rut , type_user,  name_user, last_name_user, password):

            user = User.objects.create(
                email=email,
                username=username,
                rut=rut,
                type_user=type_user,
                name_user=name_user,
                last_name_user=last_name_user,
                is_active=1,
            )
            user.set_password(password)
            user.save()
            return user

        # Extraigo datos para los tipos de user 
        email = validated_data['email']
        username = validated_data['username']
        rut = validated_data['rut']

        type_user = validated_data['type_user']
        name_user = validated_data['name_user']
        last_name_user = validated_data['last_name_user']
        password = validated_data['password']

        admin_data = validated_data.pop('admin', {})
        salesman_data = validated_data.pop('salesman', {})
        grocer_data = validated_data.pop('grocer', {})
        client_data = validated_data.pop('client', {})

        # Validar rut
        if int(rut[-1:]) != digito_verificador(rut):
            raise serializers.ValidationError(f'El rut {rut} es invalido')
        # Verificar si ya existe un hijo correspondiente al tipo de usuario
        if type_user not in ['A','S','G','C']:
            raise serializers.ValidationError('Ingrese un tipo de datos validos')            
        elif type_user == 'A' and Admin.objects.filter(user_main_id__username=validated_data['username']).exists():
            raise serializers.ValidationError('Administrador ya registrado en el sistema')
        elif type_user == 'S' and Salesman.objects.filter(user_main_id__username=validated_data['username']).exists():
            raise serializers.ValidationError('Vendedor ya registrado en el sistema')
        elif type_user == 'G' and Grocer.objects.filter(user_main_id__username=validated_data['username']).exists():
            raise serializers.ValidationError('Bodeguero ya registrado en el sistema')
        elif type_user == 'C' and Grocer.objects.filter(user_main_id__username=validated_data['username']).exists():
            raise serializers.ValidationError('Cliente ya registrado en el sistema')
        
        # Creacion de usuario por tipo

        if type_user == 'A':
            # username y email sera “nombre + tres primeras letras de su apellido paterno” y su contraseña es su rut,
            username = name_user + last_name_user[:3]
            user = create_user(username , username , rut , type_user,  name_user, last_name_user, rut)
            user_son = Admin.objects.create(user_main_id=user, **admin_data)
        elif type_user == 'S':
            user = create_user(email , username , rut , type_user,  name_user, last_name_user, password)
            user_son = Salesman.objects.create(user_main_id=user, **salesman_data)
        elif type_user == 'G':
            user = create_user(email , username , rut , type_user,  name_user, last_name_user, password)
            user_son = Grocer.objects.create(user_main_id=user, **grocer_data)
        elif type_user == 'C':
            user = create_user(email , email , rut , type_user,  name_user, last_name_user, password)
            print(f'\n\n\n\n{user}\n\n\n\n')
            print(client_data)
            user_son = Client.objects.create(user_main_id=user, **client_data)

        return user
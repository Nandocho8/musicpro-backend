from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Region(models.Model):
    name_region = models.CharField('name_region' , max_length=60, null=False)

    def __str__(self):
        return f'Region de {self.name_region}'

class Comuna(models.Model):
    name_comuna = models.CharField('name_comuna' , max_length=60, null=False)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return f'Comuna de {self.name_comuna}'

class Store(models.Model):
    name_store = models.CharField('name_store' , max_length=60, null=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Store {self.name_store}'

class User(AbstractUser):
    ACCOUNTER = 'O'
    ADMIN = 'A'
    CLIENT = 'C'
    GROCER = 'G'
    SALESMAN = 'S'
    TYPE_USER = [
        (ACCOUNTER, 'O'),
        (ADMIN, 'A'),
        (CLIENT, 'C'),
        (GROCER, 'G'),
        (SALESMAN, 'S'),
    ]

    username = models.CharField('username', blank=False, unique=True, max_length=60)
    email = models.EmailField("email", blank=False, null=False, unique=True)
    password = models.CharField(
        "password", max_length=30, blank=False, null=False)
    type_user = models.CharField("type_user", max_length=1, choices=TYPE_USER, default=CLIENT)
    name_user = models.CharField('name_user', blank=False, null=False, max_length=25)
    last_name_user = models.CharField('last_name_user', blank=False, null=False, max_length=25)
    is_active = models.BooleanField("is_active", default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.type_user} {self.name_user} {self.last_name_user}'

class Client(models.Model):
    address = models.CharField('address_cliente', max_length=50, blank=False, null=False)
    number_address = models.IntegerField('number_address',blank=False,null=False)    
    additional_address_info = models.CharField('additional_info',blank=True, max_length=50, null=False)
    user_main_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f'{self.user}'

class Admin(models.Model):
    user_main_id = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Salesman(models.Model):
    user_main_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f'{self.user}'

class Grocer(models.Model):
    user_main_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f'{self.user}'
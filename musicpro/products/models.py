from django.db import models
from users.models import *
# Create your models here.

class Type(models.Model):
    name = models.CharField('type', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('category', max_length=50, blank=False, null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField('subcategory', max_length=50, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

class Brand(models.Model):
    name = models.CharField('brand', max_length=50, blank=False, null=False)

class Product(models.Model):
    name = models.CharField('product', max_length=50, blank=False, null=False)
    description = models.TextField('description', blank=False, null=False)
    price = models.IntegerField('price',  blank=False, null=False)
    image = models.URLField('image')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=False, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)


    def __str__(self):
        return f'{self.subcategory} {self.name}'

class Stock(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank=False, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField('quantity', null=False,blank=False)

    def __str__(self):
        return f'Stock del producto {self.product} en la tienda {self.store} es {self.quantity}'

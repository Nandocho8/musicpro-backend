from django.db import models
from products.models import Product
from users.models import Store, Client, Salesman
# Create your models here.

class Payment_method(models.Model):
    name = models.CharField('name_payment_method',max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Payment(models.Model):
    
    price = models.IntegerField('price_payment',max_digits=10, blank=False, null=False)
    auth_code = models.CharField('auth_code',max_length=50, blank=False, null=False)
    payment_method = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=False, null=False)

class Order(models.Model):
    total_order

class Sale(models.Model):
    type_sale = models.CharField('type_sale', max_length=50, blank=False, null=False)
    doc_number = models.IntegerField('doc_number', blank=False, null=False)
    date_sale = models.DateField('date_sale', blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=False)
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE, blank=False, null=False)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.type_sale} N° {self.doc_number}'


class Detail_Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField('quantity', blank=False, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=False)


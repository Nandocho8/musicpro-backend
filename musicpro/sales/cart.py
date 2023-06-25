import pdfkit
from .models import *
from products.models import Stock
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from django.template.loader import get_template
import os
from azure.storage.blob import BlobServiceClient
from keys import enlace


def validate_paroduct(data):
    for detail in data:
        stock = Stock.objects.get(
            Q(product=detail['product']), Q(store=detail['store']))
        quantity = detail['quantity']
        if stock.quantity < quantity:
            return False

    return True


def html_create(template, context={}):
    contenido_html = render(None, template, context).content.decode("utf-8")
    with open('nuevo_archivo.html', 'w') as archivo:
        archivo.write(contenido_html)


@api_view(['POST'])
def Cart_Viewset(request):
    data = JSONParser().parse(request)
    details = data['details']
    if validate_paroduct(details) == False:

        return Response({
            "message": f'Cantidad Incorrecta',
        })

    payment_method = Payment_method.objects.get(id=1)
    auth_code = data['auth_code']
    price = data['price']

    payment = Payment.objects.create(
        payment_method=payment_method, auth_code=auth_code, price=price)

    order = Order.objects.create(total_order=price)
    articulos = []
    for detail in details:
        product = Product.objects.get(id=detail['product'])
        quantity = detail['quantity']
        store = Store.objects.get(id=detail['store'])
        stock = Stock.objects.get(Q(product=product), Q(store=store))
        product_stock = Stock.objects.get(id=stock.id)
        product_stock.quantity -= quantity
        product_stock.save()
        total = stock.quantity
        d = {
            'product': product.name,
            'quantity': quantity,
            'price': product.price,
            'subtotal': quantity * product.price
        }
        articulos.append(d)
        Detail_Order.objects.create(
            product=product,
            quantity=quantity,
            store=store,
            order=Order.objects.get(id=order.id)
        )

    sale = Sale.objects.create(
        type_sale="Boleta",
        date_sale=datetime.now(),
        order=Order.objects.get(id=order.id),
        payment=Payment.objects.get(id=payment.id)
    )

    context = {
        'sale': sale.id,
        'type_sale': sale.type_sale,
        'date_sale': sale.date_sale,
        'auth_code': auth_code,
        'store': store.name_store,
        'total': price,
        'details': articulos}

    html_create('ticket.html', context)
    connection_string = enlace
    container_name = "musicproboletas"
    # pdfkit_config = pdfkit.configuration(wkhtmltopdf='../')
    input_file = 'nuevo_archivo.html'
    output_pdf = pdfkit.from_file(input_file, False)

    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_path = f"boleta{sale.id}.pdf"
    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_path)
    blob_client.upload_blob(output_pdf, overwrite=True)
    url_boleta = blob_client.url
    return Response({
        'mensaje': url_boleta
    })

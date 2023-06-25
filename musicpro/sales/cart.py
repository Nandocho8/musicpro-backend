from .models import *
from products.models import Stock
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.db.models import Q


def validate_paroduct(data):
    for detail in data:
        stock = Stock.objects.get(
            Q(product=detail['product']), Q(store=detail['store']))
        quantity = detail['quantity']
        if stock.quantity < quantity:
            return False

    return True


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

    for detail in details:
        product = Product.objects.get(id=detail['product'])
        quantity = detail['quantity']
        store = Store.objects.get(id=detail['store'])
        stock = Stock.objects.get(Q(product=product), Q(store=store))
        product_stock = Stock.objects.get(id=stock.id)
        product_stock.quantity -= quantity
        product_stock.save()
        total = stock.quantity
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

    return Response({
        "message": f'Orden realizada con exito Ale ahi veo como te mando la boleta',
    })

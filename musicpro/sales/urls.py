from rest_framework import routers
from django.urls import path, include
from .viewset import *

router = routers.DefaultRouter()

router.register('api/payment_method', Payment_method_Viewset, 'payment_method')
router.register('api/payment', Payment_Viewset, 'payment')
router.register('api/order', Order_Viewset, 'order')
router.register('api/detail_order', Detail_Order_Viewset, 'detail_order')
router.register('api/sale', Sale_Viewset, 'sale')

urlpatterns = router.urls

from rest_framework import routers
from django.urls import path, include
from .viewset import *

router = routers.DefaultRouter()

router.register('api/type', Type_Viewset, 'type')
router.register('api/category', Category_Viewset, 'category')
router.register('api/subcategory', Subcategory_Viewset, 'subcategory')
router.register('api/brand', Brand_Viewset, 'brand')

urlpatterns = router.urls
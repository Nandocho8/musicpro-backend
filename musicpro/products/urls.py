from rest_framework import routers
from django.urls import path, include
from .viewset import *
from .views import hello_world

router = routers.DefaultRouter()

router.register('api/hello', hello_world, 'hello')

router.register('api/type', Type_Viewset, 'type')
router.register('api/category', Category_Viewset, 'category')
router.register('api/subcategory', Subcategory_Viewset, 'subcategory')
router.register('api/brand', Brand_Viewset, 'brand')

urlpatterns = router.urls
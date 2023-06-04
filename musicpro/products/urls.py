from rest_framework import routers
from django.urls import path, include
from .viewset import Type_Viewset

router = routers.DefaultRouter()

router.register('api/type', Type_Viewset, 'type')

urlpatterns = router.urls
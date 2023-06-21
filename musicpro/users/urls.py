from rest_framework import routers
from django.urls import path, include
from .viewset import *

router = routers.DefaultRouter()

router.register('api/user', User_Viewset, 'user')
router.register('api/region', Region_Viewset, 'region')
router.register('api/comuna', Comuna_Viewset, 'comuna')
router.register('api/store', Store_Viewset, 'store')
urlpatterns = router.urls

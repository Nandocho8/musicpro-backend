from rest_framework import routers
from django.urls import path, include
from .viewset import *

router = routers.DefaultRouter()

router.register('api/user', User_Viewset, 'user')
urlpatterns = router.urls

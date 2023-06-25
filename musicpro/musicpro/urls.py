"""musicpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users.login import login_cliente
from sales.cart import Cart_Viewset


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("backend/", include('sales.urls')),
    path("backend/", include('products.urls')),
    path("backend/", include('users.urls')),
    path("backend/api/login", login_cliente, name='login_cliente'),
    path("backend/api/cart", Cart_Viewset, name='cart_viewset'),
    # path("backend/api/factura", Factura.as_view(), name='factura'),

]

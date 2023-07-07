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
from django.urls import path, include, re_path
from django.conf import settings
from users.login import login_cliente
from sales.cart import Cart_Viewset
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API MusicPro",
        default_version='v0',
        description="Documentacion de api para music pro",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cr.contrerasv@duocuc.cl"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("backend/", include('sales.urls')),
    path("backend/", include('products.urls')),
    path("backend/", include('users.urls')),
    path("backend/api/login", login_cliente, name='login_cliente'),
    path("backend/api/cart", Cart_Viewset, name='cart_viewset'),
    # path("backend/api/factura", Factura.as_view(), name='factura'),
    re_path(r'^backend/api/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'backend/api/swagger/', schema_view.with_ui('swagger',
                                          cache_timeout=0), name='schema-swagger-ui'),
    path(r'backend/api/redoc/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),

]

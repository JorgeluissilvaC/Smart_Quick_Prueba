"""Smart_Quick_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from apps.api.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/',include('rest_auth.urls')),
    url(r'^rest-auth/registration/',include('rest_auth.registration.urls')),

    #---- CRUD  Clients----------
    path('api/v1/getclients/', get_clients),
    path('api/v1/addclient/', add_client),
    path('api/v1/updateclient/<int:client_id>', update_client),
    path('api/v1/deletecliente/<int:client_id>', delete_client),
    #---- CRUD  Products----------
    path('api/v1/getproducts/', get_products),
    path('api/v1/addproduct/', add_product),
    path('api/v1/updateproduct/<int:product_id>', update_product),
    path('api/v1/deleteproduct/<int:product_id>', delete_product),
    #---- CRUD  bills----------
    path('api/v1/getbills/', get_bills),
    path('api/v1/addbill/', add_bill),
    path('api/v1/updatebill/<int:bill_id>', update_bill),
    path('api/v1/deletebill/<int:bill_id>', delete_bill),
]

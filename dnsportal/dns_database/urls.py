"""dnsportal URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inventory_form, name='InventoryForm'),
    path(r'view', views.inventory_view, name='InventoryView'),
    path(r'delete/<int:id>', views.inventory_delete, name='InventoryDelete'),
    path(r'edit/<int:id>', views.inventory_edit, name='InventoryEdit'),
    path(r'edit/update/<int:id>', views.inventory_update, name='InventoryUpdate'),
]

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
    path('', views.handover_form, name='HandoverForm'),
    path(r'view/<slug:func>', views.handover_view, name='HandoverView'),
    path(r'edit/<int:id>', views.handover_edit, name='HandoverEdit'),
    path(r'edit/update/<int:id>', views.handover_update, name='HandoverUpdate'),
]

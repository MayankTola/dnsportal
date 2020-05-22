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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='LoginPage'),
    path('accounts/login', views.login_page, name='LoginPage'),
    path("accounts/register", views.register_view, name="Register"),
    path('accounts/logout', views.logout_view, name="logout"),
    path('home/', views.home, name='Home'),
    path('dns_lookup/', views.dns_lookup, name='DnsLookup'),
    path('lookup_results/', views.lookup_results, name='Lookup_Results'),
    path('inventory_form/', include('dns_database.urls')),
    url(r'inventory/', include('dns_database.urls')),
    url(r'handover_form/', include('handover_form.urls')),
    url(r'roster/', include('roster.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

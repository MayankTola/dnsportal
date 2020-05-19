from django.urls import path, include


from . import views

urlpatterns = [
    path(r'upload', views.upload_schedule, name='Upload Schedule'),
    path(r'view', views.view_schedule, name='View Schedule'),

]

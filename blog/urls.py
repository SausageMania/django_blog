from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BancarList.as_view(), name='bancar_list'),

]
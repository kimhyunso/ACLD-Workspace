from django.contrib import admin
from django.urls import path
from . import views


app_name = 'project'

urlpatterns = [
    path('view/', views.view, name='view'),
    path('<int:part_pk>/detail/', views.detail ,name='detail'),
]

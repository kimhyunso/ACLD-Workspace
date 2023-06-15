from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('agent/', views.agent, name='agent'),
    path('chart/', views.chart, name='chart'),
    path('addEmp/', views.addEmp, name='addEmp'),
]



from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'),
    path('receive_image/', views.receive_image, name='receive_image'),
    path('csrf_token/', views.get_csrf_token_view, name='csrf_token'),
]

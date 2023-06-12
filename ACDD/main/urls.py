<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
=======
from django.urls import path
>>>>>>> 7f468186dd7d9a89be3a3816d9584f81d4a89e8e
from . import views

app_name = 'main'


urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('receive_image/', views.receive_image, name='receive_image'),
    path('csrf_token/', views.get_csrf_token_view, name='csrf_token'),
]
=======
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('log_detail/', views.log_detail, name='log_detail'),
    path('report/', views.report, name='report'),
    path('report_detail/', views.report_detail, name='report_detail'),
    path('chart/', views.chart, name='chart'),
    path('employee/', views.employee, name='employee'),
]


>>>>>>> 7f468186dd7d9a89be3a3816d9584f81d4a89e8e

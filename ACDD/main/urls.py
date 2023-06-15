from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('log_detail/', views.log_detail, name='log_detail'),
    path('report/', views.report, name='report'),
    path('report_detail/', views.report_detail, name='report_detail'),
    path('chart/', views.chart, name='chart'),
    path('employee/', views.employee, name='employee'),
    path('sse/', views.sse_stream, name='sse_stream'),
    path('send_html/', views.send_html_to_clients, name='send_html'),
]





from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('log_detail/', views.log_detail, name='log_detail'),
    path('report/', views.report, name='report'),
    path('report_detail/', views.report_detail, name='report_detail'),
    path('chart/', views.chart, name='chart'),
    path('addEmp/', views.addEmp, name='addEmp'),
    path('addDepart', views.depart, name='depart'),
    
] + static(settings.MEDIA_URL, doucment_root=settings.MEDIA_ROOT)





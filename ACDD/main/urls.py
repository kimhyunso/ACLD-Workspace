from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('log_detail/', views.log_detail, name='log_detail'),
    path('report/', views.report, name='report'),
    path('<int:page_no>/report_detail/', views.report_detail, name='report_detail'),
    path('chart/', views.chart, name='chart'),
    path('employee/', views.employee, name='employee'),
]



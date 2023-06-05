from . import views
from django.urls import path

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('<int:page_no>/processing/', views.processing, name='processing'),
    path('agree/', views.agree, name='agree'),
    path('disagree/', views.disagree, name='disagree'),
]

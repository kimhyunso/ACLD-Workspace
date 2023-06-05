from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('<int:page_no>/processing/', views.processing, name='processing'),
    path('agree/', views.agree, name='agree'),
    path('disagree/', views.disagree, name='disagree'),
]



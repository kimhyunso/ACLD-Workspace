from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('agent/', views.agent, name='agent'),
    path('detailview/', views.chart, name='detailview'),
    path('addEmp/', views.addEmp, name='addEmp'),
    path('addDepart/', views.addDepart, name='addDepart'),
    path('get_updated_data/', views.get_updated_data, name='get_updated_data'),
    
] + static(settings.MEDIA_URL, doucment_root=settings.MEDIA_ROOT)





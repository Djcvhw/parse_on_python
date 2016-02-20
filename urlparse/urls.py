from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdata/$', views.get_data, name='get_data'),
    url(r'^loaddata/$', views.load_data, name='load_data'),
]
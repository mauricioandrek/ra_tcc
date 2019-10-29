from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.objetos_list, name='list'),
]
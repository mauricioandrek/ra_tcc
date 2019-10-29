from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.objetos_list, name='list'),
]
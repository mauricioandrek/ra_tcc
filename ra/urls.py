from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    url(r'^$', views.index, name='home'),
	url(r'^leitura/', views.leitura, name='leitura'),
    url(r'^objeto/novo', views.objeto_novo, name='objeto_novo'),
    path('objeto/<int:pk>/editar/', views.objeto_editar, name='objeto_editar'),
    path('objeto/<int:pk>/remover/', views.objeto_remover, name='objeto_remover'),
    
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Objeto
from django import template


def index(request):
	return render(request, 'pages/index.html')

def objetos_list(request):
	objetos = Objeto.objects.all()
	context = {	'objetos_list': objetos }
	return render(request, 'pages/objetos.html', context)
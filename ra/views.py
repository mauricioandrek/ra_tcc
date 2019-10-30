from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage, default_storage
from django.http import HttpResponse
from .models import Objeto
from .forms import ObjetoForm
from django import template
import uuid


def index(request):
    objetos = Objeto.objects.all()
    context = {	'objetos_list': objetos }
    return render(request, 'pages/index.html', context)

def objeto_novo(request):
    if request.method == "POST":
        form = ObjetoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.nome = request.POST.get('nome')
            objeto.id_marcador = request.POST.get('id_marcador')
            files = request.FILES.getlist('file')
            id = uuid.uuid1().hex
            for f in files:
                if ".obj" in f.name:
                    objeto.name_OBJ = f.name
                if ".mtl" in f.name:
                    objeto.name_MTL = f.name
                handle_uploaded_file(id, f)
            objeto.path_modelos = 'static/ra/objects/'+ id
            objeto.descricao = request.POST.get('descricao')
            objeto.save()
            return redirect('home')
    else:
        form = ObjetoForm()
    return render(request, 'pages/objeto_edit.html', {'form': form})
def objeto_editar(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    if request.method == "POST":
        form = ObjetoForm(request.POST, instance=objeto)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.nome = request.POST.get('nome')
            objeto.id_marcador = request.POST.get('id_marcador')
            files = request.FILES.getlist('file')
            id = uuid.uuid1().hex
            for f in files:
                if ".obj" in f.name:
                    objeto.name_OBJ = f.name
                if ".mtl" in f.name:
                    objeto.name_MTL = f.name
                handle_uploaded_file(id, f)
            objeto.path_modelos = 'static/ra/objects/'+ id
            objeto.descricao = request.POST.get('descricao')
            objeto.save()
            return redirect('home')
    else:
        form = ObjetoForm(instance=objeto)
    return render(request, 'pages/objeto_edit.html', {'form': form})
def objeto_remover(request, pk):
    objetoSelecionado = Objeto.objects.get(pk=pk)
    if objetoSelecionado.path_modelos != '' and default_storage.exists(objetoSelecionado.path_modelos):
        path_obj = objetoSelecionado.path_modelos + '/' + objetoSelecionado.name_OBJ
        path_mtl = objetoSelecionado.path_modelos + '/' + objetoSelecionado.name_MTL
        if path_obj != '' and default_storage.exists(path_obj):
            default_storage.delete(path_obj)
        if path_mtl != '' and default_storage.exists(path_mtl):
            default_storage.delete(path_mtl)
        default_storage.delete(objetoSelecionado.path_modelos)
    objetoSelecionado.delete()
    objetos = Objeto.objects.all()
    context = {	'objetos_list': objetos }
    return render(request, 'pages/index.html', context)
def leitura(request):
	objetos = Objeto.objects.all()
	context = {	'objetos_list': objetos }
	return render(request, 'pages/leitura.html', context)

def handle_uploaded_file(name, myfile):
    path = 'static/ra/objects/'+ name + '/' + myfile.name
    fs = FileSystemStorage()
    filename = fs.save(path, myfile)
    uploaded_file_url = fs.url(filename)
    return path
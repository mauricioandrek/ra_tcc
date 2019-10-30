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
            files_paths = []
            id = uuid.uuid1().hex
            for f in files:
                files_paths.append(handle_uploaded_file(id, f))
            if files_paths[0] != None:
                objeto.path_modelo_OBJ = files_paths[0]
            if files_paths[0] != None:
                objeto.path_modelo_MTL = files_paths[1]
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
            files_paths = []
            id = uuid.uuid1().hex
            for f in files:
                files_paths.append(handle_uploaded_file(id, f))
            if files_paths[0] != None:
                objeto.path_modelo_OBJ = files_paths[0]
            if files_paths[0] != None:
                objeto.path_modelo_MTL = files_paths[1]
            objeto.descricao = request.POST.get('descricao')
            objeto.save()
            return redirect('home')
    else:
        form = ObjetoForm(instance=objeto)
    return render(request, 'pages/objeto_edit.html', {'form': form})
def objeto_remover(request, pk):
    objetoSelecionado = Objeto.objects.get(pk=pk)
    if objetoSelecionado.path_modelo_OBJ != '' and default_storage.exists(objetoSelecionado.path_modelo_OBJ):
        default_storage.delete(objetoSelecionado.path_modelo_OBJ)
    if objetoSelecionado.path_modelo_MTL != '' and default_storage.exists(objetoSelecionado.path_modelo_MTL):
        default_storage.delete(objetoSelecionado.path_modelo_MTL)
    objetoSelecionado.delete()
    objetos = Objeto.objects.all()
    context = {	'objetos_list': objetos }
    return render(request, 'pages/index.html', context)
def leitura(request):
	objetos = Objeto.objects.all()
	context = {	'objetos_list': objetos }
	return render(request, 'pages/leitura.html', context)

def handle_uploaded_file(name, myfile):
    path = 'static/ra/objects/'+ name + '_' + myfile.name
    fs = FileSystemStorage()
    filename = fs.save(path, myfile)
    uploaded_file_url = fs.url(filename)
    return path
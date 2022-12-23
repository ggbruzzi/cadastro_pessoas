from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def criar(request):
    return render(request, 'index2.html')

def editar(request):
    return render(request, 'index3.html')

from django.shortcuts import render

#import de um modulo hhtp do django de envio HTTP
from django.http import HttpResponse

# Create your views here.
# regras de negocio

# def index(request):
#     return HttpResponse("<h1>Ola</h1>")

def index(request):
    return render(request, "motorartigos/index.html")

def artigo(request):
    return render(request, 'motorartigos/artigo.html')
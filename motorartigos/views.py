from django.shortcuts import render

#import de um modulo hhtp do django de envio HTTP
from django.http import HttpResponse
from motorartigos.models import Autor
from django.shortcuts import render, get_object_or_404
from .models import Artigo

# Create your views here.
# regras de negocio

# def index(request):
#     return HttpResponse("<h1>Ola</h1>")

def index(request):
    # estrutura de dados em python = collections dados guardados na memoria ram
    # lista = [1,2,3,4,5,6]  - mutavel
    # tupla = (1,2,3,4,5,6) - imutavel
    #dicionario
    #mock objects = dados de teste
    """
    autores ={
        1:{"nome": "Natalia", "biografia": "a ++", "email": "natalia@gmail.com"},
        2:{"nome": "luis", "biografia": "chosens", "email": "luis@gmail.com"},
        3:{"nome": "Bruno", "biografia": "bruninhuuuu", "email": "bruno@gmail.com"},   
    }
    """
    # objeto = instancia de uma classe (junçaõ de tudo que a classe é)
    # classe = molde do objeto

    autores = Autor.objects.all()

    return render(request, "motorartigos/index.html", {"autores": autores})

def artigo(request):
    return render(request, 'motorartigos/artigo.html')

def detalhe_artigo(request, slug):
    artigo = get_object_or_404(Artigo, slug=slug)
    return render(request, 'motorartigos/artigo.html', {'artigo': artigo})


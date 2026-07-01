from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Artigo, Autor, EixoTecnologia
# Create your views here.
# regras de negocio

# def index(request):
#     return HttpResponse("<h1>Ola</h1>")

def index(request):
    # 1. Captura o que o usuário digitou na pesquisa e o eixo clicado
    query = request.GET.get('q')  
    eixo_id = request.GET.get('eixo')  

    # Tratamento para garantir que eixo_id seja um número
    try:
        eixo_id = int(eixo_id) if eixo_id else None
    except ValueError:
        eixo_id = None

    # 2. Busca Otimizada: 
    # Em vez de passar "autores = Autor.objects.all()", usamos o select_related.
    # Ele já "embutir" os dados do Autor e do Eixo dentro de cada artigo de uma vez só!
    artigos_publicados = Artigo.objects.filter(publicada=True).select_related('id_fk_autor', 'id_fk_eixo')

    # 3. Lógica da Barra de Pesquisa (Filtra por título ou texto)
    if query:
        artigos_publicados = artigos_publicados.filter(
            Q(titulo__icontains=query) | Q(texto__icontains=query)
        )

    # 4. Lógica dos Botões de Eixo de Tecnologia
    if eixo_id:
        artigos_publicados = artigos_publicados.filter(id_fk_eixo__id=eixo_id)

    # 5. Ordenação e separação para o Carrossel
    artigos_publicados = artigos_publicados.order_by('-data_publicacao')
    artigos_recentes = artigos_publicados[:4]
    
    # 6. Busca os eixos para o Front-End poder desenhar os botões
    eixos = EixoTecnologia.objects.all()

    # Monta o contexto para enviar ao HTML
    contexto = {
        'artigos_recentes': artigos_recentes,
        'todos_artigos': artigos_publicados,
        'eixos': eixos,
        'query_atual': query,
        'eixo_atual': eixo_id,
    }
    
    # Único return necessário no final da função
    return render(request, 'motorartigos/index.html', contexto)

def artigo(request, id):
    # Busca o artigo exato pelo ID recebido da URL
    artigo_especifico = get_object_or_404(Artigo, id=id)
    
    contexto = {
        'artigo': artigo_especifico
    }
    
    return render(request, 'motorartigos/artigo.html', contexto)



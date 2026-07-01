from django.urls import path
from motorartigos.views import index, artigo
# boa pratica
# rotas
# cada pasta app com suas rotas
# arquivo de rotas do app motorartigos

urlpatterns = [
    path('', index, name="index"),
    # O <int:id> avisa ao Django que um número (o ID do artigo) será passado na URL
    path("artigo/<int:id>/", artigo, name="artigo") 
]



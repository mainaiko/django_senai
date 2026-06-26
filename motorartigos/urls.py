from django.urls import path
from motorartigos.views import index, artigo

# boa pratica
# rotas
# cada pasta app com suas rotas
# arquivo de rotas do app motorartigos

urlpatterns = [
    path('', index, name="index"),
    path("artigo/", artigo, name="artigo") # vantagem de colocar o name é a facilidade de nomear
]



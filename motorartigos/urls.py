from django.urls import path
from motorartigos.views import index

# boa pratica
# cada pasta app com suas rotas
#arquivo de rotas do app motorartigos

urlpatterns = [
    path("", index),
]



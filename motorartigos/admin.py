from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models as db_models
from .models import Autor, EixoTecnologia, Artigo
# Register your models here.
# personalização e administração da interface adm nativa do django
# designer e configurador

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')

@admin.register(EixoTecnologia)
class EixoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_fk_autor', 'id_fk_eixo', 'data_publicacao')
    search_fields = ('id_fk_autor__nome',)
    list_filter = ('id_fk_eixo', 'data_publicacao')
    formfield_overrides = {
        db_models.TextField: {'widget': TinyMCE()},  # 👉 garante o editor
    }
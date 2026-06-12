from django.contrib import admin
from .models import Autor, EixoTecnologia # import de dados

# Register your models here.
# personalização e administração da interface adm nativa do django
# designer e configurador

class AutorAdmin(admin.ModelAdmin):

    # campos
    list_display = ("nome", "biografia", "email")
    # 
    search_fields = ("numero",)

admin.site.register(Autor, AutorAdmin)

class EixoTecnologiaAdmin(admin.ModelAdmin):

    # campos
    list_display = ("nome",)
    # 
    search_fields = ("numero",)

admin.site.register(EixoTecnologia, EixoTecnologiaAdmin)

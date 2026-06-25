from django.db import models
from tinymce.models import HTMLField

# Create your models here.
# modelo do banco
# classes de entidade a classe autor representa todos os onjetos autores
# entidade = representação do mundo real
# instancia = objeto
# objeto = endereço de memoria
# def dentro de uma classe = metodo da classe

#entidade autor
class Autor(models.Model):
    #atributo
    # o atributo id é automatico
    # caracteristicas de chave primaria: imutavel, universal e unica
    # models = modulo
    # field = classe
    
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    # personalização de nome da tabela
    # class Meta:
    #     tb_name = "autor"

# entidade sobre qual eixo o artigo sera
class EixoTecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    # class Meta:
    #     tb_name = "eixo"

class Artigo(models.Model):
    texto = HTMLField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    
    id_fk_eixo = models.ForeignKey(
        EixoTecnologia,
        on_delete=models.CASCADE,
        db_column='id_fk_eixo'
    )

    id_fk_autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        db_column='id_fk_autor' 
    )

    def __str__(self):
        return f'Artigo {self.id} - {self.data_publicacao}'
    
    class Meta():
        db_table = 'artigo'

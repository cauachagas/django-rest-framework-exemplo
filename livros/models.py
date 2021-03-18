from django.db import models
from uuid import uuid4

# Create your models here.


def upload_imagem_livro(instance, filename):
    return f"{instance.id}-{filename}"


class Livros(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano = models.IntegerField()
    estado = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    criado = models.DateField(auto_now_add=True)
    imagem = models.ImageField(
        upload_to=upload_imagem_livro, blank=True, null=True)

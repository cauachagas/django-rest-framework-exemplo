from django.db import models
from uuid import uuid4

# Create your models here.


class Livros(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano = models.IntegerField()
    estado = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    criado = models.DateField(auto_now_add=True)

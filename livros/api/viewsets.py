from rest_framework import viewsets
from livros import models
from livros.api import serializers


class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()

from rest_framework import serializers
from livros import models


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livros
        fields = "__all__"

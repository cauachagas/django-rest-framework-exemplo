from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from livros.models import Livros
from ninja.orm import create_schema
from uuid import UUID

router = Router()

# Na entrada, o id será criado automáticamente
LivrosSchemaIn = create_schema(Livros, exclude=["id"])

# Na saída, o id deve ser mostrado
LivrosSchemaOut = create_schema(Livros)


@router.post("")
def registrar_livro(request, event: LivrosSchemaIn):
    Livros.objects.create(**event.dict())
    return event


@router.get("", response=List[LivrosSchemaOut])
def listar_livros(request):
    return list(Livros.objects.all())


@router.get("/{id}", response=LivrosSchemaIn)
def lista_livro_id(request, id: UUID):
    return get_object_or_404(Livros, id=UUID)
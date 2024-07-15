from typing import Annotated

from pydantic import UUID4, Field

from desafio_4_Api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(
        description='Nome da categoria', example='Scale', max_length=20)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]

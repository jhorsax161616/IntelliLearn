from pydantic import BaseModel
from sqlalchemy import DateTime
from typing import Optional

class Sala(BaseModel):
    id: Optional[int]
    nombre: str
    descripcion: str
    url_sala: str
    url_imagen: str
    horario: DateTime
    curso_id: int
    estudiante_id: int
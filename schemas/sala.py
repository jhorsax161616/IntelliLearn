from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Sala(BaseModel):
    id: Optional[int]
    nombre: str
    descripcion: str
    url_sala: str
    url_imagen: str
    horario: datetime
    curso_id: int
    estudiante_id: int
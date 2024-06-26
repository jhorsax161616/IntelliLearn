from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .estudiante_sala import Estudiante_SalaBase

class SalaBase(BaseModel):
    nombre: str
    descripcion: str
    url_sala: str
    url_imagen: str
    horario: datetime
    is_active: Optional[bool] = True

class SalaCreate(SalaBase):
    curso_id: int
    estudiante_id: int

class SalaUpdate(SalaBase):
    nombre: Optional[str]
    descripcion: Optional[str]
    url_sala: Optional[str]
    url_imagen: Optional[str]
    horario: Optional[datetime]

class SalaInDB(SalaBase):
    id: Optional[int]

    class Config:
        orm_mode = True
from pydantic import BaseModel
from typing import Optional

class Estudiante_SalaBase(BaseModel):
    pass

class Estudiante_SalaCreate(Estudiante_SalaBase):
    estudiante_id: int
    sala_id: int

class Estudiante_SalaUpdate(Estudiante_SalaBase):
    estudiante_id: Optional[int]
    sala_id: Optional[int]

class Estudiante_Sala(Estudiante_SalaBase):
    estudiante_id: int
    sala_id: int
    estudiante: Optional[dict] = {}
    sala: Optional[dict] = {}

    class Config:
        orm_mode = True
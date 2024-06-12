from pydantic import BaseModel
from typing import Optional, List
from .sala import SalaBase

class CursoBase(BaseModel):
    nombre: str
    descripcion: str

class CursoCreate(CursoBase):
    universidad_id: int

class CursoUpdate(CursoBase):
    nombre: Optional[str]
    descripcion: Optional[str]

class Curso(CursoBase):
    id: Optional[int]
    universidad: Optional[dict] = {}
    salas: List[SalaBase] = []

    class Config:
        orm_mode = True
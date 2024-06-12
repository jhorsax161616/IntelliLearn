from pydantic import BaseModel
from typing import List, Optional
from .curso import CursoBase
from .estudiante import EstudianteBase

class UniversidadBase(BaseModel):
    nombre: str
    direccion: str
    correo: str

class UniversidadCreate(UniversidadBase):
    pass

class UniversidadUpdate(UniversidadBase):
    nombre: Optional[str]
    direccion: Optional[str]
    correo: Optional[str]

class Universidad(UniversidadBase):
    id: Optional[int]
    cursos: List[CursoBase] = []
    estudiantes: List[EstudianteBase] = []

    class Config:
        orm_mode = True
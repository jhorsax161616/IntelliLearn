from pydantic import BaseModel
from typing import Optional, List
from .sala import SalaBase
from .estudiante_sala import Estudiante_SalaBase

class EstudianteBase(BaseModel):
    nombres: str
    apellidos: str
    correo: str
    universidad_id: int

class EstudianteCreate(EstudianteBase):
    hashed_password: Optional[str] = None

class EstudianteUpdate(EstudianteBase):
    nombres: Optional[str]
    apellidos: Optional[str]
    correo: Optional[str]
    universidad_id: Optional[int]
    hashed_password: Optional[str]

class EstudianteInDB(EstudianteBase):
    id: Optional[int]

    class Config:
        orm_mode = True
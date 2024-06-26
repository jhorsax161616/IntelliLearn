from pydantic import BaseModel
from typing import Optional

class Estudiante_SalaBase(BaseModel):
    estudiante_id: int
    sala_id: int

class Estudiante_SalaCreate(Estudiante_SalaBase):
    pass

class Estudiante_SalaInDB(Estudiante_SalaBase):
    pass

    class Config:
        orm_mode = True
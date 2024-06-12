from pydantic import BaseModel
from typing import Optional

class Estudiante(BaseModel):
    id: Optional[int]
    nombres: str
    apellidos: str
    correo: str
    universidad: str
    hashed_password: str
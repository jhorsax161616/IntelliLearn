from pydantic import BaseModel
from typing import Optional

class Estudiante(BaseModel):
    id: Optional[int]
    nombres: str
    apellidos: str
    correo: str
    universidad_id: int
    hashed_password: str
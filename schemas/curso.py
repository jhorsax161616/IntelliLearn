from pydantic import BaseModel
from typing import Optional

class Curso(BaseModel):
    id: Optional[int]
    nombre: str
    descripcion: str
    universidad_id: int
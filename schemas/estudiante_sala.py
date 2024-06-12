from pydantic import BaseModel
from typing import Optional

class EstudianteSala(BaseModel):
    estudiante_id: int
    sala_id: int
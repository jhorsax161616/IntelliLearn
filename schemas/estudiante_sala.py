from pydantic import BaseModel
from typing import Optional

class EstudainteSala(BaseModel):
    estudiante_id: int
    sala_id: int
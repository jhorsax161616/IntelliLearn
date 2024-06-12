from pydantic import BaseModel
from typing import Optional

class Universidad(BaseModel):
    id: Optional[int]
    nombre: str
    direccion: str
    correo: str
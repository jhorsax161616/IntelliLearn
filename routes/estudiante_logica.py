from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from services import estudiante_service as service
from schemas.estudiante_sala import Estudiante_SalaInDB

estudiante_logica = APIRouter()

@estudiante_logica.get("/estudiantes_salas/{sala_id}", response_model=list[Estudiante_SalaInDB])
def read_estudiantes_sala(sala_id: int, db: Session = Depends(get_db)):
    estudiantes_sala = service.get_estudiantes_sala(db, id_sala=sala_id)
    return estudiantes_sala

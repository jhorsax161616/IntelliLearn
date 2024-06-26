from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from services import sala_service as service
from schemas.estudiante_sala import Estudiante_SalaInDB

sala_logica = APIRouter()

@sala_logica.get("/estudiantes_salasi/{estudiante_id}", response_model=list[Estudiante_SalaInDB])
def read_salas_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    salas_estudiante = service.get_salas_estudiante(db, id_estudiante=estudiante_id)
    return salas_estudiante

@sala_logica.delete("/estudiantes_salas/{sala_id}", response_model=list[Estudiante_SalaInDB])
def delete_estudiantes_sala(sala_id: int, db: Session = Depends(get_db)):
    return service.delete_estudiantes_sala(db, id_sala=sala_id)

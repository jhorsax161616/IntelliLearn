from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from crud import estudiante_sala as crud
from services import estudiante_service as service
from schemas.estudiante_sala import Estudiante_SalaCreate, Estudiante_SalaInDB

estudiante_sala = APIRouter()

@estudiante_sala.post("/estudiantes_salas", response_model=Estudiante_SalaInDB)
def create_estudiante_sala(estudiante_sala: Estudiante_SalaCreate, db: Session = Depends(get_db)):
    db_estudiante_sala = service.get_estudiante_sala(db, id_estudiante=estudiante_sala.estudiante_id, id_sala=estudiante_sala.sala_id)
    if db_estudiante_sala:
        raise HTTPException(status_code=400, detail="Ya está registrado en la sala")
    return crud.create_estudiante_sala(db=db, estudiante_sala=estudiante_sala)

@estudiante_sala.get("/estudiantes_salas", response_model=list[Estudiante_SalaInDB])
def read_estudiantes_salas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estudiantes_salas = crud.get_estudiantes_salas(db, skip=skip, limit=limit)
    return estudiantes_salas

@estudiante_sala.delete("/estudiantes_salas/{estudiante_id}/{sala_id}", response_model=Estudiante_SalaInDB)
def delete_estudiante_sala(estudiante_id: int, sala_id: int, db: Session = Depends(get_db)):
    return crud.delete_estudiante_sala(db, id_estudiante=estudiante_id, id_sala=sala_id)

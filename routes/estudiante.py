from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from crud import estudiante as crud
from schemas.estudiante import EstudianteCreate, EstudianteUpdate, EstudianteInDB

from .login import pwd_context

estudiante = APIRouter()

@estudiante.post("/estudiantes", response_model=EstudianteInDB)
def create_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    db_estudiante = crud.get_estudiante_by_correo(db, correo=estudiante.correo) 
    if db_estudiante:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    estudiante.hashed_password = pwd_context.hash(estudiante.hashed_password)
    return crud.create_estudiante(db=db, estudiante=estudiante)

@estudiante.get("/estudiantes", response_model=list[EstudianteInDB])
def read_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estudiantes = crud.get_estudiantes(db, skip=skip, limit=limit)
    return estudiantes

@estudiante.get("/estudiantes/{estudiante_id}", response_model=EstudianteInDB)
def read_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = crud.get_estudiante(db, id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante

@estudiante.put("/estudiantes/{estudiante_id}", response_model=EstudianteInDB)
def update_estudiante(estudiante_id: int, estudiante: EstudianteUpdate, db: Session = Depends(get_db)):
    db_estudiante = crud.update_estudiante(db, id=estudiante_id, estudiante=estudiante)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante

@estudiante.delete("/estudiantes/{estudiante_id}", response_model=EstudianteInDB)
def delete_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = crud.delete_estudiante(db, id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante
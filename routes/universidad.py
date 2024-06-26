from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from crud import universidad as crud
from schemas.universidad import UniversidadCreate, UniversidadUpdate, UniversidadInDB

universidad = APIRouter()

@universidad.post("/universidades", response_model=UniversidadInDB)
def create_universidad(universidad: UniversidadCreate, db: Session = Depends(get_db)):
    db_universidad = crud.get_universidad_by_nombre(db, nombre=universidad.nombre) 
    if db_universidad:
        raise HTTPException(status_code=400, detail="La universidad ya está registrada")
    return crud.create_universidad(db=db, universidad=universidad)

@universidad.get("/universidades", response_model=list[UniversidadInDB])
def read_universidades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    universidades = crud.get_universidades(db, skip=skip, limit=limit)
    return universidades

@universidad.get("/universidades/{universidad_id}", response_model=UniversidadInDB)
def read_universidad(universidad_id: int, db: Session = Depends(get_db)):
    db_universidad = crud.get_universidad(db, id=universidad_id)
    if db_universidad is None:
        raise HTTPException(status_code=404, detail="Universidad no encontrada")
    return db_universidad

@universidad.put("/universidades/{universidad_id}", response_model=UniversidadInDB)
def update_universidad(universidad_id: int, universidad: UniversidadUpdate, db: Session = Depends(get_db)):
    db_universidad = crud.update_universidad(db, id=universidad_id, universidad=universidad)
    if db_universidad is None:
        raise HTTPException(status_code=404, detail="Universidad no encontrada")
    return db_universidad

@universidad.delete("/universidades/{universidad_id}", response_model=UniversidadInDB)
def delete_universidad(universidad_id: int, db: Session = Depends(get_db)):
    db_universidad = crud.delete_universidad(db, id=universidad_id)
    if db_universidad is None:
        raise HTTPException(status_code=404, detail="Universidad no encontrada")
    return db_universidad
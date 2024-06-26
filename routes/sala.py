from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from crud import sala as crud
from schemas.sala import SalaCreate, SalaUpdate, SalaInDB

sala = APIRouter()

@sala.post("/salas", response_model=SalaInDB)
def create_sala(sala: SalaCreate, db: Session = Depends(get_db)):
    return crud.create_sala(db=db, sala=sala)

@sala.get("/salas", response_model=list[SalaInDB])
def read_salas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    salas = crud.get_salas(db, skip=skip, limit=limit)
    return salas

@sala.get("/salas/{sala_id}", response_model=SalaInDB)
def read_sala(sala_id: int, db: Session = Depends(get_db)):
    db_sala = crud.get_sala(db, id=sala_id)
    if db_sala is None:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return db_sala

@sala.get("/salasactivas", response_model=list[SalaInDB])
def read_salas_activas(db: Session = Depends(get_db)):
    db_salas = crud.get_salas_activas(db)
    return db_salas

@sala.put("/salas/{sala_id}", response_model=SalaInDB)
def update_sala(sala_id: int, sala: SalaUpdate, db: Session = Depends(get_db)):
    db_sala = crud.update_sala(db, id=sala_id, sala=sala)
    if db_sala is None:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return db_sala

@sala.delete("/salas/{sala_id}", response_model=SalaInDB)
def delete_sala(sala_id: int, db: Session = Depends(get_db)):
    db_sala = crud.delete_sala(db, id=sala_id)
    if db_sala is None:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return db_sala

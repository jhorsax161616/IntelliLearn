from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from crud import curso as crud
from schemas.curso import CursoCreate, CursoUpdate, CursoInDB

curso = APIRouter()

@curso.post("/cursos", response_model=CursoInDB)
def create_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    db_curso = crud.get_curso_by_nombre(db, nombre=curso.nombre) 
    if db_curso:
        raise HTTPException(status_code=400, detail="El curso ya está registrado")
    return crud.create_curso(db=db, curso=curso)

@curso.get("/cursos", response_model=list[CursoInDB])
def read_cursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cursos = crud.get_cursos(db, skip=skip, limit=limit)
    return cursos

@curso.get("/cursos/{curso_id}", response_model=CursoInDB)
def read_curso(curso_id: int, db: Session = Depends(get_db)):
    db_curso = crud.get_curso(db, id=curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return db_curso

@curso.put("/cursos/{curso_id}", response_model=CursoInDB)
def update_curso(curso_id: int, curso: CursoUpdate, db: Session = Depends(get_db)):
    db_curso = crud.update_curso(db, id=curso_id, curso=curso)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return db_curso

@curso.delete("/cursos/{curso_id}", response_model=CursoInDB)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    db_curso = crud.delete_curso(db, id=curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return db_curso
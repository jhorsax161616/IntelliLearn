from sqlalchemy.orm import Session

from models import Curso
from schemas.curso import CursoCreate, CursoUpdate

def get_curso(db: Session, id: int):
    return db.query(Curso).filter(Curso.id == id).first()

def get_cursos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Curso).offset(skip).limit(limit).all()

def get_curso_by_nombre(db: Session, nombre: str):
    return db.query(Curso).filter(Curso.nombre == nombre).first()

def create_curso(db: Session, curso: CursoCreate):
    db_curso = Curso(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def update_curso(db: Session, id: int, curso: CursoUpdate):
    db_curso = db.query(Curso).filter(Curso.id == id).first()
    if db_curso:
        for key, value in curso.dict(exclude_unset=True).items():
            setattr(db_curso, key, value)
        db.commit()
        db.refresh(db_curso)
    return db_curso

def delete_curso(db: Session, id: int):
    db_curso = db.query(Curso).filter(Curso.id == id).first()
    if db_curso:
        db.delete(db_curso)
        db.commit()
    return db_curso
from sqlalchemy.orm import Session

from models.Estudiante import Estudiante
from schemas.estudiante import EstudianteCreate, EstudianteUpdate, EstudianteInDB

def get_estudiante(db: Session, id: int):
    return db.query(Estudiante).filter(Estudiante.id == id).first()

def get_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Estudiante).offset(skip).limit(limit).all()

def get_estudiante_by_correo(db: Session, correo: str) -> EstudianteInDB | None:
    return db.query(Estudiante).filter(Estudiante.correo == correo).first()

def create_estudiante(db: Session, estudiante: EstudianteCreate):
    db_estudiante = Estudiante(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def update_estudiante(db: Session, id: int, estudiante: EstudianteUpdate):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id == id).first()
    if db_estudiante:
        for key, value in estudiante.dict(exclude_unset=True).items():
            setattr(db_estudiante, key, value)
        db.commit()
        db.refresh(db_estudiante)
    return db_estudiante

def delete_estudiante(db: Session, id: int):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id == id).first()
    if db_estudiante:
        db.delete(db_estudiante)
        db.commit()
    return db_estudiante
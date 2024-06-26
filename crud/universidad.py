from sqlalchemy.orm import Session

from models.Universidad import Universidad
from schemas.universidad import UniversidadCreate, UniversidadUpdate

def get_universidad(db: Session, id: int):
    return db.query(Universidad).filter(Universidad.id == id).first()

def get_universidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Universidad).offset(skip).limit(limit).all()

def get_universidad_by_nombre(db: Session, nombre: str):
    return db.query(Universidad).filter(Universidad.nombre == nombre).first()

def create_universidad(db: Session, universidad: UniversidadCreate):
    db_universidad = Universidad(**universidad.dict())
    db.add(db_universidad)
    db.commit()
    db.refresh(db_universidad)
    return db_universidad

def update_universidad(db: Session, id: int, universidad: UniversidadUpdate):
    db_universidad = db.query(Universidad).filter(Universidad.id == id).first()
    if db_universidad:
        for key, value in universidad.dict(exclude_unset=True).items():
            setattr(db_universidad, key, value)
        db.commit()
        db.refresh(db_universidad)
    return db_universidad

def delete_universidad(db: Session, id: int):
    db_universidad = db.query(Universidad).filter(Universidad.id == id).first()
    if db_universidad:
        db.delete(db_universidad)
        db.commit()
    return db_universidad
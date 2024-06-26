from sqlalchemy.orm import Session

from models.Sala import Sala
from schemas.sala import SalaCreate, SalaUpdate

def get_sala(db: Session, id: int):
    return db.query(Sala).filter(Sala.id == id).first()

def get_salas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Sala).offset(skip).limit(limit).all()

def get_salas_activas(db: Session):
    return db.query(Sala).filter(Sala.is_active == True).all()

def create_sala(db: Session, sala: SalaCreate):
    db_sala = Sala(**sala.dict())
    db.add(db_sala)
    db.commit()
    db.refresh(db_sala)
    return db_sala

def update_sala(db: Session, id: int, sala: SalaUpdate):
    db_sala = db.query(Sala).filter(Sala.id == id).first()
    if db_sala:
        for key, value in sala.dict(exclude_unset=True).items():
            setattr(db_sala, key, value)
        db.commit()
        db.refresh(db_sala)
    return db_sala

def delete_sala(db: Session, id: int):
    db_sala = db.query(Sala).filter(Sala.id == id).first()
    if db_sala:
        db.delete(db_sala)
        db.commit()
    return db_sala
from sqlalchemy.orm import Session

from models.Estudiante_Sala import Estudiante_Sala
from schemas.estudiante_sala import Estudiante_SalaCreate

# Obtener todos los estudiantes en salas
def get_estudiantes_salas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Estudiante_Sala).offset(skip).limit(limit).all()

# Obtener todos los estudiantes de una sala
def get_estudiantes_sala(db: Session, id_sala: int):
    return db.query(Estudiante_Sala).filter(Estudiante_Sala.sala_id == id_sala).all()

# Obtener todas las salas de un estudiante
def get_salas_estudiante(db: Session, id_estudiante: int):
    return db.query(Estudiante_Sala).filter(Estudiante_Sala.estudiante_id == id_estudiante).all()

# Obtener si un estudiante está en una sala
def get_estudiante_sala(db: Session, id_estudiante: int, id_sala: int):
    return db.query(Estudiante_Sala).filter(Estudiante_Sala.estudiante_id == id_estudiante).filter(Estudiante_Sala.sala_id == id_sala).first()

# Crear un estudiante en una sala
def create_estudiante_sala(db: Session, estudiante_sala: Estudiante_SalaCreate):
    db_estudiante_sala = Estudiante_Sala(**estudiante_sala.dict())
    db.add(db_estudiante_sala)
    db.commit()
    db.refresh(db_estudiante_sala)
    return db_estudiante_sala

# Eliminar un estudiante de una sala
def delete_estudiante_sala(db: Session, id_estudiante: int, id_sala: int):
    db_estudiante_sala = db.query(Estudiante_Sala).filter(Estudiante_Sala.estudiante_id == id_estudiante).filter(Estudiante_Sala.sala_id == id_sala).first()
    if db_estudiante_sala:
        db.delete(db_estudiante_sala)
        db.commit()
    return db_estudiante_sala

# Eliminar todos los estudiantes de una sala
def delete_estudiantes_sala(db: Session, id_sala: int):
    db_estudiantes_sala = db.query(Estudiante_Sala).filter(Estudiante_Sala.sala_id == id_sala).all()
    if db_estudiantes_sala:
        for estudiante_sala in db_estudiantes_sala:
            db.delete(estudiante_sala)
        db.commit()
    return db_estudiantes_sala

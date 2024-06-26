from sqlalchemy.orm import Session

from models.Estudiante_Sala import Estudiante_Sala


# Obtener todos los estudiantes de una sala
def get_estudiantes_sala(db: Session, id_sala: int):
    return db.query(Estudiante_Sala).filter(Estudiante_Sala.sala_id == id_sala).all()

# Obtener si un estudiante está en una sala
def get_estudiante_sala(db: Session, id_estudiante: int, id_sala: int):
    return db.query(Estudiante_Sala).filter(Estudiante_Sala.estudiante_id == id_estudiante).filter(Estudiante_Sala.sala_id == id_sala).first()


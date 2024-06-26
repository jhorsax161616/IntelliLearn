from sqlalchemy.orm import Session

from models.Estudiante_Sala import Estudiante_Sala

# Obtener todas las salas de un estudiante
def get_salas_estudiante(db: Session, id_estudiante: int):
    return db.query(Estudiante_Sala).filter(Estudiante_Sala.estudiante_id == id_estudiante).all()

# Eliminar todos los estudiantes de una sala
def delete_estudiantes_sala(db: Session, id_sala: int):
    db_estudiantes_sala = db.query(Estudiante_Sala).filter(Estudiante_Sala.sala_id == id_sala).all()
    if db_estudiantes_sala:
        for estudiante_sala in db_estudiantes_sala:
            db.delete(estudiante_sala)
        db.commit()
    return db_estudiantes_sala


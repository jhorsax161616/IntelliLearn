from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.orm import relationship

from config.database import Base

class Estudiante_Sala(Base):
    __tablename__ = "estudiantes_salas"

    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), primary_key=True)
    sala_id = Column(Integer, ForeignKey("salas.id"), primary_key=True )

    estudiante = relationship("Estudiante", back_populates="estudiantes_salas")
    sala = relationship("Sala", back_populates="estudiantes_salas")

    def __repr__(self):
        return f"<Estudiante_Sala {self.estudiante_id} {self.sala_id}>"

    def __str__(self):
        return f"{self.estudiante_id} {self.sala_id}"

    def __json__(self):
        return ["estudiante_id", "sala_id"]

    def __json_relations__(self):
        return ["estudiante", "sala"]
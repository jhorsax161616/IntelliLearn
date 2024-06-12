from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from config.database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(180), nullable=False)
    apellidos = Column(String(180), nullable=False)
    correo = Column(String(180), unique=True, index=True, nullable=False)
    universidad_id = Column(Integer, ForeignKey("universidades.id"), nullable=False)
    hashed_password = Column(String(250), nullable=True)

    universidad = relationship("Universidad", back_populates="estudiantes")
    salas = relationship("Sala", back_populates="estudiante")
    estudiantes_salas = relationship("Estudiante_Sala", back_populates="estudiante")

    def __repr__(self):
        return f"<Estudiante {self.nombres} {self.apellidos}>"
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    def __json__(self):
        return ["id", "nombres", "apellidos", "correo", "universidad_id", "hashed_password"]
    
    def __json_relations__(self):
        return ["universidad", "salas", "estudiantes_salas"]
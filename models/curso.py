from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from config.database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))
    universidad_id = Column(Integer, ForeignKey("universidades.id"), nullable=False)

    universidad = relationship("Universidad", back_populates="cursos")
    salas = relationship("Sala", back_populates="curso")

    def __repr__(self):
        return f"<Curso {self.nombre}>"
    
    def __str__(self):
        return f"{self.nombre}"
    
    def __json__(self):
        return ["id", "nombre", "descripcion", "universidad_id"]
    
    def __json_relations__(self):
        return ["universidad", "salas"]
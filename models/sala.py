from sqlalchemy import Integer, ForeignKey, Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from config.database import Base

class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))
    url_sala = Column(String(250), nullable=False)
    url_imagen = Column(String(250))
    horario = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)

    curso = relationship("Curso", back_populates="salas")
    estudiante = relationship("Estudiante", back_populates="salas")
    estudiantes_salas = relationship("Estudiante_Sala", back_populates="sala")

    def __repr__(self):
        return f"<Sala {self.nombre}>"
    
    def __str__(self):
        return f"{self.nombre}"
    
    def __json__(self):
        return ["id", "nombre", "descripcion", "url_sala", "url_imagen", "horario", "curso_id", "estudiante_id"]
    
    def __json_relations__(self):
        return ["curso", "estudiante"]
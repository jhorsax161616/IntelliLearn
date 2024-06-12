from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from config.database import Base

class Universidad(Base):
    __tablename__ = "universidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(250), nullable=False, unique=True)
    direccion = Column(String(250))
    correo = Column(String(180), unique=True, index=True)

    cursos = relationship("Curso", back_populates="universidad")
    estudiantes = relationship("Estudiante", back_populates="universidad")

    def __repr__(self):
        return f"<Universidad {self.nombre}>"
    
    def __str__(self):
        return f"{self.nombre}"
    
    def __json__(self):
        return ["id", "nombre", "direccion", "correo"]
    
    def __json_relations__(self):
        return ["cursos", "estudiantes"]
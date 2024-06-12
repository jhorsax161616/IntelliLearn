from fastapi import APIRouter, Response, status
from config.db import conn
from models.sala import salas
from schemas.sala import Sala
from starlette.status import HTTP_204_NO_CONTENT #Para poder enviar un estado 


sala = APIRouter()


@sala.get("/salas", response_model=list[Sala], tags=["salas"])
def get_salas():
    return conn.execute(salas.select()).fetchall()

@sala.post("/estudiantes", response_model=Sala, tags=["estudiantes"])
def create_sala(sala: Sala):
    # Creamos nuestro usuario como un diccionario para guardar los datos obtenidos
    nueva_sala = {"nombre": sala.nombre,
                "descripcion": sala.descripcion,
                "url_imagen": sala.url_imagen,
                "url_sala": sala.url_sala,
                "horario": sala.horario,
                "curso_id": sala.curso_id,
                "estudiante_id": sala.estudiante_id}

    # Guardando los datos en la base de datos
    result = conn.execute(salas.insert().values(nueva_sala))

    return conn.execute(salas.select().where(salas.c.id == result.lastrowid)).first()

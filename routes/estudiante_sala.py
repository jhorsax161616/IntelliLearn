from fastapi import APIRouter, Response, status
from config.db import conn
from models.estudiante_sala import estudiante_salas
from schemas.estudiante_sala import EstudianteSala
from starlette.status import HTTP_204_NO_CONTENT

estudiante_sala = APIRouter()
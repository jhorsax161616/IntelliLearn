from fastapi import APIRouter, Response, status
from config.database import conn
from models.curso import cursos
from schemas.curso import Curso
from starlette.status import HTTP_204_NO_CONTENT

curso = APIRouter()

# Todo el manejo de los cursos sera interno, no se podra hacer un CRUD de cursos
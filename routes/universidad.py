from fastapi import APIRouter, Response, status
from config.db import conn
from models.universidad import universidades
from schemas.universidad import Universidad
from starlette.status import HTTP_204_NO_CONTENT

universidad = APIRouter()

# Todo el manejo de las universidades sera interno, no se podra hacer un CRUD de universidades
from fastapi import APIRouter, Response, status
from config.database import conn
from models.estudiante import estudiantes
from schemas.estudiante import Estudiante
from starlette.status import HTTP_204_NO_CONTENT #Para poder enviar un estado 

from cryptography.fernet import Fernet  # para cifrar contraseñas

key = Fernet.generate_key()  # Genera los caracteres aleatorios para el cifrado
cifrado = Fernet(key)  # La funcion para cifrar

estudiante = APIRouter()


@estudiante.get("/estudiantes", response_model=list[Estudiante], tags=["estudiantes"])
def get_estudiantes():
    return conn.execute(estudiantes.select()).fetchall()


@estudiante.post("/estudiantes", response_model=Estudiante, tags=["estudiantes"])
def create_estudiante(estudiante: Estudiante):
    # Creamos nuestro usuario como un diccionario para guardar los datos obtenidos
    new_estudiante = {"nombres": estudiante.nombres, "apellidos": estudiante.apellidos, "correo": estudiante.correo, "universidad_id": estudiante.universidad_id}

    # Se tiene que encriptar las contrasenas pero antes tenemos que cofificarlas en formatos como el utf-8
    new_estudiante["hashed_password"] = cifrado.encrypt(estudiante.hashed_password.encode("utf-8"))

    # Guardando los datos en la base de datos
    # Si lo guardamos en una variable podria aceptar distintos metodos como el .lastrowid para que nos debuelva el id del usuario creado
    result = conn.execute(estudiantes.insert().values(new_estudiante))

    '''retornamos el usuario creado
    Ejecutamos una consulta SELECT de la tabla "estudiantes" con el metodo execute de la coneccion y lo condicionamos con where
    En estudiantes.c.id -> La "c" hace referencia a la columana "id" en este caso'''
    return conn.execute(estudiantes.select().where(estudiantes.c.id == result.lastrowid)).first()


@estudiante.get("/estudiantes/{id}", response_model=Estudiante, tags=["estudiantes"])
def get_estudiante(id: str):
    return conn.execute(estudiantes.select().where(estudiantes.c.id == id)).first()


@estudiante.delete("/estudiantes/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["estudiantes"])
def delete_estudiante(id: str):

    # Una pequena validacion de que si el usuario existe
    if get_estudiante(id) == None:
        return "Usuario no encontrado"
    # Borramos
    conn.execute(estudiantes.delete().where(estudiantes.c.id == id))

    return Response(status_code=HTTP_204_NO_CONTENT)


@estudiante.put("/estudiantes/{id}", response_model=Estudiante, tags=["estudiantes"])
def update_estudiante(id: str, estudiante: Estudiante):
    conn.execute(estudiantes.update().values(nombres=estudiante.nombres, apellidos=estudiante.apellidos, correo=estudiante.correo,
                universidad_id=estudiante.universidad_id, hashed_password=cifrado.encrypt(estudiante.hashed_password.encode("utf-8"))).where(estudiantes.c.id == id))
    return conn.execute(estudiantes.select().where(estudiantes.c.id == id)).first()
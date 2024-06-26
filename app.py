from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.estudiante import estudiante
from routes.universidad import universidad
from routes.curso import curso
from routes.sala import sala
from routes.estudiante_sala import estudiante_sala
from routes.estudiante_logica import estudiante_logica
from routes.sala_logica import sala_logica

from starlette.requests import Request

from config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend de IntelliLearn",
    description="Esta es toda la parte lógica del backend de IntelliLearn, donde se manejan las rutas y la lógica de la aplicación.",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "IntelliLearn",
            "description": "Logica de IntelliLearn"
        }
    ]
)

app.include_router(universidad, tags=["Universidades - CRUD"])
app.include_router(estudiante, tags=["Estudiantes - CRUD"])
app.include_router(curso, tags=["Cursos - CRUD"])
app.include_router(sala, tags=["Salas - CRUD"])
app.include_router(estudiante_sala, tags=["Estudiantes en Salas - CRUD"])
app.include_router(estudiante_logica, tags=["Lógica de Estudiantes"])
app.include_router(sala_logica, tags=["Lógica de Salas"])

templates = Jinja2Templates(directory="templates")
# Montar el directorio de archivos estáticos
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request, 'estudiante': None, 'isLogued': False}
    )


@app.get('/principal')
def principal(request: Request):
    return templates.TemplateResponse(
        name='welcome.html',
        context={"request": request, 'estudiante': None, 'isLogued': False}
    )


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        name='login.html',
        context={"request": request}
    )

@app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse(
        name='register.html',
        context={"request": request}
    )

@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse(
        name='contactanos.html',
        context={"request": request}
    )
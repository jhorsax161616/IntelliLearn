from fastapi import FastAPI
from routes.estudiante import estudiante
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

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

app.include_router(estudiante)

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
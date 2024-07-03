from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db # Para poder obtener la base de datos

from crud import estudiante as crud
from schemas.estudiante import EstudianteInDB, EstudianteLogin

from passlib.context import CryptContext  # para cifrar contraseñas
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


login = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "c9c78e054247465cf2af1b1548f9ba75d983a76a696001adf2cac427ba62d829"
ALGORITHM = "HS256"

def authenticate_user(correo: str, password: str, db: Session):
    db_estudiante = crud.get_estudiante_by_correo(db, correo=correo)
    if not db_estudiante:
        raise HTTPException(status_code=401, detail="Usuario no encontrado", headers={"WWW-Authenticate": "Bearer"})
    if not pwd_context.verify(password, db_estudiante.hashed_password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta", headers={"WWW-Authenticate": "Bearer"})
    return db_estudiante

def create_access_token(data: dict, time_expire: Union[datetime, None] = None):
    to_encode = data.copy()
    if time_expire is None:
        time_expire = timedelta(minutes=5)

    to_encode.update({"exp": datetime.utcnow() + time_expire})
    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="No se pudo validar las credenciales", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo: str = payload.get("sub")
        if correo is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_estudiante_by_correo(db, correo=correo)
    if user is None:
        raise credentials_exception
    return user

@login.post("/token", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(correo=form_data.username, password=form_data.password, db=db)
    access_token_expires = timedelta(minutes=5)
    access_token = create_access_token(data={"sub": user.correo}, time_expire=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@login.get("/users/me", response_model=EstudianteInDB)
def read_users_me(current_user: EstudianteInDB = Depends(get_current_user)):
    return current_user
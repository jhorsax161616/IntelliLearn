from sqlalchemy import Integer, Table, Column, String
from config.db import meta, engine

estudiantes = Table("estudiantes", meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("nombres", String(180)),
    Column("apellidos", String(180)),
    Column("correo", String(180), unique=True, index=True),
    Column("universidad", String(180)),
    Column("hashed_password", String(180), nullable=True),)

meta.create_all(engine)
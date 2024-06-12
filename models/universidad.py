from sqlalchemy import Integer, Table, Column, String
from config.db import meta, engine

universidades = Table("universidades", meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("nombre", String(250)),
    Column("direccion", String(250)),
    Column("correo", String(180), unique=True, index=True))

meta.create_all(engine)
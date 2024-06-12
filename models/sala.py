from sqlalchemy import Integer, Table, Column, String, DateTime
from config.db import meta, engine

salas = Table("salas", meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("nombre", String(250)),
    Column("descripcion", String(250)),
    Column("url_sala", String(250)),
    Column("url_imagen", String(250)),
    Column("horario", DateTime),
    Column("curso_id", Integer),
    Column("estudiante_id", Integer))

meta.create_all(engine)
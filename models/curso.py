from sqlalchemy import Integer, Table, Column, String
from config.db import meta, engine

cursos = Table("cursos", meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("nombre", String(250)),
    Column("descripcion", String(250)),
    Column("universidad_id", Integer))

meta.create_all(engine)
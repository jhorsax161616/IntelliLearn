from sqlalchemy import Integer, Table, Column, String
from config.db import meta, engine

estudiante_salas = Table("estudiante_salas", meta,
    Column("estudiante_id", Integer, nullable=False),
    Column("sala_id", Integer), nullable=False)

meta.create_all(engine)
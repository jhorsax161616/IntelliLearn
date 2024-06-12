from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:musicos.-.-@localhost:3306/IntelliLearn")

meta = MetaData()

conn = engine.connect()
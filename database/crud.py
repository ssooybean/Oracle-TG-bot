from config.config import load_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models_sql import *

config = load_config("./config/.env")

engine = create_engine(
    f"""postgresql+psycopg2://{config.db.db_user}:{config.db.db_password}@{config.db.db_host}/{config.db.database}"""
)
engine.connect()

Base.metadata.create_all(bind=engine)

Session = sessionmaker(autoflush=False, bind=engine)

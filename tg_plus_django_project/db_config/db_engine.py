from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from tg_plus_django_project.config import *

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}")
session = Session(bind=engine)

Base = automap_base()
Base.prepare(engine)
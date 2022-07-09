from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# flask rest assignment with jwt for the project
flask_rest_jwt = 'postgresql+psycopg2://postgres:admin@localhost/Flask_Rest_Assignment_with_JWT'


Base = declarative_base()

# create table for every class that inherits from Base
def create_all_entities():
    Base.metadata.create_all(engine)

# creates the flights_db to run the sql operations
Session = sessionmaker()
engine = create_engine(flask_rest_jwt, echo=True)
local_session = Session(bind=engine)
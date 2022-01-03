from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

tourists_db = 'postgresql+psycopg2://postgres:admin@localhost/tourists_db'


Base = declarative_base()

# create table for every class that inherits from Base
def create_all_entities():
    Base.metadata.create_all(engine)

# creates the flights_db to run the sql operations
Session = sessionmaker()
engine = create_engine(tourists_db, echo=True)
local_session = Session(bind=engine)
# name the db flights_db (in the connection string)
# create a class for each table (inherit from Base):
# flights, countries, tickets, airline_companies, users, customers, user_roles, administrators.
# add the constraints to the fields (according to the diagrams)

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# flights_db for the project
flights_db = 'postgresql+psycopg2://postgres:admin@localhost/flights_db'


Base = declarative_base()

# create table for every class that inherits from Base
def create_all_entities():
    Base.metadata.create_all(engine)

# creates the flights_db to run the sql operations
Session = sessionmaker()
engine = create_engine(flights_db, echo=True)
local_session = Session(bind=engine)
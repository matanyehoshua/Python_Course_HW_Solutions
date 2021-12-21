# name the db flights_db (in the connection string)
# create a class for each table (inherit from Base):
# flights, countries, tickets, airline_companies, users, customers, user_roles, administrators.
# add the constraints to the fields (according to the diagrams)

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

# created table for airline_companies
class Airline_companies(Base):
    __tablename__ = 'airline_companies'

    # airline_companies table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String(), unique=True)
    country_id = Column(Integer(), ForeignKey('countries.id'))
    user_id = Column(BigInteger(), ForeignKey('users.id'), unique=True)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id}>'
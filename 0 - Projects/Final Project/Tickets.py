# name the db flights_db (in the connection string)
# create a class for each table (inherit from Base):
# flights, countries, tickets, airline_companies, users, customers, user_roles, administrators.
# add the constraints to the fields (according to the diagrams)

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

# created table for tickets
class Tickets(Base):
    __tablename__ = 'tickets'

    # tickets table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger(), ForeignKey('flights.id'), unique=True)
    customer_id = Column(BigInteger(), ForeignKey('customers.id'), unique=True)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} flight_id={self.flight_id} customer_id={self.customer_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} flight_id={self.flight_id} customer_id={self.customer_id}>'
from datetime import datetime
from sqlalchemy import Table, Column, Integer, BigInteger, String, DateTime, ForeignKey, REAL, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from db_config import Base
from Flights import Flights
from Customers import Customers

# created table for tickets
class Tickets(Base):
    __tablename__ = 'tickets'

    # tickets table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger(), ForeignKey('flights.id'), unique=True)
    customer_id = Column(BigInteger(), ForeignKey('customers.id'), unique=True)
    # relationships
    __table_args__ = (UniqueConstraint('flight_id', 'customer_id', name='una_1'),)
    flights_id = relationship('Flights', backref=backref('tickets', uselist=True))
    customers_id = relationship('Customers', backref=backref('tickets', uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} flight_id={self.flight_id} customer_id={self.customer_id} \
__table_args__={self.__table_args__} flights_id={self.flights_id} customers_id={self.customers_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} flight_id={self.flight_id} customer_id={self.customer_id} \
__table_args__={self.__table_args__} flights_id={self.flights_id} customers_id={self.customers_id}>'
from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for association with Tickets - to make M:M relationship with Flights and Customers
class Flightscustomers(Base):
    __tablename__ = 'flightscustomers'

    # user_roles table
    flight_id = Column(BigInteger(), ForeignKey('flights'), unique=False)
    customer_id = Column(BigInteger(), ForeignKey('customers'), unique=False)
    # relationships:
    flights_id = relationship("Flights", backref=backref("Flightscustomers", uselist=True))
    customers_id = relationship("Customers", backref=backref("Flightscustomers", uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<flight_id={self.flight_id} customer_id={self.customer_id} flights_id={self.flights_id} \
customers_id={self.customers_id}>'

    # __str__
    def __str__(self):
        return f'<flight_id={self.flight_id} customer_id={self.customer_id} flights_id={self.flights_id} \
customers_id={self.customers_id}>'
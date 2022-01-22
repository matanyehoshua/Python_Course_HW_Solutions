from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for flights
class Flights(Base):
    __tablename__ = 'flights'

    # flights table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    airline_company_id = Column(BigInteger(), ForeignKey('airline_companies.id'))
    origin_country_id = Column(BigInteger(), ForeignKey('countries.id'))
    destination_country_id = Column(BigInteger(), ForeignKey('countries.id'))
    departure_time = Column(DateTime(), default=datetime.utcnow())
    landing_time = Column(DateTime(), default=datetime.utcnow())
    remaining_tickets = Column(Integer())
    # relationships:
    airline_company = relationship("Airline_companies", backref=backref("flights", uselist=True))
    origin_country = relationship("Countries", foreign_keys=[origin_country_id], uselist=True)
    destination_country = relationship("Countries", foreign_keys=[destination_country_id], uselist=True)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} airline_company_id={self.airline_company_id} \
origin_country_id={self.origin_country_id} destination_country_id={self.destination_country_id} \
departure_time={self.departure_time} landing_time={self.landing_time} \
remaining_tickets={self.remaining_tickets} airline_company={self.airline_company} \
 origin_country={self.origin_country} destination_country={self.destination_country}>'
    # __str__
    def __str__(self):
        return f'<id={self.id} airline_company_id={self.airline_company_id} \
origin_country_id={self.origin_country_id} destination_country_id={self.destination_country_id} \
departure_time={self.departure_time} landing_time={self.landing_time} \
remaining_tickets={self.remaining_tickets} airline_company={self.airline_company}   \
origin_country={self.origin_country} destination_country={self.destination_country}>'

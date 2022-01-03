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
    origin_country_id = Column(Integer(), ForeignKey('countries.id'))
    destination_country_id = Column(Integer, ForeignKey('countries.id'))
    departure_time = Column(DateTime(), default=datetime.utcnow())
    landing_time = Column(DateTime(), default=datetime.utcnow())
    remaining_tickets = Column(Integer())
    flight_id = Column(BigInteger, ForeignKey('flightscustomers.id'), unique=False, nullable=False)
    # relationships:
    airline_companies_id = relationship("Airline_companies", backref=backref("flights", uselist=True))
    countries_id = relationship("Countries", backref=backref("flights", uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} airline_company_id={self.airline_company_id} \
origin_country_id={self.origin_country_id} destination_country_id={self.destination_country_id} \
departure_time={self.departure_time} landing_time={self.landing_time} \
remaining_tickets={self.remaining_tickets} flight_id={self.flight_id} \
airline_companies_id={self.airline_companies_id} countries_id={self.countries_id}>'
    # __str__
    def __str__(self):
        return f'<id={self.id} airline_company_id={self.airline_company_id} \
origin_country_id={self.origin_country_id} destination_country_id={self.destination_country_id} \
departure_time={self.departure_time} landing_time={self.landing_time} \
remaining_tickets={self.remaining_tickets} flight_id={self.flight_id} \
airline_companies_id={self.airline_companies_id} countries_id={self.countries_id}>'

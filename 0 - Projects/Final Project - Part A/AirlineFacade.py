from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Customers import Customers
from Tickets import Tickets
from Airline_companies import Airline_companies
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from exceptions.CustomerDoesNotExistException import CustomerDoesNotExistException
from exceptions.TicketsDoesNotExistException import TicketsDoesNotExistException
from exceptions.InvalidTokenException import InvalidTokenException
from db_config import local_session, create_all_entities
from FacadeBase import FacadeBase
from AnonymousFacade import AnonymousFacade
from abc import ABC, abstractmethod
# needs to inherit from FacadeBase
repo = RepoDb(local_session)


class AirlineFacade(AnonymousFacade):
    def __init__(self):
        super().__init__()
        self.repo = RepoDb(local_session)

    def get_flights_by_airline(self, airline, token):
        if not self.check_token(Airline_companies, token):
            raise InvalidTokenException('the login token is invalid!')
        flights = repo.get_all(Flights).filter(lambda f: f.airline_company_id == airline.id)
        if flights is None:
            raise AirlineCompanyDoesNotExistException('there are no airline companies!')
        else:
            return flights

    def update_airline(self, airline, token):
        if not self.check_token(Airline_companies, token):
            raise InvalidTokenException('the login token is invalid!')
        db_airline = repo.get_by_id(Airline_companies, airline)
        if db_airline is None:
            raise AirlineCompanyDoesNotExistException('there are no airline companies!')
        repo.update_by_column_value(Airline_companies, Airline_companies.name)


    def update_flight(self, flight, token):
        if not self.check_token(Airline_companies, token):
            raise InvalidTokenException('the login token is invalid!')
        error_check = repo.get_by_id(Airline_companies, Airline_companies.id)
        if error_check is None:
            raise FlightDoesNotExistException('there are no airline companies!')
        repo.update_by_id(self, Flights, flight)


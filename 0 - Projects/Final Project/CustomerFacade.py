from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from db_config import local_session, create_all_entities
from abc import ABC, abstractmethod
# needs to inherit from AnonymousFacade
repo = RepoDb(local_session)


class CustomerFacade:
    def __init__(self): # **to check**
        self.repo = RepoDb(local_session)

    def update_customer(self, customer):
        pass

    def add_ticket(self, ticket):
        pass

    def remove_ticket(self, ticket):
        pass

    def get_tickets_by_customer(self, customer):
        pass

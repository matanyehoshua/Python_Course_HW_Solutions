from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Customers import Customers
from Tickets import Tickets
from Airline_companies import Airline_companies
from Administrators import Administrators
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from exceptions.CustomerDoesNotExistException import CustomerDoesNotExistException
from exceptions.TicketsDoesNotExistException import TicketsDoesNotExistException
from exceptions.AdministratorDoesNotExistException import AdministratorDoesNotExistException
from db_config import local_session, create_all_entities
from abc import ABC, abstractmethod
# needs to inherit from AnonymousFacade
repo = RepoDb(local_session)


class AdministratorFacade:
    def __init__(self): # **to check**
        self.repo = RepoDb(local_session)

    def get_all_customers(self):
        error_check = repo.get_by_id(Customers, Customers.id)
        if error_check is None:
            raise CustomerDoesNotExistException('there are no customers!')
        repo.get_all(self, Customers)

    def add_airline(self, airline):
        repo.add(Airline_companies)

    def add_customer(self, customer):
        repo.add(Customers)

    def add_administrator(self, administrator):
        repo.add(Administrators)

    def remove_airline(self, airline):
        error_check = repo.get_by_id(Airline_companies, Airline_companies.id)
        if error_check is None:
            raise AirlineCompanyDoesNotExistException('there are no Airline Companies!')
        repo.delete_by_id(Airline_companies, Airline_companies.name, Airline_companies.id)

    def remove_customer(self, customer):
        error_check = repo.get_by_id(Customers, Customers.id)
        if error_check is None:
            raise CustomerDoesNotExistException('there are no customers!')
        repo.delete_by_id(Customers, Customers.user_id, Customers.id)

    def remove_administrator(self, administrator):
        error_check = repo.get_by_id(Administrators, Administrators.id)
        if error_check is None:
            raise AdministratorDoesNotExistException('there are no administrators!')
        repo.delete_by_id(Administrators, Administrators.user_id, Administrators.id)

    def add_airline(self, airline):
        repo.add(Airline_companies)
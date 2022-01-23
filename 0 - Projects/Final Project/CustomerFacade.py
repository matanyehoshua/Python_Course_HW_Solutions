from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Customers import Customers
from Tickets import Tickets
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from exceptions.CustomerDoesNotExistException import CustomerDoesNotExistException
from exceptions.TicketsDoesNotExistException import TicketsDoesNotExistException
from db_config import local_session, create_all_entities
from abc import ABC, abstractmethod
# needs to inherit from AnonymousFacade
repo = RepoDb(local_session)


class CustomerFacade:
    def __init__(self): # **to check**
        self.repo = RepoDb(local_session)

    def update_customer(self, customer):
        error_check = repo.get_by_id(Customers, Customers.id)
        if error_check is None:
            raise CustomerDoesNotExistException('there are no customers!')
        repo.update_by_id(self, customer)

    def add_ticket(self, ticket):
        repo.add(self, Tickets)

    def remove_ticket(self, ticket):
        error_check = repo.get_by_id(Tickets, Tickets.id)
        if error_check is None:
            raise TicketsDoesNotExistException('there are no tickets!')
        repo.delete_by_id(self, Tickets.customer_id, id)

    def get_tickets_by_customer(self, customer):
        error_check = repo.get_by_id(Customers, Customers.id)
        if error_check is None:
            raise CustomerDoesNotExistException('there are no customers!')
        repo.get_by_id(self, Customers, Customers.id)

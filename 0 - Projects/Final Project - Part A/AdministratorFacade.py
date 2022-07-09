from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Customers import Customers
from Tickets import Tickets
from Airline_companies import Airline_companies
from Administrators import Administrators
from FacadeBase import FacadeBase
from AnonymousFacade import AnonymousFacade
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


class AdministratorFacade(AnonymousFacade):
    def __init__(self):
        super().__init__()
        self.repo = RepoDb(local_session)

    def get_all_customers(self):
        customers = repo.get_all(Customers)
        if customers is None:
            raise CustomerDoesNotExistException('there are no customers!')
        else:
            return customers

    def add_airline(self, airline):
        repo.add(airline)

    def add_customer(self, customer):
        repo.add(customer)

    def add_administrator(self, administrator):
        repo.add(administrator)

    def remove_airline(self, airline_id):
        error_check = repo.get_by_id(Airline_companies, airline_id)
        if error_check is None:
            raise AirlineCompanyDoesNotExistException('there are no Airline Companies!')
        # we need to remove all flights first (starting with tickets)
        flights_list = repo.get_all(Flights)
        tickets = repo.get_all(Tickets)

        for ticket in tickets:
            repo.delete_by_id(Tickets, Tickets.id, ticket.id)

        # then we delete the flights
        for flight in flights_list:
            repo.delete_by_id(Flights, Flights.id, flight.id)

        # and finally we can remove the airline companies
        repo.delete_by_id(Airline_companies, Airline_companies.id, airline_id)

    def remove_customer(self, customers):
        error_check = repo.get_by_id(Customers, Customers.id)
        if error_check is None:
            raise CustomerDoesNotExistException('there are no customers!')
        repo.delete_by_id(Customers, customers, Customers.id)

    def remove_administrator(self, administrators):
        error_check = repo.get_by_id(Administrators, administrators.id)
        if error_check is None:
           raise AdministratorDoesNotExistException('there are no administrators!')
        repo.delete_by_id(Administrators, administrators.id, administrators.id)
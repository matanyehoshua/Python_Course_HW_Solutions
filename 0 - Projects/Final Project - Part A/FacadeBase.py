from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Customers import Customers
from Administrators import Administrators
from User_roles import User_roles
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from db_config import local_session, create_all_entities
from abc import ABC, abstractmethod

# example:     def add_flights(self, flights):
#         airline_company = flights.airline_company
#         ac = repo.get_by_id(Airline_companies, airline_company.id)
#         if ac is None:
#             raise CompanyNotExistsException('The company does not exist!')
#         repo.add(flights)
repo = RepoDb(local_session)


class FacadeBase:
    @abstractmethod
    def __init__(self):
        self.repo = RepoDb(local_session)

    def check_token(self, user_type, token):
        if user_type == Administrators and token.role == 1:
            return True
        if user_type == Airline_companies and token.role == 2:
            return True
        if user_type == Customers and token.role == 3:
            return True
    # Fourth option should be anonymous user and should be selected automatically when others are invalid
        return False

    def get_all_flights(self):
        return repo.get_all(Flights)

    def get_flight_by_id(self, flights_id):
        error_check = repo.get_by_id(Flights, flights_id)
        if error_check is None:
            raise FlightDoesNotExistException('The flight does not exist!')
        return repo.get_by_id(Flights, Flights.id)

    def get_flights_by_parameters(self, origin_country_id, destination_country_id, date):
        if Flights is None:
            raise FlightDoesNotExistException('There are no flights')
        return repo.get_by_column_value(origin_country_id, destination_country_id, date)

    def get_all_airlines(self, airline_companies_id, direction=asc):
        error_check = repo.get_by_id(Airline_companies, airline_companies_id)
        if error_check is None:
            raise AirlineCompanyDoesNotExistException('there are no listed airline companies!')
        return repo.get_all_order_by(Airline_companies, Airline_companies.name).order_by(direction(Airline_companies.name)).all()

    def get_airline_by_id(self, airline_companies_id):
        error_check = repo.get_by_id(Airline_companies, airline_companies_id)
        if error_check is None:
            raise AirlineCompanyDoesNotExistException('there are no listed airline companies!')
        return repo.get_by_id(Airline_companies, airline_companies_id)

    def get_all_countries(self, countries_id):
        error_check = repo.get_by_id(Countries, countries_id)
        if error_check is None:
            raise CountriesDoesNotExist('there are no listed Countries!')
        return repo.get_all(Countries)

    def get_country_by_id(self, countries_id):
        error_check = repo.get_by_id(Countries, countries_id)
        if error_check is None:
            raise CountriesDoesNotExist('there are no listed Countries!')
        return repo.get_by_id(Countries, countries_id)
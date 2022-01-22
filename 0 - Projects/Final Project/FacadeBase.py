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

# example:     def add_flights(self, flights):
#         airline_company = flights.airline_company
#         ac = repo.get_by_id(Airline_companies, airline_company.id)
#         if ac is None:
#             raise CompanyNotExistsException('The company does not exist!')
#         repo.add(flights)
repo = RepoDb(local_session)


class FacadeBase:
    @abstractmethod
    def __init__(self): # **to check**
        self.repo = RepoDb(local_session)

    def get_all_flights(self, Flights):
        repo.get_all(self, Flights)

    def get_flight_by_id(self, flights, id):
        error_check = repo.get_by_id(Flights, flights.id)
        if error_check is None:
            raise FlightDoesNotExistException('The flight does not exist!')
        repo.get_by_id(self, Flights, id)

    def get_flights_by_parameters(self, flights, origin_country_id, destination_country_id, date):
        repo.get_by_column_value(self, Flights).filter(flights.origin_country_id, flights.destination_country_id, flights.departure_time)
        pass

    def get_all_airlines(self, airline_companies, direction=asc):
        error_check = repo.get_by_id(Airline_companies, Airline_companies.id)
        if error_check is None:
            raise AirlineCompanyDoesNotExistException('there are no listed airline companies!')
        repo.get_all_order_by(Airline_companies).order_by(direction(Airline_companies.name)).all()

    def get_airline_by_id(self, airline_companies, id):
        error_check = repo.get_by_id(Airline_companies, Airline_companies.id)
        if error_check is None:
            raise AirlineCompanyDoesNotExistException('there are no listed airline companies!')
        repo.get_by_id(self,Airline_companies, airline_companies.id)

    def get_all_countries(self, countries, id):
        error_check = repo.get_by_id(Countries, countries.id)
        if error_check is None:
            raise CountriesDoesNotExist('there are no listed Countries!')
        repo.get_all(self, Countries)

    def get_country_by_id(self, countries, id):
        error_check = repo.get_by_id(Countries, countries.id)
        if error_check is None:
            raise CountriesDoesNotExist('there are no listed Countries!')
        repo.get_by_id(Countries, countries.id)

from RepoDb import RepoDb
from sqlalchemy import text
from Flights import Flights
from db_config import local_session, create_all_entities

repo = RepoDb(local_session)
class FlightsFacade:
    def add_flights(self, flights):
        repo.add(flights)
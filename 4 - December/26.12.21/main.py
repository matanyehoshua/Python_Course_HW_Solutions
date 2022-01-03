from RepoDb import RepoDb
from db_config import local_session, create_all_entities
from Tourist import Tourist
from Attraction import Attraction
from Visit import Visit

# create tables
create_all_entities()

repo = RepoDb(local_session)

repo.reset_auto_inc(Tourist)
repo.reset_auto_inc(Attraction)
repo.reset_auto_inc(Visit)

# adding tourists to the table
repo.add(Tourist(id=1, name='Yuki', origin_country='Japan'))
repo.add(Tourist(id=2, name='John Cena', origin_country='USA'))
# adding attractions to the table
repo.add(Attraction(id=1, name='Eiffel Tower', price=16.60))
repo.add(Attraction(id=2, name='Statue of Liberty', price=23.50))
# adding visits to the table
repo.add(Visit(id=1, tourist_id=1, attraction_id=1, year_of_visit=2020))
repo.add(Visit(id=2, tourist_id=1, attraction_id=2, year_of_visit=2021))
repo.add(Visit(id=3, tourist_id=2, attraction_id=1, year_of_visit=2021))
repo.add(Visit(id=4, tourist_id=2, attraction_id=2, year_of_visit=2022))




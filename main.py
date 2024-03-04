#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
data = data_manager.get_data()["prices"]

for location in data:
    if location["iataCode"] == "":
        data_manager.add_codes(location["id"], location["city"])
        flight_search.getIataCode(location["city"])

# pprint(data)
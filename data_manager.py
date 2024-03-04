import requests
from flight_search import FlightSearch
SHEETLY_ENDPOINT = "https://api.sheety.co/7dd2f589e67edda0fb26b95f701af3b3/myFlightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data(self):
        response = requests.get(url="https://api.sheety.co/7dd2f589e67edda0fb26b95f701af3b3/myFlightDeals/prices")
        response.raise_for_status()
        data = response.json()
        return data

    def add_codes(self, id, city):
        flight_search = FlightSearch()
        body = {
            "price": {
                "iataCode": flight_search.getIataCode(city),
            }
        }
        response = requests.put(url=f"{SHEETLY_ENDPOINT}/{id}", json=body)
        response.raise_for_status()
        print(response.text)


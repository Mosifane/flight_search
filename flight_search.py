import requests
from datetime import datetime

LOCATIONS_API_ENDPOINT = "https://api.tequila.kiwi.com/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def getIataCode(self, city):
        header = {
            "apikey": "ozDHAVX7RB1GV9BbwMrk614fSOCvOCDF"
        }
        parameters = {
            "term": city,
        }
        response = requests.get(url=f"{LOCATIONS_API_ENDPOINT}locations/query", headers=header, params=parameters)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        print(code)
        return code

    def find_flights(self):
        fly_from = "LON"
        todays_Date = datetime.now().strftime("%w/%m/%Y")


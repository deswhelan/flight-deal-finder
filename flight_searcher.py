import config
from amadeus import Client, Location, ResponseError

# TODO: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# This class is responsible for talking to the Flight Search API.
class FlightSearcher:
    def __init__(self):
        self.api_key = config.AMADEUS["api_key"]
        self.api_secret = config.AMADEUS["api_secret"]

    def get_iata_codes(self, city_names):
        """Returns a list of tuples representing a city name and that city's IATA code"""
        iata_codes = []

        amadeus = Client(
            client_id=self.api_key,
            client_secret=self.api_secret
        )

        for city_name in city_names:
            try:
                response = amadeus.reference_data.locations.get(
                    keyword=city_name,
                    subType=Location.CITY
                )
            except ResponseError as error:
                print(error)

            # TODO: stretch - handle cities "missing" from Amadeus test data
            if response.data:
                for response_datum in response.data:
                    # Exclude potential false positives (e.g. "San Sebastian Gomera" being returned on search for "San Sebastian")
                    if response_datum["name"].lower() == city_name.lower():
                        iata_codes.append((city_name, response_datum["address"]["cityCode"]))

        return iata_codes
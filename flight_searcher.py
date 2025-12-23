import config
from amadeus import Client, Location, ResponseError

# TODO: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# This class is responsible for talking to the Flight Search API.
class FlightSearcher:
    def __init__(self):
        self.api_key = config.AMADEUS["api_key"]
        self.api_secret = config.AMADEUS["api_secret"]

    def find_cheap_flights(self):
        # TODO: Get city names from Sheets
        # TODO: Get IATA code for each city
        # TODO: Populate google Sheets with IATA code(s)

        amadeus = Client(
            client_id= self.api_key,
            client_secret= self.api_secret
        )

        try:
            response = amadeus.reference_data.locations.get(
                keyword='Dublin',
                subType=Location.AIRPORT
            )
            # print(response.data)
            print(response.result)
        except ResponseError as error:
            print(error)


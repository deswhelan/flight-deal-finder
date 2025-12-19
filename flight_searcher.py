import config
import requests

# TODO: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# This class is responsible for talking to the Flight Search API.
class FlightSearcher:
    def __init__(self):
        self.api_key = config.AMADEUS["api_key"]
        self.api_secret = config.AMADEUS["api_secret"]

    def find_cheap_flights(self):
        url = ""

        body = {

        }

        headers = {

        }


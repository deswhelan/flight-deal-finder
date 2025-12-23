import config
import requests

#This class is responsible for talking to the Google Sheet.
class SheetManager:
    def __init__(self):
        self.endpoint = config.SHEETY["endpoint"]
        self.bearer_token = config.SHEETY["bearer_token"]
        self.sheet_data = self.get_sheet_data()
        self.city_names = self.get_city_names()

    def get_sheet_data(self):
        """Returns a list of dictionaries representing the data in the Google sheet as determined by the file. Data retrieved via external API call to Sheety"""
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
        }

        response = requests.get(self.endpoint, headers=headers)
        response.raise_for_status()

        return response.json()["prices"]

    def get_city_names(self):
        """returns a list representing the city name(s) present in the sheet data"""
        city_names = []

        for sheet_datum in self.sheet_data:
            city_names.append(sheet_datum["city"])

        return city_names
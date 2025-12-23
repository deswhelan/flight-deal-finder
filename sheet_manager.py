import config
import requests

#This class is responsible for talking to the Google Sheet.
class SheetManager:
    def __init__(self):
        self.endpoint = config.SHEETY["endpoint"]
        self.headers = {
            "Authorization": f"Bearer {config.SHEETY["bearer_token"]}",
        }
        self.sheet_data = self.get_sheet_data()
        self.city_names = self.get_city_names()

    def get_sheet_data(self):
        """Returns a list of dictionaries representing the data in the Google sheet as determined by the file. Data retrieved via external API call to Sheety"""
        response = requests.get(self.endpoint, headers=self.headers)
        response.raise_for_status()

        return response.json()["prices"]

    def get_city_names(self):
        """returns a list representing the city name(s) present in the sheet data"""
        city_names = []

        for row in self.sheet_data:
            city_names.append(row["city"])

        return city_names

    def save_iata_codes(self, iata_codes):
        """saves IATA codes to the row for the associated city on google sheet"""
        for iata_code in iata_codes:
            city_name = iata_code[0]
            code = iata_code[1]

            row = next((row for row in self.sheet_data if row["city"].lower() == city_name.lower()))
            row_id = row["id"]

            body = {
                "price": {
                    # Sheety camelCases all json keys.
                    # E.g. if the header on the Google sheet is "IATA Code", we must provide the key below
                    "iataCode": code
                }
            }

            response = requests.put(f"{self.endpoint}/{row_id}", json=body, headers=self.headers)
            response.raise_for_status()
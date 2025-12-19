import config
from twilio.rest import Client

# TODO: The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates.

# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self):
        self.account_sid = config.TWILIO["account_sid"]
        self.auth_token = config.TWILIO["auth_token"]
        self.from_number = config.TWILIO["from"]
        self.to_number = config.TWILIO["to"]

    def send_notification(self, cheap_flights):
        client = Client(self.account_sid, self.auth_token)

        for cheap_flight in cheap_flights:
            body = f"Low price alert! Only €{cheap_flight["price"]} to fly from {cheap_flight["departure_airport"]} to {cheap_flight["arrival_airport"]}, from {cheap_flight["outbound_flight_date"]} until {cheap_flight["return_flight_date"]}"

            message = client.messages.create(
                from_=self.from_number,
                body=body,
                to=self.to_number
            )
            print(message.status)
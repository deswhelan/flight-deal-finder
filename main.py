from sheet_manager import SheetManager
from flight_searcher import FlightSearcher
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_searcher

# Requirements:

    # TODO: Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_commercial_airports).

    # TODO: If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.

sheet_manager = SheetManager()
flight_searcher = FlightSearcher()
notification_manager = NotificationManager()

test_cheap_flights = [
    {
        "price": 90.99,
        "departure_airport": "DUB",
        "arrival_airport": "EAS",
        "outbound_flight_date": "2025-05-05",
        "return_flight_date": "2025-05-12"
    }
]

flight_searcher.find_cheap_flights()
notification_manager.send_notification(test_cheap_flights)
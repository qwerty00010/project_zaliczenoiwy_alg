from customer import Customer         # Import Twojej klasy
from services import TaxiService      # Import klasy zrobionej przez drugą osobę
from transport import Taxi            # Import klasy zrobionej przez drugą osobę

klient = Customer("Jan", "Kowalski", "jan@op.pl", "500-600-700")

serwis_taxi = Scooter_Service()

zamowiony_pojazd = klient.order_transport(serwis_scooter, "Scooter")
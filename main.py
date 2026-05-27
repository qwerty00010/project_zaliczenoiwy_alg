from customer import Customer
from services import ScooterService

klient = Customer("Jan", "Kowalski", "jan@op.pl", "500-600-700")

serwis_scootera = ScooterService()

zamowiony_pojazd = klient.order_transport(serwis_scootera)
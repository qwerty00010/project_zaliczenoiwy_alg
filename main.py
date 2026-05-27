from customer import Customer
from services import ScooterService

# 1. Tworzymy klienta
klient = Customer("Jan", "Kowalski", "jan@op.pl", "500-600-700")

# 2. POPRAWKA: Poprawna nazwa zmiennej dla serwisu hulajnóg
serwis_scootera = ScooterService()

# 3. POPRAWKA: Przekazujemy właściwą zmienną (bez zbędnego tekstowego "Scooter")
zamowiony_pojazd = klient.order_transport(serwis_scootera)
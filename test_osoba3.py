import pytest
from customer import Customer
from transport import Transport, Bike, Scooter, Taxi
from services import TransportServices, BikeService, ScooterService, TaxiService


def test_ride_history():
    """
    Testuje mechanizm zapisu i przechowywania historii przejazdów klienta.
    Weryfikuje, czy pomyślne zamówienia są zapisywane w historii,
    a zamówienia zakończone niepowodzeniem (brak pojazdu) nie trafiają do niej.
    """
    klient = Customer("Jan", "Kowalski", "jan@op.pl", "500-600-700")

    # Nowo utworzony klient powinien mieć pustą historię
    assert len(klient.ride_history) == 0

    # Tworzymy dostępne serwisy
    serwis_hulajnogi = ScooterService()
    serwis_taksowki = TaxiService()

    # Zamawiamy hulajnogę - pierwsze pomyślne zamówienie
    pojazd1 = klient.order_transport(serwis_hulajnogi)
    assert pojazd1 is not None
    assert len(klient.ride_history) == 1
    assert klient.ride_history[0]["vehicle_type"] == "Scooter"
    assert klient.ride_history[0]["arrival_time"] == "3 minutes"
    assert klient.ride_history[0]["travel_time"] == "20 minutes"

    # Zamawiamy taksówkę - drugie pomyślne zamówienie
    pojazd2 = klient.order_transport(serwis_taksowki)
    assert pojazd2 is not None
    assert len(klient.ride_history) == 2
    assert klient.ride_history[1]["vehicle_type"] == "Taxi"
    assert klient.ride_history[1]["arrival_time"] == "10 minutes"
    assert klient.ride_history[1]["travel_time"] == "10 minutes"

    # Próba ponownego zamówienia hulajnogi (powinna być niedostępna, bo self.available = False)
    pojazd3 = klient.order_transport(serwis_hulajnogi)
    assert pojazd3 is None
    # Historia nie powinna ulec zmianie
    assert len(klient.ride_history) == 2


def test_multiple_customers():
    """
    Testuje scenariusz z wieloma klientami, sprawdzając czy ich historie
    przejazdów są odizolowane i nie nakładają się na siebie.
    """
    klient1 = Customer("Anna", "Nowak", "anna@wp.pl", "111-222-333")
    klient2 = Customer("Piotr", "Zieliński", "piotr@gmail.com", "444-555-666")

    serwis_roweru = BikeService()
    serwis_taksowki = TaxiService()

    # Klient 1 zamawia rower
    pojazd1 = klient1.order_transport(serwis_roweru)
    assert pojazd1 is not None

    # Klient 2 zamawia taksówkę
    pojazd2 = klient2.order_transport(serwis_taksowki)
    assert pojazd2 is not None

    # Sprawdzenie izolacji historii
    assert len(klient1.ride_history) == 1
    assert klient1.ride_history[0]["vehicle_type"] == "Bike"

    assert len(klient2.ride_history) == 1
    assert klient2.ride_history[0]["vehicle_type"] == "Taxi"


def test_inheritance():
    """
    Testuje poprawność hierarchii dziedziczenia w projekcie.
    Upewnia się, że klasy konkretne dziedziczą po odpowiednich klasach bazowych,
    a próba instancjonowania klas abstrakcyjnych kończy się błędem.
    """
    # 1. Sprawdzenie dziedziczenia klas transportowych
    assert issubclass(Bike, Transport)
    assert issubclass(Scooter, Transport)
    assert issubclass(Taxi, Transport)

    # 2. Sprawdzenie dziedziczenia klas serwisowych
    assert issubclass(BikeService, TransportServices)
    assert issubclass(ScooterService, TransportServices)
    assert issubclass(TaxiService, TransportServices)

    # 3. Sprawdzenie, czy nie można utworzyć obiektów klas abstrakcyjnych
    with pytest.raises(TypeError):
        Transport()

    with pytest.raises(TypeError):
        TransportServices()

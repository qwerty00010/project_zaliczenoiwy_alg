import unittest
from customer import Customer
from services import BikeService, ScooterService, TaxiService
from transport import Bike, Scooter, Taxi


class TestTransportSystem(unittest.TestCase):

    def setUp(self):
        """Metoda przygotowawcza, uruchamiana przed każdym testem."""
        self.klient = Customer("Jan", "Kowalski", "jan@op.pl", "500-600-700")
        self.serwis_rowerow = BikeService()
        self.serwis_hulajnog = ScooterService()
        self.serwis_taxi = TaxiService()

    # =========================================================================
    # 1. TESTY: Tworzenie transportu (Wzorzec Factory Method)
    # =========================================================================
    def test_factory_method_creates_correct_objects(self):
        """Sprawdza, czy usługi (fabryki) tworzą obiekty odpowiednich klas."""
        pojazd_rower = self.serwis_rowerow.create_transport()
        pojazd_hulajnoga = self.serwis_hulajnog.create_transport()
        pojazd_taxi = self.serwis_taxi.create_transport()

        # Sprawdzamy, czy instancje klas są prawidłowe
        self.assertIsInstance(pojazd_rower, Bike)
        self.assertIsInstance(pojazd_hulajnoga, Scooter)
        self.assertIsInstance(pojazd_taxi, Taxi)

    # =========================================================================
    # 2. TESTY: Działanie metod (Zwracane wartości tekstowe/czasy)
    # =========================================================================
    def test_bike_methods_output(self):
        """Sprawdza poprawność danych zwracanych przez klasę Bike."""
        rower = self.serwis_rowerow.create_transport()
        self.assertEqual(rower.vehicle_type(), "Bike")
        self.assertEqual(rower.arrival_time(), "5 minutes")
        self.assertEqual(rower.travel_time(), "25 minutes")

    def test_scooter_methods_output(self):
        """Sprawdza poprawność danych zwracanych przez klasę Scooter."""
        hulajnoga = self.serwis_hulajnog.create_transport()
        self.assertEqual(hulajnoga.vehicle_type(), "Scooter")
        self.assertEqual(hulajnoga.arrival_time(), "3 minutes")
        self.assertEqual(hulajnoga.travel_time(), "20 minutes")

    def test_taxi_methods_output(self):
        """Sprawdza poprawność danych zwracanych przez klasę Taxi."""
        taxi = self.serwis_taxi.create_transport()
        self.assertEqual(taxi.vehicle_type(), "Taxi")
        self.assertEqual(taxi.arrival_time(), "10 minutes")
        self.assertEqual(taxi.travel_time(), "10 minutes")

    # =========================================================================
    # 3. TESTY: Mechanizm dostępności transportu (Property available)
    # =========================================================================
    def test_transport_delivery_when_available(self):
        """Sprawdza zamówienie, gdy transport JEST dostępny (available = True)."""
        self.serwis_taxi.available = True

        # Klient zamawia - system powinien pomyślnie zwrócić obiekt Taxi
        wynik = self.klient.order_transport(self.serwis_taxi)
        self.assertIsNotNone(wynik)
        self.assertEqual(wynik.vehicle_type(), "Taxi")

    def test_transport_delivery_when_unavailable(self):
        """Sprawdza zamówienie, gdy transport JEST NIEDOSTĘPNY (available = False)."""
        self.serwis_taxi.available = False

        # Klient próbuje zamówić - system powinien zwrócić None (brak pojazdu)
        wynik = self.klient.order_transport(self.serwis_taxi)
        self.assertIsNone(wynik)


if __name__ == "__main__":
    unittest.main()
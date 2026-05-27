from abc import ABC, abstractmethod
from transport import Transport, Bike

class TransportServices(ABC):
    """
        Abstrakcyjna klasa bazowa reprezentująca usługę transportową.

        Definiuje wspólny interfejs dla wszystkich konkretnych usług w systemie,
        przechowuje informacje o dostępności floty oraz deklaruje metodę fabrykującą.
        """

    def __init__(self):
        """Inicjalizuje usługę transportową, ustawiając dostępność domyślnie na True."""
        self.available = True

    @abstractmethod
    def create_transport(self) -> Transport:

        """
                Metoda fabrykująca (Factory Method).

                Powinna zostać nadpisana w klasach pochodnych, aby zwracać
                konkretny obiekt klasy Transport.

                Returns:
                    Transport: Instancja konkretnego środka transportu.
                """
        pass

    @abstractmethod
    def transport_name(self) -> str:

        """
                Zwraca nazwę typu transportu obsługiwanego przez dany serwis.

                Returns:
                    str: Nazwa transportu (np. "Bike", "Taxi", "Scooter").
                """

        pass

    def order_transport(self):

        """
                Obsługuje proces zamówienia transportu przez klienta.

                Sprawdza dostępność pojazdu. Jeśli jest dostępny, tworzy go za pomocą
                metody fabrykującej i wyświetla szczegóły zamówienia. W przeciwnym wypadku
                informuje użytkownika o braku dostępności pojazdów.
                """

        transport = self.create_transport()

        if self.available:
            print(f"Typ pojazdu: {transport.vehicle_type()}")
            print(f"Przewidywany czas przyjazdu: {transport.arrival_time()}")
            print(f"Przewidywany czas podróży: {transport.travel_time()}")
        else:
            print(f"Przepraszamy, transport {self.transport_name()} jest obecnie niedostępny.")

class BikeService(TransportServices):
    """Konkretna usługa transportowa odpowiedzialna za obsługę i wypożyczanie rowerów."""
    def create_transport(self) -> Transport:
        """
                Tworzy i zwraca obiekt reprezentujący rower.

                Returns:
                    Transport: Instancja klasy Bike.
                """

        return Bike()

    def transport_name(self) -> str:
        """
                Zwraca nazwę usługi.

                Returns:
                    str: "Bike"
                """

        return "Bike"


class ScooterService(TransportServices):
    """Konkretna usługa transportowa odpowiedzialna za obsługę hulajnóg elektrycznych."""
    def create_transport(self) -> Transport:
        """
                Tworzy i zwraca obiekt reprezentujący hulajnogę.

                Wykorzystuje import lokalny, aby uniknąć błędów ładowania modułu
                przed pełną implementacją klas w pliku transport.py.

                Returns:
                    Transport: Instancja klasy Scooter.
                """

        from transport import Scooter
        return Scooter()

    def transport_name(self) -> str:
        return "Scooter"


class TaxiService(TransportServices):
    """Konkretna usługa transportowa odpowiedzialna za zamawianie taksówek."""
    def create_transport(self) -> Transport:
        """
                Tworzy i zwraca obiekt reprezentujący taksówkę.

                Wykorzystuje import lokalny, aby uniknąć błędów ładowania modułu
                przed pełną implementacją klas w pliku transport.py.

                Returns:
                    Transport: Instancja klasy Taxi.
                """
        from transport import Taxi
        return Taxi()

    def transport_name(self) -> str:
        return "Taxi"

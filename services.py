from abc import ABC, abstractmethod
from transport import Transport, Bike, Scooter, Taxi

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
        metody fabrykującej, wyświetla szczegóły zamówienia i ustawia dostępność
        na False. W przeciwnym wypadku informuje o braku dostępności.
        """
        if self.available:
            transport = self.create_transport()

            print(f"Typ pojazdu: {transport.vehicle_type()}")
            print(f"Przewidywany czas przyjazdu: {transport.arrival_time()}")
            print(f"Przewidywany czas podróży: {transport.travel_time()}")

            self.available = False
            return transport
        else:
            print(f"Przepraszamy, usługa {self.transport_name()} jest obecnie niedostępna.")
            return None


class BikeService(TransportServices):
    """
    Konkretna usługa transportowa odpowiedzialna za obsługę i wypożyczanie rowerów.
    """
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
    """
    Konkretna usługa transportowa odpowiedzialna za obsługę hulajnóg elektrycznych.
    """
    def create_transport(self) -> Transport:
        """
        Tworzy i zwraca obiekt reprezentujący hulajnogę.

        Returns:
            Transport: Instancja klasy Scooter.
        """
        return Scooter()

    def transport_name(self) -> str:
        """
        Zwraca nazwę usługi.

        Returns:
            str: "Scooter"
        """
        return "Scooter"


class TaxiService(TransportServices):
    """
    Konkretna usługa transportowa odpowiedzialna za zamawianie taksówek.
    """
    def create_transport(self) -> Transport:
        """
        Tworzy i zwraca obiekt reprezentujący taksówkę.

        Returns:
            Transport: Instancja klasy Taxi.
        """
        return Taxi()

    def transport_name(self) -> str:
        """
        Zwraca nazwę usługi.

        Returns:
            str: "Taxi"
        """
        return "Taxi"
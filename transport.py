from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Abstrakcyjna klasa bazowa reprezentująca środek transportu.

    Służy jako szablon (wspólny interfejs) dla wszystkich typów pojazdów
    wykorzystywanych w systemie zamawiania transportu.
    """

    @abstractmethod
    def vehicle_type(self) -> str:
        """
        Zwraca nazwę/typ pojazdu.

        :return: Typ pojazdu jako łańcuch znaków.
        """
        pass

    @abstractmethod
    def arrival_time(self) -> str:
        """
        Zwraca przewidywany czas przyjazdu pojazdu do klienta.

        :return: Przewidywany czas przyjazdu w formacie tekstowym.
        """
        pass

    @abstractmethod
    def travel_time(self) -> str:
        """
        Zwraca przewidywany czas trwania podróży do celu.

        :return: Przewidywany czas podróży w formacie tekstowym.
        """
        pass


class Bike(Transport):
    """
    Klasa reprezentująca rower jako środek transportu.

    Charakteryzuje się bardzo krótkim czasem oczekiwania na przyjazd (dostępny
    blisko od zaraz), ale dłuższym czasem samej podróży.
    """

    def vehicle_type(self) -> str:
        """
        Zwraca nazwę typu pojazdu.
        """
        return "Bike"

    def arrival_time(self) -> str:
        """
        Zwraca przewidywany czas przyjazdu roweru.
        """
        return "5 minutes"

    def travel_time(self) -> str:
        """
        Zwraca przewidywany czas podróży rowerem.
        """
        return "25 minutes"


class Scooter(Transport):
    """
    Klasa reprezentująca hulajnogę elektryczną jako środek transportu.

    Charakteryzuje się najkrótszym czasem oczekiwania na pojazd oraz
    umiarkowanym czasem podróży.
    """

    def vehicle_type(self) -> str:
        """
        Zwraca nazwę typu pojazdu.
        """
        return "Scooter"

    def arrival_time(self) -> str:
        """
        Zwraca przewidywany czas przyjazdu hulajnogi.
        """
        return "3 minutes"

    def travel_time(self) -> str:
        """
        Zwraca przewidywany czas podróży hulajnogą.
        """
        return "20 minutes"


class Taxi(Transport):
    """
    Klasa reprezentująca taksówkę jako środek transportu.

    Charakteryzuje się najdłuższym czasem oczekiwania (dojazd kierowcy),
    ale najkrótszym czasem samej podróży ze względu na prędkość pojazdu.
    """

    def vehicle_type(self) -> str:
        """
        Zwraca nazwę typu pojazdu.
        """
        return "Taxi"

    def arrival_time(self) -> str:
        """
        Zwraca przewidywany czas przyjazdu taksówki.
        """
        return "10 minutes"

    def travel_time(self) -> str:
        """
        Zwraca przewidywany czas podróży taksówką.
        """
        return "10 minutes"

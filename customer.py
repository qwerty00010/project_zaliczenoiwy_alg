class Customer:
    """
    Klasa reprezentująca klienta w systemie rezerwacji transportu.

    Odpowiada za przechowywanie informacji o użytkowniku oraz inicjowanie procesu
    zamawiania transportu. Klasa nie tworzy bezpośrednio obiektów pojazdów,
    lecz współpracuje z zewnętrzną usługą transportową (wzorzec Factory Method).
    """

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        """
        Inicjalizuje nowy obiekt klienta z podstawowymi danymi kontaktowymi
        oraz pustą historią przejazdów.

        :param first_name: Imię klienta.
        :param last_name: Nazwisko klienta.
        :param email: Adres e-mail klienta.
        :param phone_number: Numer telefonu klienta.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.ride_history = []

    def order_transport(self, transport_service):
        """
        Inicjuje proces zamawiania określonego typu transportu.

        Metoda przekazuje żądanie do warstwy pośredniej (usługi transportowej),
        co pozwala odizolować klienta od logiki tworzenia konkretnych obiektów.
        Jeśli transport jest dostępny, szczegóły przejazdu są zapisywane
        w historii przejazdów klienta.

        :param transport_service: Obiekt klasy usługi transportowej (np. TaxiService).
        :return: Obiekt utworzonego środka transportu lub None, jeśli niedostępny.
        """
        print(f"Klient {self.first_name} {self.last_name} (email: {self.email}) inicjuje zamówienie.")

        if not transport_service.available:
            # Wywołujemy usługę, aby wyświetliła komunikat o niedostępności
            transport_service.order_transport()
            return None

        # Tworzymy obiekt transportu
        transport = transport_service.create_transport()

        # Zapisujemy informacje o przejeździe do historii
        ride_info = {
            "vehicle_type": transport.vehicle_type(),
            "arrival_time": transport.arrival_time(),
            "travel_time": transport.travel_time()
        }
        self.ride_history.append(ride_info)

        # Wywołujemy logikę zamówienia z warstwy pośredniej (services.py)
        transport_service.order_transport()

        return transport

    def display_history(self) -> None:
        """
        Wyświetla historię wszystkich zrealizowanych przejazdów klienta.
        """
        print(f"--- Historia przejazdów klienta {self.first_name} {self.last_name} ---")
        if not self.ride_history:
            print("Brak zrealizowanych przejazdów.")
            return

        for idx, ride in enumerate(self.ride_history, 1):
            print(
                f"{idx}. Pojazd: {ride['vehicle_type']}, "
                f"dojazd: {ride['arrival_time']}, "
                f"podróż: {ride['travel_time']}"
            )
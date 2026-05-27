class Customer:
    """
    Klasa reprezentująca klienta w systemie rezerwacji transportu.

    Odpowiada za przechowywanie informacji o użytkowniku oraz inicjowanie procesu
    zamawiania transportu. Klasa nie tworzy bezpośrednio obiektów pojazdów,
    lecz współpracuje z zewnętrzną usługą transportową (wzorzec Factory Method).
    """

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        """
        Inicjalizuje nowy obiekt klienta z podstawowymi danymi kontaktowymi.

        :param first_name: Imię klienta.
        :param last_name: Nazwisko klienta.
        :param email: Adres e-mail klienta.
        :param phone_number: Numer telefonu klienta.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def order_transport(self, transport_service, transport_type: str):
        """
        Inicjuje proces zamawiania określonego typu transportu.

        Metoda przekazuje żądanie do warstwy pośredniej (usługi transportowej),
        co pozwala odizolować klienta od logiki tworzenia konkretnych obiektów.

        :param transport_service: Obiekt klasy usługi transportowej (np. TaxiService).
        :param transport_type: Nazwa typu pojazdu (np. "Taxi", "Bike", "Scooter").
        :return: Obiekt utworzonego środka transportu.
        """
        print(f"Klient {self.first_name} {self.last_name} (email: {self.email}) inicjuje zamówienie na: {transport_type}.")

        # Współpraca z obiektem klasy usługi transportowej (warstwa pośrednia)
        transport = transport_service.create_transport(transport_type)

        return transport
class Customer:
    """Klasa reprezentująca klienta w systemie rezerwacji transportu."""

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    # POPRAWKA: Usunęliśmy transport_type, bo usługa już wie, jaki pojazd tworzy
    def order_transport(self, transport_service):
        """Inicjuje proces zamawiania transportu poprzez wybraną usługę."""
        print(f"Klient {self.first_name} {self.last_name} (email: {self.email}) inicjuje zamówienie.")

        # Wywołujemy logikę zamówienia z warstwy pośredniej (services.py)
        transport_service.order_transport()

        # Zwracamy stworzony obiekt pojazdu
        return transport_service.create_transport()
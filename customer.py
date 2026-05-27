class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def order_transport(self, transport_service, transport_type):
        print(
            f"Klient {self.first_name} {self.last_name} (email: {self.email}) inicjuje zamówienie na: {transport_type}.")

        # Współpraca z obiektem klasy usługi transportowej (warstwa pośrednia)
        transport = transport_service.create_transport(transport_type)

        return transport
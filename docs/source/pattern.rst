Wzorzec Projektowy: Metoda Fabrykująca (Factory Method)
=======================================================

Cel wzorca
----------
**Metoda Fabrykująca (Factory Method)** to kreacyjny wzorzec projektowy, który definiuje interfejs do tworzenia obiektów w klasie bazowej, ale pozwala podklasom zmieniać typ tworzonych obiektów.

Dzięki temu wzorcowi klasa kliencka nie musi wiedzieć, jaka konkretna klasa pojazdu (np. ``Bike``, ``Scooter`` czy ``Taxi``) zostanie zainicjalizowana. Cała odpowiedzialność za decydowanie, który obiekt należy utworzyć, zostaje przeniesiona na klasy fabrykujące (konkretne usługi, np. ``BikeService``).

Zastosowanie w projekcie
------------------------
W naszym systemie zamawiania transportu z akademika na uczelnię wzorzec ten został zaimplementowany w następujący sposób:

1. **Abstrakcyjny Produkt (``Transport``)**:
   Definiuje interfejs dla obiektów, które tworzy metoda fabrykująca. Zawiera metody abstrakcyjne:
   - ``vehicle_type()``
   - ``arrival_time()``
   - ``travel_time()``

2. **Konkretne Produkty (``Bike``, ``Scooter``, ``Taxi``)**:
   Implementują interfejs ``Transport``, zwracając specyficzne czasy przyjazdu, podróży oraz nazwy pojazdów.

3. **Abstrakcyjny Kreator (``TransportServices``)**:
   Klasa bazowa dla usług transportowych. Deklaruje metodę fabrykującą ``create_transport()``, która zwraca obiekt typu ``Transport``.
   Zawiera również metodę szablonową ``order_transport()``, która realizuje ogólny proces zamówienia pojazdu (sprawdzenie dostępności, wyświetlenie szczegółów i zmianę stanu dostępności).

4. **Konkretni Kreatorzy (``BikeService``, ``ScooterService``, ``TaxiService``)**:
   Nadpisują metodę fabrykującą ``create_transport()``, aby zwracała odpowiednią instancję produktu (np. ``BikeService`` tworzy obiekt ``Bike``).

Diagram powiązań (UML)
----------------------
Klasa ``Customer`` wchodzi w interakcję wyłącznie z ``TransportServices`` (abstrakcją), a nie z konkretnymi klasami pojazdów. Pozwala to na pełne odizolowanie klienta od logiki tworzenia konkretnych obiektów i łatwe rozszerzanie kodu o kolejne typy transportu (zasada Open/Closed).

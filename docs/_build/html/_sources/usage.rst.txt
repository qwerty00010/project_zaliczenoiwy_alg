Instrukcja Uruchomienia i Przykłady
===================================

Wymagania systemowe
-------------------
Aby uruchomić aplikację oraz testy jednostkowe, wymagane jest posiadanie zainstalowanego środowiska **Python 3.10+** oraz pakietu **pytest** (opcjonalnie do uruchamiania testów).

Instrukcja uruchomienia
-----------------------

1. **Uruchomienie scenariusza demonstracyjnego**:
   Aby uruchomić główny program demonstracyjny (plik ``main.py``), wykonaj w terminalu:

   .. code-block:: bash

      python3 main.py

2. **Uruchomienie testów jednostkowych**:
   W celu zweryfikowania poprawności działania całego systemu (w tym historii przejazdów i mechanizmu dostępności), uruchom testy za pomocą narzędzia ``pytest``:

   .. code-block:: bash

      pytest test_osoba3.py

Przykłady działania programu
----------------------------

Poniżej przedstawiono przykładowe scenariusze użycia systemu zamawiania transportu wraz z historią przejazdów.

Scenariusz 1: Pomyślne zamówienie i zapis w historii
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Klient inicjuje zamówienie hulajnogi elektrycznej. System rezerwuje pojazd, wyświetla szczegóły oraz zapisuje go w historii klienta:

.. code-block:: python

   from customer import Customer
   from services import ScooterService

   # Tworzenie klienta
   klient = Customer("Jan", "Kowalski", "jan@op.pl", "500-600-700")

   # Zamówienie dostępnego pojazdu
   serwis_scootera = ScooterService()
   pojazd = klient.order_transport(serwis_scootera)

   # Wyświetlenie historii przejazdów
   klient.display_history()

**Wyjście w konsoli:**

.. code-block:: text

   Klient Jan Kowalski (email: jan@op.pl) inicjuje zamówienie.
   Typ pojazdu: Scooter
   Przewidywany czas przyjazdu: 3 minutes
   Przewidywany czas podróży: 20 minutes

   --- Historia przejazdów klienta Jan Kowalski ---
   1. Pojazd: Scooter, dojazd: 3 minutes, podróż: 20 minutes


Scenariusz 2: Próba zamówienia zajętego pojazdu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Po pomyślnym zamówieniu, usługa staje się niedostępna (status ``available = False``). Próba ponownego zamówienia zwraca informację o braku dostępności i nie zapisuje kolejnej pozycji w historii:

.. code-block:: python

   # Próba ponownego zamówienia hulajnogi przez tego samego lub innego klienta
   pojazd2 = klient.order_transport(serwis_scootera)

**Wyjście w konsoli:**

.. code-block:: text

   Klient Jan Kowalski (email: jan@op.pl) inicjuje zamówienie.
   Przepraszamy, usługa Scooter jest obecnie niedostępna.

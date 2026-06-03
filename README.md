# System Zamawiania Transportu

Aplikacja zrealizowana w ramach projektu zespołowego, symulująca działanie systemu zamawiania transportu z akademika na uczelnię. Projekt demonstruje zastosowanie zasad programowania obiektowego (OOP) w języku Python oraz wzorca projektowego **Factory Method (Metoda Fabrykująca)**.

Program wspiera również mechanizm kontroli dostępności pojazdów, historię zrealizowanych rezerwacji dla każdego klienta, testy jednostkowe (Pytest) oraz automatyczną dokumentację kodu (Sphinx).

---

## 🛠️ Architektura i Wzorce Projektowe

Głównym założeniem systemu jest odizolowanie klienta od logiki bezpośredniego tworzenia obiektów pojazdów. Zrealizowano to za pomocą wzorca **Factory Method**:

```
[ Customer ] ──> [ TransportServices ] (Kreator ABC)
                        │
                        ├─> BikeService     ──> Tworzy [ Bike ]
                        ├─> ScooterService  ──> Tworzy [ Scooter ]
                        └─> TaxiService     ──> Tworzy [ Taxi ]
```

* **Abstrakcyjny Produkt (`Transport`)**: Klasa bazowa w `transport.py`, definiująca interfejs (`vehicle_type`, `arrival_time`, `travel_time`).
* **Konkretne Produkty (`Bike`, `Scooter`, `Taxi`)**: Reprezentują specyficzne środki transportu o zróżnicowanych czasach dojazdu i podróży.
* **Abstrakcyjny Kreator (`TransportServices`)**: Klasa bazowa w `services.py` z metodą fabrykującą `create_transport()` oraz metodą szablonową `order_transport()`.
* **Konkretni Kreatorzy (`BikeService`, `ScooterService`, `TaxiService`)**: Decydują, który pojazd utworzyć i zwrócić.

---

## 📁 Struktura Projektu

```text
project_zaliczenoiwy_alg/
│
├── customer.py          # Moduł klienta (klasa Customer, historia przejazdów)
├── services.py          # Moduł usług transportowych (klasy serwisów i fabryk)
├── transport.py         # Moduł pojazdów (klasa bazowa i konkretne podklasy)
├── main.py              # Skrypt uruchomieniowy z demonstracją scenariusza
│
├── test_osoba1.py       # Testy jednostkowe dla Osoby 1 (pojazdy, serwisy, dostępność)
├── test_osoba3.py       # Testy jednostkowe dla Osoby 3 (historia, izolacja, dziedziczenie)
│
├── docs/                # Pliki źródłowe dokumentacji Sphinx
│   ├── source/          # Pliki konfiguracyjne (.py) oraz podstrony (.rst)
│   └── build/           # Skompilowana dokumentacja HTML (generowana lokalnie)
│
├── DobrePraktyki.docx   # Zasady programowania i standardy stylu (PEP 8)
├── instrukcja-3os.docx  # Instrukcja krok po kroku dla zespołu 3-osobowego
└── README.md            # Niniejszy plik informacyjny
```

---

## 🚀 Instrukcja Uruchomienia

### Wymagania wstępne
Upewnij się, że masz zainstalowany Python w wersji 3.10 lub nowszej.

### 1. Uruchomienie demonstracji
Główny scenariusz pokazuje utworzenie klienta, pomyślną rezerwację pojazdu, automatyczną blokadę ponownej rezerwacji zajętego pojazdu oraz wyświetlenie historii przejazdów:

```bash
python3 main.py
```

### 2. Uruchomienie testów jednostkowych
Testy jednostkowe weryfikują poprawność logiki biznesowej, dziedziczenia oraz izolacji danych klientów:

```bash
# Uruchomienie wszystkich testów
pytest
```

### 3. Kompilacja dokumentacji Sphinx
Projekt zawiera skonfigurowany generator dokumentacji Sphinx z motywem `sphinx_rtd_theme`. Aby wygenerować pliki HTML na podstawie docstringów w kodzie, wykonaj:

```bash
# Wejdź do folderu docs (lub uruchom bezpośrednio z głównego katalogu)
sphinx-build -b html docs/source docs/build/html
```
Skompilowaną dokumentację można otworzyć w przeglądarce za pomocą pliku: `docs/build/html/index.html`.

---

## 👥 Podział Ról w Zespole

Projekt został zrealizowany w zespole 3-osobowym:

| Rola | Odpowiedzialność i Zrealizowane Zadania |
| :--- | :--- |
| **Osoba 1** | Implementacja modułu transportu (`transport.py`), dodanie nowych środków transportu (Scooter, Taxi), stworzenie testów jednostkowych tworzenia pojazdów i ich metod (`test_osoba1.py`). |
| **Osoba 2** | Implementacja modułu usług (`services.py`), mechanizm blokowania dostępności pojazdów (zmiana statusu `available` na `False` po zamówieniu i obsługa komunikatów o zajętości). |
| **Osoba 3** | Rozbudowa modułu klienta (`customer.py`) o system zapisu historii przejazdów, stworzenie testów historii i dziedziczenia (`test_osoba3.py`), stworzenie i konfiguracja dokumentacji Sphinx (`docs/`). |

---

## 🎓 Wymogi do Zaliczenia Projektu

Przed ostatecznym oddaniem projektu należy wygenerować wymagane pliki logów z historii Git:

```bash
git log --oneline --graph > log.txt
git reflog > reflog.txt
git log -p > history.txt
```

Następnie spakuj cały katalog projektu (wraz z wygenerowaną dokumentacją Sphinx oraz plikami logów Git) do jednego archiwum `.zip` i prześlij na platformę zaliczeniową.
# Zoo Garden Management System

## 1. Opis projektu
System „Zoo Garden" to aplikacja wspierająca zarządzanie ogrodem zoologicznym z perspektywy jego pracowników. Umożliwia dodawanie zwierząt do wybiegów z uwzględnieniem ich pojemności, zarządzanie personelem oraz monitorowanie stanu zdrowia zwierząt. System pomaga utrzymać porządek organizacyjny oraz zapewnia bezpieczeństwo i dobrostan zwierząt. Dzięki niemu użytkownicy mogą szybko wykonywać codzienne operacje bez ryzyka błędów logicznych (np. przepełnienia wybiegu).

---

## 2. Autorzy i podział pracy

| Imię i Nazwisko | Zakres odpowiedzialności |
| :--- | :--- |
| **Bartłomiej Białobrzewski** | Testy jednostkowe (`pytest`), Use Cases, diagram UML |
| **Wiktor Habryń** | Implementacja klas (zwierzęta, personel), logika systemu |
| **Bartłomiej Żołek** | Code Review, walidacja logiki, optymalizacja |

---

## 3. Struktura plików (hierarchia)

```
zoo_garden/
├── zoo/
│   ├── __init__.py              # Package initialization
│   ├── exceptions.py            # Custom exception hierarchy (ZooError, etc.)
│   ├── animals/
│   │   ├── __init__.py
│   │   ├── animal.py            # Base Animal ABC with _next_id, health property
│   │   ├── mammal.py            # Mammal class + Lion, Elephant, Monkey
│   │   ├── bird.py              # Bird class + Eagle, Penguin
│   │   └── reptile.py           # Reptile class + Crocodile
│   ├── employees/
│   │   ├── __init__.py
│   │   ├── employee.py          # Base Employee ABC
│   │   ├── zookeeper.py         # Zookeeper with enclosure assignment
│   │   ├── veterinarian.py      # Veterinarian with specialization
│   │   ├── guide.py             # Guide with languages
│   │   └── tests/
│   │       ├── test_animals.py  # Animal tests
│   │       ├── test_enclosure.py # Enclosure tests
│   │       └── test_zoo.py      # Zoo tests
│   ├── enclosure.py             # Enclosure class with dunder methods
│   ├── feeding_schedule.py      # FeedingEntry (@dataclass) and FeedingSchedule
│   └── zoo.py                   # Main Zoo class
├── demo.py                      # Demo script showing system usage
├── README.md                    # This file
├── Projekt_A_Zoo_Garden.md      # Project specification
├── improvements.md              # List of improvements to implement
├── requirements.txt             # Python dependencies
└── .gitignore
```

---

## 4. Lista klas z opisami

| Klasa | Opis | Główne atrybuty i metody |
| :--- | :--- | :--- |
| `Animal` (ABC) | Abstrakcyjna klasa bazowa reprezentująca każde zwierzę w systemie. Definiuje wspólne właściwości oraz wymusza implementację zachowania dźwiękowego. | `_id`, `_name`, `_age`, `_health`, `make_sound()`, `diet()`, `__str__()`, `__eq__()`, `__hash__()`, `__lt__()` |
| `Mammal` | Klasa pośrednia dla ssaków, rozszerzająca `Animal` o cechy charakterystyczne tej grupy. | `_fur_color`, `diet()`, `give_birth()`, `has_fur()` |
| `Bird` | Klasa pośrednia dla ptaków, definiująca ich zdolności związane z lataniem. | `_wingspan`, `_can_fly`, `diet()`, `fly()` |
| `Reptile` | Klasa pośrednia dla gadów, zawierająca ich typowe zachowania. | `_is_venomous`, `diet()`, `bask()`, `is_cold_blooded()` |
| `Lion` | Konkretna implementacja ssaka reprezentująca lwa. Nadpisuje metodę `make_sound()`. | `make_sound()`, `diet()` |
| `Elephant` | Reprezentuje słonia oraz umożliwia aktualizację jego zdrowia. | `make_sound()`, `diet()` |
| `Monkey` | Reprezentuje małpę - inteligentnego prymata. | `make_sound()`, `climb()` |
| `Eagle` | Reprezentuje ptaka drapieżnego z możliwością wydawania charakterystycznego dźwięku. | `make_sound()`, `diet()` |
| `Penguin` | Reprezentuje ptaka nielatającego. | `make_sound()`, `swim()` |
| `Crocodile` | Reprezentuje gada, implementując jego zachowanie dźwiękowe. | `make_sound()`, `diet()`, `swim()` |
| `Employee` (ABC) | Abstrakcyjna klasa bazowa dla pracowników zoo. Odpowiada za wspólne dane i kontrakt metod. | `_id`, `_name`, `_salary`, `_assigned_enclosures`, `assign_to()`, `work()`, `role()` |
| `Zookeeper` | Pracownik odpowiedzialny za opiekę nad wybiegami i zwierzętami. | `_assigned_enclosure`, `assign_to()`, `feed_animals()`, `work()`, `role()` |
| `Veterinarian` | Lekarz zajmujący się leczeniem zwierząt oraz aktualizacją ich zdrowia. | `_specialization`, `treat_animal()`, `work()`, `role()` |
| `Guide` | Przewodnik oprowadzający odwiedzających po zoo. | `_languages`, `add_language()`, `give_tour()`, `work()`, `role()` |
| `Enclosure` | Reprezentuje wybieg dla zwierząt, zarządza ich listą oraz kontroluje pojemność. | `_name`, `_capacity`, `_animals`, `add_animal()`, `remove_animal()`, `find_animal()`, `feed_all()` |
| `FeedingEntry` | Dataclass reprezentujący pojedynczy wpis w harmonogramie karmienia. | `enclosure_name`, `time`, `food_type`, `notes` |
| `FeedingSchedule` | Zarządza harmonogramem karmienia dla całego zoo. | `day`, `entries`, `add_entry()`, `remove_entry()`, `get_by_enclosure()` |
| `Zoo` | Główna klasa systemowa zarządzająca wybiegami i personelem. | `_name`, `_city`, `_enclosures`, `_employees`, `create_enclosure()`, `hire_employee()`, `find_animal()`, `report()` |

---

## 5. Relacje między klasami

- **Dziedziczenie (`Animal` → `Mammal` → `Lion`/`Elephant`/`Monkey`)**  
  Pozwala na współdzielenie logiki i wymuszenie implementacji metod w klasach potomnych.

- **Dziedziczenie (`Animal` → `Bird` → `Eagle`/`Penguin`)**  
  Wspólne cechy ptaków z możliwością latania (lub jej brakiem).

- **Dziedziczenie (`Animal` → `Reptile` → `Crocodile`)**  
  Wspólne cechy gadów, w tym zmiennocieplność.

- **Dziedziczenie (`Employee` → `Zookeeper`, `Veterinarian`, `Guide`)**  
  Umożliwia wspólne zarządzanie pracownikami oraz wykorzystanie polimorfizmu.

- **Kompozycja (`Zoo` ◆–– `Enclosure`)**  
  Wybiegi są częścią zoo i nie istnieją bez niego. Usunięcie zoo powoduje usunięcie wybiegów.

- **Agregacja (`Enclosure` ◇–– `Animal`)**  
  Zwierzęta mogą być przenoszone między wybiegami. Usunięcie wybiegu nie usuwa zwierzęcia.

- **Asocjacja (`Zookeeper` *––* `Enclosure`)**  
  Opiekun może być przypisany do wybiegu, ale istnieje niezależnie od niego.

- **Kompozycja (`FeedingSchedule` ◆–– `FeedingEntry`)**  
  Wpisy karmienia nie istnieją niezależnie od harmonogramu.

---

## 6. Harmonogram karmienia

System wykorzystuje klasę `FeedingEntry` (oznaczoną jako `@dataclass`) oraz `FeedingSchedule` do zarządzania harmonogramem karmienia:

```python
# Tworzenie harmonogramu
schedule = FeedingSchedule(day="Monday")

# Dodawanie wpisów
schedule.add_entry("Savanna", "09:00", "Hay and fruits", "Extra vitamin supplements")
schedule.add_entry("Penguin Pool", "10:30", "Fish", "Fresh catch only")
schedule.add_entry("Savanna", "15:00", "Grass", "")

# Pobieranie wpisów dla wybiegu
savanna_feedings = schedule.get_by_enclosure("Savanna")

# Usuwanie wpisu
schedule.remove_entry("Savanna", "15:00")
```

---

## 7. Wyjątki domenowe

System definiuje hierarchię wyjątków w module `exceptions.py`:

```
ZooError (bazowy)
├── EnclosureFullError           # Próba dodania zwierzęcia do pełnego wybiegu
├── AnimalNotFoundError          # Zwierzę nie zostało znalezione w wybiegu
└── InvalidAnimalDataError       # Nieprawidłowe dane zwierzęcia
```

Przykład użycia:
```python
from zoo.exceptions import EnclosureFullError, AnimalNotFoundError

try:
    enclosure.add_animal(lion)  # Raises EnclosureFullError if full
except EnclosureFullError as e:
    print(f"Cannot add animal: {e}")

try:
    enclosure.remove_animal(tiger)  # Raises AnimalNotFoundError if not present
except AnimalNotFoundError as e:
    print(f"Animal not found: {e}")
```

---

## 8. Planowane funkcjonalności

- Dodawanie zwierzęcia do wybiegu z walidacją pojemności (wyjątek `EnclosureFullError`)
- Usuwanie zwierzęcia z wybiegu (wyjątek `AnimalNotFoundError` jeśli nie znaleziono)
- Przeglądanie listy zwierząt w wybiegu
- Aktualizacja stanu zdrowia zwierzęcia (z ograniczeniem 0–100 - clamping)
- Przypisywanie pracownika do jednego lub wielu wybiegów
- Generowanie raportu pracowników i ich obowiązków
- Przeglądanie wybiegów przez pracownika (np. przewodnika)
- Harmonogram karmienia z `@dataclass` FeedingEntry

---

## 9. User Stories

1. **Jako opiekun** chcę dodać nowe zwierzę do wybiegu, żeby system automatycznie sprawdził, czy jest tam wolne miejsce.  
2. **Jako weterynarz** chcę zaktualizować stan zdrowia zwierzęcia po leczeniu, żeby mieć pewność, że dane są poprawne.  
3. **Jako dyrektor** chcę zobaczyć raport wszystkich pracowników i ich obowiązków, żeby ocenić efektywność pracy.  

---

## 10. Mechanizmy OOP

| Mechanizm | Gdzie w projekcie | Opis |
| :--- | :--- | :--- |
| Klasy abstrakcyjne (ABC) | `Animal`, `Employee` | Wymuszają implementację metod (`make_sound()`, `work()`, `role()`) |
| Dziedziczenie | `Animal` → `Mammal` → `Lion` itd. | Hierarchia klas upraszczająca rozszerzanie systemu |
| Polimorfizm | `make_sound()`, `work()`, `role()` | Różne implementacje dla różnych klas |
| Hermetyzacja (enkapsulacja) | `_health`, `_animals`, `_assigned_enclosures` | Ukrycie danych i kontrola dostępu przez metody |
| Właściwości (`@property`) | `Animal.health`, `Employee.salary` | Walidacja danych (clamping 0–100, salary >= 0) |
| Przeciążanie operatorów | `__str__()`, `__repr__()`, `__eq__()`, `__hash__()`, `__lt__()`, `__len__()`, `__contains__()`, `__getitem__()`, `__iter__()` | Pełna obsługa operatorów dla klas |
| Relacje wiele-do-wielu | `Employee` ↔ `Enclosure` | Elastyczne przypisywanie pracowników |
| @dataclass | `FeedingEntry` | Automatyczne generowanie `__init__`, `__repr__`, `__eq__` |

### Dodatkowe zalety systemu
- Zapewnienie spójności danych (np. zdrowie 0–100, brak przepełnienia wybiegów)
- Łatwa rozbudowa systemu o nowe klasy zwierząt lub pracowników
- Niskie sprzężenie i wysoka spójność klas
- Lepsze odwzorowanie rzeczywistego działania zoo
- Możliwość łatwego testowania i utrzymania kodu

---

## 11. Historia zmian

- Dodano `exceptions.py` z hierarchią wyjątków (`ZooError`, `EnclosureFullError`, `AnimalNotFoundError`, `InvalidAnimalDataError`)
- Dodano klasę `Monkey` do modułu `mammal.py`
- Zaimplementowano `FeedingEntry` (@dataclass) i `FeedingSchedule` z pełną funkcjonalnością
- Dodano walidację health (clamping 0–100) w klasie `Animal`
- Zaktualizowano wszystkie klasy o metody specjalne (dunder)
- Przeniesiono `_assigned_enclosures` z `Zookeeper` do `Employee` (zgodność z zasadą DRY)
- Dodano harmonogram karmienia do README

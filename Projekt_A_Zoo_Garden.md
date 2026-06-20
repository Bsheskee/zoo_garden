# PROJEKT SEMESTRALNY — Programowanie Obiektowe I
## Wariant A: Zoo Garden
**Semestr letni 2025/2026**

---

## 1. Wprowadzenie

### 1.1 Cel projektu
Projekt ma na celu praktyczne zastosowanie wszystkich mechanizmów programowania obiektowego poznanych na wykładach. Studenci zaprojektują i zaimplementują wybrany system wykorzystując dziedziczenie, kompozycję, polimorfizm, klasy abstrakcyjne oraz inne koncepcje OOP.

### 1.2 Cele dydaktyczne
- Projektowanie hierarchii klas wykorzystujących dziedziczenie
- Stosowanie kompozycji i agregacji do modelowania relacji między obiektami
- Implementację polimorfizmu i duck typing
- Tworzenie klas abstrakcyjnych wymuszających implementację metod
- Stosowanie enkapsulacji z użyciem `@property`
- Przeciążanie operatorów i metod specjalnych
- Definiowanie własnych wyjątków
- Pisanie testów jednostkowych z użyciem `pytest`
- Dokumentowanie kodu zgodnie z dobrymi praktykami

### 1.3 Forma realizacji
> Praca w zespole (dokładnie 3 osoby).

Wszystkie osoby oddają ten sam plik ZIP, wszystkie osoby wgrywają pliki na platformę, każda osoba odpowiada za swój przydział pracy.

---

## 2. Opis projektu: Zoo Garden

### 2.1 Koncepcja systemu
System symuluje zarządzanie ogrodem zoologicznym:

- **Zwierzęta** – różne gatunki (np. Lion, Eagle, Crocodile) z unikalnymi cechami
- **Typy zwierząt** – ssaki (Mammal), ptaki (Bird), gady (Reptile)
- **Wybiegi** – obiekty Enclosure z pojemnością i listą zwierząt
- **Pracownicy** – opiekunowie (Zookeeper), weterynarze (Veterinarian), przewodnicy (Guide)
- **Karmienie** – harmonogram z wpisami @dataclass (FeedingEntry)
- **Zdrowie** – atrybut health (0–100) z walidacją (clamping)

### 2.2 Wymagania funkcjonalne

#### 2.2.1 Klasy zwierząt
- Klasa bazowa `Animal` (ABC)
- **3 typy pośrednie:** Mammal (fur_color, give_birth), Bird (wingspan, can_fly, fly), Reptile (is_venomous, bask)
- **Dokładnie 6 konkretnych gatunków:** Lion, Elephant, Monkey, Eagle, Penguin, Crocodile
- Każdy gatunek ma unikalną metodę `make_sound()` (polimorfizm)
- Każdy typ pośredni ma własną metodę `diet()`
- Atrybut klasy `_next_id` do automatycznego ID
- Property `health` z clamping 0–100

#### 2.2.2 System pracowników
- Klasa bazowa `Employee` (ABC)
- 3 typy: Zookeeper, Veterinarian, Guide
- Zookeeper – asocjacja z Enclosure (assign_to, feed_animals)
- Veterinarian – specjalizacja (general/exotic)
- Guide – lista języków
- Metody abstrakcyjne: work(), role()

#### 2.2.3 Wybiegi (Enclosure)
- Atrybuty: name, capacity
- Agregacja z Animal (zwierzęta mogą istnieć osobno)
- Metody: add_animal (EnclosureFullError), remove_animal (AnimalNotFoundError), find_animal, feed_all
- Dunder: __len__, __contains__, __iter__, __eq__, __hash__

#### 2.2.4 Harmonogram karmienia
- `FeedingEntry` jako `@dataclass` (enclosure_name, time, food_type, notes)
- `FeedingSchedule` – kompozycja z FeedingEntry
- Metody: add_entry, remove_entry, get_by_enclosure

#### 2.2.5 Klasa Zoo
- Kompozycja z Enclosure (wybiegi nie istnieją bez zoo)
- Agregacja z Employee (pracownicy mogą istnieć osobno)
- Metody: create_enclosure, hire_employee, total_animals, find_animal, report
- Dunder: __getitem__(name), __contains__, __len__

#### 2.2.6 Hierarchia wyjątków
ZooError (bazowy) → EnclosureFullError, AnimalNotFoundError, InvalidAnimalDataError

### 2.3 Sugerowana hierarchia klas
```
Animal (ABC)
|-- Mammal -> Lion, Elephant, Monkey
|-- Bird -> Eagle, Penguin
|-- Reptile -> Crocodile

Employee (ABC)
|-- Zookeeper
|-- Veterinarian
|-- Guide

Enclosure, Zoo, FeedingSchedule, FeedingEntry(@dataclass)
```

### 2.4 Relacje
- Zoo ◆–– Enclosure (kompozycja – wybiegi nie istnieją bez zoo)
- Enclosure ◇–– Animal (agregacja – zwierzęta mogą istnieć osobno)
- Zookeeper ––  Enclosure (asocjacja – opiekun przypisany do wybiegu)
- Zoo ◇–– Employee (agregacja)

### 2.5 Demonstracja działania (demo.py)
1. Stworzenie zoo z wybiegami
2. Dodanie zwierząt do wybiegów
3. Próba dodania zwierzęcia do pełnego wybiegu (wyjątek EnclosureFullError)
4. Karmienie zwierząt (feed_all)
5. Przypisanie opiekuna do wybiegu (asocjacja)
6. Generowanie raportu o stanie zoo
7. Polimorficzne wywołanie metod na liście różnych zwierząt (make_sound, diet)

### 2.6 Zakres testów (15 scenariuszy)
1. Tworzenie zwierząt różnych typów
2. Sprawdzenie bazowych statystyk i properties
3. Dodawanie zwierząt do wybiegu
4. Walidacja pojemności wybiegu (EnclosureFullError)
5. Usuwanie zwierzęcia z wybiegu (AnimalNotFoundError)
6. Karmienie zwierząt (feed, feed_all)
7. Walidacja health (clamping 0–100)
8. Porównanie obiektów (metody specjalne __eq__)
9. Sortowanie obiektów (__lt__)
10. Walidacja danych (wyjątki przy nieprawidłowych wartościach)
11. Reprezentacje obiektów (__str__, __repr__)
12. Polimorfizm – wywołanie metod na liście różnych zwierząt
13. Dziedziczenie – sprawdzenie isinstance/issubclass
14. FeedingSchedule – dodawanie/usuwanie wpisów
15. Raport o stanie zoo

---

## 3. Szkielet klas i metod

```python
# exceptions.py
class ZooError(Exception): pass
class EnclosureFullError(ZooError): pass
class AnimalNotFoundError(ZooError): pass
class InvalidAnimalDataError(ZooError): pass

# animals.py
from abc import ABC, abstractmethod

class Animal(ABC):
    _next_id: int = 1
    def __init__(self, name: str, species: str, age: int) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...     # walidacja: nie puste
    @property
    def health(self) -> int: ...
    @health.setter
    def health(self, value: int) -> None: ...   # clamp 0-100
    @abstractmethod
    def make_sound(self) -> str: ...
    @abstractmethod
    def diet(self) -> str: ...
    def feed(self) -> str: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other) -> bool: ...        # po _id
    def __hash__(self) -> int: ...
    def __lt__(self, other) -> bool: ...        # po name

class Mammal(Animal):
    def __init__(self, name, species, age, fur_color="brown"): ...
    def diet(self) -> str: ...
    def give_birth(self) -> str: ...

class Bird(Animal):
    def __init__(self, name, species, age, wingspan=1.0, can_fly=True): ...
    def diet(self) -> str: ...
    def fly(self) -> str: ...

class Reptile(Animal):
    def __init__(self, name, species, age, is_venomous=False): ...
    def diet(self) -> str: ...
    def bask(self) -> str: ...

class Lion(Mammal):
    def __init__(self, name, age, mane=True): ...
    def make_sound(self) -> str: ...
    def diet(self) -> str: ...

class Elephant(Mammal):
    def __init__(self, name, age, tusk_length=0.0): ...
    def make_sound(self) -> str: ...
    def diet(self) -> str: ...

class Monkey(Mammal):
    def __init__(self, name, age): ...
    def make_sound(self) -> str: ...

class Eagle(Bird):
    def __init__(self, name, age): ...
    def make_sound(self) -> str: ...

class Penguin(Bird):
    def __init__(self, name, age): ...
    def make_sound(self) -> str: ...

class Crocodile(Reptile):
    def __init__(self, name, age, length=3.0): ...
    def make_sound(self) -> str: ...

# employees.py
class Employee(ABC):
    _next_id: int = 1
    def __init__(self, name: str, salary: float) -> None: ...
    @abstractmethod
    def work(self) -> str: ...
    @abstractmethod
    def role(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class Zookeeper(Employee):
    def assign_to(self, enclosure) -> None: ...
    def feed_animals(self) -> str: ...
    def work(self) -> str: ...
    def role(self) -> str: ...

class Veterinarian(Employee):
    def __init__(self, name, specialization="general", salary=7000.0): ...
    def work(self) -> str: ...
    def role(self) -> str: ...

class Guide(Employee):
    def __init__(self, name, languages=None, salary=3500.0): ...
    def work(self) -> str: ...
    def role(self) -> str: ...

# enclosure.py
class Enclosure:
    def __init__(self, name: str, capacity: int) -> None: ...
    def add_animal(self, animal) -> None: ...      # EnclosureFullError
    def remove_animal(self, animal) -> Animal: ...  # AnimalNotFoundError
    def find_animal(self, name: str): ...
    def feed_all(self) -> list: ...
    def __len__(self) -> int: ...
    def __contains__(self, animal) -> bool: ...
    def __iter__(self): ...
    def __repr__(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

# feeding.py
from dataclasses import dataclass

@dataclass
class FeedingEntry:
    enclosure_name: str
    time: str
    food_type: str
    notes: str = ""

class FeedingSchedule:
    def __init__(self, day="Monday"): ...
    def add_entry(self, enclosure_name, time, food_type, notes=""): ...
    def get_by_enclosure(self, name) -> list: ...
    def __len__(self) -> int: ...

# zoo.py
class Zoo:
    def __init__(self, name: str, city: str = "Lodz") -> None: ...
    def create_enclosure(self, name, capacity) -> Enclosure: ...
    def hire_employee(self, employee) -> None: ...
    def total_animals(self) -> int: ...
    def find_animal(self, name): ...
    def report(self) -> str: ...
    def __getitem__(self, name: str) -> Enclosure: ...
    def __contains__(self, item) -> bool: ...
    def __len__(self) -> int: ...
```

---

## 4. Pytania do obrony projektu

> ⚠️ WAŻNE: Podczas obrony prowadzący może zadać dowolne z poniższych pytań. Odpowiedzi powinny być poparte konkretnymi przykładami z kodu projektu.

### Pytania teoretyczne (1–15)
1. Dlaczego klasa Animal jest abstrakcyjna (ABC)? Które metody oznaczyłeś @abstractmethod i dlaczego właśnie te?
2. Wyjaśnij różnicę między relacjami: Zoo – Enclosure (kompozycja), Enclosure – Animal (agregacja), Zookeeper – Enclosure (asocjacja). Co się stanie z obiektami zależnymi, jeśli usuniemy obiekt nadrzędny?
3. Dlaczego atrybut _health ma setter z clamping (max(0, min(100, value)))? Co by się stało bez tej walidacji?
4. Co to jest atrybut klasy _next_id i dlaczego jest współdzielony między instancjami? Jak to się różni od atrybutu instancji?
5. Wyjaśnij, czym jest polimorfizm na przykładzie metody make_sound(). Co się stanie, jeśli wywołamy [Lion(...), Eagle(...), Crocodile(...)][i].make_sound()?
6. Dlaczego Enclosure.animals zwraca kopię listy (list(self._animals)), a nie referencję do oryginalnej? Co by się stało, gdyby zwracała referencję?
7. Jakie metody specjalne (dunder) zaimplementowałeś w klasie Enclosure i do czego każda służy?
8. Dlaczego FeedingEntry jest @dataclass, a nie zwykła klasa? Co dataclass generuje automatycznie?
9. Co by się stało, gdybyś próbował utworzyć obiekt klasy Animal() bezpośrednio? Dlaczego?
10. Wyjaśnij hierarchię wyjątków: ZooError -> EnclosureFullError. Dlaczego warto mieć bazowy wyjątek?
11. Czym różni się asocjacja od agregacji na przykładzie Zookeeper i Enclosure? Kiedy stosujemy którą relację?
12. Dlaczego metoda animals w klasie Enclosure zwraca list(self._animals)? Co to daje w kontekście bezpieczeństwa danych?
13. Wyjaśnij, jak działa wzorzec _next_id jako atrybut klasy. Czy każda podklasa Animal ma osobny licznik?
14. Co oznacza dekorator @abstractmethod i co się stanie, jeśli podklasa nie zaimplementuje metody abstrakcyjnej?
15. Dlaczego klasa FeedingSchedule stosuje kompozycję z FeedingEntry, a nie agregację? Jaka jest różnica w cyklu życia obiektów?

### Pytania praktyczne / z kodu (16–30)
16. Co wypisze print(lion) vs print(repr(lion)) jeśli lion = Lion('Simba', 5)? Dlaczego wyniki się różnią?
17. Co się stanie, gdy wykonasz enc.add_animal(lion) na pełnym wybiegu (capacity=2, już 2 zwierzęta)? Jaki wyjątek zostanie rzucony?
18. Napisz kod demonstracyjny, który tworzy zoo z dwoma wybiegami, dodaje po 3 zwierzęta do każdego i wypisuje raport.
19. Dlaczego lion1 == lion2 zwraca False nawet jeśli oba lwy mają to samo imię? Po czym porównuje __eq__?
20. Jak sprawdzisz, czy lion jest w wybiegu savanna? Napisz dwie metody (z 'in' i z find_animal()).
21. Co zwróci sorted([Lion('C',3), Eagle('A',2), Penguin('B',1)])? Po czym sortuje __lt__?
22. Jak dodać nowy gatunek zwierzęcia (np. Giraffe) do projektu? Które klasy trzeba zmodyfikować/utworzyć i jakie metody zaimplementować?
23. Wyjaśnij, dlaczego Zookeeper ma _assigned_enclosure: Optional[Enclosure] = None – co to oznacza w kontekście relacji OOP?
24. Napisz test pytest, który sprawdza że dodanie zwierzęcia do pełnego wybiegu rzuca EnclosureFullError. Użyj pytest.raises.
25. Co robi Zoo.__contains__ – jak sprawdza czy obiekt jest w zoo? Dlaczego obsługuje zarówno Animal jak i Employee?
26. Napisz fixture pytest, który tworzy zoo z jednym wybiegiem i trzema zwierzętami. Jak go użyjesz w testach?
27. Co się stanie, gdy wywołasz zoo['Savanna'] na instancji Zoo? Który dunder method jest odpowiedzialny?
28. Zademonstruj użycie isinstance() i issubclass() na hierarchii Animal. Podaj 3 przykłady.
29. Jak zaimplementowałeś metodę Zoo.report()? Jakie informacje zawiera raport?
30. Wyjaśnij, dlaczego __hash__ jest potrzebny razem z __eq__. Co się stanie, jeśli zdefiniujesz __eq__ bez __hash__?

---

## 5. Etapy realizacji projektu

### 5.1 Etap 1 – Plan (przed zjazdem 1)
Plik README.md z opisem: nazwa projektu, lista planowanych klas z krótkimi opisami, relacje między klasami, planowane funkcjonalności, 3 User Stories.

> Wgrywasz: README.md

### 5.2 Etap 2 – Szkielet klas (zjazd 1 → zjazd 2)
Kod się uruchamia, logika minimalna:

- Klasy abstrakcyjne (ABC) z `@abstractmethod`
- Hierarchia dziedziczenia
- `__init__` z enkapsulacją (`@property` z walidacją)
- Puste lub minimalne implementacje metod

> Wgrywasz: katalog z kodem

### 5.3 Etap 3 – Działający system (zjazd 2 → zjazd 3)
Pełna funkcjonalność:

- Relacje między obiektami
- Metody specjalne
- Logika biznesowa i polimorfizm
- Dokładnie 15 testów (pytest)
- Docstringi i type hints

> Wgrywasz: kompletny projekt

### 5.4 Etap 4 – Prezentacja i oddanie (zjazd 3)
Prezentacja na zajęciach + oddanie ZIP.

---

## 6. Wymagania techniczne OOP

### 6.1 Checklista mechanizmów OOP

> ⚠️ WAŻNE: W pliku CHECKLIST.md należy zaznaczyć zrealizowane mechanizmy i podać krótką lokalizację (plik:linia lub plik:metoda).

**Podstawy klas (5 pozycji)**
- [ ] Klasy i obiekty – definicja klas, tworzenie obiektów
- [ ] Konstruktor __init__ – inicjalizacja atrybutów
- [ ] Atrybuty instancji – unikalne dla każdego obiektu
- [ ] Atrybuty klasy – współdzielone między instancjami (np. _next_id)
- [ ] Metody instancji – operacje na obiektach

**Enkapsulacja i metody specjalne (7 pozycji)**
- [ ] Prywatne atrybuty – konwencja _protected lub __private
- [ ] @property – gettery
- [ ] @property.setter – settery z walidacją
- [ ] __str__() – reprezentacja dla użytkownika
- [ ] __repr__() – reprezentacja dla debugowania
- [ ] __eq__() – porównywanie obiektów
- [ ] Co najmniej 1 dodatkowa metoda specjalna (np. __lt__, __len__, __contains__, __iter__, __getitem__)

**Dziedziczenie (5 pozycji)**
- [ ] Klasa bazowa – Character/Animal/Item lub odpowiednik
- [ ] Klasy pochodne – dokładnie 3 dla głównej hierarchii, dokładnie 3 dla drugiej
- [ ] super() – wywołanie konstruktora rodzica
- [ ] Nadpisywanie metod (override) – dokładnie 1 metoda
- [ ] isinstance() i issubclass() – użyte gdziekolwiek

**Polimorfizm (2 pozycji)**
- [ ] Polimorfizm – ta sama metoda, różne implementacje
- [ ] Duck typing – lista różnych obiektów, wspólny interfejs

**Kompozycja i agregacja (2 pozycji)**
- [ ] Kompozycja – has-a, silne powiązanie
- [ ] Agregacja – has-a, słabsze powiązanie

**Klasy abstrakcyjne i operatory (3 pozycji)**
- [ ] Klasa abstrakcyjna (ABC) – import z abc
- [ ] @abstractmethod – wymuszenie implementacji
- [ ] Przeciążanie operatorów – dokładnie 1 operator

**Wyjątki (4 pozycji)**
- [ ] Własny wyjątek bazowy – dziedziczący po Exception
- [ ] Hierarchia wyjątków – dokładnie 2 specjalizowane
- [ ] Zgłaszanie wyjątków – raise w metodach
- [ ] Obsługa wyjątków – try-except

**Testowanie i dokumentacja (3 pozycji)**
- [ ] Testy pytest – dokładnie 15 testów
- [ ] Docstringi – dla wszystkich klas i metod publicznych
- [ ] Type hints – dla głównych metod

---

## 7. Testy jednostkowe

### 7.1 Wymagania
- Framework: `pytest`
- Plik: `test_*.py` (jeden lub kilka)
- **Dokładnie 15 testów** pokrywających główne funkcjonalności
- Testy muszą przechodzić (pytest zwraca sukces)
- Użycie fixture'ów do setUp
- Użycie `pytest.raises` do testowania wyjątków

---

## 8. Dokumentacja

### 8.1 Wymagane pliki
- **README.md** – opis projektu, instrukcja uruchomienia, wymagania, opis klas, lista mechanik OOP, 3 User Stories
- **CHECKLIST.md** – zaznaczone mechanizmy z sekcji 6, krótka lokalizacja w kodzie
- **JUSTIFICATION.md** – uzasadnienia decyzji projektowych

### 8.2 Type hints
Należy stosować adnotacje typów dla: parametrów metod publicznych, wartości zwracanych, atrybutów klas.

### 8.3 Docstringi w kodzie
- Dla każdej klasy
- Dla każdej metody publicznej
- Format: Google

---

## 9. Struktura projektu

```
projekt/
|-- src/
|   |-- zoo/
|       |-- __init__.py
|       |-- ...  (pliki modułów)
|       |-- exceptions.py
|-- tests/
|   |-- conftest.py
|   |-- test_*.py
|-- demo.py
|-- README.md
|-- CHECKLIST.md
|-- JUSTIFICATION.md
|-- requirements.txt
|-- .gitignore
```

### Plik requirements.txt:
```
pytest>=7.0.0
pytest-cov>=4.0.0  # opcjonalnie
```

---

## 10. Prezentacja i oddanie

### 10.1 Prezentacja (2–3 min)
- Krótki opis koncepcji projektu
- Demonstracja działania programu (uruchomienie demo.py)
- Omówienie wybranych decyzji projektowych
- Pokazanie wybranych fragmentów kodu
- Prezentację wyników testów (pytest)

### 10.2 Obrona projektu
Każda osoba odpowiada za swój przydział pracy. Prowadzący może pytać o: mechanizmy OOP, uzasadnienia decyzji, działanie fragmentów kodu, testy, własny wkład. Pytania do obrony znajdują się w sekcji 4 tego dokumentu.

### 10.3 Forma oddania
- **Format:** Archiwum ZIP
- **Nazwa pliku:** nazwisko_imie_oop1_projekt.zip
- **Zawartość:** kod źródłowy, testy, README.md, CHECKLIST.md, JUSTIFICATION.md, requirements.txt
- **Miejsce oddania:** platforma zdalnego nauczania

### 10.4 Wymagania techniczne
- Python 3.10 lub nowszy
- Kod musi działać bez błędów
- Wszystkie testy muszą przechodzić
- Kod zgodny z PEP 8

### 10.5 Przed oddaniem – checklist
- [ ] Wszystkie testy przechodzą (pytest)
- [ ] Program demonstracyjny działa poprawnie
- [ ] README.md jest kompletne i czytelne
- [ ] CHECKLIST.md jest wypełniony
- [ ] JUSTIFICATION.md zawiera wszystkie wymagane sekcje
- [ ] Kod ma docstringi i type hints
- [ ] Struktura projektu jest zgodna z wymaganiami
- [ ] Plik ZIP ma poprawną nazwę

---

**Powodzenia!**

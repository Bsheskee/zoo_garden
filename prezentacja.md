# Prezentacja — Zoo Garden Management System

> Czas prezentacji: 2–3 minuty (sekcja 10.1 specyfikacji)

---

## 1. Krótki opis koncepcji projektu

**Zoo Garden** to system zarządzania ogrodem zoologicznym napisany w Pythonie z pełnym wykorzystaniem mechanizmów OOP.

System pozwala na:
- Tworzenie zoo z wybiegami (ograniczona pojemność),
- Dodawanie 6 gatunków zwierząt (Lion, Elephant, Monkey, Eagle, Penguin, Crocodile),
- Zarządzanie 3 typami pracowników (Zookeeper, Veterinarian, Guide),
- Karmienie zwierząt, leczenie, generowanie raportów,
- Harmonogramowanie karmienia (`FeedingSchedule` + `FeedingEntry` @dataclass).

Hierarchia klas:
```
Animal (ABC)
 ├── Mammal  →  Lion, Elephant, Monkey
 ├── Bird    →  Eagle, Penguin
 └── Reptile →  Crocodile

Employee (ABC)
 ├── Zookeeper
 ├── Veterinarian
 └── Guide
```

---

## 2. Demonstracja działania programu

Uruchomienie demo:
```bash
python3 demo.py
```

Demonstrowane scenariusze (zgodnie ze specyfikacją):
1. Stworzenie zoo z wybiegami (`Zoo`, `create_enclosure`)
2. Dodanie zwierząt do wybiegów (`add_animal`)
3. Próba dodania do pełnego wybiegu → `EnclosureFullError`
4. Karmienie zwierząt (`feed_all`)
5. Przypisanie opiekuna do wybiegu (`assign_to`)
6. Generowanie raportu (`zoo.report()`)
7. Polimorficzne wywołanie `make_sound()` i `diet()` na liście różnych zwierząt

---

## 3. Omówienie wybranych decyzji projektowych

### Kompozycja vs agregacja
- `Zoo` ◆–– `Enclosure`: wybiegi tworzone przez `create_enclosure()`, nie istnieją bez zoo.
- `Enclosure` ◇–– `Animal`: zwierzę może istnieć poza wybiegiem.
- `Zookeeper` –– `Enclosure`: asocjacja — opiekun zna wybieg, ale obaj istnieją niezależnie.

### Clamping zdrowia
Zamiast rzucać wyjątek, setter `health` cicho koryguje wartość do zakresu 0–100:
```python
self._health = max(0, min(100, value))
```

### Flyable mixin
`Eagle` dziedziczy po `Bird` i `Flyable` (multiple inheritance). `Penguin` dziedziczy tylko po `Bird` i nie może latać — jest to ekspresywniejsze niż flaga `can_fly=False`.

### FeedingEntry jako @dataclass
Czysty kontener danych → `@dataclass` generuje `__init__`, `__repr__`, `__eq__` automatycznie.

---

## 4. Wybrane fragmenty kodu

### Polimorfizm — `make_sound()`
```python
animals = [Lion("Simba", 5), Eagle("Freedom", 4), Crocodile("Snap", 8)]
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")
# Simba: Roar!
# Freedom: Screech!
# Snap: Hiss!
```

### Obsługa wyjątków
```python
try:
    full_enclosure.add_animal(new_lion)
except EnclosureFullError as e:
    print(f"Błąd: {e}")
```

### Metody specjalne Enclosure
```python
enc = Enclosure("Savanna", 3)
enc.add_animal(lion)
len(enc)          # 1
lion in enc       # True
for a in enc:     # iteracja
    print(a)
```

---

## 5. Wyniki testów

Uruchomienie testów:
```bash
python3 -m pytest tests/ -v
```

**Wynik: 45 testów — wszystkie zaliczone (PASSED)**

Pokrycie wszystkich 15 scenariuszy ze specyfikacji (sekcja 2.6):
- Tworzenie i właściwości zwierząt, clamping zdrowia, polimorfizm, sortowanie
- Operacje na wybiegu: dodawanie, usuwanie, wyjątki, dunder methods
- Zoo: raport, pracownicy, harmonogram karmienia

Użyto `pytest.raises` do testowania wyjątków:
```python
with pytest.raises(EnclosureFullError):
    enclosure.add_animal(Lion("Extra", 1))

with pytest.raises(AnimalNotFoundError):
    enclosure.remove_animal(lion_not_in_enclosure)
```

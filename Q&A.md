# Q&A — Odpowiedzi do pytań obronnych

> Pytania pochodzą z sekcji 4 pliku `Projekt_A_Zoo_Garden.md`.  
> Wszystkie odwołania do kodu dotyczą aktualnego stanu repozytorium.

---

## Pytania teoretyczne (1–15)

### 1. Dlaczego klasa `Animal` jest abstrakcyjna (ABC)? Które metody oznaczyłeś `@abstractmethod` i dlaczego właśnie te?

`Animal` jest abstrakcyjna, bo reprezentuje ogólny koncept zwierzęcia — nie istnieje żadne „zwierzę w ogóle", zawsze jest to konkretny gatunek. Oznaczenie klasy jako `ABC` sprawia, że nie można stworzyć instancji bezpośrednio (`Animal("X", 5)` rzuci `TypeError`).

Metodami `@abstractmethod` są:
- `make_sound()` — każdy gatunek wydaje inny dźwięk; nie ma sensownej implementacji domyślnej,
- `diet()` — dieta zależy od gatunku (mięsożerny, roślinożerny, wszystkożerny).

Gdyby te metody nie były abstrakcyjne, podklasy mogłyby ich nie implementować i dostawać `None` lub pusty string — co prowadziłoby do cichych błędów.

**Kod:** `zoo/animals/animal.py:53–61`

---

### 2. Wyjaśnij różnicę między relacjami: Zoo–Enclosure (kompozycja), Enclosure–Animal (agregacja), Zookeeper–Enclosure (asocjacja). Co się stanie z obiektami zależnymi, jeśli usuniemy obiekt nadrzędny?

| Relacja | Typ | Co się dzieje po usunięciu nadrzędnego |
|:--------|:----|:---------------------------------------|
| `Zoo` ◆–– `Enclosure` | Kompozycja | Wybiegi są tworzone *przez* `zoo.create_enclosure()` i przechowywane w `_enclosures`. Usunięcie obiektu `Zoo` powoduje, że wybiegi tracą referencję i są usuwane przez GC. |
| `Enclosure` ◇–– `Animal` | Agregacja | Zwierzę może istnieć poza wybiegiem (jest tworzone niezależnie i dopiero potem dodawane). Usunięcie wybiegu nie niszczy obiektu zwierzęcia. |
| `Zookeeper` –– `Enclosure` | Asocjacja | Opiekun przechowuje referencję do wybiegu (`_assigned_enclosure`), ale obaj mogą istnieć niezależnie. Usunięcie wybiegu nie usuwa opiekuna i na odwrót. |

**Kod:** `zoo/zoo.py:26–27`, `zoo/enclosure.py:22`, `zoo/employees/zookeeper.py:18`

---

### 3. Dlaczego atrybut `_health` ma setter z clamping (`max(0, min(100, value))`)? Co by się stało bez tej walidacji?

Clamping gwarantuje, że zdrowie zawsze mieści się w 0–100. Bez tego:
- `lion.health = 150` → `_health = 150` (zdrowie > 100 jest niespójne logicznie),
- `lion.health = -10` → `_health = -10` (ujemne zdrowie nie ma sensu dziedzinowo).

Zamiast rzucać wyjątek (co przerywałoby działanie programu przy każdym leczeniu, które przekroczy pełne zdrowie), clamping cicho koryguje wartość. Jest to bezpieczniejsze i bardziej odporne na błędy.

**Kod:** `zoo/animals/animal.py:49–51`

---

### 4. Co to jest atrybut klasy `_next_id` i dlaczego jest współdzielony między instancjami? Jak to się różni od atrybutu instancji?

`_next_id: int = 1` zdefiniowane na poziomie klasy (przed `__init__`) jest **atrybutem klasy** — istnieje jedna kopia dla wszystkich instancji i jest dostępna przez `Animal._next_id`.

W `__init__` wykonujemy:
```python
self._id = Animal._next_id
Animal._next_id += 1
```
Każda nowa instancja pobiera aktualną wartość licznika, a potem go inkrementuje. Dzięki temu każde zwierzę ma unikalny `_id`.

**Różnica od atrybutu instancji:** atrybut instancji (np. `self._name`) jest tworzony osobno dla każdego obiektu i nie jest widoczny dla pozostałych instancji. Atrybut klasy jest jeden i współdzielony.

**Kod:** `zoo/animals/animal.py:18`, `zoo/animals/animal.py:21–22`

---

### 5. Wyjaśnij, czym jest polimorfizm na przykładzie metody `make_sound()`. Co się stanie, jeśli wywołamy `[Lion(...), Eagle(...), Crocodile(...)][i].make_sound()`?

Polimorfizm oznacza, że ta sama nazwa metody (`make_sound()`) ma różne implementacje w różnych klasach. Wywołując ją na obiekcie, Python automatycznie kieruje do właściwej implementacji na podstawie rzeczywistego typu obiektu (ang. *dynamic dispatch*).

```python
animals = [Lion("Simba", 5), Eagle("Freedom", 4), Crocodile("Snap", 8)]
for a in animals:
    print(a.make_sound())
# Roar!
# Screech!
# Hiss!
```

Kod kliencki nie musi wiedzieć, jakiego konkretnego typu jest obiekt — wystarczy, że należy do hierarchii `Animal`.

**Kod:** `zoo/animals/lion.py:11`, `zoo/animals/eagle.py:12`, `zoo/animals/crocodile.py:12`

---

### 6. Dlaczego `Enclosure.animals` zwraca kopię listy (`list(self._animals)`), a nie referencję do oryginalnej? Co by się stało, gdyby zwracała referencję?

Gdyby zwracała referencję, zewnętrzny kod mógłby modyfikować wewnętrzną listę z pominięciem walidacji:
```python
enc.animals.append(lion)       # pomija sprawdzenie pojemności
enc.animals.remove(lion)       # pomija AnimalNotFoundError
```

Zwracanie kopii chroni enkapsulację — jedynym sposobem na modyfikację listy są publiczne metody `add_animal()` i `remove_animal()`, które wykonują walidację.

**Kod:** `zoo/enclosure.py:34–35`

---

### 7. Jakie metody specjalne (dunder) zaimplementowałeś w klasie `Enclosure` i do czego każda służy?

| Metoda | Działanie | Przykład użycia |
|:-------|:----------|:----------------|
| `__len__` | Liczba zwierząt | `len(enc)` |
| `__contains__` | Sprawdzenie przynależności | `lion in enc` |
| `__iter__` | Iteracja po zwierzętach | `for a in enc:` |
| `__repr__` | Reprezentacja debuggingowa | `repr(enc)` |
| `__str__` | Reprezentacja dla użytkownika | `print(enc)` |
| `__eq__` | Porównanie po `_name` | `enc1 == enc2` |
| `__hash__` | Hash na podstawie `_name` | `{enc}`, `enc in set` |

**Kod:** `zoo/enclosure.py:89–110`

---

### 8. Dlaczego `FeedingEntry` jest `@dataclass`, a nie zwykła klasa? Co `dataclass` generuje automatycznie?

`FeedingEntry` to czysty kontener danych bez logiki biznesowej. `@dataclass` automatycznie generuje:
- `__init__` z parametrami odpowiadającymi polom,
- `__repr__` czytelny dla debugowania,
- `__eq__` porównujący pola wartościowo.

Dzięki temu unikamy ręcznego pisania boilerplate. Pole `notes: str = ""` pokazuje wartość domyślną — `@dataclass` obsługuje to elegancko.

**Kod:** `zoo/feeding_schedule.py:7–21`

---

### 9. Co by się stało, gdybyś próbował utworzyć obiekt klasy `Animal()` bezpośrednio? Dlaczego?

```python
a = Animal("Leo", 3)
# TypeError: Can't instantiate abstract class Animal
# with abstract methods diet, make_sound
```

Python nie pozwala na tworzenie instancji klas abstrakcyjnych, które mają niezaimplementowane metody `@abstractmethod`. Mechanizm ABC sprawdza to w trakcie wywołania `__new__`.

**Kod:** `zoo/animals/animal.py:6`, import `ABC` z modułu `abc`

---

### 10. Wyjaśnij hierarchię wyjątków: `ZooError → EnclosureFullError`. Dlaczego warto mieć bazowy wyjątek?

```
ZooError(Exception)
├── EnclosureFullError
├── AnimalNotFoundError
└── InvalidAnimalDataError
```

Zalety bazowego wyjątku:
- Można złapać wszystkie błędy domeny jednym `except ZooError`,
- Można też precyzyjnie łapać konkretny podtyp (`except EnclosureFullError`),
- Oddziela błędy domenowe od systemowych (`ValueError`, `KeyError`),
- Ułatwia rozbudowę — nowy typ błędu dziedziczy po `ZooError` bez zmiany istniejącego kodu.

**Kod:** `zoo/exceptions.py:4–25`

---

### 11. Czym różni się asocjacja od agregacji na przykładzie `Zookeeper` i `Enclosure`? Kiedy stosujemy którą relację?

- **Agregacja** (`Enclosure ◇–– Animal`): obiekt-część (*Animal*) może istnieć bez obiektu-całości (*Enclosure*). Zwierzę tworzymy niezależnie i dodajemy do wybiegu; może też być w żadnym wybiegu.

- **Asocjacja** (`Zookeeper –– Enclosure`): obaj partnerzy istnieją niezależnie i są powiązani przez referencję. Opiekun *zna* wybieg (ma go zapisanego w `_assigned_enclosure`), ale żaden nie należy do drugiego.

Agregację stosujemy gdy chcemy wyrazić relację „zawiera", asocjację gdy chcemy wyrazić „współpracuje z" bez implikowania własności.

**Kod:** `zoo/employees/zookeeper.py:18`, `zoo/enclosure.py:22`

---

### 12. Dlaczego metoda `animals` w klasie `Enclosure` zwraca `list(self._animals)`? Co to daje w kontekście bezpieczeństwa danych?

Patrz odpowiedź na pytanie 6. Zwracanie kopii gwarantuje, że:
- Zewnętrzny kod widzi aktualny stan listy (jest to płytka kopia, nie głęboka),
- Nie może modyfikować wewnętrznej listy `_animals` bezpośrednio,
- Każde wywołanie `.animals` zwraca niezależny obiekt listy.

**Kod:** `zoo/enclosure.py:34–35`

---

### 13. Wyjaśnij, jak działa wzorzec `_next_id` jako atrybut klasy. Czy każda podklasa `Animal` ma osobny licznik?

Nie — licznik jest we wspólnej klasie bazowej `Animal`:
```python
class Animal(ABC):
    _next_id: int = 1
```
W `__init__` używamy `Animal._next_id` (nie `self.__class__._next_id`), więc wszystkie podklasy współdzielą **jeden** licznik. `Lion("A", 1)` dostanie id=1, następny `Eagle("B", 2)` dostanie id=2 — niezależnie od gatunku.

Gdybyśmy chcieli osobnych liczników, każda podklasa musiałaby definiować własne `_next_id`.

**Kod:** `zoo/animals/animal.py:18`, `zoo/animals/animal.py:21–22`

---

### 14. Co oznacza dekorator `@abstractmethod` i co się stanie, jeśli podklasa nie zaimplementuje metody abstrakcyjnej?

`@abstractmethod` (z modułu `abc`) oznacza metodę, którą każda konkretna podklasa *musi* zaimplementować. Jeśli tego nie zrobi, Python nie pozwoli stworzyć jej instancji:

```python
class Parrot(Bird):
    pass  # brak make_sound()

p = Parrot("Polly", 2)
# TypeError: Can't instantiate abstract class Parrot
# without an implementation for abstract method 'make_sound'
```

**Kod:** `zoo/animals/animal.py:53`, `zoo/employees/employee.py:61`

---

### 15. Dlaczego klasa `FeedingSchedule` stosuje kompozycję z `FeedingEntry`, a nie agregację? Jaka jest różnica w cyklu życia obiektów?

- **Kompozycja** (`FeedingSchedule ◆–– FeedingEntry`): wpisy karmienia są tworzone *wewnątrz* metody `add_entry()` i przechowywane w `_entries`. Nie istnieją poza harmonogramem — kiedy harmonogram zostaje usunięty, jego wpisy też.

- **Agregacja**: obiekt-część może istnieć niezależnie — można by przekazywać gotowe `FeedingEntry` z zewnątrz i przechowywać je w wielu miejscach jednocześnie.

W naszym przypadku wpis nie ma sensu bez kontekstu harmonogramu, dlatego wybraliśmy kompozycję.

**Kod:** `zoo/feeding_schedule.py:59`

---

## Pytania praktyczne / z kodu (16–30)

### 16. Co wypisze `print(lion)` vs `print(repr(lion))` jeśli `lion = Lion('Simba', 5)`?

```python
lion = Lion("Simba", 5)
print(lion)        # Simba the Lion
print(repr(lion))  # Lion(name='Simba', age=5)
```

`__str__` jest przeznaczony dla użytkownika końcowego — czytelna, opisowa forma.  
`__repr__` jest dla programisty — formalny zapis pozwalający odtworzyć obiekt lub zidentyfikować go w debuggerze.

**Kod:** `zoo/animals/animal.py:66–70`

---

### 17. Co się stanie, gdy wykonasz `enc.add_animal(lion)` na pełnym wybiegu (capacity=2, już 2 zwierzęta)?

Zostanie rzucony `EnclosureFullError`:
```python
enc = Enclosure("Savanna", 2)
enc.add_animal(Lion("A", 1))
enc.add_animal(Lion("B", 2))
enc.add_animal(Lion("C", 3))
# EnclosureFullError: Enclosure 'Savanna' is full (capacity: 2)
```

Warunek sprawdzany jest w `add_animal()`: `if len(self._animals) >= self._capacity`.

**Kod:** `zoo/enclosure.py:47–48`

---

### 18. Napisz kod demonstracyjny, który tworzy zoo z dwoma wybiegami, dodaje po 3 zwierzęta do każdego i wypisuje raport.

```python
from zoo.zoo import Zoo
from zoo.animals import Lion, Elephant, Monkey, Eagle, Penguin, Crocodile

zoo = Zoo("My Zoo", "Lodz")
savanna = zoo.create_enclosure("Savanna", 3)
aviary  = zoo.create_enclosure("Aviary", 3)

savanna.add_animal(Lion("Simba", 5))
savanna.add_animal(Elephant("Dumbo", 10))
savanna.add_animal(Monkey("George", 3))

aviary.add_animal(Eagle("Freedom", 4))
aviary.add_animal(Penguin("Waddle", 2))
aviary.add_animal(Crocodile("Snap", 8))

print(zoo.report())
```

**Kod:** `demo.py:17–44`, `zoo/zoo.py:110–131`

---

### 19. Dlaczego `lion1 == lion2` zwraca `False` nawet jeśli oba lwy mają to samo imię? Po czym porównuje `__eq__`?

`Animal.__eq__` porównuje po `_id` (unikalnym identyfikatorze nadawanym przez `_next_id`):
```python
def __eq__(self, other) -> bool:
    if not isinstance(other, Animal):
        return False
    return self._id == other._id
```

Dwa osobne wywołania `Lion("Simba", 5)` tworzą dwa obiekty z różnymi `_id`, więc `lion1 == lion2` → `False`. Gdybyśmy porównywali po imieniu, dwie różne Simby byłyby nie do odróżnienia.

**Kod:** `zoo/animals/animal.py:72–75`

---

### 20. Jak sprawdzisz, czy `lion` jest w wybiegu `savanna`? Napisz dwie metody (z `in` i z `find_animal()`).

```python
# Metoda 1 — operator 'in' (używa __contains__)
if lion in savanna:
    print("lion is in savanna")

# Metoda 2 — find_animal()
found = savanna.find_animal("Simba")
if found is not None:
    print(f"Found: {found}")
```

`__contains__` sprawdza przynależność obiektu do wewnętrznej listy `_animals` przez porównanie `__eq__` (czyli po `_id`). `find_animal()` przeszukuje po nazwie.

**Kod:** `zoo/enclosure.py:92–93`, `zoo/enclosure.py:65–78`

---

### 21. Co zwróci `sorted([Lion('C',3), Eagle('A',2), Penguin('B',1)])`? Po czym sortuje `__lt__`?

```python
sorted([Lion("C", 3), Eagle("A", 2), Penguin("B", 1)])
# [Eagle('A', ...), Penguin('B', ...), Lion('C', ...)]
```

`Animal.__lt__` porównuje po `self._name < other._name` (leksykograficznie):
```python
def __lt__(self, other) -> bool:
    return self._name < other._name
```

Wynik: A < B < C → Eagle, Penguin, Lion.

**Kod:** `zoo/animals/animal.py:80–83`

---

### 22. Jak dodać nowy gatunek zwierzęcia (np. `Giraffe`) do projektu? Które klasy trzeba zmodyfikować/utworzyć i jakie metody zaimplementować?

1. Utwórz `zoo/animals/giraffe.py`:
```python
from .mammal import Mammal

class Giraffe(Mammal):
    def __init__(self, name: str, age: int, neck_length: float = 1.8) -> None:
        super().__init__(name, age)
        self._neck_length = neck_length

    def make_sound(self) -> str:
        return "Grunt!"

    def diet(self) -> str:
        return "Giraffes are herbivores, eating leaves from tall trees."
```
2. Dodaj import `Giraffe` do `zoo/animals/__init__.py` i do `__all__`.
3. Nie trzeba modyfikować żadnych innych klas — dziedziczenie i polimorfizm dbają o resztę.

**Kod:** `zoo/animals/__init__.py`

---

### 23. Wyjaśnij, dlaczego `Zookeeper` ma `_assigned_enclosure: Optional[Enclosure] = None` — co to oznacza w kontekście relacji OOP?

`Optional[Enclosure]` oznacza, że pole może przyjąć wartość `Enclosure` lub `None`. Opiekun domyślnie nie jest przypisany do żadnego wybiegu (`None`). Dopiero wywołanie `assign_to(enclosure)` ustawia referencję.

To jest klasyczna **asocjacja z opcjonalnym końcem** — opiekun *może* być powiązany z wybiegiem, ale nie *musi*. Gdyby to była kompozycja, wybieg musiałby być przekazany w konstruktorze i nie mógłby być `None`.

**Kod:** `zoo/employees/zookeeper.py:18`

---

### 24. Napisz test pytest, który sprawdza że dodanie zwierzęcia do pełnego wybiegu rzuca `EnclosureFullError`. Użyj `pytest.raises`.

```python
import pytest
from zoo.animals import Lion
from zoo.enclosure import Enclosure
from zoo.exceptions import EnclosureFullError

def test_enclosure_capacity_validation():
    enc = Enclosure("Savanna", 2)
    enc.add_animal(Lion("A", 1))
    enc.add_animal(Lion("B", 2))

    with pytest.raises(EnclosureFullError):
        enc.add_animal(Lion("C", 3))
```

Taki test już istnieje w projekcie.

**Kod:** `tests/test_enclosure.py:39–48`

---

### 25. Co robi `Zoo.__contains__` — jak sprawdza czy obiekt jest w zoo? Dlaczego obsługuje zarówno `Animal` jak i `Employee`?

```python
def __contains__(self, item) -> bool:
    if isinstance(item, Enclosure):
        return item.name in self._enclosures
    if isinstance(item, Employee):
        return item in self._employees
    if isinstance(item, str):
        return item in self._enclosures
    return False
```

Operator `in` jest wieloznaczny dla `Zoo` — można pytać zarówno o wybiegi (`"Savanna" in zoo`, `enc in zoo`) jak i o pracowników (`keeper in zoo`). Sprawdzenie `isinstance` rozróżnia, w której kolekcji szukać. To jest przykład **przeciążania operatora** (`__contains__`) z uwzględnieniem różnych typów argumentu.

**Kod:** `zoo/zoo.py:139–147`

---

### 26. Napisz fixture pytest, który tworzy zoo z jednym wybiegiem i trzema zwierzętami. Jak go użyjesz w testach?

```python
import pytest
from zoo.zoo import Zoo
from zoo.animals import Lion, Elephant, Monkey

@pytest.fixture
def populated_zoo():
    zoo = Zoo("Test Zoo", "Warsaw")
    savanna = zoo.create_enclosure("Savanna", 3)
    savanna.add_animal(Lion("Simba", 5))
    savanna.add_animal(Elephant("Dumbo", 10))
    savanna.add_animal(Monkey("George", 3))
    return zoo

def test_total_animals(populated_zoo):
    assert populated_zoo.total_animals() == 3
```

Fixture definiujemy jako funkcję z dekoratorem `@pytest.fixture`. Pytest automatycznie wstrzykuje ją do testu przez nazwę parametru.

**Kod:** `tests/test_zoo.py:14–32` (przykłady istniejących fixtures)

---

### 27. Co się stanie, gdy wywołasz `zoo['Savanna']` na instancji `Zoo`? Który dunder method jest odpowiedzialny?

Odpowiedzialny jest `__getitem__`:
```python
def __getitem__(self, name: str) -> Enclosure:
    if name not in self._enclosures:
        raise KeyError(f"Enclosure '{name}' not found")
    return self._enclosures[name]
```

`zoo['Savanna']` zwróci obiekt `Enclosure` o nazwie `'Savanna'`. Jeśli wybieg nie istnieje, zostanie rzucony `KeyError`. Dzięki temu obiekt `Zoo` zachowuje się jak słownik w kontekście dostępu do wybiegów.

**Kod:** `zoo/zoo.py:133–137`

---

### 28. Zademonstruj użycie `isinstance()` i `issubclass()` na hierarchii `Animal`. Podaj 3 przykłady.

```python
from zoo.animals import Animal, Mammal, Bird, Lion, Eagle, Penguin

lion = Lion("Simba", 5)
eagle = Eagle("Freedom", 4)

# isinstance — sprawdza typ instancji (uwzględnia dziedziczenie)
isinstance(lion, Lion)    # True — lion to Lion
isinstance(lion, Mammal)  # True — Lion dziedziczy po Mammal
isinstance(lion, Bird)    # False — Lion nie jest ptakiem

# issubclass — sprawdza hierarchię klas (nie instancje)
issubclass(Lion, Mammal)   # True
issubclass(Mammal, Animal) # True
issubclass(Eagle, Mammal)  # False — Eagle dziedziczy po Bird
```

**Kod:** `tests/test_animals.py:152–159`

---

### 29. Jak zaimplementowałeś metodę `Zoo.report()`? Jakie informacje zawiera raport?

`report()` buduje wieloliniowy string z użyciem listy `lines`:

```python
def report(self) -> str:
    lines = [
        f"=== {self._name} Zoo Report ({self._city}) ===",
        f"Total enclosures: {len(self._enclosures)}",
        f"Total employees: {len(self._employees)}",
        f"Total animals: {self.total_animals()}",
        "",
        "--- Enclosures ---",
    ]
    for enclosure in self._enclosures.values():
        lines.append(f"  {enclosure}")  # używa __str__ Enclosure
    lines.append("--- Employees ---")
    for emp in self._employees:
        lines.append(f"  {emp.name} - {emp.role()}")
    return "\n".join(lines)
```

Raport zawiera: nazwę i miasto zoo, liczby (wybiegi, pracownicy, zwierzęta), listę wybiegów z ich stanem (ile/ile zwierząt), listę pracowników z rolami.

**Kod:** `zoo/zoo.py:110–131`

---

### 30. Wyjaśnij, dlaczego `__hash__` jest potrzebny razem z `__eq__`. Co się stanie, jeśli zdefiniujesz `__eq__` bez `__hash__`?

W Pythonie obowiązuje kontrakt: **jeśli `a == b`, to `hash(a) == hash(b)`**.

Kiedy zdefiniujesz `__eq__` bez `__hash__`, Python automatycznie ustawia `__hash__ = None`, co oznacza:
- Obiektu nie można dodać do `set` ani użyć jako klucza w `dict`,
- Każda taka próba rzuci `TypeError: unhashable type`.

Dlatego w naszym kodzie zawsze definiujemy obie metody razem:
```python
def __eq__(self, other) -> bool:
    return self._id == other._id

def __hash__(self) -> int:
    return hash(self._id)  # spójne z __eq__
```

**Kod:** `zoo/animals/animal.py:72–78`, `zoo/enclosure.py:101–107`

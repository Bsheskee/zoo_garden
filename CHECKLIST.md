# Checklista mechanizmów OOP

## Podstawy klas (5 pozycji)

- [x] Klasy i obiekty – definicja klas, tworzenie obiektów
  - Wszystkie klasy: `zoo/animals/animal.py`, `zoo/animals/mammal.py`, `zoo/animals/bird.py`, `zoo/animals/reptile.py`, `zoo/employees/employee.py`, `zoo/employees/zookeeper.py`, `zoo/employees/veterinarian.py`, `zoo/employees/guide.py`, `zoo/enclosure.py`, `zoo/zoo.py`, `zoo/feeding_schedule.py`
- [x] Konstruktor __init__ – inicjalizacja atrybutów
  - `zoo/animals/animal.py:20`, `zoo/employees/employee.py:21`, `zoo/enclosure.py:17`, `zoo/zoo.py:23`, `zoo/feeding_schedule.py:36`
- [x] Atrybuty instancji – unikalne dla każdego obiektu
  - `_id`, `_name`, `_age`, `_health` w `zoo/animals/animal.py:21-25`
- [x] Atrybuty klasy – współdzielone między instancjami (np. _next_id)
  - `Animal._next_id` w `zoo/animals/animal.py:18`, `Employee._next_id` w `zoo/employees/employee.py:19`
- [x] Metody instancji – operacje na obiektach
  - Np. `feed()` w `zoo/animals/animal.py:63`, `work()` w `zoo/employees/employee.py:62`

## Enkapsulacja i metody specjalne (7 pozycji)

- [x] Prywatne atrybuty – konwencja _protected
  - `_health`, `_name`, `_age`, `_id` w `zoo/animals/animal.py`, `_animals`, `_capacity` w `zoo/enclosure.py`
- [x] @property – gettery
  - `Animal.health` w `zoo/animals/animal.py:46`, `Animal.name` w `zoo/animals/animal.py:32`, `Enclosure.animals` w `zoo/enclosure.py:31`
- [x] @property.setter – settery z walidacją
  - `Animal.health` (clamping 0-100) w `zoo/animals/animal.py:49-51`, `Animal.name` (niepuste) w `zoo/animals/animal.py:35-39`
- [x] __str__() – reprezentacja dla użytkownika
  - `Animal.__str__()` w `zoo/animals/animal.py:69`, `Enclosure.__str__()` w `zoo/enclosure.py:111`
- [x] __repr__() – reprezentacja dla debugowania
  - `Animal.__repr__()` w `zoo/animals/animal.py:66`, `Employee.__repr__()` w `zoo/employees/employee.py:71`
- [x] __eq__() – porównywanie obiektów
  - `Animal.__eq__()` (po _id) w `zoo/animals/animal.py:72`, `Employee.__eq__()` w `zoo/employees/employee.py:74`, `Enclosure.__eq__()` w `zoo/enclosure.py:103`
- [x] Dodatkowa metoda specjalna
  - `__lt__()` w `zoo/animals/animal.py:80` (sortowanie po name)
  - `__len__()` w `zoo/enclosure.py:91`, `zoo/zoo.py:139`, `zoo/feeding_schedule.py:91`
  - `__contains__()` w `zoo/enclosure.py:94`, `zoo/zoo.py:129`
  - `__iter__()` w `zoo/enclosure.py:97`
  - `__getitem__()` w `zoo/zoo.py:123`
  - `__hash__()` w `zoo/animals/animal.py:77`, `zoo/employees/employee.py:79`, `zoo/enclosure.py:108`

## Dziedziczenie (5 pozycji)

- [x] Klasa bazowa
  - `Animal` (ABC) w `zoo/animals/animal.py:6`, `Employee` (ABC) w `zoo/employees/employee.py:7`
- [x] Klasy pochodne – 3 dla głównej hierarchii, 3 dla drugiej
  - Animal: Mammal, Bird, Reptile (`zoo/animals/mammal.py:6`, `zoo/animals/bird.py:6`, `zoo/animals/reptile.py:6`)
  - Employee: Zookeeper, Veterinarian, Guide (`zoo/employees/zookeeper.py:7`, `zoo/employees/veterinarian.py:7`, `zoo/employees/guide.py:7`)
- [x] super() – wywołanie konstruktora rodzica
  - `super().__init__()` w `zoo/animals/mammal.py:15`, `zoo/animals/bird.py:16`, `zoo/animals/reptile.py:15`, `zoo/employees/zookeeper.py:16`
- [x] Nadpisywanie metod (override)
  - `make_sound()` w: Lion, Elephant, Monkey, Eagle, Penguin, Crocodile
  - `diet()` w: Lion, Elephant, Eagle, Crocodile
  - `work()`, `role()` w: Zookeeper, Veterinarian, Guide
- [x] isinstance() i issubclass() – użyte gdziekolwiek
  - `zoo/animals/animal.py:73` (__eq__), `zoo/zoo.py:131-134` (__contains__), testy w `zoo/employees/tests/test_animals.py:150-159`

## Polimorfizm (2 pozycji)

- [x] Polimorfizm – ta sama metoda, różne implementacje
  - `make_sound()`: "Roar!"/"Trumpet!"/"Screech!"/"Honk!"/"Hiss!" itd. (`zoo/animals/mammal.py:36,50,63`, `zoo/animals/bird.py:36,49`, `zoo/animals/reptile.py:35`)
  - `work()`: różne implementacje w Zookeeper/Veterinarian/Guide
- [x] Duck typing – lista różnych obiektów, wspólny interfejs
  - `demo.py:75-82`: `[lion, elephant, monkey, eagle, penguin, crocodile]` z wywołaniem `make_sound()` i `diet()`

## Kompozycja i agregacja (2 pozycji)

- [x] Kompozycja – has-a, silne powiązanie
  - `Zoo` ◆–– `Enclosure`: wybiegi tworzone przez `create_enclosure()` w `zoo/zoo.py:37`, przechowywane w `_enclosures`
  - `FeedingSchedule` ◆–– `FeedingEntry`: wpisy w `_entries` w `zoo/feeding_schedule.py:38`
- [x] Agregacja – has-a, słabsze powiązanie
  - `Enclosure` ◇–– `Animal`: zwierzęta mogą istnieć poza wybiegiem (`zoo/enclosure.py:20`)
  - `Zoo` ◇–– `Employee`: pracownicy mogą istnieć poza zoo (`zoo/zoo.py:27`)

## Klasy abstrakcyjne i operatory (3 pozycji)

- [x] Klasa abstrakcyjna (ABC) – import z abc
  - `Animal` w `zoo/animals/animal.py:6`, `Employee` w `zoo/employees/employee.py:7`
- [x] @abstractmethod – wymuszenie implementacji
  - `make_sound()`, `diet()` w `zoo/animals/animal.py:53-61`
  - `work()`, `role()` w `zoo/employees/employee.py:61-68`
- [x] Przeciążanie operatorów
  - `__lt__` w `zoo/animals/animal.py:80` – operator `<` do sortowania zwierząt po imieniu

## Wyjątki (4 pozycji)

- [x] Własny wyjątek bazowy – dziedziczący po Exception
  - `ZooError` w `zoo/exceptions.py:4`
- [x] Hierarchia wyjątków – 2 specjalizowane
  - `EnclosureFullError(ZooError)` w `zoo/exceptions.py:9`
  - `AnimalNotFoundError(ZooError)` w `zoo/exceptions.py:14`
  - `InvalidAnimalDataError(ZooError)` w `zoo/exceptions.py:19`
- [x] Zgłaszanie wyjątków – raise w metodach
  - `zoo/enclosure.py:46-48` (EnclosureFullError), `zoo/enclosure.py:62-64` (AnimalNotFoundError)
- [x] Obsługa wyjątków – try-except
  - `demo.py:51-54`, testy: `zoo/employees/tests/test_enclosure.py:46-47`, `zoo/employees/tests/test_enclosure.py:59-61`

## Testowanie i dokumentacja (3 pozycji)

- [x] Testy pytest – 15+ testów
  - 15 testów w `zoo/employees/tests/test_animals.py`
  - 15 testów w `zoo/employees/tests/test_enclosure.py`
  - 15 testów w `zoo/employees/tests/test_zoo.py`
- [x] Docstringi – dla wszystkich klas i metod publicznych
  - Wszystkie klasy i metody publiczne w `zoo/animals/`, `zoo/employees/`, `zoo/enclosure.py`, `zoo/zoo.py`, `zoo/feeding_schedule.py`
- [x] Type hints – dla głównych metod
  - Wszystkie publiczne metody w `zoo/` z adnotacjami typów

# JUSTIFICATION.md — Uzasadnienia decyzji projektowych

## 1. Dlaczego klasa Animal jest abstrakcyjna (ABC)?

Klasa `Animal` jest abstrakcyjna, ponieważ każde zwierzę w zoo musi wydawać dźwięk (`make_sound()`) i mieć określoną dietę (`diet()`), ale sposób implementacji tych metod jest unikalny dla każdego gatunku. Użycie `ABC` z `@abstractmethod` wymusza na klasach pochodnych implementację tych metod, co zapobiega tworzeniu niekompletnych obiektów.

**Kod:** `zoo/animals/animal.py:53-61`

---

## 2. Dlaczego Employee ma _assigned_enclosures (lista), a nie tylko Zookeeper?

Początkowo `_assigned_enclosures` był tylko w `Zookeeper`, ale podczas refaktoryzacji przeniesiono go do klasy bazowej `Employee`, aby:
- Umożliwić innym pracownikom (np. weterynarzom) przynależność do wybiegów
- Przestrzegać zasady DRY (Don't Repeat Yourself)
- Ułatwić przyszłą rozbudowę

**Kod:** `zoo/employees/employee.py:26`

---

## 3. Dlaczego health używa clampingu (max/min)?

Setter `health` używa `max(0, min(100, value))`, aby zapewnić, że wartość zdrowia zawsze mieści się w zakresie 0–100. Bez tego walidacji wartość mogłaby wykraczać poza dopuszczalny zakres, co prowadziłoby do niespójności danych (np. zdrowie >100 po leczeniu lub <0 po ataku). Clamping jest lepszy niż rzucanie wyjątku, ponieważ:
- Nie przerywa działania programu
- Zapewnia, że dane zawsze pozostają spójne
- Jest zgodny z oczekiwaniami użytkownika (nie można mieć "ujemnego" zdrowia)

**Kod:** `zoo/animals/animal.py:49-51`

---

## 4. Dlaczego FeedingEntry to @dataclass?

`FeedingEntry` używa dekoratora `@dataclass`, ponieważ:
- Jest prostym kontenerem danych bez logiki biznesowej
- `@dataclass` automatycznie generuje `__init__`, `__repr__`, `__eq__` i `__hash__`
- Zmniejsza ilość boilerplate code
- Zapewnia czytelną reprezentację obiektu

**Kod:** `zoo/feeding_schedule.py:7-21`

---

## 5. Dlaczego Zoo używa kompozycji z Enclosure, a agregacji z Employee?

**Kompozycja (Zoo ◆–– Enclosure):** Wybiegi są tworzone przez zoo i nie istnieją bez niego. Jeśli usuniemy zoo, wybiegi również powinny zostać usunięte. Wybieg nie ma sensu poza kontekstem zoo.

**Agregacja (Zoo ◇–– Employee):** Pracownicy mogą istnieć niezależnie od zoo. Mogą odejść z pracy, zmienić zoo, lub być zatrudnieni w innym miejscu. Ich istnienie nie zależy od konkretnego zoo.

**Kod:** `zoo/zoo.py:26-27` (enclosures jako dict, employees jako lista)

---

## 6. Dlaczego Enclosure.animals zwraca kopię listy?

Metoda `animals` zwraca `list(self._animals)`, czyli kopię wewnętrznej listy. Chroni to enkapsulację, ponieważ:
- Zapobiega bezpośredniej modyfikacji listy zwierząt z zewnątrz
- Użytkownik musi użyć `add_animal()`/`remove_animal()`, które przechodzą walidację
- Zapewnia integralność danych (nikt nie może dodać zwierzęcia do pełnego wybiegu przez listę)

**Kod:** `zoo/enclosure.py:31-33`

---

## 7. Dlaczego __eq__ w Animal porównuje po _id, a nie po name?

Porównywanie po `_id` (unikalnym identyfikatorze) jest bardziej precyzyjne niż po imieniu, ponieważ:
- Dwa zwierzęta mogą mieć to samo imię (np. "Simba" dla lwa i papugi)
- Id jest gwarantowanie unikalne dzięki `_next_id`
- Porównanie po id odzwierciedla tożsamość obiektu w systemie

**Kod:** `zoo/animals/animal.py:72-75`

---

## 8. Jakie są zalety posiadania bazowego wyjątku ZooError?

Hierarchia wyjątków z `ZooError` jako klasą bazową umożliwia:
- Łapanie wszystkich błędów zoo za pomocą jednego `except ZooError`
- Dodawanie nowych typów błędów bez zmiany istniejącego kodu
- Precyzyjne określanie, który błąd wystąpił (np. `EnclosureFullError` vs `AnimalNotFoundError`)
- Oddzielenie błędów domenowych od błędów systemowych

**Kod:** `zoo/exceptions.py:4-20`

---

## 9. Dlaczego zastosowano polimorfizm dla make_sound() i diet()?

Polimorfizm pozwala na wywołanie tej samej metody (`make_sound()`) na różnych obiektach (`Lion`, `Eagle`, `Crocodile`) i uzyskanie różnych rezultatów ("Roar!", "Screech!", "Hiss!"). Dzięki temu:
- Kod kliencki (np. demo, testy) jest prostszy i nie wymaga sprawdzania typu
- Dodanie nowego gatunku nie wymaga modyfikacji istniejącego kodu
- Spełniona jest zasada Open/Closed (otwarte na rozszerzanie, zamknięte na modyfikacje)

**Kod:** `demo.py:75-82`

---

## 10. Dlaczego Monkey nie nadpisuje metody diet()?

Monkey nie nadpisuje `diet()`, ponieważ dziedziczy ogólną dietę od `Mammal`. Jest to świadoma decyzja projektowa:
- Małpy mają zróżnicowaną dietę (wszystkożerne), podobnie jak ogólna dieta ssaków
- Nie ma potrzeby specyfikowania, jeśli implementacja rodzica jest wystarczająca
- Demonstruje, że nie każda klasa pochodna musi nadpisywać każdą metodę

**Kod:** `zoo/animals/mammal.py:56-66` (Monkey nie ma metody `diet()`)

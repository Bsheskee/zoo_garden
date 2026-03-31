# Zoo Garden Management System

## 1. Opis projektu

System „Zoo Garden” to aplikacja do zarządzania nowoczesnym ogrodem zoologicznym. Program umożliwia ewidencję zwierząt, przypisywanie ich do wybiegów oraz zarządzanie personelem. System został rozszerzony o mechanizmy zapewniające spójność danych, kontrolę dostępu do zasobów oraz lepsze odwzorowanie realnych procesów w zoo (np. przypisywanie pracowników do wielu wybiegów).

---

## 2. Autorzy i podział pracy

| Imię i Nazwisko              | Rola i zakres odpowiedzialności                             |
| :--------------------------- | :---------------------------------------------------------- |
| **Bartłomiej Białobrzewski** | Testy jednostkowe (`pytest`), Use Cases, UML                |
| **Wiktor Habryń**            | Implementacja klas (zwierzęta + personel), logika biznesowa |
| **Bartłomiej Żołek**         | Code Review, walidacja logiki, optymalizacja                |

---

## 3. Lista klas z opisami (Zgodnie z UML)

| Klasa              | Rola w systemie                 | Główne atrybuty i metody                                                                       |
| :----------------- | :------------------------------ | :--------------------------------------------------------------------------------------------- |
| **Animal** (ABC)   | Abstrakcyjna baza dla zwierząt  | `_id`, `_name`, `_age`, `_health`, `make_sound()`, `__str__()`, `__eq__()`                     |
| **Mammal**         | Klasa pośrednia dla ssaków      | `_fur_color`, `has_fur()`, `give_birth()`                                                      |
| **Bird**           | Klasa pośrednia dla ptaków      | `_wingspan`, `_can_fly`, `fly()`                                                               |
| **Reptile**        | Klasa pośrednia dla gadów       | `_is_venomous`, `bask()`                                                                       |
| **Employee** (ABC) | Abstrakcyjna baza dla personelu | `_name`, `_salary`, `_assigned_enclosures`, `perform_duty()`, `add_enclosure()`                |
| **Zookeeper**      | Opiekun wybiegów                | `perform_duty()`                                                                               |
| **Veterinarian**   | Lekarz zwierząt                 | `specialization`, `perform_duty()`, `treat_animal()`                                           |
| **Guide**          | Przewodnik                      | `languages`, `perform_duty()`                                                                  |
| **Enclosure**      | Zarządzanie wybiegami           | `_name`, `_capacity`, `_animals`, `add_animal()`, `remove_animal()`, `list_animals()`          |
| **Zoo**            | Główny system zarządzania       | `_name`, `_enclosures`, `_employees`, `add_enclosure()`, `add_employee()`, `generate_report()` |

---

## 4. Relacje między klasami

* **Zoo ◆–– Enclosure** (Kompozycja)
  Wybiegi istnieją tylko w kontekście Zoo.

* **Enclosure ◇–– Animal** (Agregacja)
  Zwierzęta mogą być przenoszone między wybiegami.

* **Employee *––* Enclosure** (Asocjacja wiele-do-wielu)
  Pracownicy mogą być przypisani do wielu wybiegów i odwrotnie.

* **Veterinarian → Animal** (Zależność)
  Weterynarz wykonuje operacje na zwierzętach (leczenie).

---

## 5. Mechanizmy OOP

* **Klasy Abstrakcyjne (ABC)**
  `Animal` i `Employee` wymuszają implementację metod (`make_sound`, `perform_duty`).

* **Hermetyzacja (@property)**

  * dostęp do danych przez właściwości
  * kontrola poprawności danych
  * mechanizm *clamping* dla zdrowia (`0–100`)

* **Polimorfizm**
  Każde zwierzę implementuje własne `make_sound()`.

* **Dziedziczenie wielopoziomowe**
  `Animal → Mammal → Lion` itd.

* **Relacje wiele-do-wielu**
  Pracownicy mogą być przypisani do wielu wybiegów (`_assigned_enclosures`).

* **Przeciążanie operatorów**
  `__str__`, `__eq__`

---

## 6. User Stories

1. **Jako opiekun** chcę dodać nowe zwierzę do wybiegu, aby system sprawdził dostępność miejsca.
2. **Jako weterynarz** chcę aktualizować zdrowie zwierzęcia, aby dane były poprawne (0–100).
3. **Jako dyrektor** chcę wygenerować raport pracowników, aby analizować efektywność.
4. **Jako przewodnik** chcę przeglądać wybiegi, aby móc oprowadzać odwiedzających.

---

## 7. Zalety systemu

### 🔹 1. Skalowalność

Dodanie nowych klas (np. Tiger) nie wymaga zmian w istniejącym kodzie.

---

### 🔹 2. Spójność danych

* zdrowie zawsze w zakresie 0–100
* brak przepełnienia wybiegów

---

### 🔹 3. Elastyczne zarządzanie personelem

Relacja wiele-do-wielu:

* pracownik może obsługiwać wiele wybiegów
* wybieg może mieć wielu pracowników

---

### 🔹 4. Realistyczne odwzorowanie świata

System lepiej oddaje rzeczywistość:

* weterynarz leczy wiele zwierząt
* przewodnik pracuje na wielu wybiegach

---

### 🔹 5. Niskie sprzężenie (low coupling)

Każda klasa ma jasno określoną odpowiedzialność.

---

### 🔹 6. Wysoka spójność (high cohesion)

Logika zdrowia → w `Animal`
Logika raportów → w `Zoo`

---

### 🔹 7. Testowalność

Każdą klasę można testować niezależnie (`pytest`).

---

### 🔹 8. Czytelność i utrzymanie

Kod zgodny z UML → łatwy onboarding nowych osób.

---

### 🔹 9. Gotowość pod rozbudowę

Możliwe rozszerzenia:

* GUI
* API
* baza danych
* system raportów PDF

---

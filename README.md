# Zoo Garden Management System

## 1. Opis projektu
System „Zoo Garden” to aplikacja wspierająca zarządzanie ogrodem zoologicznym z perspektywy jego pracowników. Umożliwia dodawanie zwierząt do wybiegów z uwzględnieniem ich pojemności, zarządzanie personelem oraz monitorowanie stanu zdrowia zwierząt. System pomaga utrzymać porządek organizacyjny oraz zapewnia bezpieczeństwo i dobrostan zwierząt. Dzięki niemu użytkownicy mogą szybko wykonywać codzienne operacje bez ryzyka błędów logicznych (np. przepełnienia wybiegu).

---

## 2. Autorzy i podział pracy

| Imię i Nazwisko | Zakres odpowiedzialności |
| :--- | :--- |
| **Bartłomiej Białobrzewski** | Testy jednostkowe (`pytest`), Use Cases, diagram UML |
| **Wiktor Habryń** | Implementacja klas (zwierzęta, personel), logika systemu |
| **Bartłomiej Żołek** | Code Review, walidacja logiki, optymalizacja |

---

## 3. Lista klas z opisami

| Klasa | Opis | Główne atrybuty i metody |
| :--- | :--- | :--- |
| `Animal` (ABC) | Abstrakcyjna klasa bazowa reprezentująca każde zwierzę w systemie. Definiuje wspólne właściwości oraz wymusza implementację zachowania dźwiękowego. | `_id`, `_name`, `_age`, `_health`, `make_sound()`, `__str__()`, `__eq__()` |
| `Mammal` | Klasa pośrednia dla ssaków, rozszerzająca `Animal` o cechy charakterystyczne tej grupy. | `_fur_color`, `has_fur()`, `give_birth()` |
| `Bird` | Klasa pośrednia dla ptaków, definiująca ich zdolności związane z lataniem. | `_wingspan`, `_can_fly`, `fly()` |
| `Reptile` | Klasa pośrednia dla gadów, zawierająca ich typowe zachowania. | `_is_venomous`, `bask()` |
| `Lion` | Konkretna implementacja ssaka reprezentująca lwa. Nadpisuje metodę `make_sound()`. | `make_sound()` |
| `Elephant` | Reprezentuje słonia oraz umożliwia aktualizację jego zdrowia. | `make_sound()`, `update_health()` |
| `Eagle` | Reprezentuje ptaka drapieżnego z możliwością wydawania charakterystycznego dźwięku. | `make_sound()` |
| `Penguin` | Reprezentuje ptaka nielatającego. | `make_sound()` |
| `Crocodile` | Reprezentuje gada, implementując jego zachowanie dźwiękowe. | `make_sound()` |
| `Employee` (ABC) | Abstrakcyjna klasa bazowa dla pracowników zoo. Odpowiada za wspólne dane i kontrakt metod. | `_name`, `_salary`, `_assigned_enclosures`, `perform_duty()`, `add_enclosure()` |
| `Zookeeper` | Pracownik odpowiedzialny za opiekę nad wybiegami i zwierzętami. | `perform_duty()` |
| `Veterinarian` | Lekarz zajmujący się leczeniem zwierząt oraz aktualizacją ich zdrowia. | `specialization`, `perform_duty()`, `treat_animal()` |
| `Guide` | Przewodnik oprowadzający odwiedzających po zoo. | `languages`, `perform_duty()` |
| `Enclosure` | Reprezentuje wybieg dla zwierząt, zarządza ich listą oraz kontroluje pojemność. | `_name`, `_capacity`, `_animals`, `add_animal()`, `remove_animal()`, `list_animals()` |
| `Zoo` | Główna klasa systemowa zarządzająca wybiegami i personelem. | `_name`, `_enclosures`, `_employees`, `add_enclosure()`, `add_employee()`, `generate_report()` |

---

## 4. Relacje między klasami

- **Dziedziczenie (`Animal` → `Mammal` → `Lion` itd.)**  
  Pozwala na współdzielenie logiki i wymuszenie implementacji metod w klasach potomnych.

- **Dziedziczenie (`Employee` → `Zookeeper`, `Veterinarian`, `Guide`)**  
  Umożliwia wspólne zarządzanie pracownikami oraz wykorzystanie polimorfizmu.

- **Kompozycja (`Zoo` ◆–– `Enclosure`)**  
  Wybiegi są częścią zoo i nie istnieją bez niego. Usunięcie zoo powoduje usunięcie wybiegów.

- **Agregacja (`Enclosure` ◇–– `Animal`)**  
  Zwierzęta mogą być przenoszone między wybiegami. Usunięcie wybiegu nie usuwa zwierzęcia.

- **Asocjacja wiele-do-wielu (`Employee` *––* `Enclosure`)**  
  Pracownik może być przypisany do wielu wybiegów, a wybieg może mieć wielu pracowników.

- **Zależność (`Veterinarian` → `Animal`)**  
  Weterynarz wykonuje operacje na zwierzętach (leczenie), ale nie posiada ich na stałe.

---

## 5. Planowane funkcjonalności

- Dodawanie zwierzęcia do wybiegu z walidacją pojemności  
- Usuwanie zwierzęcia z wybiegu  
- Przeglądanie listy zwierząt w wybiegu  
- Aktualizacja stanu zdrowia zwierzęcia (z ograniczeniem 0–100)  
- Przypisywanie pracownika do jednego lub wielu wybiegów  
- Generowanie raportu pracowników i ich obowiązków  
- Przeglądanie wybiegów przez pracownika (np. przewodnika)  

---

## 6. User Stories

1. **Jako opiekun** chcę dodać nowe zwierzę do wybiegu, żeby system automatycznie sprawdził, czy jest tam wolne miejsce.  
2. **Jako weterynarz** chcę zaktualizować stan zdrowia zwierzęcia po leczeniu, żeby mieć pewność, że dane są poprawne.  
3. **Jako dyrektor** chcę zobaczyć raport wszystkich pracowników i ich obowiązków, żeby ocenić efektywność pracy.  

---

## 7. Mechanizmy OOP

| Mechanizm | Gdzie w projekcie | Opis |
| :--- | :--- | :--- |
| Klasy abstrakcyjne (ABC) | `Animal`, `Employee` | Wymuszają implementację metod (`make_sound()`, `perform_duty()`) |
| Dziedziczenie | `Animal` → `Mammal` → `Lion` itd. | Hierarchia klas upraszczająca rozszerzanie systemu |
| Polimorfizm | `make_sound()`, `perform_duty()` | Różne implementacje dla różnych klas |
| Hermetyzacja (enkapsulacja) | `_health`, `_animals`, `_assigned_enclosures` | Ukrycie danych i kontrola dostępu przez metody |
| Właściwości (`@property`) | `Animal` (`health`) | Walidacja danych (clamping 0–100) |
| Przeciążanie operatorów | `__str__()`, `__eq__()` | Ułatwia debugowanie i porównywanie obiektów |
| Relacje wiele-do-wielu | `Employee` ↔ `Enclosure` | Elastyczne przypisywanie pracowników |

### Dodatkowe zalety systemu
- Zapewnienie spójności danych (np. zdrowie 0–100, brak przepełnienia wybiegów)  
- Łatwa rozbudowa systemu o nowe klasy zwierząt lub pracowników  
- Niskie sprzężenie i wysoka spójność klas  
- Lepsze odwzorowanie rzeczywistego działania zoo  
- Możliwość łatwego testowania i utrzymania kodu  

---

## 8. Historia zmian

- Przeniesiono _assigned_enclosures z Zookeeper do Employee jako ze kazdy pracownik ma przypisany jemu wybieg (zgodność z zasadą DRY).
- Dodano `_health` do `Animal` oraz mechanizm jego walidacji (0–100), aby spełnić wymagania dotyczące dobrostanu zwierząt.  
- Zmieniono relację `Employee`–`Enclosure` na wiele-do-wielu, aby umożliwić bardziej realistyczne przypisywanie pracowników.   
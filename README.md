# Zoo Garden Management System

## 1. Opis projektu
System „Zoo Garden” to aplikacja do zarządzania nowoczesnym ogrodem zoologicznym. Program pozwala na ewidencję zwierząt, przypisywanie ich do odpowiednich wybiegów oraz zarządzanie personelem. System kładzie nacisk na dobrostan zwierząt poprzez monitorowanie ich zdrowia oraz automatyzację limitów miejsc na wybiegach.

## 2. Autorzy i podział pracy
| Imię i Nazwisko | Rola i zakres odpowiedzialności |
| :--- | :--- |
| **Bartłomiej Białobrzewski** | Implementacja testów jednostkowych (`pytest`), opracowanie Use Cases oraz diagramu UML. |
| **Wiktor Habryń** | Przygotowanie specyfikacji `README.md`, implementacja hierarchii klas zwierząt i personelu. |
| **Bartłomiej Żołek** | Przegląd kodu (Code Review), sprawdzanie poprawności logicznej i optymalizacja algorytmów. |

## 3. Lista klas z opisami (Zgodnie z UML)

| Klasa | Rola w systemie | Główne atrybuty i metody |
| :--- | :--- | :--- |
| **Animal** (ABC) | Abstrakcyjna baza dla wszystkich zwierząt. | `_id`, `_name`, `_age`, `make_sound()`, `__str__()`, `__eq__()` |
| **Mammal** | Klasa pośrednia dla ssaków. | `has_fur: bool`, `fur_color: str`, `give_birth()` |
| **Bird** | Klasa pośrednia dla ptaków. | `wingspan`, `can_fly: bool`, `fly()` |
| **Reptile** | Klasa pośrednia dla gadów. | `is_venomous: bool`, `bask()` |
| **Employee** (ABC) | Abstrakcyjna baza dla personelu. | `name`, `salary`, `perform_duty()` |
| **Zookeeper** | Opiekun odpowiedzialny za wybiegi. | `assigned_enclosure`, `perform_duty()` |
| **Veterinarian** | Lekarz dbający o zdrowie zwierząt. | `specialization`, `perform_duty()` |
| **Guide** | Przewodnik oprowadzający gości. | `languages`, `perform_duty()` |
| **Enclosure** | Zarządzanie przestrzenią dla zwierząt. | `capacity`, `animals_list`, `add_animal()` |

## 4. Relacje między klasami

* **Zoo ◆–– Enclosure** (Kompozycja): Wybiegi nie istnieją bez obiektu Zoo.
* **Enclosure ◇–– Animal** (Agregacja): Zwierzęta są przypisane do wybiegów, ale mogą być przenoszone.
* **Zookeeper –– Enclosure** (Asocjacja): Opiekun wykonuje pracę na konkretnym wybiegu.

## 5. Mechanizmy OOP

* **Klasy Abstrakcyjne (ABC)**: `Animal` i `Employee` wymuszają implementację kluczowych metod.
* **Hermetyzacja (@property)**: Walidacja imion oraz mechanizm *clamping* dla zdrowia zwierząt (0-100).
* **Polimorfizm**: Różne implementacje metody `make_sound()` dla każdego gatunku.
* **Przeciążanie operatorów**: Wykorzystanie `__str__` oraz `__eq__`.

## 6. User Stories

1. **Jako opiekun** chcę dodać nowe zwierzę do wybiegu, aby system automatycznie sprawdził, czy jest tam wolne miejsce.
2. **Jako weterynarz** chcę zaktualizować stan zdrowia słonia po leczeniu, aby mieć pewność, że dane są aktualne.
3. **Jako dyrektor** chcę zobaczyć raport wszystkich pracowników i ich obowiązków, aby sprawdzić efektywność pracy.

# UML Class Diagram — Zoo Garden

```mermaid
classDiagram
    class Animal {
        <<abstract>>
        - _id: int
        - _name: str
        - _age: int
        - _health: int
        + _next_id: int
        + id: int
        + name: str
        + age: int
        + health: int
        + make_sound() str
        + diet() str
        + feed() str
        + __str__() str
        + __repr__() str
        + __eq__(other) bool
        + __hash__() int
        + __lt__(other) bool
    }

    class Mammal {
        - _fur_color: str
        + diet() str
        + give_birth() str
        + has_fur() bool
    }

    class Bird {
        - _wingspan: float
        - _can_fly: bool
        + diet() str
        + fly() str
    }

    class Reptile {
        - _is_venomous: bool
        + diet() str
        + bask() str
        + is_cold_blooded() bool
    }

    class Lion {
        + make_sound() str
        + diet() str
    }

    class Elephant {
        + make_sound() str
        + diet() str
    }

    class Monkey {
        + make_sound() str
        + climb() str
    }

    class Eagle {
        + make_sound() str
        + diet() str
    }

    class Penguin {
        + make_sound() str
        + swim() str
    }

    class Crocodile {
        + make_sound() str
        + diet() str
        + swim() str
    }

    class Employee {
        <<abstract>>
        - _id: int
        - _name: str
        - _salary: float
        - _assigned_enclosures: list
        + _next_id: int
        + id: int
        + name: str
        + salary: float
        + assigned_enclosures: list
        + assign_to(enclosure)
        + unassign_from(enclosure)
        + work() str
        + role() str
        + __repr__() str
        + __eq__(other) bool
        + __hash__() int
    }

    class Zookeeper {
        - _assigned_enclosure: Optional~Enclosure~
        + assigned_enclosure: Enclosure
        + assign_to(enclosure)
        + feed_animals() str
        + work() str
        + role() str
    }

    class Veterinarian {
        - _specialization: str
        + specialization: str
        + treat_animal(animal) str
        + work() str
        + role() str
    }

    class Guide {
        - _languages: list
        + languages: list
        + add_language(language)
        + give_tour(enclosure) str
        + work() str
        + role() str
    }

    class Enclosure {
        - _name: str
        - _capacity: int
        - _animals: list
        + name: str
        + capacity: int
        + animals: list
        + add_animal(animal)
        + remove_animal(animal)
        + find_animal(name) Animal
        + feed_all() list
        + __len__() int
        + __contains__(animal) bool
        + __iter__() Iterator
        + __repr__() str
        + __str__() str
        + __eq__(other) bool
        + __hash__() int
    }

    class Zoo {
        - _name: str
        - _city: str
        - _enclosures: dict
        - _employees: list
        + name: str
        + city: str
        + enclosures: dict
        + employees: list
        + create_enclosure(name, capacity) Enclosure
        + get_enclosure(name) Enclosure
        + hire_employee(employee)
        + fire_employee(employee) bool
        + total_animals() int
        + find_animal(name) Animal
        + report() str
        + __getitem__(name) Enclosure
        + __contains__(item) bool
        + __len__() int
        + __repr__() str
        + __str__() str
    }

    class FeedingEntry {
        <<dataclass>>
        + enclosure_name: str
        + time: str
        + food_type: str
        + notes: str
    }

    class FeedingSchedule {
        - _day: str
        - _entries: list
        + day: str
        + entries: list
        + add_entry(enclosure_name, time, food_type, notes)
        + remove_entry(enclosure_name, time) bool
        + get_by_enclosure(name) list
        + __len__() int
        + __repr__() str
        + __str__() str
    }

    class ZooError {
        <<exception>>
    }

    class EnclosureFullError {
        <<exception>>
    }

    class AnimalNotFoundError {
        <<exception>>
    }

    class InvalidAnimalDataError {
        <<exception>>
    }

    Animal <|-- Mammal : extends
    Animal <|-- Bird : extends
    Animal <|-- Reptile : extends
    Mammal <|-- Lion : extends
    Mammal <|-- Elephant : extends
    Mammal <|-- Monkey : extends
    Bird <|-- Eagle : extends
    Bird <|-- Penguin : extends
    Reptile <|-- Crocodile : extends

    Employee <|-- Zookeeper : extends
    Employee <|-- Veterinarian : extends
    Employee <|-- Guide : extends

    Zoo *-- Enclosure : composition
    Enclosure o-- Animal : aggregation
    Zoo o-- Employee : aggregation
    FeedingSchedule *-- FeedingEntry : composition

    Zookeeper --> Enclosure : association
    Veterinarian --> Animal : treats

    ZooError <|-- EnclosureFullError : extends
    ZooError <|-- AnimalNotFoundError : extends
    ZooError <|-- InvalidAnimalDataError : extends
```

Aby otworzyć w draw.io:
1. Skopiuj całą zawartość bloku ` ```mermaid ... ``` `
2. Otwórz draw.io
3. Wybierz: Arrange → Insert → Advanced → Mermaid
4. Wklej kod diagramu

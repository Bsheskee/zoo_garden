"""Moduł Zoo — główna klasa systemowa Zoo Garden."""

from typing import Optional

from .employees.employee import Employee
from .enclosure import Enclosure


class Zoo:
    """
    Główna klasa zarządzania zoo.

    Używa kompozycji z Enclosure (wybiegi nie istnieją bez zoo)
    i agregacji z Employee (pracownicy mogą istnieć niezależnie).

    Attributes:
        _name: Nazwa zoo.
        _city: Miasto, w którym znajduje się zoo.
        _enclosures: Słownik wybiegów (kompozycja).
        _employees: Lista pracowników (agregacja).
    """

    def __init__(self, name: str, city: str = "Lodz") -> None:
        self._name = name
        self._city = city
        self._enclosures: dict[str, Enclosure] = {}
        self._employees: list[Employee] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def city(self) -> str:
        return self._city

    @property
    def enclosures(self) -> dict:
        """Zwraca kopię słownika wybiegów."""
        return dict(self._enclosures)

    @property
    def employees(self) -> list:
        """Zwraca kopię listy pracowników."""
        return list(self._employees)

    def create_enclosure(self, name: str, capacity: int) -> Enclosure:
        """
        Tworzy nowy wybieg w zoo.

        Args:
            name: Nazwa wybiegu.
            capacity: Maksymalna liczba zwierząt.

        Returns:
            Utworzony wybieg.
        """
        enclosure = Enclosure(name, capacity)
        self._enclosures[name] = enclosure
        return enclosure

    def get_enclosure(self, name: str) -> Enclosure | None:
        """Zwraca wybieg o podanej nazwie."""
        return self._enclosures.get(name)

    def hire_employee(self, employee: Employee) -> None:
        """
        Zatrudnia nowego pracownika.

        Args:
            employee: Pracownik do zatrudnienia.
        """
        self._employees.append(employee)

    def fire_employee(self, employee: Employee) -> bool:
        """
        Zwalnia pracownika.

        Args:
            employee: Pracownik do zwolnienia.

        Returns:
            True jeśli pracownik został zwolniony, False jeśli nie znaleziono.
        """
        if employee in self._employees:
            self._employees.remove(employee)
            return True
        return False

    def total_animals(self) -> int:
        """Zwraca łączną liczbę zwierząt w zoo."""
        return sum(len(enc) for enc in self._enclosures.values())

    def find_animal(self, name: str) -> Optional:
        """
        Szuka zwierzęcia po imieniu we wszystkich wybiegach.

        Args:
            name: Imię szukanego zwierzęcia.

        Returns:
            Znalezione zwierzę lub None.
        """
        for enclosure in self._enclosures.values():
            animal = enclosure.find_animal(name)
            if animal:
                return animal
        return None

    def report(self) -> str:
        """
        Generuje raport o aktualnym stanie zoo.

        Returns:
            Sformatowany ciąg raportu.
        """
        lines = [
            f"=== {self._name} Zoo Report ({self._city}) ===",
            f"Total enclosures: {len(self._enclosures)}",
            f"Total employees: {len(self._employees)}",
            f"Total animals: {self.total_animals()}",
            "",
            "--- Enclosures ---",
        ]
        for enclosure in self._enclosures.values():
            lines.append(f"  {enclosure}")
        lines.append("")
        lines.append("--- Employees ---")
        for emp in self._employees:
            lines.append(f"  {emp.name} - {emp.role()}")
        return "\n".join(lines)

    def __getitem__(self, name: str) -> Enclosure:
        """Zwraca wybieg po nazwie używając notacji nawiasowej."""
        if name not in self._enclosures:
            raise KeyError(f"Enclosure '{name}' not found")
        return self._enclosures[name]

    def __contains__(self, item) -> bool:
        """Sprawdza, czy element (wybieg lub pracownik) należy do zoo."""
        if isinstance(item, Enclosure):
            return item.name in self._enclosures
        if isinstance(item, Employee):
            return item in self._employees
        if isinstance(item, str):
            return item in self._enclosures
        return False

    def __len__(self) -> int:
        """Zwraca liczbę wybiegów w zoo."""
        return len(self._enclosures)

    def __repr__(self) -> str:
        return f"Zoo(name={self._name!r}, city={self._city!r})"

    def __str__(self) -> str:
        return f"{self._name} Zoo in {self._city}"

"""Zoo module - main system class for Zoo Garden."""

from typing import Optional
from .enclosure import Enclosure
from .employees.employee import Employee
from .exceptions import AnimalNotFoundError


class Zoo:
    """
    Main zoo management class.

    Uses composition with Enclosure (enclosures don't exist without zoo)
    and aggregation with Employee (employees can exist independently).

    Attributes:
        _name: Name of the zoo.
        _city: City where the zoo is located.
        _enclosures: Dictionary of enclosures (composition).
        _employees: List of employees (aggregation).
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

    def create_enclosure(self, name: str, capacity: int) -> Enclosure:
        """
        Create a new enclosure in the zoo.

        Args:
            name: Name of the enclosure.
            capacity: Maximum number of animals.

        Returns:
            The created enclosure.
        """
        enclosure = Enclosure(name, capacity)
        self._enclosures[name] = enclosure
        return enclosure

    def get_enclosure(self, name: str) -> Optional[Enclosure]:
        """Get an enclosure by name."""
        return self._enclosures.get(name)

    def hire_employee(self, employee: Employee) -> None:
        """
        Hire a new employee.

        Args:
            employee: The employee to hire.
        """
        self._employees.append(employee)

    def fire_employee(self, employee: Employee) -> bool:
        """
        Fire an employee.

        Args:
            employee: The employee to fire.

        Returns:
            True if employee was fired, False if not found.
        """
        if employee in self._employees:
            self._employees.remove(employee)
            return True
        return False

    def total_animals(self) -> int:
        """Return total number of animals in the zoo."""
        return sum(len(enc) for enc in self._enclosures.values())

    def find_animal(self, name: str) -> Optional:
        """
        Find an animal by name across all enclosures.

        Args:
            name: Name of the animal to find.

        Returns:
            The animal if found, None otherwise.
        """
        for enclosure in self._enclosures.values():
            animal = enclosure.find_animal(name)
            if animal:
                return animal
        return None

    def report(self) -> str:
        """
        Generate a report about the zoo's current state.

        Returns:
            Formatted report string.
        """
        lines = [
            f"=== {self._name} Zoo Report ({self._city}) ===",
            f"Total enclosures: {len(self._enclosures)}",
            f"Total employees: {len(self._employees)}",
            f"Total animals: {self.total_animals()}",
            "",
            "--- Enclosures ---"
        ]
        for enclosure in self._enclosures.values():
            lines.append(f"  {enclosure}")
        lines.append("")
        lines.append("--- Employees ---")
        for emp in self._employees:
            lines.append(f"  {emp.name} - {emp.role()}")
        return "\n".join(lines)

    def __getitem__(self, name: str) -> Enclosure:
        """Get enclosure by name using bracket notation."""
        if name not in self._enclosures:
            raise KeyError(f"Enclosure '{name}' not found")
        return self._enclosures[name]

    def __contains__(self, item) -> bool:
        """Check if an item (enclosure or employee) is in the zoo."""
        if isinstance(item, Enclosure):
            return item.name in self._enclosures
        if isinstance(item, Employee):
            return item in self._employees
        if isinstance(item, str):
            return item in self._enclosures
        return False

    def __len__(self) -> int:
        """Return number of enclosures in the zoo."""
        return len(self._enclosures)

    def __repr__(self) -> str:
        return f"Zoo(name={self._name!r}, city={self._city!r})"

    def __str__(self) -> str:
        return f"{self._name} Zoo in {self._city}"

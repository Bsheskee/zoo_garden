"""Moduł opiekuna dla systemu Zoo Garden."""

from typing import Optional

from .employee import Employee


class Zookeeper(Employee):
    """
    Opiekun — odpowiedzialny za codzienną opiekę nad zwierzętami i wybiegami.

    Attributes:
        _assigned_enclosure: Główny wybieg, za który odpowiada opiekun.
    """

    def __init__(self, name: str, salary: float = 4000.0) -> None:
        super().__init__(name, salary)
        self._assigned_enclosure: Optional = None

    @property
    def assigned_enclosure(self):
        """Zwraca przypisany wybieg."""
        return self._assigned_enclosure

    def assign_to(self, enclosure) -> None:
        """Przypisuje opiekuna do konkretnego wybiegu."""
        self._assigned_enclosure = enclosure
        super().assign_to(enclosure)

    def feed_animals(self) -> str:
        """Karmi wszystkie zwierzęta w przypisanym wybiegu."""
        if self._assigned_enclosure:
            results = self._assigned_enclosure.feed_all()
            return f"{self._name} is feeding animals in '{self._assigned_enclosure.name}': " + ", ".join(results)
        return f"{self._name} has no assigned enclosure to feed."

    def work(self) -> str:
        return f"{self._name} is cleaning enclosures and monitoring animal behavior."

    def role(self) -> str:
        return "Zookeeper - Daily animal care, feeding, and enclosure maintenance."

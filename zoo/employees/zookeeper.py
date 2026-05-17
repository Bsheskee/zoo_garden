"""Zookeeper module for the Zoo Garden system."""

from typing import Optional
from .employee import Employee


class Zookeeper(Employee):
    """
    Zookeeper - responsible for daily care of animals and enclosures.

    Attributes:
        _assigned_enclosure: Primary enclosure this zookeeper is responsible for.
    """

    def __init__(self, name: str, salary: float = 4000.0) -> None:
        super().__init__(name, salary)
        self._assigned_enclosure: Optional = None

    @property
    def assigned_enclosure(self):
        """Return the assigned enclosure."""
        return self._assigned_enclosure

    def assign_to(self, enclosure) -> None:
        """Assign this zookeeper to a specific enclosure."""
        self._assigned_enclosure = enclosure
        super().assign_to(enclosure)

    def feed_animals(self) -> str:
        """Feed all animals in the assigned enclosure."""
        if self._assigned_enclosure:
            results = self._assigned_enclosure.feed_all()
            return f"{self._name} is feeding animals in '{self._assigned_enclosure.name}': " + ", ".join(results)
        return f"{self._name} has no assigned enclosure to feed."

    def work(self) -> str:
        return f"{self._name} is cleaning enclosures and monitoring animal behavior."

    def role(self) -> str:
        return "Zookeeper - Daily animal care, feeding, and enclosure maintenance."

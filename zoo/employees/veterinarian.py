"""Moduł weterynarza dla systemu Zoo Garden."""

from .employee import Employee


class Veterinarian(Employee):
    """
    Weterynarz — specjalista od opieki medycznej nad zwierzętami.

    Attributes:
        _specialization: Specjalizacja (general, exotic, avian itp.).
    """

    def __init__(self, name: str, specialization: str = "general", salary: float = 7000.0) -> None:
        super().__init__(name, salary)
        self._specialization = specialization

    @property
    def specialization(self) -> str:
        return self._specialization

    def treat_animal(self, animal) -> str:
        """
        Leczy zwierzę i aktualizuje jego stan zdrowia.

        Args:
            animal: Zwierzę do leczenia.

        Returns:
            Potwierdzenie leczenia.
        """
        old_health = animal.health
        animal.health = min(100, animal.health + 20)
        return f"{self._name} treated {animal.name}: health {old_health} -> {animal.health}"

    def work(self) -> str:
        return f"{self._name} is examining animals and providing medical care ({self._specialization})."

    def role(self) -> str:
        return f"Veterinarian ({self._specialization}) - Medical examinations, treatments, and health monitoring."

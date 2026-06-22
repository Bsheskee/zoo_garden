"""Moduł wybiegu dla systemu Zoo Garden."""

from collections.abc import Iterator
from typing import Optional

from .exceptions import AnimalNotFoundError, EnclosureFullError


class Enclosure:
    """
    Reprezentuje wybieg dla zwierząt w zoo.

    Attributes:
        _name: Nazwa wybiegu.
        _capacity: Maksymalna liczba zwierząt w wybiegu.
        _animals: Lista zwierząt aktualnie w wybiegu.
    """

    def __init__(self, name: str, capacity: int) -> None:
        self._name = name
        self._capacity = capacity
        self._animals: list = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def animals(self) -> list:
        """Zwraca kopię listy zwierząt, aby zapobiec modyfikacji z zewnątrz."""
        return list(self._animals)

    def add_animal(self, animal) -> None:
        """
        Dodaje zwierzę do wybiegu.

        Args:
            animal: Zwierzę do dodania.

        Raises:
            EnclosureFullError: Gdy wybieg jest pełny.
        """
        if len(self._animals) >= self._capacity:
            raise EnclosureFullError(f"Enclosure '{self._name}' is full (capacity: {self._capacity})")
        self._animals.append(animal)

    def remove_animal(self, animal) -> None:
        """
        Usuwa zwierzę z wybiegu.

        Args:
            animal: Zwierzę do usunięcia.

        Raises:
            AnimalNotFoundError: Gdy zwierzęcia nie ma w tym wybiegu.
        """
        if animal not in self._animals:
            raise AnimalNotFoundError(f"Animal '{animal.name}' not found in enclosure '{self._name}'")
        self._animals.remove(animal)

    def find_animal(self, name: str) -> Optional:
        """
        Szuka zwierzęcia po imieniu w tym wybiegu.

        Args:
            name: Imię szukanego zwierzęcia.

        Returns:
            Znalezione zwierzę lub None.
        """
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def feed_all(self) -> list:
        """
        Karmi wszystkie zwierzęta w wybiegu.

        Returns:
            Lista potwierdzeń karmienia.
        """
        return [animal.feed() for animal in self._animals]

    def __len__(self) -> int:
        return len(self._animals)

    def __contains__(self, animal) -> bool:
        return animal in self._animals

    def __iter__(self) -> Iterator:
        return iter(self._animals)

    def __repr__(self) -> str:
        return f"Enclosure(name={self._name!r}, capacity={self._capacity})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Enclosure):
            return False
        return self._name == other._name

    def __hash__(self) -> int:
        return hash(self._name)

    def __str__(self) -> str:
        return f"Enclosure '{self._name}' ({len(self._animals)}/{self._capacity} animals)"

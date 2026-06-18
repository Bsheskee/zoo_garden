"""Enclosure module for the Zoo Garden system."""

from collections.abc import Iterator
from typing import Optional

from .exceptions import AnimalNotFoundError, EnclosureFullError


class Enclosure:
    """
    Represents an enclosure/pen for animals in the zoo.

    Attributes:
        _name: Name of the enclosure.
        _capacity: Maximum number of animals the enclosure can hold.
        _animals: List of animals currently in the enclosure.
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
        """Return a copy of the animals list to prevent external modification."""
        return list(self._animals)

    def add_animal(self, animal) -> None:
        """
        Add an animal to the enclosure.

        Args:
            animal: The animal to add.

        Raises:
            EnclosureFullError: If the enclosure is at capacity.
        """
        if len(self._animals) >= self._capacity:
            raise EnclosureFullError(f"Enclosure '{self._name}' is full (capacity: {self._capacity})")
        self._animals.append(animal)

    def remove_animal(self, animal) -> None:
        """
        Remove an animal from the enclosure.

        Args:
            animal: The animal to remove.

        Raises:
            AnimalNotFoundError: If the animal is not in this enclosure.
        """
        if animal not in self._animals:
            raise AnimalNotFoundError(f"Animal '{animal.name}' not found in enclosure '{self._name}'")
        self._animals.remove(animal)

    def find_animal(self, name: str) -> Optional:
        """
        Find an animal by name in this enclosure.

        Args:
            name: The name of the animal to find.

        Returns:
            The animal if found, None otherwise.
        """
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def feed_all(self) -> list:
        """
        Feed all animals in the enclosure.

        Returns:
            List of feeding confirmation strings.
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

"""Animal classes for the Zoo Garden system."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals in the zoo.

    Attributes:
        _next_id: Class-level counter for generating unique animal IDs.
        _id: Unique identifier for the animal.
        _name: Name of the animal.
        _age: Age of the animal in years.
        _health: Health status (0-100).
    """

    _next_id: int = 1

    def __init__(self, name: str, age: int) -> None:
        self._id = Animal._next_id
        Animal._next_id += 1
        self._name = name
        self._age = age
        self._health = 100

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, min(100, value))

    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound the animal makes."""
        pass

    @abstractmethod
    def diet(self) -> str:
        """Return the diet type of the animal."""
        pass

    def feed(self) -> str:
        return f"{self._name} is being fed."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, age={self._age})"

    def __str__(self) -> str:
        return f"{self._name} the {self.__class__.__name__}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Animal):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Animal):
            return NotImplemented
        return self._name < other._name

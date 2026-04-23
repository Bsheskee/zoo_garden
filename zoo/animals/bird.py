"""Bird classes for the Zoo Garden system."""

from .animal import Animal


class Bird(Animal):
    """
    Intermediate class for birds.

    Attributes:
        _wingspan: Wingspan of the bird in meters.
        _can_fly: Whether the bird can fly.
    """

    def __init__(self, name: str, age: int, wingspan: float = 1.0, can_fly: bool = True) -> None:
        super().__init__(name, age)
        self._wingspan = wingspan
        self._can_fly = can_fly

    def diet(self) -> str:
        return "Birds eat seeds, insects, fish, or small mammals depending on species."

    def fly(self) -> str:
        if self._can_fly:
            return f"{self._name} is flying with wingspan of {self._wingspan}m."
        return f"{self._name} cannot fly."


class Eagle(Bird):
    """Eagle - majestic bird of prey."""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, wingspan=2.5)

    def make_sound(self) -> str:
        return "Screech!"

    def diet(self) -> str:
        return "Eagles are carnivores, hunting fish, rabbits, and small mammals."


class Penguin(Bird):
    """Penguin - flightless aquatic bird."""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, wingspan=0.3, can_fly=False)

    def make_sound(self) -> str:
        return "Honk!"

    def swim(self) -> str:
        return f"{self._name} is swimming."

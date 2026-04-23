"""Reptile classes for the Zoo Garden system."""

from .animal import Animal


class Reptile(Animal):
    """
    Intermediate class for reptiles.

    Attributes:
        _is_venomous: Whether the reptile is venomous.
    """

    def __init__(self, name: str, age: int, is_venomous: bool = False) -> None:
        super().__init__(name, age)
        self._is_venomous = is_venomous

    def diet(self) -> str:
        return "Reptiles are carnivores, eating insects, fish, or mammals."

    def bask(self) -> str:
        return f"{self._name} is basking in the sun to regulate body temperature."

    def is_cold_blooded(self) -> bool:
        return True


class Crocodile(Reptile):
    """Crocodile - large aquatic reptile."""

    def __init__(self, name: str, age: int, length: float = 3.0) -> None:
        super().__init__(name, age, is_venomous=False)
        self._length = length

    def make_sound(self) -> str:
        return "Hiss!"

    def diet(self) -> str:
        return "Crocodiles are apex predators, eating fish, birds, and mammals."

    def swim(self) -> str:
        return f"{self._name} is swimming with powerful tail strokes."

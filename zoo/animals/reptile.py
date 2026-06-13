"""Reptile base class for the Zoo Garden system."""

from .animal import Animal


class Reptile(Animal):
    """Intermediate base class for all reptiles."""

    def __init__(self, name: str, age: int, is_venomous: bool = False) -> None:
        super().__init__(name, age)
        self._is_venomous = is_venomous

    def diet(self) -> str:
        return "Reptiles are carnivores, eating insects, fish, or mammals."

    def bask(self) -> str:
        return f"{self._name} is basking in the sun to regulate body temperature."

    def is_cold_blooded(self) -> bool:
        return True

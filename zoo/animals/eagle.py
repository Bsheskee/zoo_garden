"""Orzeł — majestatyczny ptak drapieżny."""

from .bird import Bird
from .flyable import Flyable


class Eagle(Bird, Flyable):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, wingspan=2.5)

    def make_sound(self) -> str:
        return "Screech!"

    def diet(self) -> str:
        return "Eagles are carnivores, hunting fish, rabbits, and small mammals."

    def fly(self) -> str:
        return f"{self._name} is flying with wingspan of {self._wingspan}m."

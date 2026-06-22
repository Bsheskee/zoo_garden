"""Krokodyl — duży wodny gad."""

from .reptile import Reptile


class Crocodile(Reptile):
    def __init__(self, name: str, age: int, length: float = 3.0) -> None:
        super().__init__(name, age, is_venomous=False)
        self._length = length

    def make_sound(self) -> str:
        return "Hiss!"

    def diet(self) -> str:
        return "Crocodiles are apex predators, eating fish, birds, and mammals."

    def swim(self) -> str:
        return f"{self._name} is swimming with powerful tail strokes."

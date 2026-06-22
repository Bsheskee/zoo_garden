"""Słoń — największy lądowy ssak."""

from .mammal import Mammal


class Elephant(Mammal):
    def __init__(self, name: str, age: int, tusk_length: float = 0.0) -> None:
        super().__init__(name, age)
        self._tusk_length = tusk_length

    def make_sound(self) -> str:
        return "Trumpet!"

    def diet(self) -> str:
        return "Elephants are herbivores, eating grasses, fruits, and tree bark."

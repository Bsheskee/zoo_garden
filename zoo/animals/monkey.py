"""Monkey — intelligent primate."""

from .mammal import Mammal


class Monkey(Mammal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def make_sound(self) -> str:
        return "Ooh ooh ah ah!"

    def climb(self) -> str:
        return f"{self._name} is climbing a tree."

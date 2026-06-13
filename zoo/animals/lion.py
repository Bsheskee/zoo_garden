"""Lion — king of beasts."""

from .mammal import Mammal


class Lion(Mammal):
    def __init__(self, name: str, age: int, mane: bool = True) -> None:
        super().__init__(name, age)
        self._mane = mane

    def make_sound(self) -> str:
        return "Roar!"

    def diet(self) -> str:
        return "Lions are carnivores, hunting zebras, wildebeests, and other prey."

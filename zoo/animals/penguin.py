"""Penguin — flightless aquatic bird."""

from .bird import Bird


class Penguin(Bird):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, wingspan=0.3)

    def make_sound(self) -> str:
        return "Honk!"

    def swim(self) -> str:
        return f"{self._name} is swimming."

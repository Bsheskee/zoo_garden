"""Klasa bazowa Bird dla systemu Zoo Garden."""

from .animal import Animal


class Bird(Animal):
    """Pośrednia klasa bazowa dla wszystkich ptaków."""

    def __init__(self, name: str, age: int, wingspan: float = 1.0) -> None:
        super().__init__(name, age)
        self._wingspan = wingspan

    def diet(self) -> str:
        return "Birds eat seeds, insects, fish, or small mammals depending on species."

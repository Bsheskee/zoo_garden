"""Klasa bazowa Mammal dla systemu Zoo Garden."""

from .animal import Animal


class Mammal(Animal):
    """Pośrednia klasa bazowa dla wszystkich ssaków."""

    def __init__(self, name: str, age: int, fur_color: str = "brown") -> None:
        super().__init__(name, age)
        self._fur_color = fur_color

    def diet(self) -> str:
        return "Mammals are herbivores, carnivores, or omnivores with specialized teeth."

    def give_birth(self) -> str:
        return f"{self._name} gives birth to live young."

    def has_fur(self) -> bool:
        return True

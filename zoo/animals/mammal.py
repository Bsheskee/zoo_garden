"""Mammal classes for the Zoo Garden system."""

from .animal import Animal


class Mammal(Animal):
    """
    Intermediate class for mammals.

    Attributes:
        _fur_color: Color of the mammal's fur.
    """

    def __init__(self, name: str, age: int, fur_color: str = "brown") -> None:
        super().__init__(name, age)
        self._fur_color = fur_color

    def diet(self) -> str:
        return "Mammals are herbivores, carnivores, or omnivores with specialized teeth."

    def give_birth(self) -> str:
        return f"{self._name} gives birth to live young."

    def has_fur(self) -> bool:
        return True


class Lion(Mammal):
    """Lion - the king of beasts."""

    def __init__(self, name: str, age: int, mane: bool = True) -> None:
        super().__init__(name, age)
        self._mane = mane

    def make_sound(self) -> str:
        return "Roar!"

    def diet(self) -> str:
        return "Lions are carnivores, hunting zebras, wildebeests, and other prey."


class Elephant(Mammal):
    """Elephant - the largest land mammal."""

    def __init__(self, name: str, age: int, tusk_length: float = 0.0) -> None:
        super().__init__(name, age)
        self._tusk_length = tusk_length

    def make_sound(self) -> str:
        return "Trumpet!"

    def diet(self) -> str:
        return "Elephants are herbivores, eating grasses, fruits, and tree bark."


class Monkey(Mammal):
    """Monkey - intelligent primate."""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def make_sound(self) -> str:
        return "Ooh ooh ah ah!"

    def climb(self) -> str:
        return f"{self._name} is climbing a tree."

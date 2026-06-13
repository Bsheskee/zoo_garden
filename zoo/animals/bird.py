"""Bird base class for the Zoo Garden system."""

from .animal import Animal


class Bird(Animal):
    """Intermediate base class for all birds."""

    def __init__(self, name: str, age: int, wingspan: float = 1.0) -> None:
        super().__init__(name, age)
        self._wingspan = wingspan

    def diet(self) -> str:
        return "Birds eat seeds, insects, fish, or small mammals depending on species."

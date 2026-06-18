"""Animals package — public API for all animal classes."""

from .animal import Animal
from .bird import Bird
from .crocodile import Crocodile
from .eagle import Eagle
from .elephant import Elephant
from .flyable import Flyable
from .lion import Lion
from .mammal import Mammal
from .monkey import Monkey
from .penguin import Penguin
from .reptile import Reptile

__all__ = [
    "Animal",
    "Bird",
    "Crocodile",
    "Eagle",
    "Elephant",
    "Flyable",
    "Lion",
    "Mammal",
    "Monkey",
    "Penguin",
    "Reptile",
]

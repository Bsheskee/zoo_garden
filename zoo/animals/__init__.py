"""Animals package — public API for all animal classes."""

from .animal import Animal
from .flyable import Flyable
from .mammal import Mammal
from .bird import Bird
from .reptile import Reptile
from .elephant import Elephant
from .lion import Lion
from .monkey import Monkey
from .eagle import Eagle
from .penguin import Penguin
from .crocodile import Crocodile

__all__ = [
    "Animal",
    "Flyable",
    "Mammal",
    "Bird",
    "Reptile",
    "Elephant",
    "Lion",
    "Monkey",
    "Eagle",
    "Penguin",
    "Crocodile",
]

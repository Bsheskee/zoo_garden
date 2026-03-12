from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Base class for all animals in the zoo.
    """

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name}, age={self._age})"

    def __str__(self):
        return f"{self._name} ({self.__class__.__name__})"

    def __eq__(self, other):
        return isinstance(other, Animal) and self.name == other.name
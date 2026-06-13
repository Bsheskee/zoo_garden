"""Flyable interface for animals capable of flight."""

from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> str: ...

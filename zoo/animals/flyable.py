"""Interfejs Flyable dla zwierząt zdolnych do lotu."""

from abc import ABC, abstractmethod


class Flyable(ABC):
    """Mixin dla zwierząt potrafiących latać."""

    @abstractmethod
    def fly(self) -> str: ...

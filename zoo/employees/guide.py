"""Guide module for the Zoo Garden system."""

from typing import Optional
from .employee import Employee


class Guide(Employee):
    """
    Guide - leads tours and educates visitors about animals.

    Attributes:
        _languages: List of languages the guide speaks.
    """

    def __init__(self, name: str, languages: Optional[list] = None, salary: float = 3500.0) -> None:
        super().__init__(name, salary)
        self._languages = languages if languages else ["English"]

    @property
    def languages(self) -> list:
        return list(self._languages)

    def add_language(self, language: str) -> None:
        """Add a language to the guide's repertoire."""
        if language not in self._languages:
            self._languages.append(language)

    def give_tour(self, enclosure) -> str:
        """
        Give a tour of an enclosure.

        Args:
            enclosure: The enclosure to tour.

        Returns:
            Tour description string.
        """
        return f"{self._name} is giving a tour of '{enclosure.name}' in {', '.join(self._languages)}."

    def work(self) -> str:
        return f"{self._name} is leading visitor tours and explaining animal behavior."

    def role(self) -> str:
        return f"Guide - Educational tours in {', '.join(self._languages)}."

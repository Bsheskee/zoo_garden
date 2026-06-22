"""Moduł przewodnika dla systemu Zoo Garden."""

from .employee import Employee


class Guide(Employee):
    """
    Przewodnik — oprowadza zwiedzających i edukuje ich o zwierzętach.

    Attributes:
        _languages: Lista języków, którymi posługuje się przewodnik.
    """

    def __init__(self, name: str, languages: list | None = None, salary: float = 3500.0) -> None:
        super().__init__(name, salary)
        self._languages = languages if languages else ["English"]

    @property
    def languages(self) -> list:
        return list(self._languages)

    def add_language(self, language: str) -> None:
        """Dodaje język do repertuaru przewodnika."""
        if language not in self._languages:
            self._languages.append(language)

    def give_tour(self, enclosure) -> str:
        """
        Prowadzi wycieczkę po wybiegu.

        Args:
            enclosure: Wybieg do zwiedzenia.

        Returns:
            Opis wycieczki.
        """
        return f"{self._name} is giving a tour of '{enclosure.name}' in {', '.join(self._languages)}."

    def work(self) -> str:
        return f"{self._name} is leading visitor tours and explaining animal behavior."

    def role(self) -> str:
        return f"Guide - Educational tours in {', '.join(self._languages)}."

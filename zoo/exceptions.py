"""Własne wyjątki systemu Zoo Garden."""


class ZooError(Exception):
    """Wyjątek bazowy dla wszystkich błędów związanych z zoo."""

    pass


class EnclosureFullError(ZooError):
    """Zgłaszany przy próbie dodania zwierzęcia do pełnego wybiegu."""

    pass


class AnimalNotFoundError(ZooError):
    """Zgłaszany gdy zwierzę nie zostało znalezione w wybiegu lub zoo."""

    pass


class InvalidAnimalDataError(ZooError):
    """Zgłaszany gdy dane zwierzęcia są nieprawidłowe."""

    pass

"""Custom exceptions for the Zoo Garden system."""


class ZooError(Exception):
    """Base exception for all zoo-related errors."""
    pass


class EnclosureFullError(ZooError):
    """Raised when trying to add an animal to a full enclosure."""
    pass


class AnimalNotFoundError(ZooError):
    """Raised when an animal is not found in an enclosure or zoo."""
    pass


class InvalidAnimalDataError(ZooError):
    """Raised when animal data is invalid."""
    pass

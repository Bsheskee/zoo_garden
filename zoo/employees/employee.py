"""Moduł pracownika dla systemu Zoo Garden."""

from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Abstrakcyjna klasa bazowa dla wszystkich pracowników zoo.

    Attributes:
        _next_id: Licznik klasy generujący unikalne identyfikatory pracowników.
        _id: Unikalny identyfikator pracownika.
        _name: Imię i nazwisko pracownika.
        _salary: Wynagrodzenie pracownika.
        _assigned_enclosures: Lista wybiegów przypisanych do pracownika.
    """

    _next_id: int = 1

    def __init__(self, name: str, salary: float = 5000.0) -> None:
        self._id = Employee._next_id
        Employee._next_id += 1
        self._name = name
        self._salary = salary
        self._assigned_enclosures: list = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @property
    def assigned_enclosures(self) -> list:
        """Zwraca kopię listy przypisanych wybiegów."""
        return list(self._assigned_enclosures)

    def assign_to(self, enclosure) -> None:
        """Przypisuje pracownika do wybiegu."""
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)

    def unassign_from(self, enclosure) -> None:
        """Odpisuje pracownika od wybiegu."""
        if enclosure in self._assigned_enclosures:
            self._assigned_enclosures.remove(enclosure)

    @abstractmethod
    def work(self) -> str:
        """Zwraca opis czynności wykonywanych przez pracownika."""
        pass

    @abstractmethod
    def role(self) -> str:
        """Zwraca opis roli pracownika."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, salary={self._salary})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Employee):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

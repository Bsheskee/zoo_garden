"""Employee module for the Zoo Garden system."""

from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Abstract base class for all zoo employees.

    Attributes:
        _next_id: Class-level counter for generating unique employee IDs.
        _id: Unique identifier for the employee.
        _name: Name of the employee.
        _salary: Employee's salary.
        _assigned_enclosures: List of enclosures assigned to this employee.
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
        """Return a copy of assigned enclosures."""
        return list(self._assigned_enclosures)

    def assign_to(self, enclosure) -> None:
        """Assign this employee to an enclosure."""
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)

    def unassign_from(self, enclosure) -> None:
        """Unassign this employee from an enclosure."""
        if enclosure in self._assigned_enclosures:
            self._assigned_enclosures.remove(enclosure)

    @abstractmethod
    def work(self) -> str:
        """Return what the employee does at work."""
        pass

    @abstractmethod
    def role(self) -> str:
        """Return the role description of this employee."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, salary={self._salary})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Employee):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

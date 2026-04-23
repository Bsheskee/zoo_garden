"""Feeding schedule module for the Zoo Garden system."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class FeedingEntry:
    """
    Represents a single feeding entry in the schedule.

    Attributes:
        enclosure_name: Name of the enclosure to feed.
        time: Time of feeding (e.g., "09:00").
        food_type: Type of food to serve.
        notes: Optional additional notes.
    """
    enclosure_name: str
    time: str
    food_type: str
    notes: str = ""


class FeedingSchedule:
    """
    Manages the feeding schedule for the zoo.

    Uses composition with FeedingEntry - entries don't exist
    independently from the schedule.

    Attributes:
        _day: Day of the week for this schedule.
        _entries: List of feeding entries.
    """

    def __init__(self, day: str = "Monday") -> None:
        self._day = day
        self._entries: list[FeedingEntry] = []

    @property
    def day(self) -> str:
        return self._day

    @property
    def entries(self) -> list:
        """Return a copy of entries to prevent external modification."""
        return list(self._entries)

    def add_entry(self, enclosure_name: str, time: str, food_type: str, notes: str = "") -> None:
        """
        Add a feeding entry to the schedule.

        Args:
            enclosure_name: Name of the enclosure to feed.
            time: Time of feeding.
            food_type: Type of food.
            notes: Optional notes.
        """
        entry = FeedingEntry(enclosure_name, time, food_type, notes)
        self._entries.append(entry)

    def remove_entry(self, enclosure_name: str, time: str) -> bool:
        """
        Remove a feeding entry by enclosure name and time.

        Args:
            enclosure_name: Name of the enclosure.
            time: Time of the feeding.

        Returns:
            True if entry was removed, False if not found.
        """
        for i, entry in enumerate(self._entries):
            if entry.enclosure_name == enclosure_name and entry.time == time:
                self._entries.pop(i)
                return True
        return False

    def get_by_enclosure(self, name: str) -> list:
        """
        Get all feeding entries for a specific enclosure.

        Args:
            name: Name of the enclosure.

        Returns:
            List of feeding entries for the enclosure.
        """
        return [e for e in self._entries if e.enclosure_name == name]

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        return f"FeedingSchedule(day={self._day!r}, entries={len(self._entries)})"

    def __str__(self) -> str:
        return f"Feeding Schedule for {self._day} ({len(self._entries)} entries)"

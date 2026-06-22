"""Moduł harmonogramu karmienia dla systemu Zoo Garden."""

from dataclasses import dataclass


@dataclass
class FeedingEntry:
    """
    Reprezentuje pojedynczy wpis w harmonogramie karmienia.

    Attributes:
        enclosure_name: Nazwa wybiegu do nakarmienia.
        time: Godzina karmienia (np. "09:00").
        food_type: Typ podawanego pokarmu.
        notes: Opcjonalne dodatkowe uwagi.
    """

    enclosure_name: str
    time: str
    food_type: str
    notes: str = ""


class FeedingSchedule:
    """
    Zarządza harmonogramem karmienia zoo.

    Używa kompozycji z FeedingEntry — wpisy nie istnieją
    niezależnie od harmonogramu.

    Attributes:
        _day: Dzień tygodnia dla tego harmonogramu.
        _entries: Lista wpisów karmienia.
    """

    def __init__(self, day: str = "Monday") -> None:
        self._day = day
        self._entries: list[FeedingEntry] = []

    @property
    def day(self) -> str:
        return self._day

    @property
    def entries(self) -> list:
        """Zwraca kopię wpisów, aby zapobiec modyfikacji z zewnątrz."""
        return list(self._entries)

    def add_entry(self, enclosure_name: str, time: str, food_type: str, notes: str = "") -> None:
        """
        Dodaje wpis karmienia do harmonogramu.

        Args:
            enclosure_name: Nazwa wybiegu do nakarmienia.
            time: Godzina karmienia.
            food_type: Typ pokarmu.
            notes: Opcjonalne uwagi.
        """
        entry = FeedingEntry(enclosure_name, time, food_type, notes)
        self._entries.append(entry)

    def remove_entry(self, enclosure_name: str, time: str) -> bool:
        """
        Usuwa wpis karmienia według nazwy wybiegu i godziny.

        Args:
            enclosure_name: Nazwa wybiegu.
            time: Godzina karmienia.

        Returns:
            True jeśli wpis usunięto, False jeśli nie znaleziono.
        """
        for i, entry in enumerate(self._entries):
            if entry.enclosure_name == enclosure_name and entry.time == time:
                self._entries.pop(i)
                return True
        return False

    def get_by_enclosure(self, name: str) -> list:
        """
        Pobiera wszystkie wpisy karmienia dla danego wybiegu.

        Args:
            name: Nazwa wybiegu.

        Returns:
            Lista wpisów karmienia dla wybiegu.
        """
        return [e for e in self._entries if e.enclosure_name == name]

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        return f"FeedingSchedule(day={self._day!r}, entries={len(self._entries)})"

    def __str__(self) -> str:
        return f"Feeding Schedule for {self._day} ({len(self._entries)} entries)"

"""Testy klasy Zoo."""

import pytest

from zoo.animals import Eagle, Elephant, Lion
from zoo.employees.guide import Guide
from zoo.employees.veterinarian import Veterinarian
from zoo.employees.zookeeper import Zookeeper
from zoo.enclosure import Enclosure
from zoo.feeding_schedule import FeedingSchedule
from zoo.zoo import Zoo


@pytest.fixture
def zoo():
    return Zoo("Central Zoo", "Warsaw")


@pytest.fixture
def enclosure():
    return Enclosure("Savanna", 3)


@pytest.fixture
def lion():
    return Lion("Simba", 5)


@pytest.fixture
def eagle():
    return Eagle("Freedom", 4)


def test_create_zoo(zoo):
    """Test 1: Tworzenie zoo."""
    assert zoo.name == "Central Zoo"
    assert zoo.city == "Warsaw"
    assert len(zoo) == 0


def test_create_enclosure(zoo):
    """Test 2: Tworzenie wybiegu przez zoo."""
    enc = zoo.create_enclosure("Aviary", 5)
    assert enc.name == "Aviary"
    assert enc.capacity == 5
    assert "Aviary" in zoo._enclosures


def test_hire_employee(zoo):
    """Test 3: Zatrudnianie pracownika."""
    keeper = Zookeeper("John", 4000)
    zoo.hire_employee(keeper)
    assert keeper in zoo._employees
    assert len(zoo._employees) == 1


def test_total_animals(zoo, enclosure):
    """Test 4: Całkowita liczba zwierząt."""
    zoo._enclosures["Savanna"] = enclosure
    enclosure.add_animal(Lion("Simba", 5))
    enclosure.add_animal(Elephant("Dumbo", 10))

    assert zoo.total_animals() == 2


def test_find_animal_in_zoo(zoo, enclosure):
    """Test 5: Wyszukiwanie zwierzęcia we wszystkich wybiegach."""
    lion = Lion("Simba", 5)
    zoo._enclosures["Savanna"] = enclosure
    enclosure.add_animal(lion)

    found = zoo.find_animal("Simba")
    assert found == lion

    not_found = zoo.find_animal("Nala")
    assert not_found is None


def test_zoo_getitem(zoo, enclosure):
    """Test 6: Pobieranie wybiegu po nazwie (__getitem__)."""
    zoo._enclosures["Savanna"] = enclosure
    assert zoo["Savanna"] == enclosure


def test_zoo_contains(zoo, enclosure, lion):
    """Test 7: Operator __contains__ dla wybiegów i pracowników."""
    zoo._enclosures["Savanna"] = enclosure

    assert "Savanna" in zoo
    assert enclosure in zoo

    keeper = Zookeeper("John", 4000)
    zoo.hire_employee(keeper)
    assert keeper in zoo


def test_zoo_report(zoo):
    """Test 8: Generowanie raportu zoo."""
    report = zoo.report()
    assert "Central Zoo" in report
    assert "Warsaw" in report
    assert "Total enclosures:" in report
    assert "Total employees:" in report


def test_zoo_str_repr(zoo):
    """Test 9: Reprezentacje tekstowe zoo."""
    assert "Central Zoo" in str(zoo)
    assert "Warsaw" in str(zoo)
    assert "Central Zoo" in repr(zoo)


def test_fire_employee(zoo):
    """Test 10: Zwalnianie pracownika."""
    keeper = Zookeeper("John", 4000)
    zoo.hire_employee(keeper)

    assert zoo.fire_employee(keeper) is True
    assert keeper not in zoo._employees

    assert zoo.fire_employee(keeper) is False


def test_zookeeper_feed_animals(zoo, enclosure):
    """Test 11: Opiekun karmi zwierzęta w przypisanym wybiegu."""
    lion = Lion("Simba", 5)
    enclosure.add_animal(lion)
    zoo._enclosures["Savanna"] = enclosure

    keeper = Zookeeper("John", 4000)
    keeper.assign_to(enclosure)

    result = keeper.feed_animals()
    assert "John" in result
    assert "Savanna" in result


def test_veterinarian_treat_animal(zoo, enclosure, lion):
    """Test 12: Weterynarz leczy zwierzę."""
    enclosure.add_animal(lion)
    zoo._enclosures["Savanna"] = enclosure

    vet = Veterinarian("Dr. Smith", "exotic", 7000)
    lion.health = 50

    result = vet.treat_animal(lion)
    assert "Dr. Smith" in result
    assert lion.health == 70  # +20 health


def test_guide_languages(zoo):
    """Test 13: Przewodnik z wieloma językami."""
    guide = Guide("Maria", ["English", "Spanish", "French"], 3500)
    zoo.hire_employee(guide)

    assert len(guide.languages) == 3
    assert "Spanish" in guide.languages

    guide.add_language("German")
    assert "German" in guide.languages


def test_feeding_schedule(zoo):
    """Test 14: Operacje na harmonogramie karmienia."""
    schedule = FeedingSchedule("Monday")
    schedule.add_entry("Savanna", "09:00", "Hay", "Extra vitamins")
    schedule.add_entry("Savanna", "15:00", "Grass", "")
    schedule.add_entry("Aviary", "10:00", "Seeds", "")

    assert len(schedule) == 3

    savanna_entries = schedule.get_by_enclosure("Savanna")
    assert len(savanna_entries) == 2


def test_feeding_schedule_remove(zoo):
    """Test 15: Usuwanie wpisu z harmonogramu karmienia."""
    schedule = FeedingSchedule("Monday")
    schedule.add_entry("Savanna", "09:00", "Hay", "")
    schedule.add_entry("Savanna", "15:00", "Grass", "")

    assert schedule.remove_entry("Savanna", "09:00") is True
    assert schedule.remove_entry("Savanna", "09:00") is False
    assert len(schedule) == 1

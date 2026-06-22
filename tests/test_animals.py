"""Testy klas zwierząt."""

import pytest

from zoo.animals import Crocodile, Eagle, Elephant, Lion, Monkey, Penguin


@pytest.fixture
def lion():
    return Lion("Simba", 5)


@pytest.fixture
def elephant():
    return Elephant("Dumbo", 10)


@pytest.fixture
def monkey():
    return Monkey("George", 3)


@pytest.fixture
def eagle():
    return Eagle("Freedom", 4)


@pytest.fixture
def penguin():
    return Penguin("Waddle", 2)


@pytest.fixture
def crocodile():
    return Crocodile("Snap", 8)


def test_create_animals():
    """Test 1: Tworzenie różnych typów zwierząt."""
    lion = Lion("Simba", 5)
    elephant = Elephant("Dumbo", 10)
    assert lion.name == "Simba"
    assert elephant.name == "Dumbo"


def test_animal_stats_and_properties():
    """Test 2: Sprawdzenie podstawowych statystyk i właściwości."""
    lion = Lion("Simba", 5)
    assert lion.age == 5
    assert lion.health == 100
    assert lion.id is not None


def test_health_clamping():
    """Test 3: Ograniczanie wartości zdrowia (clamping 0-100)."""
    lion = Lion("Simba", 5)
    lion.health = 150
    assert lion.health == 100
    lion.health = -10
    assert lion.health == 0


def test_make_sound_polymorphism():
    """Test 4: Polimorficzna metoda make_sound."""
    animals = [
        (Lion("Simba", 5), "Roar!"),
        (Elephant("Dumbo", 10), "Trumpet!"),
        (Monkey("George", 3), "Ooh ooh ah ah!"),
        (Eagle("Freedom", 4), "Screech!"),
        (Penguin("Waddle", 2), "Honk!"),
        (Crocodile("Snap", 8), "Hiss!"),
    ]
    for animal, expected_sound in animals:
        assert animal.make_sound() == expected_sound


def test_diet_methods():
    """Test 5: Metody diet dla różnych typów zwierząt."""
    lion = Lion("Simba", 5)
    eagle = Eagle("Freedom", 4)
    crocodile = Crocodile("Snap", 8)

    assert "carnivore" in lion.diet().lower()
    assert "carnivore" in eagle.diet().lower() or "hunt" in eagle.diet().lower()
    assert "predator" in crocodile.diet().lower() or "carnivore" in crocodile.diet().lower()


def test_mammal_features(lion):
    """Test 6: Cechy charakterystyczne ssaków."""
    assert lion.has_fur() is True
    assert "live young" in lion.give_birth()


def test_bird_features(eagle, penguin):
    """Test 7: Cechy charakterystyczne ptaków."""
    from zoo.animals import Flyable

    assert "flying" in eagle.fly()
    assert isinstance(eagle, Flyable)
    assert not isinstance(penguin, Flyable)
    assert "swimming" in penguin.swim()


def test_reptile_features(crocodile):
    """Test 8: Cechy charakterystyczne gadów."""
    assert crocodile.is_cold_blooded() is True
    assert "basking" in crocodile.bask().lower()


def test_animal_comparison():
    """Test 9: Porównywanie zwierząt (__eq__, __hash__, __lt__)."""
    lion1 = Lion("Simba", 5)
    lion2 = Lion("Simba", 3)  # Same ID sequence, different object

    # Same object comparison
    assert lion1 == lion1

    # Different IDs should not be equal
    assert lion1 != lion2

    # Hash based on ID
    assert hash(lion1) == hash(lion1)


def test_animal_sorting():
    """Test 10: Sortowanie zwierząt (__lt__)."""
    animals = [
        Lion("Charlie", 3),
        Eagle("Alpha", 2),
        Penguin("Beta", 1),
    ]
    sorted_animals = sorted(animals)
    assert sorted_animals[0].name == "Alpha"
    assert sorted_animals[1].name == "Beta"
    assert sorted_animals[2].name == "Charlie"


def test_animal_str_repr():
    """Test 11: Reprezentacje tekstowe."""
    lion = Lion("Simba", 5)
    assert "Simba" in str(lion)
    assert "Lion" in str(lion)
    assert "Simba" in repr(lion)


def test_feed_method():
    """Test 12: Metoda karmienia."""
    lion = Lion("Simba", 5)
    assert "fed" in lion.feed().lower()


def test_isinstance_checks(lion, elephant):
    """Test 13: Sprawdzanie isinstance i issubclass."""
    from zoo.animals import Animal, Mammal

    assert isinstance(lion, Lion)
    assert isinstance(lion, Mammal)
    assert isinstance(lion, Animal)
    assert issubclass(Lion, Mammal)
    assert issubclass(Mammal, Animal)


def test_name_validation():
    """Test 14: Walidacja imienia."""
    lion = Lion("Simba", 5)
    lion.name = "Mufasa"
    assert lion.name == "Mufasa"

    with pytest.raises(ValueError):
        lion.name = ""


def test_unique_ids():
    """Test 15: Generowanie unikalnych identyfikatorów."""
    lion1 = Lion("Simba", 5)
    lion2 = Lion("Nala", 4)
    lion3 = Lion("Mufasa", 6)

    assert lion1.id != lion2.id
    assert lion2.id != lion3.id
    assert lion1.id != lion3.id

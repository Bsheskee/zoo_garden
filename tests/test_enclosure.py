"""Tests for Enclosure class."""

import pytest
from zoo.enclosure import Enclosure
from zoo.animals.mammal import Lion, Elephant
from zoo.exceptions import EnclosureFullError, AnimalNotFoundError


@pytest.fixture
def enclosure():
    return Enclosure("Savanna", 3)


@pytest.fixture
def lion():
    return Lion("Simba", 5)


@pytest.fixture
def elephant():
    return Elephant("Dumbo", 10)


def test_create_enclosure(enclosure):
    """Test 1: Creating enclosure."""
    assert enclosure.name == "Savanna"
    assert enclosure.capacity == 3
    assert len(enclosure) == 0


def test_add_animal_to_enclosure(enclosure, lion):
    """Test 2: Adding animal to enclosure."""
    enclosure.add_animal(lion)
    assert lion in enclosure
    assert len(enclosure) == 1


def test_enclosure_capacity_validation(enclosure, lion, elephant):
    """Test 3: Enclosure capacity validation (EnclosureFullError)."""
    monkey = Lion("George", 3)

    enclosure.add_animal(lion)
    enclosure.add_animal(elephant)
    enclosure.add_animal(monkey)

    with pytest.raises(EnclosureFullError):
        enclosure.add_animal(Lion("Nala", 4))


def test_remove_animal(enclosure, lion):
    """Test 4: Removing animal from enclosure."""
    enclosure.add_animal(lion)
    enclosure.remove_animal(lion)
    assert lion not in enclosure
    assert len(enclosure) == 0


def test_remove_nonexistent_animal(enclosure, lion):
    """Test 5: Removing nonexistent animal raises AnimalNotFoundError."""
    with pytest.raises(AnimalNotFoundError):
        enclosure.remove_animal(lion)


def test_find_animal(enclosure, lion, elephant):
    """Test 6: Finding animal by name."""
    enclosure.add_animal(lion)
    enclosure.add_animal(elephant)

    found = enclosure.find_animal("Simba")
    assert found == lion

    not_found = enclosure.find_animal("Nala")
    assert not_found is None


def test_feed_all_animals(enclosure, lion, elephant):
    """Test 7: Feeding all animals."""
    enclosure.add_animal(lion)
    enclosure.add_animal(elephant)

    results = enclosure.feed_all()
    assert len(results) == 2
    assert all("fed" in r.lower() for r in results)


def test_enclosure_dunder_methods(enclosure, lion):
    """Test 8: Enclosure dunder methods (__len__, __contains__, __iter__)."""
    enclosure.add_animal(lion)

    assert len(enclosure) == 1
    assert lion in enclosure

    # Test iteration
    animals = list(enclosure)
    assert lion in animals


def test_enclosure_str_repr(enclosure):
    """Test 9: Enclosure string representations."""
    assert "Savanna" in str(enclosure)
    assert "Savanna" in repr(enclosure)


def test_enclosure_equality():
    """Test 10: Enclosure equality (__eq__, __hash__)."""
    enc1 = Enclosure("Savanna", 3)
    enc2 = Enclosure("Savanna", 5)  # Same name, different capacity
    enc3 = Enclosure("Aviary", 3)

    assert enc1 == enc2  # Same name
    assert enc1 != enc3

    # Hash should be based on name
    assert hash(enc1) == hash(enc2)


def test_animals_property_returns_copy(enclosure, lion):
    """Test 11: animals property returns a copy."""
    enclosure.add_animal(lion)

    animals1 = enclosure.animals
    animals2 = enclosure.animals

    # Should be different list objects
    assert animals1 is not animals2
    assert animals1 == animals2


def test_enclosure_hash_in_set():
    """Test 12: Enclosure can be used in sets (requires __hash__)."""
    enc1 = Enclosure("Savanna", 3)
    enc2 = Enclosure("Savanna", 5)

    enclosure_set = {enc1, enc2}
    assert len(enclosure_set) == 1  # Same name, same hash


def test_add_multiple_animals(enclosure):
    """Test 13: Adding multiple animals."""
    animals = [
        Lion("Simba", 5),
        Lion("Nala", 4),
        Elephant("Dumbo", 10),
    ]

    for animal in animals:
        enclosure.add_animal(animal)

    assert len(enclosure) == 3


def test_enclosure_empty_feed(enclosure):
    """Test 14: Feeding empty enclosure."""
    results = enclosure.feed_all()
    assert results == []


def test_enclosure_full_error_message(enclosure, lion):
    """Test 15: EnclosureFullError contains meaningful message."""
    elephant = Elephant("Dumbo", 10)
    monkey = Lion("George", 3)

    enclosure.add_animal(lion)
    enclosure.add_animal(elephant)
    enclosure.add_animal(monkey)

    with pytest.raises(EnclosureFullError) as exc_info:
        enclosure.add_animal(Lion("Nala", 4))

    assert "Savanna" in str(exc_info.value)
    assert "full" in str(exc_info.value).lower()

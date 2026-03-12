from zoo.enclosure import Enclosure
from zoo.animals.lion import Lion


def test_add_animal():
    enc = Enclosure("Savannah", 2)
    lion = Lion("Simba", 4)

    enc.add_animal(lion)

    assert lion in enc.animals
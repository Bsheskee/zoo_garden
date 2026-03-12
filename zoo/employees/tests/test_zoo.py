from zoo.zoo import Zoo
from zoo.enclosure import Enclosure


def test_add_enclosure():
    zoo = Zoo("City Zoo")
    enc = Enclosure("Bird House", 5)

    zoo.add_enclosure(enc)

    assert enc in zoo.enclosures
from zoo.animals.lion import Lion


def test_lion_sound():
    lion = Lion("Simba", 5)
    assert lion.make_sound() == "Roar"


def test_animal_equality():
    a1 = Lion("Simba", 5)
    a2 = Lion("Simba", 3)

    assert a1 == a2
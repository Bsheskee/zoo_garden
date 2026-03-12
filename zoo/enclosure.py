class Enclosure:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        if len(self.animals) >= self.capacity:
            raise ValueError("Enclosure is full")
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f"Enclosure {self.name} ({len(self.animals)}/{self.capacity})"
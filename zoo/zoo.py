class Zoo:

    def __init__(self, name):
        self.name = name
        self.enclosures = []
        self.employees = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_animals(self):
        animals = []
        for enclosure in self.enclosures:
            animals.extend(enclosure.animals)
        return animals
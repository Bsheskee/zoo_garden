from .employee import Employee

class Zookeeper(Employee):

    def __init__(self, name, enclosure=None):
        super().__init__(name)
        self.enclosure = enclosure

    def perform_duty(self):
        return "Feeding animals"
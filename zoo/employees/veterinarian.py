from .employee import Employee


class Veterinarian(Employee):

    def perform_duty(self):
        return "Treating animals"
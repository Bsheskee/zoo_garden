"""Demo script for Zoo Garden Management System."""

from zoo.animals.mammal import Lion, Elephant, Monkey
from zoo.animals.bird import Eagle, Penguin
from zoo.animals.reptile import Crocodile
from zoo.enclosure import Enclosure
from zoo.zoo import Zoo
from zoo.exceptions import ZooError, EnclosureFullError, AnimalNotFoundError, InvalidAnimalDataError
from zoo.feeding_schedule import FeedingSchedule, FeedingEntry
from zoo.employees.zookeeper import Zookeeper
from zoo.employees.veterinarian import Veterinarian
from zoo.employees.guide import Guide


def main():
    print("=" * 60)
    print("ZOO GARDEN MANAGEMENT SYSTEM - DEMO")
    print("=" * 60)

    # 1. Create zoo with enclosures
    print("\n--- 1. Creating Zoo ---")
    zoo = Zoo("Central Zoo", "Warsaw")
    savanna = zoo.create_enclosure("Savanna", 3)
    aviary = zoo.create_enclosure("Aviary", 4)
    pond = zoo.create_enclosure("Pond", 2)
    print(f"Created zoo: {zoo}")
    print(f"Enclosures: {[e.name for e in zoo._enclosures.values()]}")

    # 2. Add animals to enclosures
    print("\n--- 2. Adding Animals ---")
    lion = Lion("Simba", 5)
    elephant = Elephant("Dumbo", 10)
    monkey = Monkey("George", 3)
    eagle = Eagle("Freedom", 4)
    penguin = Penguin("Waddle", 2)
    crocodile = Crocodile("Snap", 8)

    savanna.add_animal(lion)
    savanna.add_animal(elephant)
    savanna.add_animal(monkey)
    aviary.add_animal(eagle)
    aviary.add_animal(penguin)
    pond.add_animal(crocodile)

    print(f"Savanna animals: {[a.name for a in savanna]}")
    print(f"Aviary animals: {[a.name for a in aviary]}")
    print(f"Pond animals: {[a.name for a in pond]}")

    # 3. Try to add animal to full enclosure (EnclosureFullError)
    print("\n--- 3. Testing EnclosureFullError ---")
    try:
        savanna.add_animal(eagle)
    except EnclosureFullError as e:
        print(f"Caught EnclosureFullError: {e}")

    # 4. Feed animals
    print("\n--- 4. Feeding Animals ---")
    results = savanna.feed_all()
    for r in results:
        print(f"  {r}")

    # 5. Assign zookeeper to enclosure
    print("\n--- 5. Assigning Zookeeper ---")
    keeper = Zookeeper("John", 4000)
    keeper.assign_to(savanna)
    print(f"Zookeeper {keeper.name} assigned to: {keeper._assigned_enclosure.name}")
    print(keeper.feed_animals())

    # 6. Generate zoo report
    print("\n--- 6. Zoo Report ---")
    print(zoo.report())

    # 7. Polymorphism demonstration
    print("\n--- 7. Polymorphism Demo ---")
    animals = [lion, elephant, monkey, eagle, penguin, crocodile]
    print("Animal sounds:")
    for animal in animals:
        print(f"  {animal.name}: {animal.make_sound()}")

    print("\nAnimal diets:")
    for animal in animals:
        print(f"  {animal.name}: {animal.diet()}")

    # 8. Health clamping demonstration
    print("\n--- 8. Health Clamping Demo ---")
    print(f"Lion health before: {lion.health}")
    lion.health = 150  # Should clamp to 100
    print(f"After setting 150: {lion.health}")
    lion.health = -10  # Should clamp to 0
    print(f"After setting -10: {lion.health}")

    # 9. Feeding schedule
    print("\n--- 9. Feeding Schedule Demo ---")
    schedule = FeedingSchedule("Monday")
    schedule.add_entry("Savanna", "09:00", "Hay and fruits", "Extra vitamins")
    schedule.add_entry("Aviary", "10:30", "Seeds and grains", "")
    schedule.add_entry("Pond", "11:00", "Fish", "Fresh catch")
    schedule.add_entry("Savanna", "15:00", "Grass", "")

    print(f"Schedule: {schedule}")
    print(f"Savanna feedings: {schedule.get_by_enclosure('Savanna')}")

    # 10. Employee polymorphism
    print("\n--- 10. Employee Demo ---")
    vet = Veterinarian("Dr. Smith", "exotic", 7000)
    guide = Guide("Maria", ["English", "Spanish", "French"], 3500)

    zoo.hire_employee(keeper)
    zoo.hire_employee(vet)
    zoo.hire_employee(guide)

    print("\nEmployee roles:")
    for emp in zoo._employees:
        print(f"  {emp.name}: {emp.role()}")
        print(f"    Work: {emp.work()}")

    # Vet treating animal
    print(f"\n{vet.treat_animal(lion)}")

    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()

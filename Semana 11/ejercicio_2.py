class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0


class Bus:
    max_passengers = 10

    def __init__(self):
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < Bus.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus")
        else:
            print("The bus is full, no more passengers can be added.")

    def remove_passenger(self, person):
        for passenger in self.passengers:
            if passenger.name.lower() == person.name.lower():
                self.passengers.remove(passenger)
                print(f"{person.name} got off the bus.")
                return

        print(f"{person.name} is not on the bus.")


person1 = Person("Carlos")
person2 = Person("Ana")
person3 = Person("Juan")

my_bus = Bus()

my_bus.add_passenger(person1)
my_bus.add_passenger(person2)
my_bus.add_passenger(person3)

# ? The commented code is just to test that the code works correctly.
# for i in range(7):
#     my_bus.add_passenger(Person(f"Passenger{i+4}"))

# my_bus.add_passenger(Person("Last"))

my_bus.remove_passenger(person1)

print([passenger.name for passenger in my_bus.passengers])

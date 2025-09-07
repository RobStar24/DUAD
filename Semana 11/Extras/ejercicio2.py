class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Guau"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Miau"


dog = Dog("Terry")
cat = Cat("Monino")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

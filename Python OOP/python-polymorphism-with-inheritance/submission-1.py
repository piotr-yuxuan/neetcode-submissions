from typing import override


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")


# TODO: Create the Dog and Cat classes with make_sound method
class Dog(Animal):
    @override
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    @override
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")

# TODO: Create a common interface that takes any object of type Animal (or its subclasses) and calls their make_sound method
def my_function(animal: Animal) -> None:
    animal.make_sound()

# Do not change the code below
my_function(Animal("Rabbit"))
my_function(Dog("Buddy"))
my_function(Cat("Whiskers"))

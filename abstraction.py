from abc import ABC, abstractmethod

# Abstract base class (parent class)
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method
    @abstractmethod
    def make_sound(self):
        pass

    # Regular method
    def show_info(self):
        return f"The {self.name} is an animal"

# Child class
class Dog(Animal):
    def __init__(self):
        super().__init__("dog")

    # Implementing the abstract method
    def make_sound(self):
        return "Woof!"

# Creating an object
dog_obj = Dog()

# Using methods from both parent and child classes
print(dog_obj.show_info())  # Output: The dog is an animal
print("Sound:", dog_obj.make_sound())  # Output: Sound: Woof!

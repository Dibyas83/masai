
"""
Abstract Base Classes (ABCs) in object-oriented programming can indeed contain concrete methods alongside abstract methods.
Concrete methods in an ABC are:
Fully implemented: Unlike abstract methods, which only declare a signature and require implementation in subclasses, concrete methods within an ABC have a complete implementation within the abstract class itself.
Inheritable: Subclasses that extend or implement the ABC automatically inherit these concrete methods. They can use them directly without needing to redefine them.
Overridable (with conditions): Subclasses can choose to override concrete methods inherited from an ABC to provide a specialized implementation, as long as the concrete method is not marked as final (or equivalent in the specific language).
Provide default behavior: Concrete methods in an ABC are often used to provide common or default functionality that many subclasses can utilize. This reduces code duplication and promotes reusability.
Why include concrete methods in an ABC?
Shared functionality: When multiple subclasses will share a common behavior, defining it as a concrete method in the ABC centralizes the logic and avoids redundant implementations.
Default implementations: Concrete methods can provide a sensible default implementation that subclasses can either accept or override if they need different behavior.
Template Method Pattern: Concrete methods in an ABC can be used in conjunction with abstract methods to implement the Template Method design pattern, where the ABC defines the overall algorithm (template) with some steps being concrete and others left to subclasses to implement.
Example (Python):
Python
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):  # Concrete method
        print("Moving...")

    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
dog.move()  # Uses concrete method from Animal
print(dog.make_sound())

cat = Cat()
cat.move()  # Uses concrete method from Animal
print(cat.make_sound())
# In this example, Animal is an ABC with a concrete method move() and an abstract method make_sound().
# Both Dog and Cat inherit the move() method and provide their specific implementation for make_sound().

"""
Python does not come with any abstract classes by default. Python has a module called ABC that serves 
as the foundation for building Abstract Base Classes (ABC). ABC works by decorating methods of the 
base class as abstract and then registering concrete classes as implementations of the abstract base. 
When a method is decorated with the keyword @abstractmethod, it becomes abstract.
  
An abstract class cannot be instantiated, can contain both abstract (unimplemented) and concrete 
(implemented) methods, and serves as a blueprint for other classes. In contrast, a concrete class 
can be instantiated to create objects, must have all its methods, including any inherited abstract 
methods, fully implemented, and is used to provide the actual functionality. 

Feature 	        Abstract Class	                         Concrete Class
Instantiation	Cannot be instantiated	                    Can be instantiated
Methods	   Can contain both abstract (unimplemented) 	 Must have all methods implemented; 
            and concrete (implemented) methods           contains only concrete methods
Keyword	    Declared with the abstract keyword	         Declared with the class keyword
Purpose	    Acts as a blueprint for other classes and 	 Provides a full, complete implementation and 
            is intended for inheritance                  is meant to be used directly
Inheritance	Can be inherited from but not used directly	    Can be used directly without further extension

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def refuel(self): # Concrete method in an abstract class
        print("Vehicle is being refueled.")

class Car(Vehicle):  # Concrete class inheriting from abstract class
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

# vehicle = Vehicle() # This would raise a TypeError as Vehicle is abstract
my_car = Car()
my_car.start_engine()
my_car.refuel()




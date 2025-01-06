class A:
    def greet(self):
        print("Hello from a")

class B(A):
    def greet(self):
        print("Hello from B")


obj = B()
print(obj.greet())


# a to do llist  - methods a class should have , but not how to implement them
# if a class says " i follow this interface" , it promises to have certain methods.
"""
python doesnt have a keyword interface . we use
- Abstract Base Class(ABC) to enforce that certain methods must be defined
- Duck Typing to accept any object that has the required methods

Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby,
 PHP, Javascript, etc. where the type or the class of an object is less important than the 
 method it defines. Using Duck Typing, we do not check types at all. Instead, we check for 
 the presence of a given method or attribute.

The name Duck Typing comes from the phrase:

“If it looks like a duck and quacks like a duck, it’s a duck”

Advantages of Duck Typing

Flexibility and Polymorphism: Duck typing promotes flexible code where functions can operate on
 objects based on their behavior rather than their specific type, facilitating polymorphism and code reuse.
Simplified Code: Duck typing eliminates the need for explicit type checks, resulting in cleaner,
 more concise code that is easier to read and maintain.
Enhanced Reusability: Functions designed with duck typing can be reused across different parts of the
 codebase, reducing duplication and improving overall code quality.
 
Disadvantages of Duck Typing

Runtime Errors: Duck typing may lead to runtime errors if an object passed to a function does not implement the 
expected methods, which can be harder to detect and debug.
Difficulty in Understanding External Code: Understanding the expected behavior of objects in external code 
without proper documentation or type annotations can be challenging, requiring trial and error or external resources.

To get the MRO of a class, you can use either the __mro__ attribute or the mro() method. The __mro__ attribute 
returns a tuple, but the mro() method returns a python list.
"""


class Dog:
    def sound(self):
        print("Bark")

    def move(self):
        print("Run")


class Cat:
    def sound(self):
        print("Meow")

    def move(self):
        print("Jump")


def animal_actions(animal):
    animal.sound()
    animal.move()


dog = Dog()
cat = Cat()

animal_actions(dog)
animal_actions(cat)
print("=============================super")
"""
The super() function is used to give access to methods and properties of a parent or sibling class.

The super() function returns an object that represents the parent class.
"""
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

print("--------------------------------------")
from abc import ABC,abstractmethod


class printable(ABC):
    @abstractmethod
    def print_data(self):
        pass


class Report(printable):
    def print_data(self):
        print("sales data")


r =Report()
print(r.print_data())

print("-------------------------------------")

class Printer:
    def print_data(self):
        print("print doc")


def use_printable(obj):
    obj.print_data()

p = Printer()
use_printable(p)

# multiple inheritance
"""
a child class inherits from a single parent class
when inherts from multi class -multiple inheritence
"""
#class ChildClass(Parentclass1,Parentclass2):
# order decides what is used
class Engine:
    def start(self):
        print("start")


class Radio:
    def start(self):
        print("play")


class Car(Engine,Radio): # engine written first
    pass


c = Car()
c.start()


# Early vs Late Binding
"""
early - deciding which method to call at compile-time(in static languages)
late - deciding which method to call at runtime(pythons way).this provides flexibility but error also appear at
runtime if methods dont exist.
The main advantage to early binding is efficiency. Because all information necessary to call a function is 
determined at compile time,these types of function calls are very fast. The opposite of early binding is 
late binding. Late binding refers to function calls that are not resolved until run time

Early binding refers to assignment of values to variables during design time whereas 
late binding refers to assignment of values to variables during run time.

Early-bound objects are significantly faster than late-bound objects and make your code easier to read 
and maintain by stating exactly what kind of objects are being used.


Flexibility: Late binding allows for more flexible code, enabling polymorphism and dynamic method resolution.
 Code Reusability: It facilitates writing reusable and extensible code through inheritance and polymorphism
"""
class Bird:
    def fly(self):
        print("Bird flying")

class Airplane:
    def fly(self):
        print("plane flying")

class fish:
    def swim(self):
        print("fish swiming")

# a function that uses duck typing
def let_fly(obj): # done for object
    obj.fly()

bird = Bird()
plane = Airplane()
let_fly(bird)
let_fly(plane)
# let_fly(fish) fish doesnot have a fly method



class Engine:
    def start_engine(self):
        print("start")


class Wheels:
    def start_wheels(self):
        print("rollig")


class Car(Engine,Wheels):  # engine written first
    def drive(self):
        print('car is driving')


c = Car()
c.start_engine()
c.start_wheels()
c.drive()

print("------------------------[[[[[[[[[[[[[[[[")
class Engine:
    def start(self):
        print("start")


class Wheels:
    def start(self):
        print("rollig")


class Car(Engine,Wheels):  # engine written first
    def start(self):
        print('car is driving')


c = Car()
print(c.start())

print("========================")
class Engine:
    def start(self):
        print("start")


class Wheels:
    def start(self):
        print("rollig")


class Car(Engine,Wheels):  # engine written first
    pass


c = Car()
print(c.start())

# Python program to demonstrate
# duck typing



class Specialstring:

    def __len__(self):
        return 21


# Driver's code
if __name__ == "__main__":
    string = Specialstring()
    print(len(string))

print("=========================---------------------")
class Engine:
    def start(self):
        print("start")


class Wheels(Engine):
    pass


class Car(Wheels):  # engine written first
    def flying(self):
        print("flying")


c = Car()
c.start()
c.flying()



class Logger:
    def log(self, message):
        print(f"Log: {message}")

class AdvancedLogger(Logger):
    def log(self, message):
        super().log(message)
        print(f"Advanced Log: {message}")

logger = AdvancedLogger()
logger.log("System error")




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        super().__init__(name, salary)  # This calls the parent class __init__

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")













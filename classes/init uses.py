

"""
The purpose of the __init__ method is to allow the class to set initial values for the attributes
of an object when it is first created. This method takes the “self” parameter, which refers to
the instance being created, and any additional parameters the class needs to set initial values
for the object's attributes

In Python classes, __init__ (the constructor) is used to initialize an object's attributes when it's
created. It's essential when you need to set initial values for an object's properties based on
arguments passed during object creation. If you don't need to initialize attributes or want to use
default values, you can omit the __init__ method.

When to use __init__:
Initialization of attributes:
Use __init__ to assign initial values to object attributes (instance variables) when a new object is
created.
Object creation with arguments:
When you need to pass data to the class during instantiation, __init__ allows you to define the parameters
that are accepted and used to set initial attribute values.

Setting default values:
You can use __init__ to assign default values to attributes if no arguments are provided during object
creation.

When not to use __init__:

Simple classes with no initial state:
If your class is very simple and doesn't require any initialization logic when an object is created, you
can omit __init__.

Classes that rely on other methods for initialization:
If the initialization of an object's attributes is handled by other methods within the class, you might
choose not to include __init__.

Class is just a container:
If your class acts primarily as a container for data or other objects, and you don't need to perform any
specific initialization actions during object creation, you can omit __init__.
Example:
Python
"""
from typing import Self

class Dog:
    def __init__(self, name, breed) -> None: # b constructor by default it always returns none
        self.name = name # attribute
        self.breed = breed

    def bark(self) -> None: # method
        print(f" {self.name} is Woofing!")  # self refers to instances of class.to refer to the instance values use self

    def get_info(self, v: int) -> None:
        print(v)
        print(f'{self.name} is a {self.breed}')

    def __str__(self) -> str: # str dunda method inbuilt - this will not show address in print(dog1)
        return f'{self.breed},{self.name}'

    def __add__(self,other: Self) -> str: # add dunda method inbuilt - this will not show address in print(dog1)
        return f'{self.breed} & {other.breed}'


dog1 = Dog("Buddy", "Golden Retriever") #attributes. Creating an object(dog1) with init
dog2: Dog = Dog("Bud", "Dogesh_Bhai") # Creating an object(dog2) with init
print(dog1.name) # output: Buddy
print(dog1.breed) # output: Golden Retriever
dog2.get_info(5)
print(dog1) # dunda method
print(dog1 + dog2)
"""
In this example, __init__ is used to initialize the name and breed attributes of a Dog object when a new 
Dog object is created using the Dog("Buddy", "Golden Retriever") line. 

"""











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
class Dog:
    def __init__(self, name, breed): # constructor
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

dog1 = Dog("Buddy", "Golden Retriever") # Creating an object with init
print(dog1.name) # output: Buddy
print(dog1.breed) # output: Golden Retriever
"""
In this example, __init__ is used to initialize the name and breed attributes of a Dog object when a new 
Dog object is created using the Dog("Buddy", "Golden Retriever") line. 

"""









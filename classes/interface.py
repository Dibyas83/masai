

"""
What is an Interface in Python?
The interface in object-oriented languages like Python is a set of method signatures that the implementing class is expected to provide. Writing ordered code and achieving abstraction are both possible through interface implementation.

Example:

Python "object interfaces" are implemented in the module zope.interface.  It is maintained by the Zope Toolkit project. Two objects, "Interface" and "Attribute," are directly exported by the package. Several helper methods are also exported by it. Compared to Python's built-in abc module, it strives to give stronger semantics and better error messages.

Declaring interface: In Python, an interface is defined using Python class statements and is a subclass of interface.Interface which is the parent interface for all interfaces.

pip install zope.interface
"""
import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("foo")
    def method1(self, x):
        pass
    def method2(self):
        pass

print(type(MyInterface))
print(MyInterface.__module__)
print(MyInterface.__name__)

# get attribute
x = MyInterface['x']
print(x)
print(type(x))
"""

An abstract
Implementing interface: The interface acts as a blueprint for designing classes, so interfaces are implemented using the implementer decorator on the class. If a class implements an interface, then the instances of the class provide the interface. Objects can provide interfaces directly, in addition to what their classes implement.

"""



import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("foo")
    def method1(self, x):
        pass
    def method2(self):
        pass

@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return x**2
    def method2(self):
        return "foo"

obj1 = MyClass()

print(obj1.method1(5))
print(obj1.method2())


#We declared that MyClass implements MyInterface. This means that instances of MyClass provide MyInterface.

"""










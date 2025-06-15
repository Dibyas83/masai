

"""
Bro code

object = bundle of related attributes (variables) and methods(functions)
ex - phone,book
we need class(blueprint) to  design the struture and layout of an objects or objects

to create car object we need
to contruct a car object we need a special type of method called constructor it works like a function


"""
from matplotlib.pyplot import title
from matplotlib.style.core import library
from networkx.algorithms.distance_measures import radius

from car import Car  # imported from another file car, with class Car

# init is the function . self means this object we are creating or current or myself-this is constructor method
# model,color  are some attributes a car should have.to assign these attributes we use self
# we need this method to construct objects
car1 = Car("mustang",2024,"red",False)
car2 = Car("must",2025,"white",True)
print(car1) #this will give address of the object
print(car1.year) # will give the attribute  which was given as input
print(car2.color)

car1.drive()
car2.stop()
car2.describe()
print(car2.wheels)
print(Car.wheels) # wheels is a property all objects have ,all objects donit have the same property that are defined
print(Car.noof_cars,"nos")


#--------------------------











# inheritance and late binding
class A:

    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def greet(self):
        print("hello")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class B(A):
    def greet(self):
        print("hello from b")
    def sleep(self):
        print(f"{self.name} is stand sleeping")

class C(A):
    def greet(self):
        print("hello from c")

class Q(A):
    pass

class D(B,C,A):
    pass
c = C("cat")
d =D("gar")
d.greet()
q = Q("scooby")
print(d.name,q.name)
print(d.is_alive,d.sleep(),q.sleep(),"p")
print(c.sleep(),"c")
print(c.eat(),"c")
print(q.sleep(),q.eat())
print(q.eat())
b = B("horse")
b.sleep()
"""
<car.Car object at 0x0000026802266900>
2024
white
car mustang is running
must has stopped
2025 white must
4
4
2 nos
hello from b
gar scooby
gar is stand sleeping
scooby is sleeping
True None None p
cat is sleeping
None c
cat is eating
None c
scooby is sleeping
scooby is eating
None None          - when inherited as this method is not its own
scooby is eating
None
horse is stand sleeping
"""

class Animal:
    def __init__(self,name1):
        self.name = name1
    def beathes(self):
        print(f" {self.name} breathes co2 out")

class Prey(Animal):
    def flee(self):
        print(f" {self.name} is fleeing")

class Predator(Animal):
    def hunting(self):
        print(f"{self.name} is  stalking")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabit("peter")
hawk = Hawk("raptor")
fish = Fish("nemo")

rabbit.flee()
hawk.hunting()
fish.hunting()
fish.beathes()




"""

# Abstract class: - a class that cant be instantiated on its own; meant to be subclassed.
they can contain abstract methods, which are declared but have no implementation
benefits - 1 prevents Instantiation of the class itself
           2 requires children to use inherited abstract methods
"""
from abc import ABC,abstractmethod

class Vehicle(ABC):  # I DONT ANY BODY TO MAKE a vehicle object so made this an abstract class and add
    #some abstract method which will be inherited by its children to declar an abstract method we need decoarator
    @abstractmethod
    def go(self):
        pass     # will be defined in children classes
    @abstractmethod
    def stop(self):
        pass

class Cars(Vehicle):  # need to include all abstract methods no pass
    def go(self):
        print("drive")

    def stop(self):
        print("brake")

class Boat(Vehicle):
    def go(self):
        print(" sail ")

    def stop(self):
        print("anchored") # both methods to be defined one missed will not work


# vehicl = Vehicle()  - Can't instantiate abstract class Vehicle without an implementation
# for abstract methods 'go', 'stop'
ford = Cars()
ford.go()
ford.stop()

#-----------------------------------
# super() = function used in a child class(subclass) to call methods from a parent class(superclass).
# Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self,color,is_filled):  # common attributes
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)  # called the constructer of superclass
        self.radius = radius

    def area(self):
        print(f"{3.14 * self.radius ** 2} is the areaa")

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"{self.width ** 2} is the areaa")

class Triangle(Shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color,is_filled)
        super().describe()
        self.height = height
        self.width = width

circ = Circle("red",True,10)
sq = Square("red",False,11)
tria = Triangle("blue",True,10,8)
print(circ.color)
#print(circ.filled)
print(tria.is_filled)
circ.describe()
circ.area()
sq.describe()



class Interface(ABC): # bikr
    @abstractmethod
    def action(self):  # no handle defined
        pass

class PartialImplementation(Interface): # inheriting
    #pass          wouldnt work
    def action(self):
        print("install at top")
    #Intentionally not implementing 'action' not defined

obj = PartialImplementation() # Can't instantiate abstract class PartialImplementation without an implementation for abstract method 'action'
obj.action()

"""
polymerphism = to have many forms or faces
ways to achieve polymorphism
1 inheritance = an object could be treated of the same type as a parent class
2 "Duck typing" = object must have necessary attributes/methods
"""
from abc import ABC

class Shape1:

    @abstractmethod
    def area1(self):
        pass

class Circle1(Shape1):
    def __init__(self,rad):
        self.rad = rad

    def area1(self):
        return 3.14 * self.rad ** 2

class Square1(Shape1):

    def __init__(self,side):
        self.side = side

    def area1(self):
        return self.side ** 2

class Triangle1(Shape1):
    def __init__(self, base, height):
        self.height = height
        self.base = base

    def area1(self):
        return self.base * self.height * 0.5

class Pizza(Circle1):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.top = topping

shapes = [Circle1(4),Square1(6),Triangle1(11,6),Pizza("cheesse",12)] # objects in list.circle is a circle and shape - two forms
for shape in shapes:
    print(f"{shape.area1()} cm") # cir.ar > sq.ar > tr.ar

"""
duck typing - object must have the min necessary attributes/methods
"if it looks like a duck quacks like a duck ,it must be a duck" 
"""
class Animals:
    alive = True

class Dog(Animals):
    def speak(self):
        print("woof woof")

class Cat(Animals):
    def speak(self):
        print("meow")

class Carr:
    alive = False
    def speak(self):
        print("hunk")

anime = [Cat(),Dog(),Carr()]
for ani in anime:
    ani.speak()

"""
agression = represents a relationship where one object( contaINer the whole) contain
references to one or more independent objects (the parts)  - like renting
"""
class Library:
    def __init__(self,names):
        self.names = names
        self.books = []

    def add_books(self,book):
        self.books.append(book)

    def list_books(self):
        return (f"{book.title} by {book.author}" for book in self.books)

class Books:
    def __init__(self,title,author):
        self.title = title
        self.author = author
# library and book exist without each other

library = Library("new york public library")
book1 =Books("magic","pc")
book2 = Books("magical adv","jk")
book3 = Books("hsrry","rowlings")
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(library.names)

for booky in library.list_books():
    print(booky)
#composition = the composed objects directly owns its components,which cannot exist
# independently "owns a" relationship - like owning

class Engine:
    def __init__(self,hp):
        self.hp = hp


class Wheel:
    def __init__(self, size):
        self.size = size

class Carrr: # composed object - within car class we will construct engine and wheel
    def __init__(self,make,model,hp,wh_size):
        self.make = make
        self.model = model
        self.engine = Engine(hp)
        self.wheels = [Wheel(wh_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.hp}(hp) {self.wheels[0].size} in"

caar1 = Carrr("ford","mustang",500,18)
caar2 = Carrr("asss","hole",2000,20)
print(caar1.display_car())
print(caar2.display_car())

# nested - allows you to logically group classes that are closely related
# Encapsultes private details that arnt relevant  outside of the outer class
# keeps the namespace clean; reduces the possibility of naming conflicts
class Company:
    class Employee:
        print("first")

class Non_profit:
    class Employee:
        print("second")

#----------------
class Company:

    class Employee:
        def __init__(self,name,position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self,company_name):
        self.compname = company_name
        self.employees = []

    def add_emp(self,name,position):
        new_employee= self.Employee(name,position)
        self.employees.append(new_employee)

    def listemp(self):
        return  [emp.get_details() for emp in self.employees]

comp1 = Company(" itt ")
comp2 = Company(" ittss ")
print(comp1.compname)
comp1.add_emp("eugene","manager")
comp1.add_emp("hgjghj","ghgd")
comp2.add_emp("jghj","gh")
comp2.add_emp("jghkkk","ghhhh")
#print(comp.listemp())
for emps in comp1.listemp():
    print(emps)
for emps in comp2.listemp():
    print(emps)

#static methods - a method that that belong to class rather any object from that class(instance)
# usually used for general utility functions ,that do not need  access to class data

# instance method = best for operations on instances of class(objects)

class Employeee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}" # this is instance each object created using this class will get their own getinfo method


    @staticmethod
    def isvalid_position(position): # no self we are not working with any abject created from this class
        validpositions = ["manager","cashyer","cook"]
        return  position in validpositions # boolean checks if pos in validpos
emp1 = Employeee("yruryurtu","rtr")
print(Employeee.isvalid_position("fightr")) # no need of object ,directly accessed through class
print(emp1.get_info()) # acessed through object emp1 of class

# class methods = uses cls,besst for class-level dtaa or requires acess to the class it self

class Student:
    count = 0 # class variable
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # when create student object we acces class of student take count variable aND inc
        Student.total_gpa += gpa

    def getinfo(self): # instance meethod
        return f"{self.name} {self.gpa}"

    @classmethod
    def getcount(cls):
        return f" total no of students:{cls.count}"

    @classmethod
    def getavgpa(cls):
        return f" {cls.total_gpa / cls.count} "

stud1 = Student("spongbob",3.2)
stud2 = Student("mickey",4)
stud3 = Student("mouse",2)
# these all will be processed

print(Student.getcount())
print(Student.getavgpa())

# magic methods or dunder method - they are automatically called by many pythons built in operations.they
# allow developers to define or customize the behaviour of objects

class Bookks:
    def __init__(self,title,auth,pages):
        self.title = title
        self.auth = auth
        self.pages = pages

    def __str__(self): # istead of returning  mem addres ,a string representation of object will be
        # printed when we print directly to the consol
        return f"{self.title} by {self.auth}"

    def __eq__(self, other):
        return self.title == other.title and self.auth == other.auth

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return f"{self.pages + other.pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.auth

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "auth":
            return self.auth
        elif key == "pages":
            return  self.pages
        else:
            return f"key '{key}' was not found" # key is audio



book1 = Bookks("the hobbit","tolkien",310)
book2 = Bookks("the Ring","dayan",3100)
books = Bookks("the lion,the wwitch and wardrobe","disney",500)
print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
# print(book1['title']) use getitems
print(book1['pages'])

# property - decorator used to define a method as a property(it can be accesed like an attribute)
# add aditional logic when read, write,or delete attributes
# gives getter(read),setter(write) and deleter method

class Rectanglee:
    def __init__(self,width,height):
        self._width = width # making it private so that not acess these objects outside of class
        self._height = height
    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter   # set or write the new width to create a logic
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("must be greater than 0")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle = Rectanglee(3.1345,4.1244)

rectangle.width = 5
rectangle.height = -4

print(rectangle._width)
print(rectangle.width)
print(rectangle._height)
print(rectangle.height)
# to delete attribute

del rectangle.width
del rectangle.height






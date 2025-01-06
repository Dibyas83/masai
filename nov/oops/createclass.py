"""
Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

"""
class MyClass:
  x = 5
  """

Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:
  """

p1 = MyClass()
print(p1.x)

"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary
 to do when the object is being created:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"""
The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

Example
The string representation of an object WITHOUT the __str__() function:
"""
print("------------------------------10")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)

print("--------------------------------------11")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

"""
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:
Note: The self parameter is a reference to the current instance of the class, and is used
to access variables that belong to the class.


"""
print("------------------------------------77")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc1(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc1()


class Ether:

  def __init__(self,contains,size):
    self.contains = contains
    self.size = size

  def space(self):
    print("nothing but vaccum and ",self.contains,self.size)


class Sky(Person):
  def speak(self):
    print("fly")


class Road(Person):
  def fly(self):
    print("with planes")


err = Ether("vaccum","everywhere")
err.space()





print("---------------------------------------22")
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc2(abd):
    print("Hello my name is " + abd.name)

p1 = Person("John", 36)
p1.myfunc2()
p1.age = 40
del p1.age
del p1

"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""
print("--------------------------------------45")
class Person2:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
# Use the Person class to create an object, and then execute the printname method:
# Add a property called graduationyear to the Student class:
"""
In the example below, the year 2019 should be a variable, and passed into the Student
class when creating student objects. To do so, add another parameter in the __init__() function:
"""
class Student(Person2):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year
    #Person2.__init__(self, fname, lname)
# Add a method called welcome to the Student class:
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
  def wel(self):
    print("welcom",self.firstname,"to junle" )

x2 = Student("Mike", "Olsen",2019)
w1 = Person2("rohit","saluja")
w1.printname()
x2.printname()
x2.welcome()
x2.wel()
# Use the Student class to create an object, and then execute the printname method:
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
"""
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
By using the super() function, you do not have to use the name of the parent element, it will automatically 
inherit the methods and properties from its parent.

"""












"""
Each object is an instance of a class. Each class presents to the outside
world a concise and consistent view of the objects that are instances of this class

The class definition typically specifies instance variables,
also known as data members, that the object contains, as well as the methods, also
known as member functions, that the object can execute

the organized architect designing a house or apartment will view them as
separate modules that interact in well-defined ways. In so doing, he or she is using
modularity to bring a clarity of thought that provides a natural way of organizing
functions into distinct manageable units.
Python’s standard
libraries include, for example, the math module, which provides definitions for key
mathematical constants and functions, and the os module, which provides support
for interacting with the operating system

If software modules are written in a general way, the modules
can be reused when related need arises in other contexts. This is particularly rel￾evant in a study of data
structures, which can typically be designed with sufficient
abstraction and generality to be reused in many applications.

abstraction is to distill a complicated system down to its most funda￾mental parts. describing the parts of
a system involves naming them and
explaining their functionality. Applying the abstraction paradigm to the design of
data structures gives rise to abstract data types (ADTs). An ADT is a mathematical
model of a data structure that specifies the type of data stored, the operations sup￾ported on them, and the
 types of parameters of the operations. An ADT specifies
what each operation does, but not how it does it. We will typically refer to the
collective set of behaviors supported by an ADT as its public interface

 Python has a tradition of treating abstractions
implicitly using a mechanism known as /duck typing/. As an interpreted and dy￾namically typed language,
there is no “compile time” checking of data types in
Python, and no formal requirement for declarations of abstract base classes. In￾stead programmers assume
that an object supports a set of known behaviors, with
the interpreter raising a run-time error if those assumptions fail

Python supports abstract data types using a mechanism known
as an abstract base class (ABC). An abstract base class cannot be instantiated
(i.e., you cannot directly create an instance of that class), but it defines one or more
common methods that all implementations of the abstraction must have. An ABC
is realized by one or more concrete classes that inherit from the abstract base class
while providing implementations for those method declared by the ABC
Python’s abc module provides formal support for ABCs, although we omit such declarations for simplicity

Encapsulation yields robustness
and adaptability, for it allows the implementation details of parts of a program to
change without adversely affecting other parts, thereby making it easier to fix bugs
or add new functionality with relatively local changes to a component

Throughout this book, we will adhere to the principle of encapsulation, making
clear which aspects of a data structure are assumed to be public and which are
assumed to be internal details. With that said, Python provides only loose support
for encapsulation. By convention, names of members of a class (both data members
and member functions) that start with a single underscore character (e.g., secret)
are assumed to be nonpublic and should not be relied upon

-----------
Traditional software development involves several phases. Three major steps are:
1. Design
2. Implementation
3. Testing and Debugging
In this section, we briefly discuss the role of these phases, and we introduce sev￾eral good practices for
 programming in Python, including coding style, naming
conventions, formal documentation, and unit testing

there are some rules of thumb that we can apply when determining how to design our classes:

• Responsibilities: Divide the work into different actors, each with a different
responsibility. Try to describe responsibilities using action verbs. These
actors will form the classes for the program.
• Independence: Define the work for each class to be as independent from
other classes as possible. Subdivide responsibilities between classes so that
each class has autonomy over some aspect of the program. Give data (as in￾stance variables) to the class that
 has jurisdiction over the actions that require
access to this data.
• Behaviors: Define the behaviors for each class carefully and precisely, so
that the consequences of each action performed by a class will be well un￾derstood by other classes that
interact with it. These behaviors will define
the methods that this class performs, and the set of behaviors for a class are
the interface to the class, as these form the means for other pieces of code to
interact with objects from the class.

 Class-Responsibility-Collaborator (CRC) cards are simple in￾dex cards that subdivide the work required of a
 program. The main idea behind this
tool is to have each card represent a component, which will ultimately become a
class in the program

a standard approach to explain and document the
design is the use of UML (Unified Modeling Language) diagrams to express the
organization of a program. UML diagrams are a standard visual notation to express
object-oriented software designs. Several computer-aided tools are available to
build UML diagrams. One type of UML figure is known as a class diagram.

The diagram has three portions, with the first designating
the name of the class, the second designating the recommended instance variables,
and the third designating the recommended methods of the cl

“CamelCase” convention
in which the first letter of each word is capitalized (e.g., CreditCard)
If multiple words are combined, they should be separated by under￾scores (e.g., make payment). The name of
a function should typically
be a verb that describes its affect.

Python provides integrated support for embedding formal documentation directly
in source code using a mechanism known as a /docstring/

ef scale(data, factor):
”””Multiply all entries of numeric data list by the given factor.”””
for j in range(len(data)):
data[j] = factor
----------------------------
Testing
At the very minimum, we should make sure that every method of a class is tested at least once
(method coverage). Even better, each code statement in the program should be
executed at least once (statement coverage).
Programs often tend to fail on special cases of the input. Such cases need to be
carefully identified and tested. For example, when testing a method that sorts (that
is, puts in order) a sequence of integers, we should consider the following inputs:
• The sequence has zero length (no elements).
• The sequence has one element.
• All the elements of the sequence are the same.
• The sequence is already sorted.
• The sequence is reverse sorted

Bottom-up testing proceeds from lower-level components to higher-level com￾ponents. For example,
bottom-level functions, which do not invoke other functions,
are tested first, followed by functions that call only bottom-level functions, and so
on. Similarly a class that does not depend upon any other classes can be tested
before another class that depends on the former. This form of testing is usually
described as /unit testing/, as the functionality of a specific component is tested in
isolation of the larger software projec

----------------------------------------------

In Python,- every piece of data is represented as an instance of some class.
A class provides a set of behaviors in the form of member functions (also known
as methods), with implementations that are common to all instances of that class.
A class also serves as a blueprint for its instances, effectively determining the way
that state information for each instance is represented in the form of attributes (also
known as fields, instance variables, or data members)

The
body includes definitions for all methods of the class. These methods are defined as
functions, using techniques introduced in Section 1.5, yet with a special parameter,
named self, that serves to identify the particular instance upon which a member is
invoked
assume that a user of our class has a variable, my card, that identifies
an instance of the CreditCard class. When the user calls my card.get balance( ),
identifier self, within the definition of the get balance method, refers to the card
known as my card by the caller. The expression, self. balance refers to an instance
variable, named balance, stored as part of that particular credit card’s state

"""
import collections

from pygame.examples.video import answer

"""
# A consumer credit card.
Create a new credit card instance.
The initial balance is zero.
customer the name of the customer (e.g., John Bowman )
bank the name of the bank (e.g., California Savings )
acnt the acount identifier (e.g., 5391 0375 9387 5309 )
limit credit limit (measured in dollars)
"""
class CreditCard:

    def __init__ (self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
#”””Return name of the customer.”””
        return self._customer
    def get_bank(self):
#”””Return the bank s name.”””
        return self._bank
    def get_account(self):
#”””Return the card identifying number (typically stored as a string).”””
        return self._account
    def get_limit(self):
#”””Return current credit limit.”””
        return self._limit
    def get_balance(self):
#   ”””Return current balance.”””
        return self._balance

class Definitions:
    def charge(self, price):
#”””Charge given price to the card, assuming sufficient credit limit.
#return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
#”””Process customer payment that reduces balance.”””
        self._balance -= amount

"""
The
charge function typically adds the given price to the credit card balance, to reflect
a purchase of said price by the customer. However, before accepting the charge,
our implementation verifies that the new purchase would not cause the balance to
exceed the credit limit. The make payment charge reflects the customer sending
payment to the bank for the given amount, thereby reducing the balance on the
card.

Internally, this results in a call to the specially named init method that serves
as the constructor of the class. Its primary responsibility is to establish the state of
a newly created credit card object with appropriate instance variables. In the case
of the CreditCard class, each object maintains five instance variables, which we
name: customer, bank, account, limit, and balance. The initial values for the
first four of those five are provided as explicit parameters that are sent by the user
when instantiating the credit card, and assigned within the body of the construc￾tor. For example, the command
self. customer = customer, assigns the instance variable self. customer to the parameter customer; note that
 because customer is unqualified on the right-hand side, it refers to the parameter in the local namespace.

 _balance, implies that it is intended as nonpublic.
Users of a class should not directly access such members

"""

if __name__ == '__main__ ':
    wallet = []
    wallet.append(CreditCard( 'John Bowman ', 'California Savin' ,'5391 0375 9387', 2500))
    wallet.append(CreditCard( 'John Bowman ', 'California Feder' ,'3485 0399 3395', 3500))
    wallet.append(CreditCard( 'John Bowman' , 'California Finae' ,'5391 0375 9387', 5000))
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3 *val)
    for c in range(3):
        print( 'Customer =' ,wallet[c].get_customer( ))
        print( 'Bank =' , wallet[c].get_bank( ))
        print( 'Account = ', wallet[c].get_account( ))
        print( 'Limit = ', wallet[c].get_limit( ))
        print( 'Balance = ', wallet[c].get_balance( ))
        while wallet[c].get_balance( ) > 100:
            wallet[c].make_payment(100)
            print( 'New_balance = ', wallet[c].get_balance( ))
            print( )

"""
Operator Overloading and Python’s Special Methods

syntax a+b invokes addition for numeric types, yet concatenation for
sequence types.
he author
of a class may provide a definition using a technique known as operator overload￾ing. This is done by 
implementing a specially named method. In particular, the + operator is overloaded by implementing a
method named add , which takes the right-hand operand as a parameter and which returns the result of the
expres￾sion. That is, the syntax, a+b, is converted to a method call on object a of the form, a. --add--(b)

overloading and overriding

Here is the information about overloading and overriding in Python:
Overloading
Definition: Overloading refers to the ability to have multiple methods with the same name but different 
parameters within the same class. This allows a single method name to be used for various operations.
Python's Approach: Python does not directly support method overloading in the traditional sense. Instead, 
it uses techniques like default arguments, variable-length arguments (*args, **kwargs), and decorators like
 @singledispatch to achieve similar behavior.
 
There are two main types of overloading in Python:
1. Method Overloading:
Concept:
Method overloading allows you to define multiple methods within the same class that share the same name but have
 different parameter lists (different number of parameters, different types of parameters).
Python's Approach:
Python doesn't support method overloading in the same way as languages like Java or C++. In Python, if you define
 multiple methods with the same name in a class, the last one defined will overwrite the previous ones.
Achieving Overloading:
You can achieve similar effects using:
Default arguments: You can provide default values for some parameters, allowing the method to be called with 
different numbers of arguments.*args and **kwargs:** You can use variable-length argument lists (*args for 
positional arguments and **kwargs for keyword arguments) to handle different numbers of inputs.

@overload decorator: From the typing module, this decorator allows you to provide type hints for different 
method signatures, although the implementation must still handle multiple types.
multipledispatch library: This library provides a way to dispatch function calls based on the types of arguments
 passed, effectively enabling method overloading.
2. Operator Overloading:
Concept:
Operator overloading allows you to define how standard operators (like +, -, *, /, ==, etc.) behave when applied
 to objects of your custom classes.
Python's Approach:
You achieve operator overloading by implementing special methods (also known as "magic methods" or "dunder 
methods") in your class.
Examples:
To overload the + operator, you define the __add__ method.
To overload the == operator, you define the __eq__ method.
To overload the indexing operator [], you define the __getitem__ and __setitem__ methods.
Use Cases:
Operator overloading is useful for creating custom data types that behave intuitively with standard operators,
 such as vectors, matrices, or custom numerical types.
Key Takeaways:
Python doesn't have traditional method overloading like some other languages.
You can achieve similar behavior using default arguments, variable-length argument lists, type hinting with
 overload, or libraries like multipledispatch.
Operator overloading allows you to customize the behavior of standard operators for your custom classes t
hrough special methods
Examples: 
Python

    # Using default arguments
    def add(a, b, c=0):
        return a + b + c

    # Using *args
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    # Using @singledispatch
    from functools import singledispatch

    @singledispatch
    def greet(name):
        return f"Hello, {name}!"

    @greet.register(int)
    def _(name):
        return f"Number: {name}"
Overriding
Definition: Overriding occurs when a subclass provides a specific implementation for a method that is already 
defined in its superclass. The subclass's method replaces the method of the same name in the superclass, allowing
 for customized behavior.
Mechanism: Python fully supports method overriding, which is a key aspect of inheritance and polymorphism.
Example: 
Python

    class Animal:
        def speak(self):
            print("Generic animal sound")

    class Dog(Animal):
        def speak(self):
            print("Woof!")

    animal = Animal()
    dog = Dog()

    animal.speak()  # Output: Generic animal sound
    dog.speak()     # Output: Woof!
Key Differences
Overloading: allows multiple methods with the same name but different parameters within the same class. 
Overriding: allows a subclass to redefine a method from its superclass, changing its behavior. 
Python uses techniques like default arguments and *args/**kwargs to mimic overloading, while it fully 
supports overriding. 
In summary: Overloading and overriding are essential concepts in object-oriented programming that improve 
code adaptability. Python's approach to overloading is different from other languages, but it achieves similar
results using alternative mechanisms. 

"""
def add(datatype, *args):
    # if datatype is int initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str initialize answer as ''
    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

"""

Python | Method Overloading
Last Updated : 12 Sep, 2024
Method Overloading:

Two or more methods have the same name but different numbers of parameters or different types of parameters,
 or both. These methods are called overloaded methods and this is called method overloading. 

Like other languages (for example, method overloading in C++) do, python does not support method overloading 
by default. But there are different ways to achieve method overloading in Python. 

The problem with method overloading in Python is that we may overload the methods but can only use the latest
 defined method. 


# First product method.
# Takes two argument and print their
# product
​
​
def product(a, b):
    p = a * b
    print(p)
​
# Second product method
# Takes three argument and print their
# product
​
​
def product(a, b, c):
    p = a * b*c
    print(p)
​
# Uncommenting the below line shows an error
# product(4, 5)
​
​
# This line will call the second product method
product(4, 5, 5)

Output
100
In the above code, we have defined two product methods we can only use the second product method, as python 
does not support method overloading. We may define many methods of the same name and different arguments, but
we can only use the latest defined method. Calling the other method will produce an error. Like here calling
product(4,5) will produce an error as the latest defined product method takes three arguments.

Thus, to overcome the above problem we can use different ways to achieve the method overloading.

Method 1 (Not The Most Efficient Method):


We can use the arguments to make the same function work differently i.e. as per the arguments.




# Function to take multiple arguments
def add(datatype, *args):
​
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0
​
    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''
​
    # Traverse through the arguments
    for x in args:
​
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x
​
    print(answer)
​
​
# Integer
add('int', 5, 6)
​
# String
add('str', 'Hi ', 'Geeks')

Output
11
Hi Geeks
Method 2 (Not the efficient one):

We can achieve method overloading in python by user defined function using "None" keyword as default parameter.

Code explanation:

The first parameter of  "add" method is set to None. This will give us the option to call it with or without
 a parameter.

When we pass arguments to the add method (Working):

The method checks if both the parameters are available or not. 
As we have already given default parameter values as "None", if any of the value is not passed it will remain
 "None".Using If-Else statements, we can achieve method overloading by checking each parameter as single statement.



# code
def add(a=None, b=None):
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a+b)
​
​
# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)

Output
5
2
The problem with above methods is that, it makes code more complex with multiple if/else statement and is 
not the desired way to achieve the method overloading.

Method 3 (Efficient One):

By Using Multiple Dispatch Decorator 

Multiple Dispatch Decorator Can be installed by: 

pip3 install multipledispatch
If pip is not installed on your device:

Click here for "Windows"

Click here for "Linux"


from multipledispatch import dispatch

# passing one parameter


@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(2, 3)  # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
Output: 

6
12
17.985999999999997
In Backend, Dispatcher creates an object which stores different implementation and on runtime, it selects
 the appropriate method as the type and number of parameters passed.

Example of Overriding:
class Parent:
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        print("Inside Child")

c = Child()
c.show()  # Output: Inside Child
Overriding refers to the ability of a subclass to provide a specific implementation of a method that is
 already defined in its superclass. This is a common feature in object-oriented programming and is fully 
 supported in Python. This allows a method to behave differently depending on the subclass that implements it.
 
Overloading in Python is not supported in the traditional sense where multiple methods can have the same 
name but different parameters. However, Python supports operator overloading and allows methods to handle 
arguments of different types, effectively overloading by type checking inside methods.
Does Python Allow Operator Overloading?
Yes, Python allows operator overloading. You can define your own behavior for built-in operators when they 
are applied to objects of classes you define. This is done by redefining special methods in your class, such
 as __add__ for +, __mul__ for *, etc.

Example of Operator Overloading:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)  # Output: (3, 5)
What is __init__ in Python?
The __init__ method in Python is a special method used for initializing newly created objects. It's called
automatically when a new object of a class is created. This method can have arguments through which you can 
pass values for initializing object attributes.

Example of __init__:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("John", 30)
p.greet()  # Output: Hello, my name is John and I am 30 years old.
What is Encapsulation in Python?
Encapsulation is a fundamental concept in object-oriented programming that involves bundling the data
(attributes) and methods (functions) that operate on the data into a single unit or class. It restricts
direct access to some of the object's components, which can prevent the accidental modification of data
and allows for safer and more structured code. In Python, encapsulation is implemented using private 
(denoted by double underscores __) and protected (denoted by single underscore _) attributes and methods.

Example of Encapsulation:
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.__balance = amount  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance

acct = Account("John")
acct.deposit(100)
print(acct.get_balance())  # Output: 100
# print(acct.__balance)  # This will raise an error because __balance is private

------------------------------
Common Syntax Special Method Form
a+b a.--add__(b); alternatively b. radd (a)
a − b a.__sub__(b); alternatively b. rsub (a)
a b a. mul (b); alternatively b. rmul (a)
a/b a. truediv (b); alternatively b. rtruediv (a)
a // b a. floordiv (b); alternatively b. rfloordiv (a)
a%b a. mod (b); alternatively b. rmod (a)
a b a. pow (b); alternatively b. rpow (a)
a << b a. lshift (b); alternatively b. rlshift (a)
a >> b a. rshift (b); alternatively b. rrshift (a)
a&b a. and (b); alternatively b. rand (a)
aˆb a. xor (b); alternatively b. rxor (a)
a | b a. or (b); alternatively b. ror (a)
a += b a. iadd (b)
a −= b a. isub (b)
a = b a. imul (b)
... ...
+a a. pos ( )
−a a. neg ( )
˜a a. invert ( )
abs(a) a. abs ( )
a < b a. lt (b)
a <= b a. le (b)
a > b a. gt (b)
a >= b a. ge (b)
a == b a. eq (b)
a != b a. ne (b)
v in a a. contains (v)
a[k] a. getitem (k)
a[k] = v a. setitem (k,v)
del a[k] a. delitem (k)
a(arg1, arg2, ...) a. call (arg1, arg2, ...)
len(a) a. len ( )
hash(a) a. hash ( )
iter(a) a. iter ( )
next(a) a. next ( )
bool(a) a.--bool--( )
float(a) a. float ( )
int(a) a. int ( )
repr(a) a. repr ( )
reversed(a) a. reversed ( )
str(a) a. str ( )
Table 2.1: Overloaded operations, im

For example, in a three-dimensional space, we might wish to represent a vector with coordinates 
(5,−2, 3). Although it might be tempting to directly use a Python list to represent those coordinates
, a list does not provide an appropriate abstraction for a geometric vector. In particular, if using lists,
 the ex￾pression [5, −2, 3] + [1, 4, 2] results in the list [5, −2, 3, 1, 4, 2]. When working with vectors,
if u =(5,−2, 3) and v =(1, 4, 2), one would expect the expression,u+v, to return a three-dimensional vector
 with coordinates (6, 2, 5)
"""
class Vector:
# ”””Represent a vector in a multidimensional space.”””
    def __init__(self, d):
#Create d-dimensional vector of zeros.”””
        self.coords = [0]*d
    def __len__(self):
#Return the dimension of the vector.”””
        return len(self.coords)
    def __getitem__(self, j):
#”””Return jth coordinate of vector.”””
        return self.coords[j]
    def __setitem__(self, j, val):
#Set jth coordinate of vector to given value.”””
        self.coords[j] = val
    def __add__(self, other):
#Return sum of two vectors.”””
        if len(self) != len(other): # relies on len method
            raise ValueError( 'dimensions must agree' )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
#Return True if vector has same coordinates as other.”””
        return self.coords == other.coords
    def __ne__(self, other):
#Return True if vector differs from other.”””
        return not self == other # rely on existing eq definition
    def __str__(self):
#Produce string representation of vector.”””
        return '<' + str(self.coords)[1:-1] + '>' # adapt list representation


v = Vector(5) # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
v[-1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
print(v[4]) # print 45 (via getitem )
u=v+v # <0, 46, 0, 0, 90> (via add )
print(u) # print <0, 46, 0, 0, 90>
total = 0
for entry in v: # implicit iteration via len and getitem
    total += entry
"""
------------------------
iteraore

an iterator for a collec￾tion provides one key behavior: It supports a special method named next that
returns the next element of the collection, if any, or raises a StopIteration exception
to indicate that there are no further elements.Fortunately, it is rare to have to directly implement
an iterator class. Our pre￾ferred approach is the use of the generator syntax (also described in 
Section 1.8),which automatically produces an iterator of yielded values.Python also helps by providing
an automatic iterator implementation for any class that defines both len and getitem . To provide an 
instructive exam￾ple of a low-level iterator, Code Fragment 2.5 demonstrates just such an iterator
class that works on any collection that supports both len and getitem .This class can be instantiated
as SequenceIterator(data). It operates by keeping an internal reference to the data sequence, as 
well as a current index into the sequence.Each time next is called, the index is incremented, until 
reaching the end of the sequence.

"""
class SequenceIterator:
#”””An iterator for any of Python s sequence types.”””
    def __init__(self, sequence):
# ”””Create an iterator for the given sequence.”””
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on first call to next
    def __next__(self):
# ”””Return the next element, or else raise StopIteration error.”””
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]  # return the data element
        else:
            raise StopIteration( ) # there are no more elements
    def __iter__(self):
#”””By convention, an iterator must return itself as an iterator.”””
        return self

#----------------------------
"""
Example: Range Class
we develop our own implementation of a class that mimics Python’s built-in range class. Before 
introducing our class, we discuss the history of the built-in version. Prior to Python 3 being 
released, range was implemented as a function, and it returned a list instance with elements in
the specified range. For example, range(2, 10, 2) returned the list [2, 4, 6, 8].However, a 
typical use of the function was to support a for-loop syntax, such as for k in range(10000000).
Unfortunately, this caused the instantiation and initial￾ization of a list with the range of 
numbers. That was an unnecessarily expensive step, in terms of both time and memory usage

range in Python 3 is entirely different (to be fair, the “new” behavior existed in Python 2 under the 
name xrange). It uses a strategy known as /lazy evaluation/. Rather than creating a new list instance, 
range is a class that can effectively represent the desired range of elements without ever storing them 
explicitly in memory. To better explore the built-in range class, we recommend that you create an 
instance as r = range(8, 140, 5). The result is a relatively lightweight object, an instance of the range
class, that has only a few behaviors. The syntax len(r) will report the number of elements that are in the
given range (27, in our example). A range also supports the getitem method,so that syntax r[15] reports the
sixteenth element in the range (as r[0] is the firstelement). Because the class supports both len and 
getitem , it inherits automatic support for iteration (see Section 2.3.4), which is why it is possible to
execute a for loop over a range

The biggest challenge in the implementation is properly computing
the number of elements that belong in the range, given the parameters sent by the
caller when constructing a range. By computing that value in the constructor, and
storing it as self._length, it becomes trivial to return it from the __len__ method. To
properly implement a call to __getitem__ (k), we simply take the starting value of
the range plus k times the step size (i.e., for k=0, we return the start value). There
are a few subtleties worth examining in the code

1-We compute the number of elements in the range as
max(0, (stop − start + step − 1) // step)
It is worth testing this formula for both positive and negative step sizes

2-The getitem method properly supports negative indices by converting
an index −k to len(self)−k before computing the result
"""
class Range:
#”””A class that mimic s the built-in range class.”””
    def __init__(self,start1, stop1=None, step1=1):
        """Initialize a Range instance.
        Semantics is similar to built-in range class.
        """
        if step1 == 0:
            raise ValueError('step cannot be 0 ')
        if stop1 is None:  # special case of range(n)
            start1, stop1 = 0, start1  # should be treated as if range(0,n)
        self._length = max(0, (stop1 - start1 + step1 - 1) // step1) # calculate the effective length once
        self._start = start1 # need knowledge of start and step (but not stop) to support getitem
        self._step = step1
    def __len__(self):
        return self._length  # Return number of entries in the range
    def __getitem__(self, k):

        if k < 0: # Return entry at index k (using standard interpretation if negative).”””
            k += len(self) # attempt to convert negative index
        if not 0 <= k < self._length:
            raise IndexError( 'index out of range ')
        return self._start + k *self._step

#-------------------------

# Inheritance
"""
An example of such a hierarchy is shown in Figure 2.4. Using mathematical notations, the set of houses
is a subset of the set of buildings, but a superset of the set of ranches. The correspondence between 
levels is often referred to as an “is a” relationship, as a house is a building, and a ranch is a house

hierarchical design is useful in software development, as common function￾ality can be grouped at the most 
general level, thereby promoting reuse of code,while differentiated behaviors can be viewed as extensions
of the general case, In object-oriented programming, the mechanism for a modular and hierarchical 
orga￾nization is a technique known as inheritance

the existing class is typically described as the base class, parent class, or super￾class, while the 
newly defined class is known as the subclass or child class
A subclass may specialize an existing behavior by providing a new im￾plementation that overrides an 
existing method. A subclass may also extend its superclass by providing brand new methods.

Another example of a rich inheritance hierarchy is the organization of various ex￾ception types in Python
The BaseException class is the root of the entire hierar￾chy, while the more specific Exception class 
includes most of the error types thatwe have discussed. Programmers are welcome to define their own 
special exception classes to denote errors that may occur in the context of their application

Extending the CreditCard Class
To demonstrate the mechanisms for inheritance in Python, we revisit the CreditCardclass of Section 2.3,
implementing a subclass that, for lack of a better name, we name PredatoryCreditCard. The new class will
differ from the original in two ways: (1) if an attempted charge is rejected because it would have 
exceeded thecredit limit, a $5 fee will be charged, and (2) there will be a mechanism for assess￾ing a 
monthly interest charge on the outstanding balance, based upon an AnnualPercentage Rate (APR) specified as
a constructor parameter.In accomplishing this goal, we demonstrate the techniques of specialization and
extension.To charge a fee for an invalid charge attempt, we override theexisting charge method, thereby
specializing it to provide the new functionality(although the new version takes advantage of a call to
the overridden version). To provide support for charging interest, we extend the class with a new method 
named process month.


"""
class PredatoryCreditCard(CreditCard):
#”””An extension to CreditCard that compounds interest and fees.”””
    def __init__(self, customer, bank, acnt, limit, apr):

        super().__init__(customer, bank, acnt, limit)  # call super constructor of class credit card
        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
Return True if charge was processed.
Return False and assess 5 fee if charge is denied.
        :param self:
        :param price:
        :return:
        """
        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5 # assess penalty
        return success # caller expects return value

    def process_month(self):

        if self._balance > 0: #Assess monthly interest on outstanding balance.if positive balance, convert APR to
            # monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

"""
Create a new predatory credit card instance.
The initial balance is zero. customer the name of the customer (e.g., John Bowman )
bank the name of the bank (e.g., California Savings )
acnt the acount identifier (e.g., 5391 0375 9387 5309 )
limit credit limit (measured in dollars)
apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
"""
"""
Members
that are declared as protected are accessible to subclasses, but not to the generalpublic, while members that are 
declared as private are not accessible to either. Inthis respect, we are using balance as if it were protected 
(but not private).Python does not support formal access control, but names beginning with a sin￾gle underscore are
conventionally akin to protected, while names beginning with a double underscore (other than special methods) are
akin to private. In choosing to use protected data, we have created a dependency in that our PredatoryCreditCard
class might be compromised if the author of the CreditCard class were to change the internal designIf we were to 
redesign the original CreditCard class, we mightadd a nonpublic method, set balance, that could be used by 
subclasses to affect a change without directly accessing the data member balanc

Hierarchy of Numeric Progressions
As a second example of the use of inheritance, we develop a hierarchy of classes for
iterating numeric progressions. A numeric progression is a sequence of numbers,
where each number depends on one or more of the previous numbers. For example,
an arithmetic progression determines the next number by adding a fixed constant
to the previous value, and a geometric progression determines the next number
by multiplying the previous value by a fixed constant. In general, a progression
requires a first value, and a way of identifying a new value based on one or more
previous values.
we develop a hierarchy of classes stemming
from a general base class that we name Progression (see Figure 2.7). Technically,
the Progression class produces the progression of whole numbers: 0, 1, 2, . . ..
However, this class is designed to serve as the base class for other progression types,
providing as much common functionality as possible, and thereby minimizing the
burden on the subclasses.
                            Progression
                            
ArithmeticProgression  GeometricProgression  FibonacciProgression

constructor for this class accepts a starting value for the progression
(0 by default), and initializes a data member, self. current, to that value
Progression class implements the conventions of a Python iterator (see
Section 2.3.4), namely the special next and iter methods. If a user of
the class creates a progression as seq = Progression( ), each call to next(seq) will
return a subsequent element of the progression sequence. It would also be possi￾ble to use a for-loop syntax, 
for value in seq:, although we note that our default progression is defined as an infinite sequenc

To better separate the mechanics of the iterator convention from the core logic
of advancing the progression, our framework relies on a nonpublic method named
advance to update the value of the self. current field. In the default implementa￾tion, advance adds one to the 
current value, but our intent is that subclasses willoverride advance to provide a different rule for computing 
the next entry

"""
class Progression:
    """
    iterator producing a generic progression.Default iterator produces the whole nos 0,1,2,
    """
    def __init__(self,start=0):
        self._current = start

    def _advance(self):
        """

        update self._current to a new value.This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression

        """
        self._current += 1

    def __next__(self): #return the next element or else raise Stopiteration error
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):  # by convention ,an iterator must return itself as an iterator
        return self

    def print_progression(self,n): # print next n values of the progression
        print(' '.join(str(next(self)) for j in range(n)))

"""
ArithmeticProgression
class, which relies on Progression as its base class. The constructor for this new
class accepts both an increment value and a starting value as parameters, although
default values for each are provided. By our convention, ArithmeticProgression(4)
produces the sequence 0,4,8,12,... , and ArithmeticProgression(4, 1) produces
the sequence 1,5,9,13,

The body of the ArithmeticProgression constructor calls the super constructor
to initialize the current data member to the desired start value. Then it directly
establishes the new increment data member for the arithmetic progression. The
only remaining detail in our implementation is to override the advance method so
as to add the increment to the current val


"""
class Arithmeticprogression(Progression):  # iterator producing an  arithmetic progression

    def __init__(self,increment=1,start=0): # create new arithmetic progression
        super().__init__(start)
        self._increment = increment

    def _advance(self): #update current value by adding the fixed increment
        self._current += self._increment

"""
Code Fragment 2.10 presents our implementation of a GeometricProgression
class. The constructor uses 2 as a default base and 1 as a default starting value, but
either of those can be varied using optional parameters.
"""
class Geometricprog(Progression):

    def __init__(self,base=2,start=1): # create a new gp
        super().__init__(start)
        self._base = base

    def _advance(self): # update curr val
        self._current *= self._base

#fib
class Fibprog(Progression):

    def __init__(self,first=0,second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

if __name__ =='__main__':
    print('default progression')
    Progression().print_progression(11)

    print('AP with increment 5:')
    Arithmeticprogression(5).print_progression(11)

    print('AP with increment 5 and start 2:')
    Arithmeticprogression(5,2).print_progression(11)

    print('GP with default base:')
    Geometricprog().print_progression(11)

    print('GP with base 3:')
    Geometricprog(3).print_progression(11)

    print('fibnaci with default base:')
    Fibprog().print_progression(11)

    print('fibnaci with start 4 ,6:')
    Fibprog(4,6).print_progression(11)

"""
ABC CLASSES
In classic object-oriented terminology, we say a class is an abstract base class
if its only purpose is to serve as a base class through inheritance. More formally,
an abstract base class is one that cannot be directly instantiated, while a concrete
class is one that can be instantiated. By this definition, our Progression class is
technically concrete, although we essentially designed it as an abstract base class

In statically typed languages such as Java and C++, an abstract base class servesas a formal type that may 
guarantee one or more abstract methods. This provides support for polymorphism, as a variable may have an abstract
base class as its de￾clared type, even though it refers to an instance of a concrete subclass. Because
there are no declared types in Python, this kind of polymorphism can be accom￾plished without the need for a 
unifying abstract base class. For this reason, there is not as strong a tradition of defining abstract base classes
 in Python, although Python’s abc module provides support for defining a formal abstract base class

Python’s collections module provides several abstract base classes that assist
when defining custom data structures that share a common interface with some of
Python’s built-in data structures. These rely on an object-oriented software design
pattern known as the template method pattern. The template method pattern is
when an abstract base class provides concrete behaviors that rely upon calls to
other abstract behaviors. In that way, as soon as a subclass provides definitions for
the missing abstract behaviors, the inherited concrete behaviors are well defined

Sequence abstract base class defines be￾haviors common to Python’s list, str, and tuple classes, as sequences 
that sup￾port element access via an integer index. More so, the collections.Sequence class
provides concrete implementations of methods, count, index, and contains
that can be inherited by any class that provides concrete implementations of both
__len__ and __getitem__ .

"""
from abc import ABCMeta,abstractmethod      # need these definitions

class Sequence(metaclass=ABCMeta):  # base case

    @abstractmethod
    def __len__(self):  # returns length
        pass


    @abstractmethod
    def __getitem__(self, j):  #return the element at index j
        pass


    def __contains__(self, val): # return if val is in seq
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    def index(self,val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self,val): #returns no of elements equal to given value
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

"""
This implementation relies on two advanced Python techniques. The first is that
we declare the ABCMeta class of the abc module as a metaclass of our Sequence
class. A metaclass is different from a superclass, in that it provides a template for
the class definition itself. Specifically, the ABCMeta declaration assures that the
constructor for the class raises an error.
e @abstractmethod decorator
immediately before the len and getitem methods are declared. That de￾clares these two particular methods to be 
abstract, meaning that we do not provide an implementation within our Sequence base class, but that we expect 
any concrete subclasses to support those two methods. Python enforces this expectation, by dis￾allowing 
instantiation for any subclass that does not override the abstract methods with concrete implementations.
if a subclass provides its own implementation of an inherited behaviors from a base class, the new definition 
overrides the inherited one. This technique can be used when we have the ability to provide a more effi-cient 
implementation for a behavior than is achieved by the generic approach. As an example, the general implementation
of contains for a sequence is based on a loop used to search for the desired value

"""
# class Range(collections.Sequence):
"""
 Namespaces and Object-Orientation
A namespace is an abstraction that manages all of the identifiers that are defined in
a particular scope, mapping each name to its associated value. In Python, functions,
classes, and modules are all first-class objects, and so the “value” associated with
an identifier in a namespace may in fact be a function, class, or module

instance namespace
which man￾ages attributes specific to an individual object. For example, each instance of our
CreditCard class maintains a distinct balance, a distinct account number, a distinct
credit limit, and so on (even though some instances may coincidentally have equiv￾alent balances, or equivalent 
credit limits). Each credit card will have a dedicated instance namespace to manage such values class namespace 
for each class that has been defined. This namespace is used to manage members that are to be shared by all
instances of a class, or used without reference to any particular instance. For example, the make payment 
method of the CreditCard class from Section 2.3 is not stored independently by each instance of that class.
That member function is stored within the namespace of the CreditCard class

"""
class CreditCard:
    def make_payment(self, amount):
        pass


class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5 # this is a class-level member
    def charge(self, price):
        success = super( ).charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success
"""
Nested Classes
It is also possible to nest one class definition within the scope of another class.
this technique is unrelated to the concept of inheritance, as class B does not inherit from class A

Nesting one class in the scope of another makes clear that the nested class exists for support of the 
outer class. Furthermore, it can help reduce potential name conflicts, because it allows for a similarly
named class to exist in another context. For example- we will later introduce a data structure known as a
linked list and will define a nested node class to store the individual components of the list. We will
also introduce a data structure known as a tree that depends upon its own nested node class. These two 
structures rely on different node definitions, and by nesting those within the respective container classes,
we avoid ambiguity
it allows for a more advanced form of inheritance in which a subclass of the outer
class overrides the definition of its nested class

Python represents each namespace with an instance of the built-in dict
class (see Section 1.2.3) that maps identifying names in that scope to the associated
objects. While a dictionary structure supports relatively efficient name lookups,
it requires additional memory usag

class CreditCard:
    __slots__ = _'customer' ,' _bank' , '_account' , '_balance' , '_limit'
In this example, the right-hand side of the assignment is technically a tuple (see
discussion of automatic packing of tuples in Section 1.9.3)

The declaration
in the subclass should only include names of supplemental methods that are newly
introduced
class PredatoryCreditCard(CreditCard):
__slots__ = '_apr'
-------------------------------
the process that is used when retrieving a name in Python’s object-oriented framework. When the dot operator
syntax is used to access an existing member, such as obj.foo, the.Python interpreter begins a name resolution
process, described as follows:
1. The instance namespace is searched; if the desired name is found, its associ￾ated value is used.
2. Otherwise the class namespace, for the class to which the instance belongs,
is searched; if the name is found, its associated value is used.
3. If the name was not found in the immediate class namespace, the search con￾tinues upward through the inheritance
hierarchy, checking the class name￾space for each ancestor (commonly by checking the superclass class, then 
itssuperclass class, and so on). The first time the name is found, its associate value is used.
4. If the name has still not been found, an AttributeError is raised.
"""

"""
we wish to create a new list named palette, which is a copy of the warmtones list.
However, we want to subsequently be able to add additional colors to palette, or
to modify or remove some of the existing colors, without affecting the contents of
warmtones. If we were to execute the command
palette = warmtones
this creates an alias, as shown in Figure 2.9. No new list is created; instead, the
new identifier palette references the original list.
                        list
warmtones                                   palette
red                                         red
green                                       green
blue                                        blue
color                                       color
43                                          52
124                                         163
249                                         169

Figure 2.9: Two aliases for the same list of colors.
Unfortunately, this does not meet our desired criteria, because if we subsequently
add or remove colors from “palette,” we modify the list identified as warmtones.
We can instead create a new instance of the list class by using the syntax:
palette = list(warmtones)
In this case, we explicitly call the list constructor, sending the first list as a param￾eter. This causes a new list to be created, as shown in Figure 2.10; however, it is
what is known as a shallow copy. The new list is initialized so that its contents are
precisely the same as the original sequence. However, Python’s lists are referential
(see page 9 of Section 1.2.3), and so the new list represents a sequence of references
to the same elements as in the first.
Although palette and warmtones are distinct lists, there remains indi￾rect aliasing, for example, with palette[0] and warmtones[0] as aliases for the same
color instance.
We prefer that palette be what is known as a deep copy of warmtones. In a
deep copy, the new copy references its own copies of those objects referenced by
the original version. (See Figure 2.11.)
Python provides a very convenient module (rather than aliasing), named
copy, that can produce both shallow copies and deep copies of arbitrary objects

the copy function creates a shallow copy
of its argument, and the deepcopy function creates a deep copy of its argument.
After importing the module, we may create a deep copy for our example, as shown
in Figure 2.11, using the command:
palette = copy.deepcopy(warmtones)


"""

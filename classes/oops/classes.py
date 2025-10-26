
"""


Encapsulation in Python
Last Updated : 23 Oct, 2024
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the
 idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing
  variables and methods directly and can prevent the accidental modification of data. To prevent accidental
  change, an object’s variable can only be changed by an object’s method. Those types of variables are known
  as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
 The goal of information hiding is to ensure that an object’s state is always valid by controlling access to
 attributes that are hidden from the outside world.

"""

def test(a=[]):
    a.append(1)
    return a

print(test())





























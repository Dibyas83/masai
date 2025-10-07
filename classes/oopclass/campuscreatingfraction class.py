
# creating a new data type

class Fraction:

    def __init__(self,n,d):
        self.num = n
        self.den = d

    """
    if x is a class object and we write print(x) python will search __str__ inside class, and the code inside it will be executed
    """
    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self, other): # x will be self , y is other
        temp_num = self.num *other.den + self.den*other.num
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num,temp_den)

    def __sub__(self, other): # x will be self , y is other
        temp_num = self.num *other.den - self.den*other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)

    def __mul__(self, other): # x will be self , y is other
        temp_num = self.num  * other.num
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num,temp_den)

    def __truediv__(self, other): # x will be self , y is other
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num,temp_den)

x = Fraction(4,5)
print(x)
y = Fraction(5,6)
print(x+y)  # we have to tell how will the objects be added.def __add__ when + is there python searches _add_
print(x-y)
print(x*y)
print(x/y)

# if we add this file to lib ,he can create objects using this class


"""
Step-by-Step Guide to Create A Library
Step 1: Initialize Your Project. ...
Step 2: Create a Directory for Your Package. ...
Step 3: Add __init. ...
Step 4: Add Modules. ...
Step 5: Write into the Modules. ...
Step 6: Add setup.py. ...
Step 7: Add Tests & Other Files [Optional] ...
Step 9: Install and Use the Library.
"""









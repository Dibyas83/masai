
"""
Setters in Python are methods used to modify the value of an object's attribute. They are commonly used in conjunction with getters to control access and modification of class attributes, promoting data encapsulation.
Here's a breakdown of their use:
Purpose:
Controlled Modification:
Setters allow you to implement logic when an attribute's value is changed. This can include validation, data transformation, or triggering other actions.
Data Encapsulation:
By using setters, you can prevent direct access to an attribute and enforce rules on how it's modified, protecting the object's internal state.
Implementation:
@property decorator:
Python's @property decorator is used to define a getter method. A corresponding setter method is defined using @property_name.setter, where property_name is the name of the property.
Method:
The setter method takes one argument (in addition to self), which represents the new value to be assigned to the attribute.
"""
"""
decorator gives class attributes get,set,del functionality

"""



class Employees:

    numof_emp = 0
    raise_amt = 1.04 # class variable
#init method takes self as instance and first,last ,pay as arguments

    def __init__(self,firstn,lastn,payx):
        self.firstn = firstn
        self.lastn = lastn
        self.payx = payx
        #self.mailn = firstn + '_' + lastn + '@company.com'  - decorator used

    #property decorator allows us to define a method and we can access it as an attribute
    # lets make email attribute as method
    @property  # now we can acess as attribute
    def mailn(self):
        return '{}.{}@email.com'.format(self.firstn,self.lastn)

    @property
    def fulname(self):
        return '{} {}'.format(self.firstn,self.lastn)

    def pay_raise(self):
        #self.payx = int(self.payx * raise_amt)
        self.payx = int(self.payx * Employees.raise_amt) # class variable can be accessed through class or instance of class
        self.payx = int(self.payx * self.raise_amt) # class variable can be accessed through class or instance of class

    @fulname.setter
    def fulname(self,name):
        firstn,lastn = name.split(' ')
        self.firstn = firstn
        self.lastn = lastn

    @fulname.deleter
    def fulname(self):
        print('Delete name')
        self.firstn = None
        self.lastn = None

emp11 = Employees("haa","hee",3000)
emp22 = Employees("bum","bam",2000)

emp11.fulname = 'cor andy' # it will not disturb mail
emp11.firstn = 'jim' # but we dont want change email even if name changes


print(emp11.mailn)
print(emp11.firstn)
#print(emp11.mailn()) - #acessing as method when not using decorator
print(emp11.fulname)

del emp11.fulname # it will set first and last name to none

#----------------------------------------------
# Geeks using normal function
class Geek:
    def __init__(self, age=0):
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    # setter method
    def set_age(self, x):
        self._age = x


raj = Geek()

# setting the age using setter
raj.set_age(21)

# retrieving age using getter
print(raj.get_age())

print(raj._age)
"""
Explanation:

A Geek class is defined with an _age attribute.
The get_age() method is the getter, which retrieves the value of _age.
The set_age() method is the setter, which assigns a value to _age.
The setter method is used to set the age and the getter method is used to retrieve it.

Using property() function
In this method, the property() function is used to wrap the getter, setter and deleter methods for an attribute, providing a more streamlined approach
"""


class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks()

mark.age = 10

print(mark.age)

"""
Explanation:

A Geeks class is created with an internal _age attribute.
The get_age() function retrieves the value, set_age() sets it and del_age() deletes the attribute.
The property() function binds these methods to the age attribute.
The age attribute is accessed and set using the property function.

Using @property decorators
In this approach, the @property decorator is used for the getter and the @<property_name>.setter decorator is used for the setter. This approach allows a more elegant way to define getter and setter methods.
"""

class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Geeks()

mark.age = 19

print(mark.age)

















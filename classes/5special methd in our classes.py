
"""
special classes that emulate built in methods and operating overloading
they are represented bu double underscores or dunder

ex - __init__, __repr__(unambiguous representation of an object used for logging,debugging  meant to be seen for other developer) , __str__(a readable representation of object,as display to end user)

"""

class Employees:

    numof_emp = 0
    raise_amt = 1.04 # class variable
#init method takes self as instance and first,last ,pay as arguments

    def __init__(self,firstn,lastn,payx): #this init  method is a constructor or initialiser.when we create method within the class they receive the instances as first argument automatically .self is the first argument then first,last..
        self.firstn = firstn # set instance variable
        self.lastn = lastn
        self.payx = payx
        self.mailn = firstn + '_' + lastn + '@company.com'
# name email,pay are all atributes of our class
        Employees.numof_emp += 1

    def fulname(self):
        return '{} {}'.format(self.firstn,self.lastn)

    def pay_raise(self):
        #self.payx = int(self.payx * raise_amt)
        self.payx = int(self.payx * Employees.raise_amt) # class variable can be accessed through class or instance of class
        self.payx = int(self.payx * self.raise_amt) # class variable can be accessed through class or instance of class

    def __repr__(self): #trying to return a string that i can use to recreate the object
        return "Employee('{}','{}','{}')".format(self.firstn,self.lastn,self.payx)


    def __str__(self): # readable end user
        return '{} - {}'.format(self.fulname(),self.mailn)

    #def add(self,other):
    def __add__(self, other):
        return self.payx + other.payx

    def __len__(self): # ex if need to know the char  name would take
        return len(self.fulname())
print(Employees.numof_emp,"no of")
emp11 = Employees("haa","hee",3000)
emp22 = Employees("bum","bam",2000)
print(Employees.numof_emp,"no of")

#print(emp11)

print(repr(emp22))
print(repr(emp11))
print(str(emp11))

#print(emp11.__repr__())
#print(emp11.__str__())

print(1+2) # it will use dunder add in the background
print(int.__add__(1,2)) # using int object and add dunder

print(str.__add__('a','b'))

print(emp11 + emp22)
print(len('test'))
print('test'.__len__())







"""
class variable is same  or shared among each instance ,inst var is unique
like raise for all employees is same
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

print(Employees.numof_emp,"no of")
emp11 = Employees("hjd","hjk",300)
emp22 = Employees("bum","bam",200)
print(Employees.numof_emp,"no of")

print(emp11.mailn)
print(emp22.mailn)
print(emp22.fulname())
print(Employees.fulname(emp22))

print(emp11.payx)
emp11.pay_raise() # using method
print(emp11.payx)

print(Employees.raise_amt)
print(emp11.raise_amt)  # when we try to access attribute on instance,it will first check if instance contains that attribute or if the class from which it inherits from has that attribute
print(emp22.raise_amt)
print(emp22.__dict__)
print(Employees.__dict__)

Employees.raise_amt = 1.05 # for all emp
emp11.raise_amt = 1.06 # only for emp11







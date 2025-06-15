

"""
inheritence allows us to inherit attribute and methods from parent class
by which we can create subclases ,and get all the functionality of parent class
and then override  or create new functionality without affecting parent class

lets create diff type of employee - developer and managers
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

class Developer(Employees):
    raise_amt = 1.12

    def __init__(self, firstn, lastn, payx, prog_lang):
        super().__init__(firstn,lastn,payx)
        Employees.__init__(self,firstn,lastn,payx) # to be handled by employ class
        self.prog_lang = prog_lang # this handled by Deve class

class Manager(Employees): # it will manage only list of employee
    def __init__(self, firstn, lastn, payx, employees = None): # none is default argument
        super().__init__(firstn, lastn, payx)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addemp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rememp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printemp(self):
        for emp in self.employees:
            print("--",emp.fulname())

print(Employees.numof_emp,"no of")
emp11 = Employees("hjd","hjk",300)
emp22 = Employees("bum","bam",200)
print(Employees.numof_emp,"no of")
dev1 = Developer("fggfj","fghfh",1222,"python")
dev2 = Developer("fgfj","fhfh",2212,"java")
mgr1 = Manager("htht","yhet",5555,[dev1])
print(mgr1.mailn)
mgr1.addemp(dev2)
mgr1.rememp(dev1)
mgr1.printemp()

print(isinstance(mgr1,Manager))
print(isinstance(mgr1,Employees))
print(isinstance(mgr1,Developer))

print(issubclass(Developer,Employees))
print(issubclass(Manager,Employees))
print(issubclass(Manager,Developer))

print(dev1.mailn) # method of resolution- 1 develooper 2 employees 3 builtins.object
print(dev2.mailn)

print(help(Developer))
print(Employees.fulname(emp22))

print(emp11.payx)
emp11.pay_raise() # using method
dev1.pay_raise() # using method
dev2.pay_raise() # using method
print(emp11.payx)
print(dev1.payx,"devpat")
print(dev2.payx,"devpat")

print(Employees.raise_amt)
print(emp11.raise_amt)  # when we try to access attribute on instance,it will first check if instance contains that attribute or if the class from which it inherits from has that attribute
print(dev2.raise_amt)
print(dev1.raise_amt)
print(emp22.__dict__)
print(Employees.__dict__)






















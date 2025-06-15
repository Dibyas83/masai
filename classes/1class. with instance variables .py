"""
methods are functions asosiated with class

"""
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.first = 'corey'
emp1.sec = 'anderson'
emp1.mail = 'ds@gmail.com'

emp2.first = 'cor'
emp2.sec = 'ander'
emp2.mail = 'dsuii@gmail.com'

print(emp1.mail)
print(emp2.mail)

#----------------

class Employees:
#init method takes self as instance and first,last ,pay as arguments
    def __init__(self,firstn,lastn,payx): #this init  method is a constructor or initialiser.when we create method within the class they receive the instances as first argument automatically .self is the first argument then first,last..
        self.firstn = firstn # set instance variable
        self.lastn = lastn
        self.payx = payx
        self.mailn = firstn + '_' + lastn + '@company.com'
# name email,pay are all atributes of our class
    def fulname(self):
        return '{} {}'.format(self.firstn,self.lastn)
emp11 = Employees("hjd","hjk",300)
emp22 = Employees("bum","bam",200)

print(emp11.mailn)
print(emp22.mailn)
print(emp22.fulname())
print(Employees.fulname(emp22))







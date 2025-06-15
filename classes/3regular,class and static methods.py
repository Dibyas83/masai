

import time
import datetime


"""
regular methods automatically pass  instance  as first argument - by calling self
class methods automatically pass the class  as first argument - by calling cls
static methods pass nothing automatically,tey dont pass instance or class,they behave like regular functions
how can it take class as first argument , by using class methods ,using classs decorator
"""

class Employees:

    numof_emp = 0
    raise_amt = 1.04

    def __init__(self,firstn,lastn,payx):

        self.firstn = firstn
        self.lastn = lastn
        self.payx = payx
        self.mailn = firstn + '_' + lastn + '@company.com'

        Employees.numof_emp += 1

    def fulname(self):
        return '{} {}'.format(self.firstn,self.lastn)

    def pay_raise(self):
        #self.payx = int(self.payx * raise_amt)
        self.payx = int(self.payx * Employees.raise_amt)
        self.payx = int(self.payx * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt = amt

    # class methods as alternate contructor ,means use class methods to provide multiple ways to create objects
    @classmethod
    def from_string(cls, emp_str):
        firstn, lastn, payx = emp_str.split("-")
        return cls(firstn, lastn, payx)

    @classmethod
    def fromtimestamp(cls,t):
        #construct a date from a postx timestamp(liketime.time())
        y,m,d,hh,mm,ss,weekday,jday,dst = time.localtime(t)
        return cls(y,m,d)

    @classmethod
    def today(cls):
        # construct a date from time.time())
        t = time.time()
        return cls.fromtimestamp(t)

    # static -lets take a simple fuctiom that takes a date and returns if it is working day or not
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
"""
import time

obj = time.localtime()

print(obj)

print(time.asctime(obj))

--------------
import time

secs = 950000000

obj = time.localtime(secs)

print("Local time for seconds =", secs)
print(obj)
------------------------
import time

# Time with fractional seconds
secs = 950000000.81956

obj = time.localtime(secs)

print("Local time for seconds =", secs)
print(obj)
"""


#Employees.set_raise_amt(1.08)
print(Employees.numof_emp,"no of")
emp11 = Employees("hjd","hjk",300)
emp22 = Employees("bum","bam",200)
print(Employees.numof_emp,"no of")
my_date = datetime.date(2016,7,10)
print(Employees.is_workday(my_date))

emp11_str = "hjd-hjk-300"
emp22_str = "bum-bam-200"
emp23_str = "bam-bum-100"

firstn,lastn,payx =emp22_str.split("-")
new_emp = Employees(firstn,lastn,payx)
new_emp_1 = Employees.from_string(emp11_str)

print(new_emp.mailn)
print(new_emp_1.mailn)

print(emp11.payx)
emp11.pay_raise() # using method
print(emp11.payx)

Employees.set_raise_amt(1.08)
emp11.set_raise_amt(1.07)
print(Employees.raise_amt)
print(emp11.raise_amt)
print(emp22.raise_amt)
print(emp22.__dict__)
print(Employees.__dict__)


Employees.raise_amt = 1.05 # for all emp
emp11.raise_amt = 1.06 # only for emp11

print(Employees.raise_amt,"after")
print(emp11.raise_amt,"af")
print(emp22.raise_amt,"af")

"""
from datetime import date

class DatePrinter:
    @classmethod
    def print_current_date(cls):
        today = date.today()
        print("Current date:", today)

# Example usage:
DatePrinter.print_current_date()
--------------
import datetime

class TimePrinter:
    @classmethod
    def print_local_time(cls):
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Example usage
TimePrinter.print_local_time()


"""













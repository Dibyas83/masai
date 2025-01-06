

try:
    a = int(input())
    print("2")
except:
    print("3")


try:
    file = open('data.txt','r')
    data = file.read()
    number = int(data)
except FileNotFoundError:
    print('file not found.')
except ValueError:
    print("could not convert into integer")

try:
    no = int(input())
except ValueError:
    print("could not convert into integer")
else:
    print("enter no")

if a < 0:
    raise ValueError("age cant be neg")
else:
    print("your age is ",a)

class Newescepyion(Exception):
    pass

def sq_rt(no):
    if no < 0:
        raise Newescepyion("no cant be neg")
    return no ** 0.5

try:
    result = sq_rt(-9)
except Newescepyion as e:
    print(e)















"""

try block lets you test a block of code for errors
except block lets you handle the error
finally block lets you execute code , regardless of the result of the try and except blocks

What are Exceptions?
Exceptions are unexpected events during program execution that disrupt the normal flow of instructions.
They help detect and handle errors gracefully without crashing the program.
Analogy: Think of exceptions as speed bumps in a road—handling them ensures a smoother journey.
Why Handle Exceptions?
User Experience: Prevents abrupt program crashes.
Debugging: Offers insights into what went wrong.
Program Stability: Ensures unexpected situations don’t bring your code to a hal

try:
# Code that may raise an exception
except SomeException as e:
# Code to handle the exception



"""

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
except (ZeroDivisionError, ValueError):
    print("An error occurred!")
"""

else Clause
Purpose: Executes code only if no exceptions are raised.
"""
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {num}")
"""

finally Clause
Purpose: Executes code regardless of whether an exception occurred or not.
"""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution completed!")

"""
5. Raising and Creating Custom Exceptions
Raising Exceptions with raise
Purpose: Manually trigger exceptions to enforce conditions in your program.
"""
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        print(f"Your age is {age}.")


"""
Custom Exceptions
Create user-defined exceptions for specific scenarios in your program.


class CustomError(Exception):
    pass


raise CustomError("This is a custom exception!")
"""


print("----------------------------")
# x= "ABC" sometimes abc is stored in cache and gives result
try:
    print(x)
except NameError:
    print(" variable x is not defined")
except:
    print("exceptiom occurred") # default for all other errors


try:
    print("")
    try:
        print(2/0)
    except ZeroDivisionError:
        print("divide by zero is not valid")

except NameError:
    print(" variable x is not defined")


try:
    print("hello")
except:
    print("exceptiom occurred") # default for all other errors
else:
    print("nothing wrong")



try:
    print(y)
except:
    print("exceptiom occurred") # default for all other errors
else:
    print("nothing wrong")
finally:
    print(" try except is finished")


try:
    f = open("file.txt")
    try:
        f.write(" i am writing") # no writing permission
    except:
        print("Something went wrong")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")

"""


try:
    amount check in account
except:
    # not possible,acc banned
    negetive
else:
    positive,amt debited and credited to other acc
finally:
    msg come to my mobile-"amt credited to me"
"""
"""

a =-1
if a <0:
    raise Exception("Sorry,no numbers below zero ")
print(a)
"""
# custom exception


class NegativeDivisionFault(Exception): # exception class in python library we are inheriting
    # for custom errors

    def __init__(self,message,error_code):
        super().__init__()
        self.message=message
        self.error_code = error_code

    def __str__(self): # overriding

        #return f"{self.message} "
        return f"{self.message} (Error Code: {self.error_code})"

print("-------------------------------------------8797")
def divide(a,b):
    if b < 0:
        raise NegativeDivisionFault("Division by neg not allowed",100)
    return a/b

g = divide(5,-9)
print(g)


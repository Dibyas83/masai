
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
-----------
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add
 as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function
is called, we pass along a first name, which is used inside the function to print the full name:
-----------
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

------------------------
By default, a function must be called with the correct number of arguments.Meaning that if your function
expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

----------------------------
If you do not know how many arguments that will be passed into your function, add a * before the
parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

---------------------
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

"""


def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add 
two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:


"""
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His fast name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")  # keyword arguments passed according to data available

# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it
 will be treated as the same data type inside the function.
"""

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# To let a function return a value, use the return statement:


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction6():
  pass

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

# To specify that a function can have only positional arguments, add , / after the arguments:


def my_function(x, /):
  print(x)

my_function(3)
# my_function(x = 3)
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)

# To specify that a function can have only keyword arguments, add *, before the arguments:
# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)
# my_function(3)

# ou can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


"""
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls 
itself. This has the benefit of meaning that you can loop through data to reach a result.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
 We use the k variable as the data, which decrements (-1) every time we recurse. The recursion 
 ends when the condition is not greater than 0 (i.e. when it is 0)
"""
print("----------------------------------------77")
def tri_recursion(k):
  if(k > 0):
    result1 = k + tri_recursion(k - 1)
    print(result1)

  else:
    result1 = 0
  return result1

print("Recursion Example Results:")
tri_recursion(3)














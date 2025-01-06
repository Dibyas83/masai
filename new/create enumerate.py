# Convert a tuple into an enumerate object:

x = ('apple', 'banana', 'cherry')
y = enumerate(x,1)
print(y)
"""

Definition and Usage
The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

The enumerate() function adds a counter as the key of the enumerate object.

Syntax
enumerate(iterable, start)
Parameter Values
Parameter	Description
iterable	An iterable object
start	A Number. Defining the start number of the enumerate object. Default 0

"""

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))
print (list(enumerate(l1,2)))
print(dict(enumerate(l1,1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))


l2 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

# changing index and printing separately
for count, ele in enumerate(l2, 100):
    print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l2):
    print(count)
    print(ele)
"""

Accessing the Next Element
In Python, the enumerate() function serves as an iterator, inheriting all associated iterator functions and methods. Therefore, we can use the next() function and __next__() method with an enumerate object.

To access the next element in an enumerate object, you can use the next() function. It takes the enumerate object as input and returns the next value in the iteration.
"""



fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)
next_element = next(enum_fruits)
print(f"Next Element: {next_element}")


# You can call next() again to retrieve subsequent elements:
next_element = next(enum_fruits)
print(f"Next Element: {next_element}")


# ow to use enumerate in Python?
# Enumerate in Python is used to loop over an iterable and automatically
# provide an index for each item. It returns tuples with the index and corresponding value from the iterable. Example:


my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(index, value)










thistuple = ("apple", "banana", "cherry","apple")
print(type(thistuple))
print(len(thistuple))
print(type(thistuple))
"""
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
"""
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1[-1])
thistuple11 = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple11)

histuple = ("apple", "banana", "cherry")
print(histuple)
y = list(histuple)
y.append("orange")
y.remove("apple")
histuple = tuple(y)
print(histuple)
print("-------------------------99")

"""
Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create
 a new tuple with the item(s), and add it to the existing tuple:
"""
thistuple22 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple22 += y

print(thistuple22)
del thistuple22
# [][]print(thistuple22) #this will raise an error because the tuple no longer exists

"""
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
"""
fruits1 = ("apple", "banana", "cherry")

(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)
print("-----------------------------------------------666")
fruits22 = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green1, yellow1, red1) = fruits22
(green1, yellow1, *red1) = fruits22

print(green1)
print(yellow1)
print(red1)

thistuple52 = ("apple", "banana", "cherry")
for x in thistuple52:
  print(x)

thistuple57 = ("apple", "banana", "cherry")
for i in range(len(thistuple57)):
  print(thistuple57[i])

thistuple62 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple62):
  print(thistuple62[i])
  i = i + 1


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
mytuple88 = tuple1 * 2
print(mytuple88)

"""
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
t = (1, 2, 3, 4, 5)

# tuples are indexed
print(t[1])
print(t[4])

# tuples contain duplicate elements
t = (1, 2, 3, 4, 2, 3)
print(t)

# updating an element
# t[1] = 100
# print(t)
# TypeError: 'tuple' object does not support item assignment

# traversing
# Define a tuple
t = (1, 2, 3, 4, 5)

# Traverse through each item in the tuple
for x in t:
    print(x, end=" ")

"""
Nesting of Python Tuples
A nested tuple in Python means a tuple inside another tuple.
"""
# Code for creating nested tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')

t3 = (t1, t2)
print(t3)

# code to test slicing
t = (0 ,1, 2, 3)

print(t[1:])
print(t[::-1])
print(t[2:4])

# python code for creating tuples in a loop
t = ('gfg',)

# Number of time loop runs
n = 5
for i in range(int(n)):
    t = (t,)
    print(t)

# creating tuple
# Creating a tuple without brackets
t = 4, 5, 6
print(t)  # Output: (4, 5, 6)

# Creating a tuple using the tuple() constructor
t = tuple([7, 8, 9])
print(t)  # Output: (7, 8, 9)

# empty tuple
# Creating an empty tuple
t = ()
print(t)  # Output: ()

# Creating a single-element tuple
t = (10, ) # Comma is important here
print(t)  # Output: (10,)
print(type(t))

# What if we do not use comma
t = (10) # This an integer (not a tuple)
print(t)
print(type(t))

# Tuple packing
a, b, c = 11, 12, 13
t = (a, b, c)
print(t)  # Output: (11, 12, 13)

# Creating a list of tuples manually
a = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
print(a)

a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']

# Initialize an empty list
res = []

# Using a loop to create tuples and add them to the list
for i in range(len(a)):
    res.append((a[i], b[i]))

print(res)

# Creating a list of tuples using list comprehension
a = [(x, x ** 2) for x in range(5)]
print(a)

a = [[1, 'apple'], [2, 'orange'], [3, 'cherry']]

# List comprehension to create a list of tuples
a = [tuple(x) for x in a]
print(a)

"""
Using zip()
We can create a list of tuples from any number of list using the zip() function. The zip() 
function takes multiple lists and create pairs of elements from all the list and returns a zip object, 
after that we need to convert this zip object back to list.

"""
# Two lists with ids and name
a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']

# Zip the lists and convert back into a list
a = list(zip(a, b))
print(a)

a = [[1, 'apple'], [2, 'orange'], [3,'cherry']]

# Using map to convert each list to a tuple
b = list(map(tuple, a))

print(b)

print("--------------------5554")

tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple.count(3))

# Creating tuples
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
Tuple2 = ('python', 'geek', 'python','for', 'GFG', 'python', 'geeks')

# count the appearance of 3
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# count the appearance of python
res = Tuple2.count('python')
print('Count of Python in Tuple2 is:', res)

print("----33")

# Creating tuples
Tuple = (0, 1, "GFG", [3,2], 1,[3, 2], 'geeks', (0), ('G', 'F'))

# count the appearance of [3, 2]
res = Tuple.count([3, 2])
print('Count of [3, 2] in Tuple is:', res)

my_tuple = ((1, 2), ('a', 'b'), (1, 2), ('c', 'd'), ('a', 'b'))
count_tuple = my_tuple.count((1, 2))
print(count_tuple)
count_xy = my_tuple.count(('x', 'y'))
print(count_xy)

print("--------------------------222")

"""
Example 2: Using tuple max() Method for string elements
Here we are finding the maximum element out of the tuple that constitutes
 string elements based on length.

"""
# Creating tuples
Tuple = ( "Geeks", "For", "Geeks", "GeeksForGeeks")

res = max(Tuple)
print('Maximum of Tuple is', res)

# alphabets tuple
alphabets = ('GFG', 'gfg', 'gFg', 'GfG', 'Gfg')

res = max(alphabets)
print('Maximum of Tuple is', res)

# Creating tuples
Tuple = ( -1, 3, 4, -2, 5, 6 )

res = min(Tuple)
print('Minimum of Tuple is', res)


# Creating tuples
Tuple = ( "Geeks", "For", "Geeks", "GeeksForGeeks")

res = min(Tuple)
print('Minimum of Tuple is', res)

print("--------------------3434")
# remove empty list

a = [(1, 2), (), (3, 4), (), (5,)]
res = []

# Iterate over the list 'a'
for t in a:

    # If tuple is not empty then add it to res.
    if t:
        res.append(t)

print(res)


a = [(1, 2), (), (3, 4), (), (5,)]
res = [t for t in a if t]

print(res)


a = [(1, 2), (), (3, 4), (), (5,)]

res = list(filter(lambda t: t, a))

# By using None as the first parameter in filter,
# it removes any falsy values (like empty tuples)

# res = list(filter(None, a)) # This will also work

print(res)


# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


# Driver Code
tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
print(Reverse(tuples))


# Reversing a list using reversed()
def Reverse(tuples):
	new_tup = ()
	for k in reversed(tuples):
		new_tup = new_tup + (k,)
	print new_tup

# Driver Code
tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)


def reverse_tuple(t):
	new_tuple = ()
	for i in range(len(t)-1, -1, -1):
		new_tuple += (t[i],)
	return new_tuple

tuples = ('z','a','d','f','g','e','e','k')
print(reverse_tuple(tuples))
# Output: ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')

# recursive function
def reverse_tuple(t):
#condition checking
	if len(t) == 0:
		return t
	else:
		return(t[-1],)+reverse_tuple(t[:-1])
original_tuple = ('z','a','d','f','g','e','e','k')
# function call
reversed_tuple = reverse_tuple(original_tuple)
print("Original Tuple: ", original_tuple)
print("Reversed Tuple: ", reversed_tuple)

print("-----------------------------------------766")


tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
rev_strineg = ''.join(tuples)[::-1]
rev_tuples1 = tuple(rev_strineg)
print(rev_tuples1)

# Python3 code to demonstrate
# get nth tuple element from list
# using list comprehension

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using list comprehension to get names
res = [lis[1] for lis in test_list]

# printing result
print("List with only nth tuple element (i.e names) : " + str(res))
print("---------------------------------876")
# Python3 code to demonstrate
# get nth tuple element from list
# using map() + itemgetter()
from operator import itemgetter

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using map() + itemgetter() to get names
res = list(map(itemgetter(1), test_list))

# printing result
print("List with only nth tuple element (i.e names) : " + str(res))

print("------------------------7654")
# Python code to demonstrate
# get nth tuple element from list
# using zip()

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using zip() to get names
res = list(zip(*test_list)[1])

# printing result
print("List with only nth tuple element (i.e names) : " + str(res))

print("---------------987")

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is:", test_list)

# using the map function and a lambda function to access the nth element of each tuple
n = 1 # specify the index of the element to access
res = list(map(lambda x: x[n], test_list))

# printing result
print("List with only nth tuple element:", res)
#This code is contributed by Edula Vinay Kumar Reddy

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is:", test_list)
print("-----------------------------------------7678")

# using a for loop to access the nth element of each tuple
n = 1 # specify the index of the element to access
res = []
for tup in test_list:
	res.append(tup[n])

# printing result
print("List with only nth tuple element:", res)

print("-----------------6786")

# Python3 code to demonstrate
# get nth tuple element from list
# using reduce()

from functools import reduce

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using reduce() to get nth tuple element
n = 1 # replace n with the index of the tuple element you want
res = reduce(lambda acc, tup: acc + [tup[n]], test_list, [])

# printing result
print("List with only nth tuple element (i.e names) : " + str(res))

print("---------------234")
# import numpy module
import numpy as np

# initialize list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# print original list
print("The original list is : " + str(test_list))

# convert list of tuples to a 2D numpy array
arr = np.array(test_list)

# specify the index of the element to access
n = 1

# extract the nth column from the
# array using fancy indexing
res_arr = arr[:, n]

# convert the resulting 1D numpy
# array to a list
res = res_arr.tolist()

# print list with only the nth tuple element
print("List with only nth tuple element (i.e names) : " + str(res))
print("-------------------------6789")
a = ("Jenifer", "Sally", "Jane")
x = sorted(a, key=len) # len gives length
print(x)

def myfunc(n):
  return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)

# Python code to sort the tuples using float element
# Function to sort using sorted()
def Sort(tup):
	# reverse = True (Sorts in Descending order)
	# key is set to sort using float elements
	# lambda has been used
	return(sorted(tup, key = lambda x: float(x[1]), reverse = True))

# Driver Code
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
	('anand', '4.256'), ('gaurav', '10.365')]
print(Sort(tup))


# Python code to sort the tuples using float element
# Inplace way to sort using sort()
def Sort(tup):
	# reverse = True (Sorts in Descending order)
	# key is set to sort using float elements
	# lambda has been used
	tup.sort(key = lambda x: float(x[1]), reverse = True)
	print(tup)

# Driver Code
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
	('anand', '4.256'), ('gaurav', '10.365')]
Sort(tup)


# Python3 code to demonstrate working of
# Ways to concatenate tuples
# using + operator

# initialize tuples
test_tup1 = (1, 3, 5)
test_tup2 = (4, 6)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Ways to concatenate tuples
# using + operator
res = test_tup1 + test_tup2

# printing result
print("The tuple after concatenation is : " + str(res))



# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + lambda

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using map() + lambda
res = tuple(map(lambda i, j: i & j, test_tup1, test_tup2))

# printing result
print("Resultant tuple after AND operation : " + str(res))

# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + iand()
import operator

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using map() + iand()
res = tuple(map(operator.iand, test_tup1, test_tup2))

# printing result
print("Resultant tuple after AND operation : " + str(res))

# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using List comprehension

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using List comprehension
res = tuple([i & j for i,j in zip(test_tup1, test_tup2)])

# printing result
print("Resultant tuple after AND operation : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy


def bitwise_and_tuples(tup1, tup2):
	result = []
	for i in range(len(tup1)):
		result.append(tup1[i] & tup2[i])
	return tuple(result)
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)
res = bitwise_and_tuples(test_tup1, test_tup2)
print(res)



#sum
# Python 3 code to demonstrate working of
# Tuple elements inversions
# Using map() + list() + sum()

# initializing tup
test_tup = ([7, 8], [9, 1], [10, 7])

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))

# printing result
print("The summation of tuple elements are : " + str(res))


# Python3 code to demonstrate working of
# Removing duplicates from tuple
# using tuple() + set()

# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Removing duplicates from tuple
# using tuple() + set()
res = tuple(set(test_tup))

# printing result
print("The tuple after removing duplicates : " + str(res))


# Python3 code to demonstrate working of
# Removing duplicates from tuple
# using OrderedDict() + fromkeys()
from collections import OrderedDict

# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Removing duplicates from tuple
# using OrderedDict() + fromkeys()
res = tuple(OrderedDict.fromkeys(test_tup).keys())

# printing result
print("The tuple after removing duplicates : " + str(res))


# Python3 code to demonstrate working of
# Removing duplicates from tuple

# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Removing duplicates from tuple
x=[]
for i in test_tup:
	if i not in x:
		x.append(i)
res=tuple(x)

# printing result
print("The tuple after removing duplicates : " + str(res))


# Python3 code to demonstrate working of
# Removing duplicates from tuple using list comprehension

# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Removing duplicates from tuple using list comprehension
# creating a list of only unique elements from the tuple
res = tuple([x for i, x in enumerate(test_tup) if x not in test_tup[:i]])

# printing result
print("The tuple after removing duplicates : " + str(res))
#This code is contributed by Vinay Pinjala.


# Python3 code to demonstrate working of
# Removing duplicates from tuple using Counter() from collections module

# import Counter from collections module
from collections import Counter

# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Removing duplicates from tuple using Counter() from collections module
# creating a tuple from Counter dictionary keys
res = tuple(Counter(test_tup).keys())

# printing result
print("The tuple after removing duplicates : " + str(res))


# Python3 code to demonstrate working of
# Check if element is present in tuple
# using loop

# initialize tuple
test_tup = (10, 4, 5, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize N
N = 6

# Check if element is present in tuple
# using loop
res = False
for ele in test_tup:
	if N == ele:
		res = True
		break

# printing result
print("Does tuple contain required value ? : " + str(res))

# Python3 code to demonstrate working of
# Check if element is present in tuple
# Using in operator

# initialize tuple
test_tup = (10, 4, 5, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize N
N = 6

# Check if element is present in tuple
# Using in operator
res = N in test_tup

# printing result
print("Does tuple contain required value ? : " + str(res))

t = (10, 4, 5, 6, 8)
n = 6
x = [i for i in t if i == n]
print(["yes" if x else "no"])

t = (10, 4, 5, 6, 8)
n = 6
x112 = tuple(filter(lambda i: (i == n), t))
print(["yes" if x112 else "no"])

# Python3 code to demonstrate working of
# Check if element is present in tuple
# using loop

# initialize tuple
test_tup = (10, 4, 5, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize N
N = 6

# Check if element is present in tuple
# using loop
res = False
if(test_tup.count(N) >= 1):
	res = True
# printing result
print("Does tuple contain required value ? : " + str(res))




























"""
Tuple Operations in Python
Last Updated : 11 Apr, 2025
Python Tuple is a collection of objects separated by commas. A tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.




# Note : In case of list, we use square
# brackets []. Here we use round brackets ()
tup = (10, 20, 30)

print(tup)
print(type(tup))

Output
(10, 20, 30)
<class 'tuple'>
What is Immutable in Tuples?
Unlike Python lists, tuples are immutable. Some Characteristics of Tuples in Python.

Like Lists, tuples are ordered and we can access their elements using their index values
We cannot update items to a tuple once it is created.
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created.
Let us see this with an example.




tup = (1, 2, 3, 4, 5)

# tuples are indexed
print(tup[1])
print(tup[4])

# tuples contain duplicate elements
tup = (1, 2, 3, 4, 2, 3)
print(t)

# updating an element
tup[1] = 100
print(tup)
Output:

2
5
(1, 2, 3, 4, 2, 3)
Traceback (most recent call last):
  File "Solution.py", line 12, in <module>
    t[1] = 100
TypeError: 'tuple' object does not support item assignment
Accessing Values in Python Tuples
Tuples in Python provide two ways by which we can access the elements of a tuple.

Python Access Tuple using a Positive Index
Using square brackets we can get the values from tuples in Python.




tup = (10, 5, 20)

print("Value in tup[0] = ", tup[0])
print("Value in tup[1] = ", tup[1])
print("Value in tup[2] = ", tup[2])

Output
Value in tup[0] =  10
Value in tup[1] =  5
Value in tup[2] =  20
Access Tuple using Negative Index
In the above methods, we use the positive index to access the value in Python, and here we will use the negative index within [].




tup = (10, 5, 20)

print("Value in tup[-1] = ", tup[-1])
print("Value in tup[-2] = ", tup[-2])
print("Value in tup[-3] = ", tup[-3])

Output
Value in tup[-1] =  20
Value in tup[-2] =  5
Value in tup[-3] =  10
Different Operations Related to Tuples
Below are the different operations related to tuples in Python:

Traversing Items of Python Tuples
Like List Traversal, we can traverse through a tuple using for loop.




# Define a tuple
tup = (1, 2, 3, 4, 5)

# Traverse through each item in the tuple
for x in tup:
    print(x, end=" ")

Output
1 2 3 4 5
Concatenation of Python Tuples
To Concatenation of Python Tuples, we will use plus operators(+).




# Code for concatenating 2 tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')

# Concatenating above two
print(tup1 + tup2)

Output
(0, 1, 2, 3, 'python', 'geek')
Nesting of Python Tuples
A nested tuple in Python means a tuple inside another tuple.




# Code for creating nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')

tup3 = (tup1, tup2)
print(tup3)

Output
((0, 1, 2, 3), ('python', 'geek'))
Repetition Python Tuples
We can create a tuple of multiple same elements from a single element in that tuple.




# Code to create a tuple with repetition
tup = ('python',)*3
print(tup)

Output
('python', 'python', 'python')
Try the above without a comma and check. You will get tuple3 as a string ‘pythonpythonpython’.

Slicing Tuples in Python
Slicing a Python tuple means dividing a tuple into small tuples using the indexing method. In this example, we slice the tuple from index 1 to the last element. In the second print statement, we printed the tuple using reverse indexing. And in the third print statement, we printed the elements from index 2 to 4.




# code to test slicing
tup = (0 ,1, 2, 3)

print(tup[1:])
print(tup[::-1])
print(tup[2:4])

Output
(1, 2, 3)
(3, 2, 1, 0)
(2, 3)
Note: In Python slicing, the end index provided is not included.

Deleting a Tuple in Python
In this example, we are deleting a tuple using ‘del’ keyword. The output will be in the form of error because after deleting the tuple, it will give a NameError.

Note: Remove individual tuple elements is not possible, but we can delete the whole Tuple using Del keyword.




# Code for deleting a tuple
tup = ( 0, 1)

del tup
print(tup)
Output:

Hangup (SIGHUP)
Traceback (most recent call last):
  File "Solution.py", line 5, in <module>
    print(t)
NameError: name 't' is not defined
Finding the Length of a Python Tuple
To find the length of a tuple, we can use Python’s len() function and pass the tuple as the parameter.




# Code for printing the length of a tuple
tup = ('python', 'geek')
print(len(tup))

Output
2
Multiple Data Types With Tuple
Tuples in Python are heterogeneous in nature. This means tuples support elements with multiple datatypes.




# tuple with different datatypes
tup = ("immutable", True, 23)
print(tup)

Output
('immutable', True, 23)
Converting a List to a Tuple
We can convert a list in Python to a tuple by using the tuple() constructor and passing the list as its parameters.




# Code for converting a list and a string into a tuple
a = [0, 1, 2]
tup = tuple(a)

print(tup)

Output
(0, 1, 2)
Output:

Tuples take a single parameter which may be a list, string, set, or even a dictionary(only keys are taken as elements), and converts them to a tuple.

Tuples in a Loop
We can also create a tuple with a single element in it using loops.




# python code for creating tuples in a loop
tup = ('gfg',)

# Number of time loop runs
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

Output
(('gfg',),)
((('gfg',),),)
(((('gfg',),),),)
((((('gfg',),),),),)
(((((('gfg',),),),),),)
Different Ways of Creating a Tuple
Using round brackets
Without Brackets
Tuple Constructor
Empty Tuple
Single Element Tuple
Using Tuple Packing
Using Round Brackets



tup = ("gfg", "Python")
print(tup)

Output
('gfg', 'Python')
Using Comma Separated



# Creating a tuple without brackets
tup = 4, 5, 6
print(tup)

Output
(4, 5, 6)
Using Tuple Constructor



# Creating a tuple using the tuple() constructor
tup = tuple([7, 8, 9])
print(tup)

Output
(7, 8, 9)
Creating an Empty Tuple



# Creating an empty tuple
tup = ()
print(tup)

Output
()
Single Element Tuple



# Creating a single-element tuple
tup = (10, ) # Comma is important here
print(tup)  # Output: (10,)
print(type(tup))

# What if we do not use comma
tup = (10) # This an integer (not a tuple)
print(tup)
print(type(tup))

Output
(10,)
<class 'tuple'>
10
<class 'int'>
Tuple Packing



# Tuple packing
a, b, c = 11, 12, 13
tup = (a, b, c)
print(tup)

Output
(11, 12, 13)
Tuple Built-In Methods
Tuples support only a few methods due to their immutable nature. The two most commonly used methods are count() and index()

Built-in-Method	Description
index( )	Find in the tuple and returns the index of the given value where it’s available
count( )	Returns the frequency of occurrence of a specified value
Tuple Built-In Functions
Built-in Function	Description
all()	Returns true if all element are true or if tuple is empty
any()	return true if any element of the tuple is true. if tuple is empty, return false
len()	Returns length of the tuple or size of the tuple
enumerate()	Returns enumerate object of tuple
max()	return maximum element of given tuple
min()	return minimum element of given tuple
sum()	Sums up the numbers in the tuple
sorted()	input elements in the tuple and return a new sorted list
tuple()	Convert an iterable to a tuple.
Tuples VS Lists
Similarities	Differences
Functions that can be used for both lists and tuples:

len(), max(), min(), sum(), any(), all(), sorted()

Methods that cannot be used for tuples:

append(), insert(), remove(), pop(), clear(), sort(), reverse()

Methods that can be used for both lists and tuples:

count(), Index()

we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) data types.
Tuples can be stored in lists.	Iterating through a ‘tuple’ is faster than in a ‘list’.
Lists can be stored in tuples.	‘Lists’ are mutable whereas ‘tuples’ are immutable.
Both ‘tuples’ and ‘lists’ can be nested.	Tuples that contain immutable elements can be used as a key for a dictionary.

"""

"""
Python Tuple Methods
Last Updated : 22 Jul, 2021
Python Tuples is an immutable collection of that are more like lists. Python Provides a couple of methods to work with tuples. In this article, we will discuss these two methods in detail with the help of some examples.

Count() Method
The count() method of Tuple returns the number of times the given element appears in the tuple.

Syntax:

tuple.count(element)
Where the element is the element that is to be counted.

Example 1: Using the Tuple count() method




# Creating tuples
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
Tuple2 = ('python', 'geek', 'python',
          'for', 'java', 'python')

# count the appearance of 3
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# count the appearance of python
res = Tuple2.count('python')
print('Count of Python in Tuple2 is:', res)
Output:

Count of 3 in Tuple1 is: 3
Count of Python in Tuple2 is: 3
Example 2: Counting tuples and lists as elements in Tuples




# Creating tuples
Tuple = (0, 1, (2, 3), (2, 3), 1,
         [3, 2], 'geeks', (0,))

# count the appearance of (2, 3)
res = Tuple.count((2, 3))
print('Count of (2, 3) in Tuple is:', res)

# count the appearance of [3, 2]
res = Tuple.count([3, 2])
print('Count of [3, 2] in Tuple is:', res)
Output:

Count of (2, 3) in Tuple is: 2
Count of [3, 2] in Tuple is: 1
Index() Method
The Index() method returns the first occurrence of the given element from the tuple.

Syntax:

tuple.index(element, start, end)
Parameters:

element: The element to be searched.
start (Optional): The starting index from where the searching is started
end (Optional): The ending index till where the searching is done
Note: This method raises a ValueError if the element is not found in the tuple.

Example 1: Using Tuple Index() Method




# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# getting the index of 3
res = Tuple.index(3)
print('First occurrence of 3 is', res)

# getting the index of 3 after 4th
# index
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)
Output:

First occurrence of 3 is 3
First occurrence of 3 after 4th index is: 5
Example 2: Using Tuple() method when the element is not found




# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# getting the index of 3
res = Tuple.index(4)
Output:

ValueError: tuple.index(x): x not in tuple

"""
"""
Create a List of Tuples in Python
Last Updated : 14 Feb, 2025
The task of creating a list of tuples in Python involves combining or transforming multiple data elements into a sequence of tuples within a list. Tuples are immutable, making them useful when storing fixed pairs or groups of values, while lists offer flexibility for dynamic collections. For example, given two separate lists like [1, 2, 3] and [‘apple’, ‘orange’, ‘cherry’], the goal is to combine them into a list of tuples like [(1, ‘apple’), (2, ‘orange’), (3, ‘cherry’)].

Using zip()
zip() is the most efficient approach to combine two or more separate lists into a list of tuples. It pairs elements from each list based on their index and stops when the shortest list ends. This method is optimized, making it fast and memory efficient and is preferred for combining data into tuples.




a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']

res = list(zip(a, b))

print(res)

Output
[(1, 'apple'), (2, 'orange'), (3, 'cherry')]
Explanation: zip() pairs elements from lists a and b by index, creating tuples like (a[0], b[0]), (a[1], b[1]), etc. and returns an iterator, which is converted into a list using list().

Table of Content

Using map()
Using list comprehension
Using for loop
Using map()
map() is the most efficient approach to convert a list of lists into a list of tuples. It applies the tuple() constructor to each sublist, transforming each inner list into a tuple. This approach is optimized, making it faster than list comprehension when working with nested lists. It is highly recommended when transforming list-based data into tuples.




a = [[1, 'apple'], [2, 'orange'], [3, 'cherry']]

res = list(map(tuple, a))
print(res)

Output
[(1, 'apple'), (2, 'orange'), (3, 'cherry')]
Explanation: map() converts each inner list in a into a tuple by applying tuple() to every sublist. It returns an iterator, which is converted into a list using list().

Using list comprehension
This method combines zip() with list comprehension to form a list of tuples. It is slightly less efficient than bare zip() due to the extra comprehension layer, but it offers more flexibility and readability when additional operations need to be performed while pairing data from two lists. It is frequently used for clarity in custom logic scenarios.




a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']

res = [(x, y) for x, y in zip(a, b)]

print(res)

Output
[(1, 'apple'), (2, 'orange'), (3, 'cherry')]
Explanation :list comprehension pairs elements from a and b using zip(), forming (x, y) tuples and produces a list of tuples as the result.

Using for loop
This traditional approach involves iterating through two separate lists using a for loop and append() to build a list of tuples manually. While functional, it is less efficient compared to zip() because Python-level loops introduce overhead. This method is still useful when detailed control over the loop is required, but it is not recommended for simple tuple creation tasks.




a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']

res = []
for i in range(len(a)):
    res.append((a[i], b[i]))

print(res)

Output
[(1, 'apple'), (2, 'orange'), (3, 'cherry')]
Explanation: for loop iterates over indices of a and b using range(len(a)), forming tuples (a[i], b[i]), and appends them to res.

"""
"""
How to Take a Tuple as an Input in Python?
Last Updated : 19 Nov, 2024
Tuples are immutable data structures in Python making them ideal for storing fixed collections of items. In many situations, you may need to take a tuple as input from the user. Let's explore different methods to input tuples in Python.

The simplest way to take a tuple as input is by using the split() method to convert a single input string into individual elements and then converting that list into a tuple. Suitable for cases where you expect the user to input all elements in a single line.


# Taking input
a = input("Enter elements separated by spaces: ").split()

# Converting list to tuple
t = tuple(a)
print(t)
Output:

Enter elements separated by spaces: 1 2 3 4 5
('1', '2', '3', '4', '5')
Explanation: The split() method splits the input string based on whitespace (by default), creating a list of elements. tuple(l) converts the list to a tuple.

We can also use map() in case of Homogeneous data types. This method allows you to take a single line of space-separated input, convert each element to a specified type (like integers), and store them in a tuple.


# Taking multiple integer inputs from the user
t = tuple(map(int, input("Enter elements separated by spaces: ").split()))
print(t)




Let's take a look at other methods of taking tuple as input in python:

Table of Content

Using a for Loop(When you Know Tuple Size beforehand)
Using map()(Taking Multiple Inputs in Single Line)
Using List Comprehension(Input collection and conversion in a single line)


Using eval()
eval() method allows to directly input a tuple in standard tuple syntax, which eliminates the need of additional conversion.


# Direct tuple input
t = eval(input("Enter a tuple: "))  # Ex: (1, 2, 3)
print(t)
Output:

Enter a tuple: (10, 20, 30) 
(10, 20, 30)
Using a for Loop
A more flexible approach is to use a for loop to collect user input, which is useful when individual inputs need validation.


# Taking input
n = int(input("Enter the number of elements: "))
a = []
for _ in range(n):
    val = input(f"Enter element {_ + 1}: ")
    a.append(val)

# Converting list to tuple
t = tuple(a)

print(t)
Output:

Enter the number of elements: 3
Enter element 1: 23
Enter element 2: 45
Enter element 3: 12
('23', '45', '12')
Explanation: It first prompts for the number of elements and uses a for loop to collect input one element at a time and at the end appends each input to a list which is then converted to a tuple.

Using List Comprehension
List comprehension offers a concise way to collect inputs and convert them into a tuple. It combines input collection and conversion in a single line and provides a clean and readable solution for collecting inputs.




# Taking input
n = int(input("Enter the number of elements: "))
t = tuple(input(f"Enter element : ") for i in range(n))

print(t)
Output:

Enter the number of elements: 4
Enter element : apple
Enter element : banana
Enter element : cherry
Enter element : date
('apple', 'banana', 'cherry', 'date')
Explanation: It first collects inputs using list comprehension in a single line and then converts the collected input list directly into a tu

"""


"""
Tuples in Python are immutable, which means their elements cannot be directly changed, added, or removed after creation. However, you can effectively "add" items to a tuple by creating a new tuple that incorporates the desired elements.
Here are the common methods to achieve this: Tuple Concatenation (+ operator).
This is the most straightforward way to add elements to a tuple. You combine the original tuple with another tuple (containing the new element(s)) using the + operator. This operation results in a new tuple.
Python

    my_tuple = (1, 2, 3)
    new_element = 4
    updated_tuple = my_tuple + (new_element,) # Note the comma for a single-element tuple
    print(updated_tuple)
You can also concatenate with a tuple containing multiple elements: 
Python

    my_tuple = (1, 2, 3)
    new_elements = (4, 5, 6)
    updated_tuple = my_tuple + new_elements
    print(updated_tuple)
Type Conversion (Tuple to List, Modify, List to Tuple):
If you need to perform more complex modifications like inserting elements at specific positions, converting the tuple to a list is a flexible approach. Lists are mutable, allowing you to use methods like append(), insert(), or extend(). After modification, convert the list back to a tuple.
Python

    my_tuple = (1, 2, 3)
    temp_list = list(my_tuple)
    temp_list.append(4)
    updated_tuple = tuple(temp_list)
    print(updated_tuple)
To insert at a specific index:
Python

    my_tuple = (1, 2, 3)
    temp_list = list(my_tuple)
    temp_list.insert(1, 99) # Insert 99 at index 1
    updated_tuple = tuple(temp_list)
    print(updated_tuple)
"""









"""
Enumerate() in Python
Last Updated : 20 Jan, 2025
enumerate() function adds a counter to each item in a list or other iterable. It turns the iterable into something we can loop through, where each item comes with its number (starting from 0 by default). We can also turn it into a list of (number, item) pairs using list().

Let’s look at a simple example of an enumerate() with a list.




a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))

Output
Index 0: Geeks
Index 1: for
Index 2: Geeks
[(0, 'Geeks'), (1, 'for'), (2, 'Geeks')]
Explanation: enumerate(a) provides both the index (i) and the element (name) during iteration.

Table of Content

Syntax of enumerate() method
Using a Custom Start Index
Using Enumerate object in Loops
Accessing the Next Element
Syntax of enumerate() method
enumerate(iterable, start=0)


Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is to be started, by default it is 0
Return:
Returns an iterator with index and element pairs from the original iterable
Using a Custom Start Index
By using enumrate() starts indexing from 0, we can customize this using the start parameter. if want the index to begin at value other than 0.




a = ["geeks", "for", "geeks"]

#Looping through the list using enumerate
# starting the index from 1
for index, x in enumerate(a, start=1):
    print(index, x)

Output
1 geeks
2 for
3 geeks
Using Enumerate object in Loops
Enumerate() is used with a list called a. It first prints tuples of index and element pairs. Then it changes the starting index while printing them together. Finally, it prints the index and element separately, each on its own line.




a = ["Geeks", "for", "Geeks"]

# printing the tuples in object directly
for ele in enumerate(a):
    print (ele)

Output
(0, 'Geeks')
(1, 'for')
(2, 'Geeks')
Accessing the Next Element
In Python, the enumerate() function serves as an iterator, inheriting all associated iterator functions and methods. Therefore, we can use the next() function and __next__() method with an enumerate object.




a = ['Geeks', 'for', 'Geeks']

# Creating an enumerate object from the list 'a'
b = enumerate(a)

# This retrieves the first index-element pair from 'b'
nxt_val = next(b)
print(nxt_val)

Output
(0, 'Geeks')
We can call next() again to retrieve subsequent elements:




next_element = next(b)
print(b)
Output:

(1, 'for')
Each time the next() is called, the internal pointer of the enumerate object moves to the next element, returning the corresponding tuple of index and value.

"""






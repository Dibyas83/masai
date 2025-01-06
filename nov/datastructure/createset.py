"""
Sets in Python
Last Updated : 19 Dec, 2024
A Set in Python is used to store a collection of items with the following properties.

No duplicate elements. If try to insert the same item again, it overwrites previous one.
An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
True and 1 is considered the same value


"""
# typecasting list to set
s123 = set(["a", "b", "c"])
print(s123)

# Adding element to the set
s123.add("d")
print(s123)
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset10 = {"apple", "banana", "cherry"}
thisset10.add("orange")

print("banana" in thisset10)

thisset11 = {"apple", "banana", "cherry"}
print("banana" not in thisset11)


thisset22 = {"apple", "banana", "cherry"}
tropical22 = {"pineapple", "mango", "papaya"}
thisset22.update(tropical22)
print(thisset22)


thisset33 = {"apple", "banana", "cherry"}
mylist33 = ["kiwi", "orange"]
thisset33.update(mylist33)
# thisset33.remove("anana")
thisset33.discard("anana")
x = thisset33.pop()

print(thisset33)

"""
If the item to remove does not exist, remove() will raise an error.
The return value of the pop() method is the removed item.
The clear() method empties the set:
The del keyword will delete the set completely:
The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.

The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.


The & operator only allows you to join sets with sets, and not with other data types
 like you can with the intersection() method.
 The intersection_update() method will also keep ONLY the duplicates, but it will 
 change the original set instead of returning a new set.

The difference_update() method will also keep the items from the first set that are not in the other set, but 
it will change the original set instead of returning a new set.

The symmetric_difference() method will keep only the elements that are NOT present in both sets.
The symmetric_difference_update() method will also keep all but the duplicates, but it will 
change the original set instead of returning a new se


    Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

"""
thisset44 = {"apple", "banana", "cherry"}
thisset44.clear()
print(thisset44)

thisset49 = {"apple", "banana", "cherry","rty"}
del thisset49
# print(thisset49)

set1 = {"a", "b", "c",1,2}
set2 = {1, 2, 3}
set11 = {1, 2, 3,4,"y","z"}

set3 = set1.union(set2)
myset26 = set1.union(set2, set3, set11)
set4 = set1 | set11
myset23 = set1 | set2 | set3 |set4
set31 = set1.intersection(set2)
set32 = set1 & set2

# Python3 program for intersection() function
set11 = {2, 4, 5, 6}
set22 = {4, 6, 7, 8}
set33 = {1, 0, 12}

print(set1 & set2)
print(set1 & set3)

print(set1 & set2 & set3)


set1 = set(set11)
set2 = set(set22)

# union of two empty sets
print("set1 intersection set2 : ",set(set1).intersection(set(set2)))


set39 = set1 - set2
set42 = set1.symmetric_difference(set2)
set43 = set1 ^ set2
set1.symmetric_difference_update(set2) # unique removed

# Program to perform different set operations
# as we do in mathematics

# sets are define
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)


print(set3)
print(set4)
print(myset23)
print(myset26)
print(set31)
print(set32)
# print(set38)
print(set39)
print(set42)
print(set43)

x1 = {"a", "b", "c"}
y = (1, 2, 3)

z = x1.union(y)
print(z)

set15= {"apple", "banana", "cherry"}
set25 = {"google", "microsoft", "apple"}
set15.intersection_update(set25)
print(set15)

set1 = {"apple", "banana", "cherry","ert"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

set3 = set1.symmetric_difference(set2)

"""
Python Frozen Sets
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. It can be done with frozenset() method in Python.

While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

If no parameters are passed, it returns an empty frozenset.
"""
# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
s = set(["a", "b","c"])

print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])
# fs.add("h")

print("\nFrozen Set")
print(fs)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set

# Python Program to
# demonstrate union of
# two sets

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union()
# function
population = people.union(vampires)

print("Union using union() function")
print(population)

# Union using "|"
# operator
population = people|dracula

print("\nUnion using '|' operator")
print(population)

# Python program to
# demonstrate intersection
# of two sets

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Intersection using
# intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using
# "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)

# Create a set
my_set = {1, 2, 3, 4, 5}

# Check if an element is in the set
if 3 in my_set:
    print("Element found in the set")
else:
    print("Element not found in the set")


# import random module
import random

# create a set with integer elements
data = {7058, 7059, 7072, 7074, 7076}


# check 7058
print(7058 in data)

# check 7059
print(7059 in data)

# check 7071
print(7071 in data)

# import random module
import random

# create a set with integer elements
data = {7058, 7059, 7072, 7074, 7076}


# check 7058
print(7058 not in data)

# check 7059
print(7059 not in data)

# check 7071
print(7071 not in data)


import operator as op
# create a set with integer elements
data = {7058, 7059, 7072, 7074, 7076}

# check 7058
print(op.countOf(data, 7058) > 0)

# check 7059
print(op.countOf(data, 7059) > 0)

# check 7071
print(op.countOf(data, 7071) > 0)
"""
Using | Operator (Pipe Operator)
The pipe operator internally calls the union() function, which can be used to perform the task of updating
 the Python set with new elements
"""
# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing adding elements
up_ele = [1, 5, 10]

# | performing task of updating
test_set |= set(up_ele)

# printing result
print("Set after adding elements : " + str(test_set))


# initializing set
test_set = {6, 4, 2, 7, 9}
test_list = list(test_set)

# printing original list
print("The original set is : " + str(test_list))

# initializing adding elements
up_ele = [1, 5, 10]

# adding elements to list using list comprehension
test_list += [ele for ele in up_ele if ele not in test_list]

# printing result
print("Set after adding elements : " + str(set(test_list)))
#This code is contributed by Vinay Pinjala.


# import functools
from functools import reduce

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original list
print("The original list is : " + str(test_set))

# initializing adding elements
up_ele = [1, 5, 10]

# using reduce and union function to append elements to set
result_set = reduce(lambda res, ele: res.union(set([ele])), up_ele, test_set)

# printing result
print("Set after adding elements : " + str(result_set))

s1 = {1, 2, 3, 4}
print("Before popping: ",s1)
s1.pop()
s1.pop()
s1.pop()

print("After 3 elements popped, s1:", s1)


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(s2.issubset(s1))

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print(A.issubset(B))
print(B.issubset(A))

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B))
print(B.issubset(A))


print(A.issubset(C))
print(C.issubset(B))

# Python3 code to demonstrate working of
# Symmetric Difference of Multiple sets
# Using Counter() + chain.from_iterable()
from collections import Counter
from itertools import chain

# initializing list
test_list = [{5, 3, 2, 6, 1},
             {7, 5, 3, 8, 2},
             {9, 3},
             {0, 3, 6, 7}]

# printing original list
print("The original list is : " + str(test_list))

# getting frequencies using Counter()
# from_iterable() flattens the list
freq = Counter(chain.from_iterable(test_list))

# getting frequency count 1
res = {idx for idx in freq if freq[idx] == 1}

# printing result
print("Symmetric difference of multiple list : " + str(res))

# Python3 code to demonstrate working of
# Symmetric Difference of Multiple sets
# Using Counter() + chain.from_iterable() + items()
from collections import Counter
from itertools import chain

# initializing list
test_list = [{5, 3, 2, 6, 1},
             {7, 5, 3, 8, 2},
             {9, 3}, {0, 3, 6, 7}]

# printing original list
print("The original list is : " + str(test_list))

# clubbing operations using items() to get items
res = {key for key, val in Counter(chain.
                                   from_iterable(test_list)).
items() if val == 1}

# printing result
print("Symmetric difference of multiple list : " + str(res))


















d = [2,3,5,7,2,4,1]
t = [2,3,5,7,2,4,1,99]
d.sort()
t.sort(reverse=True)
print(d)


thislist5 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist4 = ["orange", "mango", "kiwi", "Pineapple", "Banana"]
thislist6 = ["orange", "mango", "kiwi", "Pineapple", "Banana"]
thislist6.sort()
thislist4.sort( key= str.lower)
print(thislist5)
print(thislist6)
print(thislist4)


"""
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""





mylist = ["apple", "banana", "cherry"]
mylist.sort()
print(type(mylist))
print(len(mylist))

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
thislist[1] = "uop"
print(thislist)

"""

You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:

"""

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist11 = ["banana", "Orange", "Kiwi", "cherry"]
thislist11.append("lorange")
thislist11.insert(1, "korange")
tropical = ["mango", "pineapple", "papaya"]
thislist11.extend(tropical)
"""
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:

The clear() method empties the list.

The list still remains, but it has no content.

"""
thistuple22 = ("kiwik", "porange")
thislist11.extend(thistuple22)
thislist11.pop(3)
thislist11.remove("banana")   # first accurence
print(thislist11)
print("===========================88")
thislist11.reverse()
print(thislist11)

thislist88 = ["apple", "banana", "cherry"]

del thislist88[0]
# del thislist

print(thislist88)

thislist55 = ["apple", "banana", "cherry"]
thislist55.clear()
print(thislist55)

thislist45 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist45):
  print(thislist45[i])
  i = i + 1


thislist23 = ["hpple", "tanana", "eherry"]
[print(x) for x in thislist23]

#  list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist34 = []

for x in fruits:
  if "a" in x:
    newlist34.append(x)

print(newlist34)

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist56 = [x for x in fruits1 if "a" in x]

print(newlist56)

newlist55 = [x for x in fruits if x != "apple"]
print(newlist55)

newlist44 = [x for x in range(10)]

newlist69 = [x for x in range(10) if x < 5]

newlist24 = [x.upper() for x in fruits]

newlist25 = ['hello' for x in fruits]

newlist35 = [x if x != "banana" else "orange" for x in fruits]


"""
You cannot copy a list simply by typing list2 = list1, because: list2 
will only be a reference to list1, and changes made in list1 will 
automatically also be made in list2.



"""

thislist76 = ["apple", "banana", "cherry"]
mylist78 = thislist76.copy()
print(mylist78)

thislistb = ["apple", "banana", "cherry"]
mylistab = list(thislistb)
print(mylistab)

thislistb = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


list1 = [5,6,7,8]
list2 = [5,3,8,9]
list3 = list1 + list2
print(list3)

list14 = [11,12]
for x in list2:
  list14.append(x) # single element

print(list14)

list16 = ["a", "b" , "c"]
list26 = [1, 2, 3]

list16.extend(list26)
print(list16)

"""
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
x = 5
c = complex(x)

print(c)

"""
Python does not have a random() function to make a random
 number, but Python has a built-in module called random 
 that can be used to make random numbers:
"""
import random

print(random.randrange(1, 10))









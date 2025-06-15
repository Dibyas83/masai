

"""
ordered = indexed
mutable = can be changed
separated by comas ,multiple data types can be inside it.


append(): Adds an element to the end of the list.
copy(): Returns a shallow copy of the list.
clear(): Removes all elements from the list.
count(): Returns the number of times a specified element appears in the list.
extend(): Adds elements from another list to the end of the current list.
index(): Returns the index of the first occurrence of a specified element.
insert(): Inserts an element at a specified position.
pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
remove(): Removes the first occurrence of a specified element.
reverse(): Reverses the order of the elements in the list.
sort(): Sorts the list in ascending order (by default).
Examples of List Methods
append():
Syntax: list_name.append(element)


In the code below, we will add an element to the list.




a = [1, 2, 3]

# Add 4 to the end of the list
a.append(4)
print(a)

Output
[1, 2, 3, 4]
copy():
Syntax: list_name.copy()


In the code below, we will create a copy of a list.




a = [1, 2, 3]

# Create a copy of the list
b = a.copy()
print(b)

Output
[1, 2, 3]
clear():
Syntax: list_name.clear()


In the code below, we will clear all elements from the list.




a = [1, 2, 3]

# Remove all elements from the list
a.clear()
print(a)

Output
[]
count():
Syntax: list_name.count(element)


In the code below, we will count the occurrences of a specific element in the list.




a = [1, 2, 3, 2]

# Count occurrences of 2 in the list
print(a.count(2))

Output
2
extend():
Syntax: list_name.extend(iterable)


In the code below, we will extend the list by adding elements from another list.




a = [1, 2]

# Extend list a by adding elements from list [3, 4]
a.extend([3, 4])
print(a)

Output
[1, 2, 3, 4]
index():
Syntax: list_name.index(element)


In the code below, we will find the index of a specific element in the list.




a = [1, 2, 3]

# Find the index of 2 in the list
print(a.index(2))

Output
1
insert():
Syntax: list_name.insert(index, element)


In the code below, we will insert an element at a specific position in the list.




a = [1, 3]

# Insert 2 at index 1
a.insert(1, 2)
print(a)

Output
[1, 2, 3]
pop():
Syntax: list_name.pop(index)


In the code below, we will remove the last element from the list.




a = [1, 2, 3]

# Remove and return the last element in the list
a.pop()
print(a)

Output
[1, 2]
remove():
Syntax: list_name.remove(element)


In the code below, we will remove the first occurrence of a specified element from the list.




a = [1, 2, 3]

# Remove the first occurrence of 2
a.remove(2)
print(a)

Output
[1, 3]
reverse():
Syntax: list_name.reverse()


In the code below, we will reverse the order of the elements in the list.




a = [1, 2, 3]

# Reverse the list order
a.reverse()
print(a)

Output
[3, 2, 1]
sort():
Syntax: list_name.sort(key=None, reverse=False)


In the code below, we will sort the elements of the list in ascending order




a = [3, 1, 2]

# Sort the list in ascending order
a.sort()
print(a)

Output
[1, 2, 3]

"""

# slicing is like  string slicing

a = ["app","iot","ui","doc","digit","user"]
print(a[2],"1")
print(a[1:2],"2")
print(a[:2],"3")
print(a[::2],"4") # step of 2
print(a[-2],"5")
print(a[-1],"6")
print(a[-3:-1],"7") # -3,-2 printed
print(a[::-1],"7") # -1 steps
print(a[::-1],"7") # -1 steps

g =0
while g < len(a):
    print(a[g])
    g += 1

print(a.count("ui"))
a.insert(3,"ui")
print(a)
a.remove("digit")
a.pop(2)
print(a)
b = []
b = a.copy()
print(b)
b.append("help")
b.insert(5,"ok")
print(a)
print(b)
a.extend(b)
a.reverse()
a.sort()
e = ""
e = a.sort()
print(a)
print(e)




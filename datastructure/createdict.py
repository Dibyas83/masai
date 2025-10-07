#  A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.


"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)


thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2["model"]
x1 = thisdict2.get("model")
x2 = thisdict.keys()
print(x2)

print(thisdict2)

print(x)
print(x1)
print(x2)
thisdict2["color"] = "white"
thisdict2["year"] = 2018

print(thisdict2)
print("------------------------------888")
print(x2) #after the change
x5 = thisdict2.values()
print(x5)
x6 = thisdict2.items()
if "model" in thisdict2:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
"""
thisdict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict6.update({"year": 2020})
thisdict6.pop("model")
print(thisdict6)
thisdict2.popitem()
print(thisdict2)
"""
ou can use the dictionary update |= operator, represented by the pipe and equal 
sign characters, to update a dictionary in-place with the given dictionary or values.
"""
site = {'Website':'DigitalOcean', 'Tutorial':'How To Add to a Python Dictionary', 'Author':'Sammy'}

guests = {'Guest1':'Dino Sammy', 'Guest2':'Xray Sammy'}

site |= guests

print("site: ", site)

dict1 = {'a':'one', 'b':'two'}
dict2 = {'b':'letter two', 'c':'letter three'}

dict3 = dict1 | dict2

print("dict3: ", dict3)

dict_example = {'a': 1, 'b': 2}

print("original dictionary: ", dict_example)

dict_example['a'] = 100  # existing key, overwrite
dict_example['c'] = 3  # new key, add
dict_example['d'] = 4  # new key, add

print("updated dictionary: ", dict_example)

# add the following if statements

if 'c' not in dict_example.keys():
    dict_example['c'] = 300

if 'e' not in dict_example.keys():
    dict_example['e'] = 5

print("conditionally updated dictionary: ", dict_example)

dict = {'key1': 'geeks', 'key2': 'for'}
print("Current Dict is: ", dict)

# adding dict1 (key3, key4 and key5) to dict
dict1 = {'key3': 'geeks', 'key4': 'is', 'key5': 'fabulous'}
dict.update(dict1)

# by assigning
dict.update(newkey1='portal')
print(dict)
"""
Add New Key value to a Dictionary in Python using Dictionary Comprehension
This code creates a new dictionary updated_dict by unpacking the key-value pairs
 from existing_dict and adding a new key-value pair (new_key: new_value). The
  ** operator is used to unpack the existing dictionary into the new one. The 
  result is printed with the new key-value added.
"""

existing_dict = {'key1': 'value1', 'key2': 'value2'}
new_key = 'key3'
new_value = 'value3'

updated_dict = {**existing_dict, new_key: new_value}
print(updated_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict['key1']  # Removes ‘key1’
print(my_dict)  # Output: {‘key2’: ‘value2’}

# Or using pop()
removed_value = my_dict.pop('key2')  # Also removes ‘key2’ and returns the value
print(my_dict)  # Output: {}
print(removed_value)  # Output: ‘value2’


my_dict = {}
key = input("enter the key: ",)
value = input("Enter the value: ",)
my_dict[key] = value
print(my_dict)

key_value_list = []
n = int(input("Enter number of pairs: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    key_value_list.append({key: value})
print(key_value_list)

# As shown in image

# Creating a Nested Dictionary
Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

Dict = { }
print("Initial nested dictionary:-")
print(Dict)

Dict['Dict1'] = {}

# Adding elements one at a time
Dict['Dict1']['name'] = 'Bob'
Dict['Dict1']['age'] = 21
print("\nAfter adding dictionary Dict1")
print(Dict)

# Adding whole dictionary
Dict['Dict2'] = {'name': 'Cara', 'age': 25}
print("\nAfter adding dictionary Dict1")
print(Dict)


print("---------------------------------------------------------1111")
# the del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely:
# The clear() method empties the dictionary:

# Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
print("----------------------------------------------------")
for j in thisdict:
  print(thisdict[j])

# You can also use the values() method to return values of a dictionary:

for i in thisdict.values():
  print(i)
for y in thisdict.keys():
  print(y)
for m,n in thisdict.items():
  print(m,n)

"""
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().


"""
mydict4 = thisdict.copy()
print(mydict4)
#mydict5 = dict(thisdict)
#print(mydict5)
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily1 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# if you want to add three dictionaries into a new dictionary

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily2["child2"]["name"])
print("----------------------====================")
"""

You can loop through a dictionary by using the items() method like this:

Example
Loop through the keys and values of all nested dictionaries:
"""
for x, obj in myfamily1.items():
  print(x)

  print(obj)

  for y in obj:
    print(y + ':', obj[y])
print("==========================================551")
# Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":- dictionary.setdefault(keyname, value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)

# Create a dictionary with 3 keys, all with the value 0:

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)
"""

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""
# create a python dictionary
d = {"name": "Geeks", "topic": "dict", "task": "iterate"}

# loop over dict values
for val in d.values():
    print(val)
print("---------------------------------566")
# create a python dictionary
d = {"name": "Geeks", "topic": "dict", "task": "iterate"}

# default loooping gives keys
for keys in d:
  print(keys)

# looping through keys
for keys in d.keys():
  print(keys)

# create a python dictionary
d = {"name": "Geeks", "topic": "dict", "task": "iterate"}

# iterating both key and values
for key, value in d.items():
    print(f"{key}: {value}")

print("---------------------------445")

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
map_keys = map(statesAndCapitals.get, statesAndCapitals)
for key in map_keys:
    print(key)


print("-----------------------------------554")
"""
Create a Dictionary in Python
In Python, a dictionary can be created by placing a sequence of elements within
curly {} braces, separated by a ‘comma’. 
In this example, we first declared an empty dictionary D, then added the 
elements from the Python list L into the dictionary
"""
# Initialize an empty dictionary
D = {}

L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]

# Loop to add key-value pair
# to dictionary
for i in range(len(L)):
    # If the key is already
    # present in dictionary
    # then append the value
    # to the list of values
    if L[i][0] in D:
        D[L[i][0]].append(L[i][1])

    # If the key is not present
    # in the dictionary then add
    # the key-value pair
    else:
        D[L[i][0]] = []
        D[L[i][0]].append(L[i][1])

print(D)

"""
In this example, we will add another element to the existing dictionary
 in Python. We are provided with the key and value separately and will add 
 this pair to the dictionary my_dict.
"""
# Key to be added
key_ref = 'More Nested Things'
my_dict = {
    'Nested Things': [{'name', 'thing one'}, {'name', 'thing two'}]
}

# Value to be added
my_list_of_things = [{'name', 'thing three'}, {'name', 'thing four'}]

# try-except to take care of errors
# while adding key-value pair
try:
    my_dict[key_ref].append(my_list_of_things)

except KeyError:
    my_dict = {**my_dict, **{key_ref: my_list_of_things}}

print(my_dict)
"""

# Creating an empty Dictionary
Dict121 = {}
t12 = [(1, 'Geeks'), (2, 'For')]
Dict121 = dict((t12))
print(Dict121)
"""

# Creating a Dictionary
# with each item as a Pair

# Initializing an empty dictionary
squares_dict = {}

# Using a for loop to populate the dictionary
for num in range(1, 6):
    squares_dict[num] = num ** 2

# Displaying the initialized dictionary
print(squares_dict)


# Example list of the tuples
pairs_list = [('a', 1), ('b', 2), ('c', 3)]

# Initializing a dictionary using a for loop and the list of tuples
new_dict = {}
for key, value in pairs_list:
    new_dict[key] = value

# Displaying the initialized dictionary
print(new_dict)


# Using list comprehension to initialize a dictionary
squares_dict_comp = {num: num ** 2 for num in range(1, 6)}

# Displaying the initialized dictionary using the list comprehension
print(squares_dict_comp)



# Python3 code to demonstrate working of
# Initialize dictionary keys with Matrix
# Using list comprehension

# initializing N
num = 4

# Initialize dictionary keys with Matrix
# Using list comprehension
res = {'gfg': [[] for _ in range(num)], 'best': [[] for _ in range(num)]}

# printing result
print("The Initialized dictionary : " + str(res))


# Using for loop
for_loop_person = {}
for key in ['name', 'age']:
    if key == 'name':
        for_loop_person[key] = 'Bob'
    else:
        for_loop_person[key] = 22
print(for_loop_person)
print(type(for_loop_person))


# Using dict.fromkeys()
keys_person = ['name', 'age']
values_person = ['Eva', 35]
fromkeys_person = dict.fromkeys(keys_person, values_person)

print(fromkeys_person)
print(type(fromkeys_person))


# Using Dictionary Comprehension
comprehension_person = {key: 'Alice' if key == 'name' else 28 for key in ['name', 'age']}
print(comprehension_person)
print(type(comprehension_person))


# Python code to initialize a dictionary
# with only keys from a list

# List of keys
keyList = ["Paras", "Jain", "Cyware"]

# initialize dictionary
d = {}

# iterating through the elements of list
for i in keyList:
	d[i] = None

print(d)

# Python code to initialize a dictionary
# with only keys from a list

# List of Keys
keyList = ["Paras", "Jain", "Cyware"]

# Using Dictionary comprehension
myDict = {key: None for key in keyList}
print(myDict)




# Python3 code to demonstrate working of
# Initialize dictionary with multiple keys
# Using loop

# declare dictionary
test_dict = {}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize keys
test_keys = ['gfg', 'is', 'best']

# Using loop
# Initialize dictionary with multiple keys
for keys in test_keys:
	test_dict[keys] = 4

# printing result
print("Dictionary after updating multiple key-value : " + str(test_dict))



# Iterate Through a Dictionary Using List Comprehension
# defining dictionary related to GeeksforGeeks
geeks_data = {'language': 'Python', 'framework': 'Django', 'topic': 'Data Structures'}

keys = [key for key in geeks_data.keys()]
values = [value for value in geeks_data.values()]

# Print keys
print(keys)
for key in keys:
    print(key)

# Print values
print("Values")
for value in values:
    print(value)


# defining dictionary related to GeeksforGeeks
geeks_data = {'language': 'Python', 'framework': 'Django', 'topic': 'Data Structures'}

# Iterate through keys
print('Keys')
for key in geeks_data.keys():
    print(key)

# Iterate through values
print("Values")
for value in geeks_data.values():
    print(value)

"""
Iterate Through Specific Keys in a Dictionary in Python
Last Updated : 27 Nov, 2024
Sometimes we need to iterate through only specific keys in a dictionary rather than going through all of them. We can use various methods to iterate through specific keys in a dictionary in Python.

Using dict.get() Method
"""
d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to check
keys = ["a", "b", "e", "d"]

# Iterate through specific keys using get()
for key in keys:
   # Returns None if key doesn't exist
    value = d.get(key)
    if value is not None:
        print(key, value)



d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to iterate over
keys = ["a", "b", "e", "d"]

for key in keys:
  # Check if key exists in the dictionary
    if key in d:
        print(key, d[key])



d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to iterate over
keys = ["a", "b", "e", "d"]

for key in keys:
  # Check if key exists in the dictionary
    if key in d:
        print(key, d[key])

print("----------------------------------67587")

d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys to filter
keys = ["a", "c", "d"]

# Use filter to get keys that are in d
new_keys = filter(lambda k: k in d, keys)

# Iterate through filtered keys
for key in new_keys:
    print(key, d[key])

# Python3 code to demonstrate working of
# Iterating through value lists dictionary
# Using list comprehension

# Initialize dictionary
test_dict = {'gfg': [1, 2], 'is': [4, 5], 'best': [7, 8]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using list comprehension
# Iterating through value lists dictionary
res = [[i for i in test_dict[x]] for x in test_dict.keys()]

# printing result
print("The list values of keys are : " + str(res))

# Python3 code to demonstrate working of
# Iterating through value lists dictionary
# Using from_iterable() + product() + items()
import itertools

# Initialize dictionary
test_dict = {'gfg': [1, 2], 'is': [4, 5], 'best': [7, 8]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Iterating through value lists dictionary
# Using from_iterable() + product() + items()
res = []
for key, value in (
        itertools.chain.from_iterable(
            [itertools.product((k,), v) for k, v in test_dict.items()])):
    res.append(value)

# printing result
print("The list values of keys are : " + str(res))

# Python3 code to demonstrate working of
# Iterating through value lists dictionary
# Using map() + lambda

# Initialize dictionary
test_dict = {'gfg': [1, 2], 'is': [4, 5], 'best': [7, 8]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Iterating through value lists dictionary
# Using map() + lambda
res = []
for i in test_dict.values():
    res.append(list(map(lambda x: x, i)))

# printing result
print("The list values of keys are : " + str(res))
# This code is contributed by Edula Vinay Kumar Reddy

# Python3 code to demonstrate working of
# Iterating through value lists dictionary
# Using for loop + list comprehension

# Initialize dictionary
test_dict = {'gfg': [1, 2], 'is': [4, 5], 'best': [7, 8]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Iterating through value lists dictionary
# Using for loop + list comprehension
res = []
for val in test_dict.values():

	res.append([x for x in val])

# printing result
print("The list values of keys are : " + str(res))














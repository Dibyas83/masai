

#A List with Duplicates
mylist = ["a", "b", "a", "c", "e"]
mylist2 = ["a", "b", "a", "c", "d"]
mylist = list(dict.fromkeys(mylist2,mylist))
print(mylist)
#Create a dictionary, using the List items as keys. This will automatically remove any duplicates
# because dictionaries cannot have duplicate keys

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"]) # Call the function, with a list as a parameter:

print(mylist)


"""
Dictionaries in Python
Last Updated : 12 Feb, 2025
A Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.

Example: Here, The data is stored in key:value pairs in dictionaries, which makes it easier to find values.




d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
How to Create a Dictionary
In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.




# create dictionary using { }
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
{'a': 'Geeks', 'b': 'for', 'c': 'Geeks'}


From Python 3.7 Version onward, Python dictionary are Ordered.
Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.
Keys must be immutable: This means keys can be strings, numbers, or tuples but not lists.
Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
Dictionary internally uses Hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
Table of Content

Accessing Dictionary Items
Adding and Updating Dictionary Items
Removing Dictionary Items
Iterating Through a Dictionary
Nested Dictionaries
Accessing Dictionary Items
We can access a value from a dictionary by using the key within square brackets orget()method.




d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))  

Output
Alice
Alice
Adding and Updating Dictionary Items
We can add new key-value pairs or update existing keys by using assignment.




d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

Output
{1: 'Python dict', 2: 'For', 3: 'Geeks', 'age': 22}
Removing Dictionary Items
We can remove items from dictionary using the following methods:

del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair.



d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Geeks
Key: 3, Value: Geeks
{}
Iterating Through a Dictionary
We can iterate over keys [using keys() method] , values [using values() method] or both [using item() method] with a for loop.




d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

Output
1
2
age
Geeks
For
22
1: Geeks
2: For
age: 22
Read in detail – Ways to Iterating Over a Dictionary

Nested Dictionaries


Example of Nested Dictionary:




d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(d)


Create a Dictionary with Key as First Character and Value as Words Starting with that Character – Python
Last Updated : 14 Apr, 2025
We are given a string of words and the goal is to group these words into a dictionary where each key is the first character of a word and the corresponding value is a list of all words starting with that character. For example, in “Hello World”, the words “Hello” and “World” start with ‘H’ and ‘W’ respectively, so the result is {‘H’: [‘Hello’], ‘W’: [‘World’]}. Let’s explore different ways to implement this efficiently in Python.

Using collections.defaultdict
defaultdict from the collections module automatically create empty lists for new keys. As you loop through each word, it appends the word to the list based on its first character. It’s highly efficient and it maintains insertion order.




from collections import defaultdict

t = "Hello World"
res = defaultdict(list)

for w in t.split():
    res[w[0]].append(w)

print(dict(res))

Output
{'H': ['Hello'], 'W': ['World']}
Explanation:

defaultdict(list) creates a dictionary with default empty lists for new keys.
t.split() splits the string t into [‘Hello’, ‘World’].
for each word w, append it to res[w[0]], where w[0] is the first character of the word.
Using dict.setdefault()
setdefault() is a dictionary method that simplifies inserting a key if it doesn’t exist. It returns the value if the key exists or sets it to a default (like an empty list) if it doesn’t. This avoids if-else logic and is great when you want a clean, built-in way to group values by keys without importing anything.




t = "Welcome to GeeksForGeeks"
res = {}

for w in t.split():
    res.setdefault(w[0], []).append(w)

print(res)

Output
{'W': ['Welcome'], 't': ['to'], 'G': ['GeeksForGeeks']}
Explanation:

t.split() splits the string t into [‘Welcome’, ‘to’, ‘GeeksForGeeks’].
res.setdefault(w[0], []) ensures the key w[0] (first letter of the word) exists with an empty list if it doesn’t.
append(w) adds the word w to the list at res[w[0]].
Using if condition
This classic approach manually checks if a key (the first character) exists in the dictionary. If it does, it appends the word to the list otherwise, it creates a new list. It’s great for beginners because of its simplicity and it works efficiently while preserving word order.




t = "Hello World"
res = {}

for w in t.split():
    first = w[0]
    if first in res:
        res[first].append(w)
    else:
        res[first] = [w]

print(res)

Output
{'H': ['Hello'], 'W': ['World']}
Explanation:

t.split() splits the string t into [‘Hello’, ‘World’].
For each word w, get the first letter first, check if first exists as a key in res. If yes, append w to the list, else create a new key with a list containing w.
Using dictionary comprehension
This method first creates an ordered list of first characters to preserve input order, then uses dictionary comprehension to group matching words. It’s easy to understand but it re-checks all words for each key, making it less efficient. Still a good choice for short or readable scripts.




t = "Welcome to GeeksForGeeks"
w = t.split()

seen = []
for i in w:
    ch = i[0]
    if ch not in seen:
        seen.append(ch)

res = {ch: [i for i in w if i.startswith(ch)] for ch in seen}
print(res)

Output
{'W': ['Welcome'], 't': ['to'], 'G': ['GeeksForGeeks']}
Explanation:

t.split() splits the string t into [‘Welcome’, ‘to’, ‘GeeksForGeeks’].
seen is a list that keeps track of the first letter of each word.
For each word i, get the first letter ch and if ch is not in seen, append it.



Python – Create a Dictionary using List with None Values
Last Updated : 28 Jan, 2025
The task of creating a dictionary from a list of keys in Python involves transforming a list of elements into a dictionary where each element becomes a key. Each key is typically assigned a default value, such as None, which can be updated later.

For example, if we have a list like [“A”, “B”, “C”], the goal is to convert it into a dictionary like {‘A’: None, ‘B’: None, ‘C’: None}.

Using dictionary comprehension
Dictionary comprehension is an efficient way to create dictionaries in a single line. It is highly efficient and easy to read, making it the go-to approach for initializing dictionaries with a predefined structure. This method is ideal when we need a fast and clear solution without creating intermediate objects.




li = [1, 2, 3, 4, 5]
res = {key: None for key in li}

print(res)

Output
{1: None, 2: None, 3: None, 4: None, 5: None}
Explanation: {key: None for key in li} iterates over each element in the list li, adding each element as a key to the dictionary res with the value set to None. This results in a dictionary where each element from the list is a key, and its corresponding value is None.

Table of Content

Using dict.from keys()
Using zip()
Using for loop
Using dict.from keys()
dict.fromkeys() is a built-in function explicitly designed for initializing dictionaries with a common value. It takes an iterable of keys and a default value, which is perfect for this task. It’s straightforward, clean and optimized for initializing dictionaries, making it a great choice when clarity is a priority.




li = [1, 2, 3, 4, 5]
res = dict.fromkeys(li, None)

print(res)

Output
{1: None, 2: None, 3: None, 4: None, 5: None}
Explanation: res = dict.fromkeys(li, None) uses the fromkeys() of the dict class to create a new dictionary. It takes an iterable li , where each element becomes a key in the dictionary and the second argument None sets the value for each key.

Using zip()
This approach combines the power of zip() and dict() to pair elements from a list with a corresponding sequence of values None in this case . It is particularly flexible, as it allows us to initialize keys with any set of corresponding values. While slightly less efficient, it’s useful when handling more dynamic scenarios.




li = [1, 2, 3, 4, 5]
res = dict(zip(li, [None] * len(li)))

print(res)

Output
{1: None, 2: None, 3: None, 4: None, 5: None}
Explanation: dict(zip(li, [None] * len(li))) pairs elements from li with None using zip(), creating tuples like (1, None). The dict() function then converts these pairs into a dictionary where the elements from li are keys, and the value for each key is None.

Using for loop
For loop is a traditional approach that involves iterating over a list and adding key-value pairs one at a time. While not as concise or efficient as other methods, it is a straightforward way to understand dictionary construction




li = [1, 2, 3, 4, 5]
res = {} # initialize empty dictionary

for key in li:
    res[key] = None
print(res)

Output
{1: None, 2: None, 3: None, 4: None, 5: None}
Explanation: This code iterates over each element in the list li and adds it as a key to the dictionary res, assigning None as the value for each key.
"""
"""
Create a List using Custom Key-Value Pair of a Dictionary – Python
Last Updated : 28 Jan, 2025
The task of creating a list using custom key-value pairs from a dictionary involves extracting the dictionary’s keys and values and organizing them into a list of tuples. This allows for the flexibility of representing data in a sequence that maintains the relationship between keys and values.

For example, if we have a dictionary like {‘a’: 1, ‘b’: 2, ‘c’: 3}, the goal is to convert it into a list like [(‘a’, 1), (‘b’, 2), (‘c’, 3)].

Using zip()
zip() combines two or more iterables into tuples. To create a list from a dictionary’s key-value pairs, we can use zip() to combine the keys and values separately and then create the desired list. Although the zip() is useful in certain scenarios, it’s less common for creating lists of key-value pairs from a dictionary directly.




d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = d.keys()
val = d.values()
res = list(zip(key, val))
print(res)

Output
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
Explanation:

d.keys() retrieves the keys from the dictionary d .
d.values() retrieves the values from the dictionary d .
zip() combines the two iterables into pairs. It pairs the first key with the first value, the second key with the second value and so on.
Table of Content

Using map()
Using list comprehension
Using loop
Using map()
map() allows us to apply a transformation to each element in an iterable. While it’s more commonly used with lists, we can combine map() with a lambda function to extract and create custom key-value pairs from a dictionary.




d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

res = list(map(lambda item: (item[0], item[1]), d.items()))
print(res)

Output
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
Explanation:

d.items() returns key-value pairs as tuples: (‘a’, 1), (‘b’, 2), (‘c’, 3), (‘d’, 4).
map() applies the lambda function to each item, extracting the key and value as a tuple.
list() converts the result to a list.
Using list comprehension
List comprehension is a efficient way to construct lists. It’s particularly useful when we need to process or transform items from an iterable. Using list comprehension, we can efficiently extract custom key-value pairs and create the desired list:




d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}

res = [(key, val) for key, val in d.items()]
print(res)

Output
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
Explanation: List Comprehension iterates over the dictionary’s key-value pairs and creates a list of tuples.

Using loop
for loop is one of the most straightforward and flexible ways to extract key-value pairs from a dictionary. It allows us to iterate over the dictionary’s items explicitly, providing full control over the process of extracting and transforming data.




d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}

res= [] # initialized an empty list

for key, val in d.items():
    res.append((key, val))
print(res)

Output
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
Explanation:

for loop iterates over each key-value pair in the dictionary d .
.items() returns a sequence of tuples, each containing a key and its associated value.



Convert Dictionary String Values to List of Dictionaries – Python
Last Updated : 31 Jan, 2025
We are given a dictionary where the values are strings containing delimiter-separated values and the task is to split each string into separate values and convert them into a list of dictionaries, with each dictionary containing a key-value pair for each separated value. For example: consider this dictionary {“Gfg”: “1:2:3”, “best”: “4:8:11”} then the output should be [{‘Gfg’: ‘1’, ‘best’: ‘4’}, {‘Gfg’: ‘2’, ‘best’: ‘8’}, {‘Gfg’: ‘3’, ‘best’: ’11’}].

Using zip() and split()
We can first split the values in the dictionary using split(‘:’) and then use zip() to pair corresponding elements from all lists.




d = {"Gfg": "1:2:3", "best": "4:8:11"}

# Splitting values and using zip to pair corresponding elements
res = [dict(zip(d.keys(), vals)) for vals in zip(*[v.split(':') for v in d.values()])]

print(res)

Output
[{'Gfg': '1', 'best': '4'}, {'Gfg': '2', 'best': '8'}, {'Gfg': '3', 'best': '11'}]
Explanation:

We use split(‘:’) to break each string into a list of values.
zip(*[v.split(‘:’) for v in d.values()]) transposes these lists thus pairing corresponding elements together.
dict(zip(d.keys(), vals)) creates a dictionary for each paired group hence, final result is a list of dictionaries.
Using enumerate and split()
This method uses a loop to iterate through the dictionary and splits the string values by the : delimiter and then each split value is assigned to a separate dictionary. The result is a list of dictionaries where each dictionary contains key-value pairs corresponding to the split values.




from collections import defaultdict

d1 = {"Gfg": "1:2:3", "best": "4:8:11"}

d2 = defaultdict(dict)
for k in d1:
    for i, v in enumerate(d1[k].split(':')):
        d2[i][k] = v

r = [d2[i] for i in d2]
print(r)

Output
[{'Gfg': '1', 'best': '4'}, {'Gfg': '2', 'best': '8'}, {'Gfg': '3', 'best': '11'}]
Explanation:

dictionary d is iterated using a loop that splits each string by : and maps the results to temporary dictionaries indexed by split positions.
temporary dictionaries are then collected into a final list r containing dictionaries with split values for each key.


---------------
Create Nested Dictionary using given List – Python
Last Updated : 04 Feb, 2025
The task of creating a nested dictionary in Python involves pairing the elements of a list with the key-value pairs from a dictionary. Each key from the list will map to a dictionary containing a corresponding key-value pair from the original dictionary. For example, given the dictionary a = {‘Gfg’: 4, ‘is’: 5, ‘best’: 9} and the list b = [8, 3, 2], the task is to create a nested dictionary like this:{8: {‘Gfg’: 4}, 3: {‘is’: 5}, 2: {‘best’: 9}} .

Using zip()
zip() pair elements from two or more iterables. In this case, it pairs the elements of the list with the key-value pairs from the dictionary. After pairing the elements, We can create a nested dictionary by iterating over the zipped pairs.




a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]

res = {key: {k: v} for key, (k, v) in zip(b, a.items())}
print(res)

Output
{8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
Explanation: zip(b, a.items()) pairs each element of b with a key-value pair from a, assigning the list element to key and the dictionary pair to (k, v). The comprehension {key: {k: v}} then creates a nested dictionary where each key from b maps to its corresponding {k: v} from a.

Using for loop
This method also uses the zip() function, but the key difference is that the looping process is slightly more explicit and manual. Here, we directly iterate over the zipped elements without using dictionary comprehension.




a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]

res = {}
for key, (k, v) in zip(b, a.items()):
    res[key] = {k: v}
    
print(res)

Output
{8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
Explanation: for loop uses zip(b, a.items()) to pair each element from b with a key-value pair from a. For each pair, res[key] = {k: v} assigns a nested dictionary {k: v} to key, creating res where each key from b maps to the corresponding key-value pair from a.

Using dict()
While this method uses zip() to pair the list and dictionary items, it applies the dict() constructor to explicitly create the final nested dictionary. In this case, the dict() constructor is used with a lambda function to wrap each value in another dictionary.




a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]

res = dict(map(lambda key_val: (key_val[0], {key_val[1][0]: key_val[1][1]}), zip(b, a.items())))
print(res)

Output
{8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
Explanation: zip(b, a.items()) to pair elements from b with key-value pairs from a. The map with lambda creates tuples where each element from b is a key, and its value is a nested dictionary from a. dict() then converts these tuples into the final dictionary res.

---------------

Create Dictionary Of Tuples – Python
Last Updated : 12 Feb, 2025
The task of creating a dictionary of tuples in Python involves mapping each key to a tuple of values, enabling structured data storage and quick lookups. For example, given a list of names like [“Bobby”, “Ojaswi”] and their corresponding favorite foods as tuples [(“chapathi”, “roti”), (“Paraota”, “Idly”, “Dosa”)], the goal is to generate a dictionary like {‘Bobby’: (‘chapathi’, ‘roti’), ‘Ojaswi’: (‘Paraota’, ‘Idly’, ‘Dosa’)}.

Using dictionary literal
This is the most straightforward method to define a dictionary where keys map to tuple values. It is best suited for small, predefined datasets where values do not change frequently. Additionally, Python allows tuples to be used as dictionary keys since they are immutable, making it useful for scenarios where fixed sets of values need mapping.




# tuple of favourite food as key
# value is name of student
d = {("chapathi", "roti"): 'Bobby', 
        ("Paraota", "Idly", "Dosa"): 'ojaswi'}

print(d)

Output
{('chapathi', 'roti'): 'Bobby', ('Paraota', 'Idly', 'Dosa'): 'ojaswi'}
Table of Content

Using dict()
Using dictionary comprehension
Using default dict
Using dict()
This method allows for dynamic creation of dictionaries from lists, tuples, or other iterables. It is particularly useful when working with structured data from databases, CSV files or APIs, as it provides flexibility in building dictionaries programmatically. This approach is highly efficient when handling large datasets .




d = dict([
    ('Bobby', ('chapathi', 'roti')),
    ('Ojaswi', ('Paraota', 'Idly', 'Dosa'))
])

print(d)

Output
{'Bobby': ('chapathi', 'roti'), 'Ojaswi': ('Paraota', 'Idly', 'Dosa')}
Explanation: dict() constructor converts a list of tuples into a dictionary, where each tuple represents a key-value pair.

Using dictionary comprehension
This approach provides a concise way to construct dictionaries of tuples from existing lists or sequences. It is especially useful when performing data transformations, mapping relationships or filtering elements dynamically. Since dictionary comprehension is optimized in Python, this method ensures better performance over traditional loops while keeping the code clean and readable.




a = ['Bobby', 'Ojaswi']  # name
b = [('chapathi', 'roti'), ('Paraota', 'Idly', 'Dosa')]  # food

d = {name: food for name, food in zip(a, b)}

print(d)

Output
{'Bobby': ('chapathi', 'roti'), 'Ojaswi': ('Paraota', 'Idly', 'Dosa')}
Explanation: zip(a, b) pairs elements from the two lists a for names and b for food tuples. Dictionary comprehension then constructs a dictionary where names are keys and food tuples are values.

Using default dict
This method is highly useful in scenarios where missing keys should have default tuple values instead of causing a KeyError. It simplifies dictionary handling in cases where data is being incrementally built or updated, such as aggregating user preferences, handling missing data gracefully or setting up default structures for further updates.




from collections import defaultdict

d = defaultdict(tuple)
d['Bobby'] = ('chapathi', 'roti')
d['Ojaswi'] = ('Paraota', 'Idly', 'Dosa')

print(dict(d))

Output
{'Bobby': ('chapathi', 'roti'), 'Ojaswi': ('Paraota', 'Idly', 'Dosa')}
Explanation: defaultdict(tuple) creates a dictionary with a default tuple value to prevent KeyError for missing keys. Assigning values (d[‘Bobby’] = (‘chapathi’, ‘roti’)) stores names as keys and food tuples as values. dict(d) converts it back to a regular dictionary .

----------------
Creating Dictionary of Sets in Python
Last Updated : 08 Feb, 2025
The task of creating a dictionary of sets in Python involves storing multiple unique values under specific keys, ensuring efficient membership checks and eliminating duplicates. For example, given student data where “Roll-no” maps to {1, 2, 3, 4, 5} and “Aadhaar No” maps to {11, 22, 33, 44, 55}, the goal is to create dictionary of set will be {‘Roll-no’: {1, 2, 3, 4, 5}, ‘Aadhaar No’: {33, 11, 44, 22, 55}}.

Using if condition
This method explicitly checks if a key exists in the dictionary before adding values. It provides better control but requires more lines of code and is less efficient compared to defaultdict and setdefault(). It is useful when additional conditions or logic need to be applied before insertion.




d = {} # initialize empty dictionary

if "Roll-no" not in d:
    d["Roll-no"] = set()
d["Roll-no"].update([1, 2, 3, 4, 5])

if "Aadhaar No" not in d:
    d["Aadhaar No"] = set()
d["Aadhaar No"].update([11, 22, 33, 44, 55])

print(d)

Output
{'Roll-no': {1, 2, 3, 4, 5}, 'Aadhaar No': {33, 11, 44, 22, 55}}
Explanation: if “Roll-no” is not in d, it is set as an empty set, then .update([1, 2, 3, 4, 5]) adds elements. The same logic applies to “Aadhaar No”, ensuring values are stored uniquely.

Table of Content

Using dict.setdefault()
Using if condition
Using dictionary comprehension
Using dictionary comprehension
Dictionary comprehension allows creating a dictionary with predefined keys, each mapped to an empty set. This method is useful when we know the keys beforehand but is not ideal for dynamically adding new keys later.




d = {key: set() for key in ["Student Roll-no", "Student Aadhaar No"]}

d["Student Roll-no"].update([1, 2, 3, 4, 5])
d["Student Aadhaar No"].update([11, 22, 33, 44, 55])

print(d)

Output
{'Student Roll-no': {1, 2, 3, 4, 5}, 'Student Aadhaar No': {33, 11, 44, 22, 55}}
Explanation: dictionary comprehension initialize keys (“Student Roll-no” and “Student Aadhaar No”) with empty sets in a single line. Then, .update([1, 2, 3, 4, 5]) and .update([11, 22, 33, 44, 55]) efficiently add values.

Using defaultdict(set)
defaultdict from the collections module is the most efficient way to create a dictionary of sets. It automatically initializes an empty set when a new key is accessed, eliminating the need for manual key existence checks. This method is highly efficient for dynamically adding values without extra code complexity.




from collections import defaultdict

d = defaultdict(set) 

d["Roll-no"] |= {1, 2, 3, 4, 5}
d["Aadhaar No"] |= {11, 22, 33, 44, 55}

print(d)

Output
defaultdict(<class 'set'>, {'Roll-no': {1, 2, 3, 4, 5}, 'Aadhaar No': {33, 22, 55, 11, 44}})
Explanation: |= operator updates sets by adding all elements from {1, 2, 3, 4, 5} to “Roll-no”, initializing it if absent. Similarly, d[“Aadhaar No”] |= {11, 22, 33, 44, 55} adds values while ensuring uniqueness, as sets automatically ignore duplicates.

Using dict.setdefault()
setdefault() initializes a key with a set only if it does not exist. It allows updating the dictionary dynamically while maintaining clean and concise code. This method is slightly less efficient than defaultdict because it requires a function call for each key update.




d = {} 

d.setdefault("Roll-no", set()).update([1, 2, 3, 4, 5])
d.setdefault("Aadhaar No", set()).update([11, 22, 33, 44, 55])

print(d)

Output
{'Roll-no': {1, 2, 3, 4, 5}, 'Aadhaar No': {33, 11, 44, 22, 55}}
Explanation: setdefault() ensures that “Roll-no” is initialized as an empty set if it doesn’t exist, then .update([1, 2, 3, 4, 5]) adds elements. Similarly, d.setdefault(“Aadhaar No”, set()).update([11, 22, 33, 44, 55]) initializes and updates “Aadhaar No”.


-----------

Python – Convert Matrix to Dictionary
Last Updated : 29 Jan, 2025
The task of converting a matrix to a dictionary in Python involves transforming a 2D list or matrix into a dictionary, where each key represents a row number and the corresponding value is the row itself.
For example, given a matrix li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]], the goal is to convert it into a dictionary like {1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}.

Using enumerate
enumerate() automatically generates sequential indices and associates each matrix row with its corresponding index. It returns pairs of values, index and the corresponding row. These pairs are then used in dictionary comprehension to create dictionary entries, where the key is the index and the value is the row.




li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

res = {idx + 1: val for idx, val in enumerate(li)}
print(res)

Output
{1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
Explanation: enumerate(li) generates index-value pairs for each row in li and idx + 1 adjusts the index to start from 1, creating a dictionary with row numbers as keys and rows as values using dictionary comprehension.

Table of Content

Using range
Using zip()
Using loop
Using range
range() generates a sequence of indices, which are then used as keys in the dictionary. By using dictionary comprehension, we can pair these indices with the corresponding rows of the matrix. The key is the index and the value is the row. This method provides direct control over the row numbering and is simple to implement.




li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

res = {idx + 1: li[idx] for idx in range(len(li))}
print(res)

Output
{1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
Explanation: range(len(li)) generates indices from 0 to 2 and idx + 1 adjusts the index to start from 1, while li[idx] accesses the rows, creating key-value pairs with row numbers as keys and corresponding rows as values.

Using zip()
zip() combine two iterables , the sequence of row numbers generated by range() and the rows of the matrix. It pairs each row number with its corresponding row from the matrix and then dict() convert these pairs into a dictionary, where the row number serves as the key and the matrix row is the value.




li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

res = dict(zip(range(1, len(li) + 1), li))
print(res)

Output
{1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
Explanation: range(1, len(li) + 1) generates row numbers from 1 to 3 and zip(range(1, len(li) + 1), li) pairs each row number with its corresponding row in li. dict() then converts these pairs into a dictionary res .

Using loop
enumerate() iterate over the matrix, providing both the index and the corresponding row . For loop processes each pair and the key-value pair is manually added to an initially empty dictionary. The index is typically adjusted by adding 1 to start from 1 instead of 0. This approach offers more flexibility and is particularly useful if additional logic is needed during the dictionary construction.




li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
res = {} # Initialize an empty dictionary 

for idx, val in enumerate(li):
    res[idx + 1] = val
print(res)

Output
{1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
Explanation: enumerate(li) generates pairs of index idx and value val from the matrix li. The for loop iterates through these pairs and idx + 1 adjusts the index to start from 1 instead of 0. res[idx + 1] = val adds each row val to the dictionary res with its corresponding row number (idx + 1) as the key.


------------------


Python – Convert Matrix to Coordinate Dictionary
Last Updated : 14 Mar, 2023
Sometimes, while working with Python dictionaries, we can have problem in which we need to perform the conversion of matrix elements to their coordinate list. This kind of problem can come in many domains including day-day programming and competitive programming. Lets discuss certain ways in which this task can be performed.


Input : test_list = [[‘g’, ‘g’, ‘g’], [‘g’, ‘g’, ‘g’]] Output : {‘g’: {(0, 1), (1, 2), (0, 0), (1, 1), (1, 0), (0, 2)}} Input : test_list = [[‘a’, ‘b’, ‘c’]] Output : {‘a’: {(0, 0)}, ‘b’: {(0, 1)}, ‘c’: {(0, 2)}}


Method #1 : Using loop + enumerate() The combination of above functionalities can be used to perform this task. In this, we use brute force to extract elements and assign indices to them with the help of enumerate(). 




# Python3 code to demonstrate working of 
# Convert Matrix to Coordinate Dictionary
# Using loop + enumerate()
 
# initializing list
test_list = [['g', 'f', 'g'], ['i', 's', 'g'], ['b', 'e', 's', 't']]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Convert Matrix to Coordinate Dictionary
# Using loop + enumerate()
res = dict()
for idx, sub in enumerate(test_list):
    for j, ele in enumerate(sub):
        if ele in res:
            res[ele].add((idx, j))
        else:
            res[ele] = {(idx, j)}
 
# printing result 
print("The Coordinate Dictionary : " + str(res)) 
Output : 

The original list is : [[‘g’, ‘f’, ‘g’], [‘i’, ‘s’, ‘g’], [‘b’, ‘e’, ‘s’, ‘t’]] The Coordinate Dictionary : {‘g’: {(1, 2), (0, 0), (0, 2)}, ‘f’: {(0, 1)}, ‘t’: {(2, 3)}, ‘i’: {(1, 0)}, ‘b’: {(2, 0)}, ‘e’: {(2, 1)}, ‘s’: {(1, 1), (2, 2)}}


Time Complexity: O(n*m) where n is the total number of values in the column  and m is the total number of values in the row in the list “test_list”. 
Auxiliary Space: O(k) where k is the length of the list “test_list”. 

  Method #2 : Using setdefault() + loop This method operates in similar way as above, just the difference is that setdefault() reduces the task of memoizing the element value and key presence checks. 




# Python3 code to demonstrate working of 
# Convert Matrix to Coordinate Dictionary
# Using setdefault() + loop
 
# initializing list
test_list = [['g', 'f', 'g'], ['i', 's', 'g'], ['b', 'e', 's', 't']]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Convert Matrix to Coordinate Dictionary
# Using setdefault() + loop
res = dict()
for idx, ele in enumerate(test_list):
    for j, sub in enumerate(ele):
        res.setdefault(sub, set()).add((idx, j))
 
# printing result 
print("The Coordinate Dictionary : " + str(res)) 
Output : 

The original list is : [[‘g’, ‘f’, ‘g’], [‘i’, ‘s’, ‘g’], [‘b’, ‘e’, ‘s’, ‘t’]] The Coordinate Dictionary : {‘g’: {(1, 2), (0, 0), (0, 2)}, ‘f’: {(0, 1)}, ‘t’: {(2, 3)}, ‘i’: {(1, 0)}, ‘b’: {(2, 0)}, ‘e’: {(2, 1)}, ‘s’: {(1, 1), (2, 2)}}


Time Complexity: O(n*n) where n is the number of elements in the dictionary. The  setdefault() + loop is used to perform the task and it takes O(n*n) time.
Auxiliary Space: O(n) additional space of size n is created where n is the number of elements in the dictionary.


----------------

Python – Frequency Grouping Dictionary
Last Updated : 22 Apr, 2023
Sometimes, while working with Python dictionaries, we can have a problem in which we need to perform the grouping of dictionary data, in a way in which we need to group all the similar dictionaries key with its frequency. This kind of problem has its application in web development domain. Let’s discuss certain ways in which this task can be performed.


Input : test_list = [{‘best’: 2, ‘Gfg’: 1}, {‘best’: 2, ‘Gfg’: 1}] 
Output : [{‘freq’: 2, ‘Gfg’: 1}] 


Input : test_list = [{‘Gfg’: 1, ‘best’: 2}, {‘Gfg’: 2, ‘best’: 1}] 
Output : [{‘Gfg’: 1, ‘freq’: 1}, {‘Gfg’: 2, ‘freq’: 1}]


Method #1 : Using defaultdict() + list comprehension The combination of above functions can be used to perform this task. In this, we initialize the defaultdict with integer to get the frequency and list comprehension is used to compile the resultant dictionary. 




# Python3 code to demonstrate working of 
# Frequency Grouping Dictionary
# Using defaultdict() + list comprehension
from collections import defaultdict
 
# initializing list
test_list = [{'Gfg' :  1, 'best' : 2}, 
             {'Gfg' :  1, 'best' : 2},
             {'Gfg' :  2, 'good' : 3},
             {'Gfg' :  2, 'best' : 2},
             {'Gfg' :  2, 'good' : 3}]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Frequency Grouping Dictionary
# Using defaultdict() + list comprehension
temp = defaultdict(int)
for sub in test_list:
    key = sub['Gfg']
    temp[key] += 1
 
res = [{"Gfg": key, "freq": val} for (key, val) in temp.items()]
 
# printing result 
print("The frequency dictionary : " + str(res)) 
Output : 

The original list is : [{‘Gfg’: 1, ‘best’: 2}, {‘Gfg’: 1, ‘best’: 2}, {‘good’: 3, ‘Gfg’: 2}, {‘Gfg’: 2, ‘best’: 2}, {‘good’: 3, ‘Gfg’: 2}] The frequency dictionary : [{‘Gfg’: 1, ‘freq’: 2}, {‘Gfg’: 2, ‘freq’: 3}]


Time complexity: O(n), where n is the number of elements in the input list.
Auxiliary space: O(n), since we are using a defaultdict to store the frequency of each element in the input list, and the resulting list also has n elements.

Method #2: Using a regular dictionary and a for loop

Step-by-step explanation:

We initialize the test_list with the same values as in Method #1.
We print the original list using the print() function and str() function to convert the list to a string.
We create an empty dictionary called temp.
We iterate through each element in test_list using a for loop.
We extract the value associated with the key ‘Gfg’ in the current element using the sub[‘Gfg’] syntax.
We check if the current key is already in the temp dictionary using the if key in temp syntax. If it is, we increment the value by 1 using the temp[key] += 1 syntax. If it’s not, we add a new key-value pair with a value of 1 using the temp[key] = 1 syntax.
We create a new list called res using a list comprehension. We iterate through each key-value pair in the temp dictionary using the temp.items() syntax, and create a new dictionary with keys “Gfg” and “freq” and the corresponding values from the temp dictionary. We enclose this dictionary in curly braces to create a dictionary object, and enclose this object in square brackets to create a list object.
We print the result using the print() function and str() function to convert the list to a string.




# initializing list
test_list = [{'Gfg': 1, 'best': 2},
             {'Gfg': 1, 'best': 2},
             {'Gfg': 2, 'good': 3},
             {'Gfg': 2, 'best': 2},
             {'Gfg': 2, 'good': 3}]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Frequency Grouping Dictionary using a regular dictionary and a for loop
temp = {}
for sub in test_list:
    key = sub['Gfg']
    if key in temp:
        temp[key] += 1
    else:
        temp[key] = 1
 
res = [{"Gfg": key, "freq": val} for (key, val) in temp.items()]
 
# printing result
print("The frequency dictionary : " + str(res))
Output
The original list is : [{'Gfg': 1, 'best': 2}, {'Gfg': 1, 'best': 2}, {'Gfg': 2, 'good': 3}, {'Gfg': 2, 'best': 2}, {'Gfg': 2, 'good': 3}]
The frequency dictionary : [{'Gfg': 1, 'freq': 2}, {'Gfg': 2, 'freq': 3}]
Time complexity:  O(n), where n is the length of the test_list.

Auxiliary space:  O(n)
--------------------------
Python – Remove duplicate values in dictionary
Last Updated : 27 Apr, 2023
Sometimes, while working with Python dictionaries, we can have problem in which we need to perform the removal of all the duplicate values of dictionary, and we are not concerned if any key get removed in the process. This kind of application can occur in school programming and day-day programming. Let’s discuss certain ways in which this task can be performed. 

Method #1 : Using loop This is the brute force way in which we perform this task. In this, we keep track of occurred value, and remove it if it repeats. 




# Python3 code to demonstrate working of
# Remove duplicate values in dictionary
# Using loop
 
# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Remove duplicate values in dictionary
# Using loop
temp = []
res = dict()
 
for key, val in test_dict.items():
   
    if val not in temp:
        temp.append(val)
        res[key] = val
 
# printing result
print("The dictionary after values removal : " + str(res))
Output : 

The original dictionary is : {‘gfg’: 10, ‘for’: 10, ‘geeks’: 20, ‘is’: 15, ‘best’: 20} The dictionary after values removal : {‘gfg’: 10, ‘geeks’: 20, ‘is’: 15}


Time complexity: O(n), where n is the number of elements in the dictionary.
Auxiliary space: O(n), as we are using a temporary list of size n to store unique values.

Method #2: Using dictionary comprehension 

The following problem can also be performed using dictionary comprehension. In this, we perform task in similar way as above method, just as a shorthand. 




# Python3 code to demonstrate working of
# Remove duplicate values in dictionary
# Using dictionary comprehension
 
# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Remove duplicate values in dictionary
# Using dictionary comprehension
temp = {val: key for key, val in test_dict.items()}
res = {val: key for key, val in temp.items()}
 
# printing result
print("The dictionary after values removal : " + str(res))
Output : 

The original dictionary is : {‘gfg’: 10, ‘for’: 10, ‘geeks’: 20, ‘is’: 15, ‘best’: 20} The dictionary after values removal : {‘gfg’: 10, ‘geeks’: 20, ‘is’: 15}


Time complexity: O(n), where n is the number of elements in the dictionary. 
Auxiliary space: O(n), where n is the number of elements in the dictionary. 

Method 3: use the setdefault() method.

Follow the below steps:

Initialize an empty dictionary.
Loop through each key-value pair in the original dictionary.
Use the setdefault() method to add the key-value pair to the new dictionary if the value is not already present in the dictionary.
Return the new dictionary.
Below is the implementation of the above approach:




# Python3 code to demonstrate working of
# Remove duplicate values in dictionary
# Using setdefault() method
 
# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Remove duplicate values in dictionary
# Using setdefault() method
 
res = {}
for key, val in test_dict.items():
    res.setdefault(val, key)
 
# printing result
print("The dictionary after values removal : " +
      str(dict((v, k) for k, v in res.items())))
Output
The original dictionary is : {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
The dictionary after values removal : {'gfg': 10, 'is': 15, 'best': 20}
Time complexity: O(n)
Auxiliary space: O(n)

Method #4: Using the values() method and set()

Approach:

Initialize an empty dictionary res.
Loop through the values of the original dictionary test_dict using the values() method.
Check if the value is already in the res dictionary using the if not val in res.values() condition.
If the value is not already in the res dictionary, add it as a key to the res dictionary with a default value of None.
Return the res dictionary.
Below is the implementation of the above approach:




# Python3 code to demonstrate working of
# Remove duplicate values in dictionary
# Using values() method and set()
 
# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Remove duplicate values in dictionary
# Using values() method and set()
unique_values = set(test_dict.values())
 
res = {}
 
for val in unique_values:
    for key in test_dict.keys():
 
        if test_dict[key] == val:
            res[key] = val
            break
 
# Printing result
print("The dictionary after values removal : " + str(res))
Output
The original dictionary is : {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
The dictionary after values removal : {'gfg': 10, 'best': 20, 'is': 15}
Time complexity: O(n^2), where n is the number of key-value pairs in the original dictionary.
Auxiliary space: O(n), where n is the number of unique values in the original dictionary.

Method #5: Using collections.defaultdict

Approach:

Import the defaultdict module from the collections library.
Initialize a defaultdict object and set its default value to an empty list.
Iterate through the items of the dictionary and append the key to the list of the value in the defaultdict object.
Create a new dictionary by iterating through the items of the defaultdict object and selecting the first value of each list.
Print the resulting dictionary.
Below is the implementation of the above approach:




from collections import defaultdict
 
# initializing dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Remove duplicate values in dictionary
# Using defaultdict
d = defaultdict(list)
for k, v in test_dict.items():
    d[v].append(k)
res = {k: v[0] for k, v in d.items()}
 
# printing result
print("The dictionary after values removal : " + str(res))
Output
The original dictionary is : {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
The dictionary after values removal : {10: 'gfg', 15: 'is', 20: 'best'}
Time complexity: O(n), where n is the number of items in the dictionary.
Auxiliary space: O(n), for the defaultdict object.

Method #6: Using a list comprehension

Step-by-step approach:

Create an empty list called seen_values to keep track of the values that have already been seen.
Create a new dictionary called result_dict to store the non-duplicate values.
Loop through the key-value pairs in the original dictionary (test_dict).
For each key-value pair, check if the value is already in seen_values.
If the value is not in seen_values, add the key-value pair to result_dict.
If the value is already in seen_values, skip it.
Add the value to seen_values.
Return the result_dict.
Below is the implementation of the above approach:




def remove_duplicate_values_dict(test_dict):
    seen_values = []
    result_dict = {}
    for key, value in test_dict.items():
        if value not in seen_values:
            result_dict[key] = value
            seen_values.append(value)
        print(f"Seen values so far: {seen_values}")
    return result_dict
test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
result_dict = remove_duplicate_values_dict(test_dict)
print(result_dict)
Output
Seen values so far: [10]
Seen values so far: [10, 15]
Seen values so far: [10, 15, 20]
Seen values so far: [10, 15, 20]
Seen values so far: [10, 15, 20]
{'gfg': 10, 'is': 15, 'best': 20}
Time complexity: O(n), where n is the number of key-value pairs in the input dictionary.
Auxiliary space: O(n), where n is the number of unique values in the input dictionary.

Method #7: Using dict.fromkeys() and keys()

The dict.fromkeys() method can be used to create a new dictionary with keys from an iterable and values set to a default value. In this case, we can create a dictionary with keys from the values of the original dictionary and values set to None. We can then use a loop to iterate over the original dictionary and set the values of the new dictionary to the corresponding key if the value has not already been encountered.




# Python3 code to demonstrate working of 
# Remove duplicate values in dictionary
# Using dict.fromkeys() and keys()
 
# initializing dictionary
test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Remove duplicate values in dictionary
# Using dict.fromkeys() and keys()
vals_dict = dict.fromkeys(test_dict.values(), None)
res = {}
for key, val in test_dict.items():
    if vals_dict[val] is None:
        vals_dict[val] = key
        res[key] = val
 
# printing result 
print("The dictionary after values removal : " + str(res))
Output
The original dictionary is : {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
The dictionary after values removal : {'gfg': 10, 'is': 15, 'best': 20}
Time Complexity: O(n)
Auxiliary Space: O(n)

------------------

To create a dictionary in Python using the zip() function, pair two iterables (like lists or tuples) together, with one serving as keys and the other as values. Then, convert the zipped object into a dictionary using the dict() constructor. 
Python

keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)
# Expected output: {'a': 1, 'b': 2, 'c': 3}
If the iterables have different lengths, zip() will truncate to the length of the shortest one.
Python

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)
# Expected output: {'a': 1, 'b': 2, 'c': 3}

-------------

Convert Two Lists into a Dictionary – Python
Last Updated : 18 Apr, 2025
We are given two lists, we need to convert both of the list into dictionary. For example we are given two lists a = [“name”, “age”, “city”], b = [“Geeks”, 30,”Delhi”], we need to convert these two list into a form of dictionary so that the output should be like {‘name’: ‘Geeks’, ‘age’: 30, ‘city’: ‘Delhi’}. We can do this using methods like zip, dictionary comprehension , itertools.starmap. Let’s implement these methods practically.

Using zip
Use zip to pair elements from two lists, where the first list provides the keys and second provides the values after that we convert the zipped object into a dictionary using dict() which creates key-value pairs.




a = ["name", "age", "city"]
b = ["Alice", 30, "New York"]

res = dict(zip(a, b))
print(res)

Output
{'name': 'Alice', 'age': 30, 'city': 'New York'}
Explanation:

zip(a, b) pairs each element from list a with the corresponding element from list b, creating tuples of key-value pairs.
dict() function is used to convert the zipped pairs into a dictionary where elements from a become the keys and elements from b become values
Using Dictionary Comprehension
Use dictionary comprehension to iterate over the pairs generated by zip(a, b), creating key-value pairs where elements from list a are the keys and elements from list b are the values. This creates the dictionary in a single concise expression.




a = ["name", "age", "city"]
b = ["Alice", 30, "New York"]

res = {key: value for key, value in zip(a, b)}
print(res)

Output
{'name': 'Alice', 'age': 30, 'city': 'New York'}
Explanation:

Dictionary comprehension iterates over pairs generated by zip(a, b), where each pair consists of a key from list a and a value from list b.
For each pair the key-value pair is directly added to dictionary res in one concise expression.
Using a Loop
Iterate through both lists simultaneously using zip and for each pair, add the first element as the key and second as the value to the dictionary.




a = ["name", "age", "city"]
b = ["Alice", 30, "New York"]

res = {}

for k, v in zip(a, b):
    res[k] = v

print(res)

Output
{'name': 'Alice', 'age': 30, 'city': 'New York'}
Explanation:

An empty dictionary res is created, and zip(a, b) is used to iterate through both lists yielding pairs of keys and values.
During each iteration, key from list “a” is added to the dictionary with its corresponding value from list “b”
Using itertools.starmap
Use itertools.starmap to apply a lambda function that takes two arguments (key and value) to each pair generated by zip(a, b). This creates key-value pairs and passes them directly into dict() to form dictionary.




from itertools import starmap

a = ["name", "age", "city"]
b = ["Alice", 30, "New York"]

res = dict(starmap(lambda k, v: (k, v), zip(a, b)))
print(res)

Output
{'name': 'Alice', 'age': 30, 'city': 'New York'}
Explanation:

starmap applies a lambda function to each pair from zip(a, b), where each pair consists of a key and a value.
lambda function returns the key-value pair (k, v) and dict() converts the results into a dictionary.












"""
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
if 2 in d:
    print(d[2])
d[4] = True
print(d)























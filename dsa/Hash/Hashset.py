
"""


In Python, the built-in set data type functions as a hash set. It is an unordered collection of unique elements, implemented using a hash table internally. This design allows for highly efficient operations like adding, removing, and checking for the presence of elements, typically in average O(1) constant time.
Key characteristics of Python's set (hash set):
Uniqueness: Sets only store unique elements. Attempting to add a duplicate element will have no effect.
Unordered: Elements in a set do not maintain any specific order, unlike lists or tuples. Their position is determined by their hash value.
Hashable Elements: Only immutable and hashable data types (like numbers, strings, and tuples) can be stored in a set. Mutable types like lists and dictionaries are not hashable and cannot be directly added to a set.
Efficient Operations: Due to its hash table implementation, operations like add(), remove(), and in (membership testing) are very fast on average.
Creating and using a Python set:
Python

"""
# Creating an empty set
my_set = set()

# Creating a set with initial elements
another_set = {1, 2, 3, "apple", "banana"}

# Adding elements
my_set.add(10)
my_set.add("hello")
my_set.add(10) # This will not add a duplicate

# Removing elements
my_set.remove(10) # Raises KeyError if element not found
my_set.discard("world") # Removes if present, does nothing if not found

# Checking for membership
if "hello" in my_set:
    print("hello is in the set")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2) # {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set1.intersection(set2) # {3, 4}

# Difference
difference_set = set1.difference(set2) # {1, 2}




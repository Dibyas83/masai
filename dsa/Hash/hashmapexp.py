

"""

In Python, hashmaps are primarily implemented through the built-in dictionary data type. Dictionaries store
data in key-value pairs, where each unique key is mapped to a specific value.
Key characteristics and implementation:
Key-Value Pairs: Dictionaries store data as key: value pairs. For example:
"""
my_hashmap = {"name": "Alice", "age": 30, "city": "New York"}

"""
Hashing Function: The keys of a dictionary are processed by an internal hashing function. This function converts 
the key into a numerical hash value, which is then used to determine the memory location (or "bucket") where the 
key-value pair will be stored. This allows for efficient data retrieval. 

Fast Lookups: Due to the use of hashing, dictionaries provide very fast lookup times, typically averaging O(1) 
complexity, meaning the time to find a value associated with a key remains relatively constant regardless of the 
dictionary's size.

Immutable Keys: Dictionary keys must be of an immutable type (e.g., strings, numbers, tuples). This is because 
the hash value of a key must remain constant throughout its lifetime to ensure consistent storage and retrieval. 
Values, however, can be of any data type (mutable or immutable). 

Unordered (Pre-Python 3.7): Historically, dictionaries did not guarantee the order of insertion. However, as of 
Python 3.7, dictionaries preserve the order in which items are added.
Collision Handling: When two different keys produce the same hash value (a "collision"), dictionaries employ 
techniques like chaining or open addressing to manage these collisions and ensure that all key-value pairs can 
be stored and retrieved correctly.

"""

# Creating a dictionary (hashmap)
student_grades = {
    "John": "A",
    "Mary": "B+",
    "David": "C"
}

# Accessing values
print(student_grades["John"])  # Output: A

# Adding a new key-value pair
student_grades["Sarah"] = "A-"
print(student_grades)  # Output: {'John': 'A', 'Mary': 'B+', 'David': 'C', 'Sarah': 'A-'}

# Updating a value
student_grades["David"] = "B"
print(student_grades["David"])  # Output: B

# Checking for key existence
if "Mary" in student_grades:
    print("Mary's grade is in the dictionary.")

# Removing a key-value pair
del student_grades["Cathy"] # This will raise a KeyError if 'Cathy' is not present
student_grades.pop("David") # This will return the value of 'David' before removing
print(student_grades)

"""
Collision handling in hashmaps (dictionaries) in Python is crucial for maintaining efficient data storage and 
retrieval, as collisions occur when different keys hash to the same index in the hash table. Python's dict 
implementation primarily uses a technique called open addressing with probing to handle these collisions.

Here's how collision handling generally works in Python's dict:
Hashing and Initial Slot Calculation: When a key-value pair is to be inserted or retrieved, Python calculates a 
hash value for the key using the built-in hash() function. This hash value is then used to determine the initial 
slot (index) in the underlying array (table) where the key-value pair should reside.

Collision Detection: If the calculated slot is already occupied by another key-value pair, a collision is detected.

Probing for an Empty Slot: Python employs a probing strategy to find an alternative empty slot. Instead of simply 
moving to the next sequential slot (linear probing), CPython uses a more sophisticated random probing or 
pseudo-random probing mechanism. This involves calculating a sequence of alternative slots based on the original 
hash and a probing counter, aiming to distribute colliding elements more evenly and reduce clustering.

Insertion or Lookup:
Insertion: When inserting, the system probes until an empty slot is found, and the new key-value pair is placed there.

Lookup: When looking up a key, the system follows the same probing sequence. It compares the hash and the key 
itself at each probed slot until a match is found. If no match is found after exhausting all possible probes, 
it indicates the key is not present.

Resizing and Rehashing: To prevent performance degradation due to a high number of collisions and long probing 
sequences, Python's dict automatically resizes the underlying hash table and rehashes all existing key-value pairs 
when the load factor (the ratio of occupied slots to total slots) exceeds a certain threshold (typically around 
two-thirds full). This helps maintain efficient average-case performance for dictionary operations.

Key takeaway: While you don't typically implement collision handling directly when using Python's built-in dict, 
understanding these underlying mechanisms helps in appreciating the efficiency and robustness of Python dictionaries. 
The use of open addressing with sophisticated probing and automatic resizing ensures that dictionary operations 
remain fast even with a large number of elements and potential collisions
"""











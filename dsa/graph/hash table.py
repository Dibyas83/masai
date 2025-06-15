

"""
DSA Hash Tables
Hash Table
A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.

In a Linked List, finding a person "Bob" takes time because we would have to go from one node to the next, checking each node, until the node with "Bob" is found.

And finding "Bob" in an Array could be fast if we knew the index, but when we only know the name "Bob", we need to compare each element (like with Linked Lists), and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored, using something called a hash function.

Building A Hash Table from Scratch
To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.

We will build the Hash Set in 5 steps:

Starting with an array.
Storing names using a hash function.
Looking up an element using a hash function.
Handling collisions.
The basic Hash Set code example and simulation.
Step 1: Starting with an array
Using an array, we could store names like this:

my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
To find "Bob" in this array, we need to compare each name, element by element, until we find "Bob".

If the array was sorted alphabetically, we could use Binary Search to find a name quickly, but inserting or deleting names in the array would mean a big operation of shifting elements in memory.

To make interacting with the list of names really fast, let's use a Hash Table for this instead, or a Hash Set, which is a simplified version of a Hash Table.

To keep it simple, let's assume there is at most 10 names in the list, so the array must be a fixed size of 10 elements. When talking about Hash Tables, each of these elements is called a bucket.

my_hash_set = [None,None,None,None,None,None,None,None,None,None]
Step 2: Storing names using a hash function
Now comes the special way we interact with the Hash Set we are making.

We want to store a name directly into its right place in the array, and this is where the hash function comes in.

A hash function can be made in many ways, it is up to the creator of the Hash Table. A common way is to find a way to convert the value into a number that equals one of the Hash Set's index numbers, in this case a number from 0 to 9. In our example we will use the Unicode number of each character, summarize them and do a modulo 10 operation to get index numbers 0-9.

Example
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'Bob' has hash code:",hash_function('Bob'))
The character "B" has Unicode code point 66, "o" has 111, and "b" has 98. Adding those together we get 275. Modulo 10 of 275 is 5, so "Bob" should be stored as an array element at index 5.

The number returned by the hash function is called the hash code.

Unicode number: Everything in our computers are stored as numbers, and the Unicode code point is a unique number that exist for every character. For example, the character A has Unicode number (also called Unicode code point) 65. Just try it in the simulation below. See this page for more information about how characters are represented as numbers.

Modulo: A mathematical operation, written as % in most programming languages (or
m
o
d
 in mathematics). A modulo operation divides a number with another number, and gives us the resulting remainder. So for example, 7 % 3 will give us the remainder 1. (Dividing 7 apples between 3 people, means that each person gets 2 apples, with 1 apple to spare.)

After storing "Bob" where the hash code tells us (index 5), our array now looks like this:

my_hash_set = [None,None,None,None,None,'Bob',None,None,None,None]
We can use the hash function to find out where to store the other names "Pete", "Jones", "Lisa", and "Siri" as well.

After using the hash function to store those names in the correct position, our array looks like this:

my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]
Step 3: Looking up a name using a hash function
We have now established a super basic Hash Set, because we do not have to check the array element by element anymore to find out if "Pete" is in there, we can just use the hash function to go straight to the right element!

To find out if "Pete" is stored in the array, we give the name "Pete" to our hash function, we get back hash code 8, we go directly to the element at index 8, and there he is. We found "Pete" without checking any other elements.

Example
my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def contains(name):
    index = hash_function(name)
    return my_hash_set[index] == name

print("'Pete' is in the Hash Set:",contains('Pete'))
When deleting a name from our Hash Set, we can also use the hash function to go straight to where the name is, and set that element value to None.

Step 4: Handling collisions
Let's also add "Stuart" to our Hash Set.

We give "Stuart" to our hash function, and we get the hash code 3, meaning "Stuart" should be stored at index 3.

Trying to store "Stuart" creates what is called a collision, because "Lisa" is already stored at index 3.

To fix the collision, we can make room for more elements in the same bucket, and solving the collision problem in this way is called chaining. We can give room for more elements in the same bucket by implementing each bucket as a linked list, or as an array.

After implementing each bucket as an array, to give room for potentially more than one name in each bucket, "Stuart" can also be stored at index 3, and our Hash Set now looks like this:

my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa', 'Stuart'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]
Searching for "Stuart" in our Hash Set now means that using the hash function we end up directly in bucket 3, but then be must first check "Lisa" in that bucket, before we find "Stuart" as the second element in bucket 3.

Step 5: Hash Set code example and simulation
To complete our very basic Hash Set code, let's have functions for adding and searching for names in the Hash Set, which is now a two dimensional array.

Run the code example below, and try it with different values to get a better understanding of how a Hash Set works.

Example
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10

def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))
The next two pages show better and more detailed implementations of Hast Sets and Hash Tables.

Try the Hash Set simulation below to get a better ide of how a Hash Set works in principle.

Hash Set

0:ThomasJens
1:
2:Peter
3:Lisa
4:Charlotte
5:AdeleBob
6:
7:
8:Michaela
9:
Hash Code

275 % 10 = 5

Try interacting with the Hash Set0

Bob

contains()add()remove()size()
Uses of Hash Tables
Hash Tables are great for:

Checking if something is in a collection (like finding a book in a library).
Storing unique items and quickly finding them (like storing phone numbers).
Connecting values to keys (like linking names to phone numbers).
The most important reason why Hash Tables are great for these things is that Hash Tables are very fast compared Arrays and Linked Lists, especially for large sets. Arrays and Linked Lists have time complexity
O
(
n
)
 for search and delete, while Hash Tables have just
O
(
1
)
 on average! Read more about time complexity here.

Hash Set vs. Hash Map
A Hash Table can be a Hash Set or a Hash Map. The next two pages describe these data structures in more detail.

Here's how Hash Sets and Hash Maps are different and similar:

Hash Set	Hash Map
Uniqueness and storage	Every element is a unique key.	Every entry is a key-value-pair, with a key that is unique, and a value connected it.
Use case	Checking if an element is in the set, like checking if a name is on a guest list.	Finding information based on a key, like looking up who owns a certain telephone number.
Is it fast to search, add and delete elements?	Yes, average
O
(
1
)
.	Yes, average
O
(
1
)
.
Is there a hash function that takes the key, generates a hash code, and that is the bucket where the element is stored?	Yes	Yes
Hash Tables Summarized
Hash Table elements are stored in storage containers called buckets.

Every Hash Table element has a part that is unique that is called the key.

A hash function takes the key of an element to generate a hash code.

The hash code says what bucket the element belongs to, so now we can go directly to that Hash Table element: to modify it, or to delete it, or just to check if it exists. Specific hash functions are explained in detail on the next two pages.

A collision happens when two Hash Table elements have the same hash code, because that means they belong to the same bucket. A collision can be solved in two ways.

Chaining is the way collisions are solved in this tutorial, by using arrays or linked lists to allow more than one element in the same bucket.

Open Addressing is another way to solve collisions. With open addressing, if we want to store an element but there is already an element in that bucket, the element is stored in the next available bucket. This can be done in many different ways, but we will not explain open addressing any further here.

Conclusion
Hash Tables are powerful tools in programming, helping you to manage and access data efficiently.

Whether you use a Hash Set or a Hash Map depends on what you need: just to know if something is there, or to find detailed information about it

"""

"""
DSA Hash Maps
Hash Maps
A Hash Map is a form of Hash Table data structure that usually holds a large number of entries.

Using a Hash Map we can search, add, modify, and remove entries really fast.

Hash Maps are used to find detailed information about something.

In the simulation below, people are stored in a Hash Map. A person can be looked up using a person's unique social security number (the Hash Map key), and then we can see that person's name (the Hash Map value).

Hash Map

0:123-4569Jens
1:
2:123-4570Peter
3:123-4571Lisa
4:
5:123-4672Adele123-4573Michaela
6:
7:
8:123-4567Charlotte123-6574Bob
9:123-4568Thomas
Hash Code

0 % 10 = 0

Try interacting with the Hash Map0

XXX
-
XXXX
Name

put()remove()get()size()
Note: The Hash Map would be more useful if more information about each person was attached to the corresponding social security number, like last name, birth date, and address, and maybe other things as well. But the Hash Map simulation above is made to be as simple as possible.

It is easier to understand how Hash Maps work if you first have a look at the two previous pages about Hash Tables and Hash Sets. It is also important to understand the meaning of the words below.

Entry: Consists of a key and a value, forming a key-value pair.
Key: Unique for each entry in the Hash Map. Used to generate a hash code determining the entry's bucket in the Hash Map. This ensures that every entry can be efficiently located.
Hash Code: A number generated from an entry's key, to determine what bucket that Hash Map entry belongs to.
Bucket: A Hash Map consists of many such buckets, or containers, to store entries.
Value: Can be nearly any kind of information, like name, birth date, and address of a person. The value can be many different kinds of information combined.
Finding The Hash Code
A hash code is generated by a hash function.

The hash function in the simulation above takes the numbers in the social security number (not the dash), add them together, and does a modulo 10 operation (% 10) on the sum of characters to get the hash code as a number from 0 to 9.

This means that a person is stored in one of ten possible buckets in the Hash Map, according to the hash code of that person's social security number. The same hash code is generated and used when we want to search for or remove a person from the Hash Map.

The Hash Code gives us instant access as long as there is just one person in the corresponding bucket.

In the simulation above, Charlotte has social security number 123-4567. Adding the numbers together gives us a sum 28, and modulo 10 of that is 8. That is why she belongs to bucket 8.

Modulo: A mathematical operation, written as % in most programming languages (or 
m
o
d
 in mathematics). A modulo operation divides a number with another number, and gives us the resulting remainder. So for example, 7 % 3 will give us the remainder 1. (Dividing 7 apples between 3 people, means that each person gets 2 apples, with 1 apple to spare.)

Direct Access in Hash Maps
Searching for Charlotte in the Hash Map, we must use the social security number 123-4567 (the Hash Map key), which generates the hash code 8, as explained above.

This means we can go straight to bucket 8 to get her name (the Hash Map value), without searching through other entries in the Hash Map.

In cases like this we say that the Hash Map has constant time 
O
(
1
)
 for searching, adding, and removing entries, which is really fast compared to using an array or a linked list.

But, in a worst case scenario, all the people are stored in the same bucket, and if the person we are trying to find is last person in this bucket, we need to compare with all the other social security numbers in that bucket before we find the person we are looking for.

In such a worst case scenario the Hash Map has time complexity 
O
(
n
)
, which is the same time complexity as arrays and linked lists.

To keep Hash Maps fast, it is therefore important to have a hash function that will distribute the entries evenly between the buckets, and to have around as many buckets as Hash Map entries.

Having a lot more buckets than Hash Map entries is a waste of memory, and having a lot less buckets than Hash Map entries is a waste of time.

Note: A social security number can be really long, like 11 digits, which means it is possible to store 100 billion people with unique social security numbers. This is a lot more than in any country's population, and even a lot more than there are people on Earth.

Using an array where each person's social security number is the index in the array where this person is stored is therefore a huge waste of space (mostly empty buckets).

Using a Hash Map (or a database with similar properties) makes more sense as the number of buckets can be adjusted to the number of people.

Hash Map Implementation
Hash Maps in Python are typically done by using Python's own dictionary data type, but to get a better understanding of how Hash Maps work we will not use that here.

To implement a Hash Map in Python we create a class SimpleHashMap.

Inside the SimpleHashMap class we have a method __init__ to initialize the Hash Map, a method hash_function for the hash function, and methods for the basic Hash Map operations: put, get, and remove.

We also create a method print_map to better see how the Hash Map looks like.

Example
class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # A list of buckets, each is a list (to handle collisions)

    def hash_function(self, key):
        # Sum only the numerical values of the key, ignoring non-numeric characters
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10  # Perform modulo 10 on the sum

    def put(self, key, value):
        # Add or update a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key-value pair if not found

    def get(self, key):
        # Retrieve a value by key
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def remove(self, key):
        # Remove a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return

    def print_map(self):
        # Print all key-value pairs in the hash map
        print("Hash Map Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")
Using the SimpleHashMap class we can create the same Hash Map as in the top of this page:

Example
class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # A list of buckets, each is a list (to handle collisions)

    def hash_function(self, key):
        # Sum only the numerical values of the key, ignoring non-numeric characters
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10  # Perform modulo 10 on the sum

    def put(self, key, value):
        # Add or update a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key-value pair if not found

    def get(self, key):
        # Retrieve a value by key
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def remove(self, key):
        # Remove a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return

    def print_map(self):
        # Print all key-value pairs in the hash map
        print("Hash Map Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

# Creating the Hash Map from the simulation
hash_map = SimpleHashMap(size=10)

# Adding some entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

# Demonstrating retrieval
print("\nName associated with '123-4570':", hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.put("123-4570","James")

# Checking if Peter is still there
print("Name associated with '123-4570':", hash_map.get("123-4570"))
"""






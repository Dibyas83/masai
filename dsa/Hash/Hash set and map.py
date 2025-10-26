
"""
Python sets are implemented using hash tables, where each element is stored as a key in the table with an
associated value of None. Hashing ensures that the set operations like add, remove, and lookup are highly efficient,
in a constant time O(1).

Important points:

Hash Set does not allow duplicate values.
Sets in Python are unordered, because the elements are stored based on their hash values, not by their order of insertion.
Sets use hashing to provide fast lookups, insertions, and deletions.
Hash Set are Mutable. You can add or remove elements after creating the set.
Sets can only store hashable elements, like numbers, strings, and tuples (not lists or dictionaries).

Use remove() to delete an element (raises an error if it doesn't exist).
Use discard() to delete an element (does not raise an error if the element is missing).
Use pop() to remove and return a random element.

- Sets are unordered, so you cannot access elements by index.
- Sets only store immutable (hashable) elements like numbers, strings, and tuples. Lists
and dictionaries cannot be stored in a set.
"""
se = {3,6,3,7,8,9}

print(se)  # {3, 6, 7, 8, 9}

se.add(11)
#se.remove(13)
se.remove(3)
se.discard(15)
rem_item = se.pop()
print(rem_item)


"""

Sometimes, instead of the sequential data storage structure, we need to map the data to its corresponding 
information. This is known as mapping data structure.
One of the most popular and important such representations of data is a hash table. 

A hash table, also known as a hash map, stores information in the form of key-value pairs. Each key is unique 
and is used as a reference to identify the data associated with it. This is a reason why hash tables are used 
as a look-up data structure. Hash tables provide fast insertion and access of key-value pairs stored in them.

The keys are mapped to values and stored in the memory using a hash function. Data of any size can be mapped 
to fixed-size values using the hashing algorithm. The hash function can be any function like mod (%), plus(+) 
or any custom function based on the need.

Hash tables are implemented in Python using the built-in data-type called a dictionary. Dictionary is a Python 
specific implementation of a hash table. Let us see how to perform different operations on hash tables using 
Python.

"""
cricket = {'Name': 'Anthony', 'Runs': 46, 'Wickets': 2, 'Wides': 3}
print(cricket)
print(type(cricket))
print(cricket['Name'], "scored", cricket['Runs'], "runs and took", cricket['Wickets'], "wickets")


#You can also use the get() method to get the value for a particular key.
print(cricket.get('Runs'))
print(cricket.keys())
print(cricket.values())

cricket['Runs'] = 58

cricket['No Balls'] = 2
cricket['Players'] = 11
print(cricket)

#del(): Removes the key-value pair from the dictionary for the given key.
del cricket['Wides']
print(cricket)

#pop(): Similar to del, removes the key-value pair for given key.
cricket.pop('Wickets')
print(cricket)

#popitem(): This function removes the last inserted item from hash table.
cricket.popitem()

#Collision Resolution: When different keys produce the same hash value (a collision), dictionaries employ techniques
#like open addressing or separate chaining to handle them. Python's internal implementation manages this automatically.
"""
A hash table is a data structure that allows for quick insertion, deletion, and retrieval of data. It works 
by using a hash function to map a key to an index in an array. In this article, we will implement a hash
table in Python using separate chaining to handle collisions.

Separate chaining is a technique used to handle collisions in a hash table. When two or more keys map to the same 
index in the array, we store them in a linked list at that index. This allows us to store multiple values at the 
same index and still be able to retrieve them using their key.

Create two classes: 'Node' and 'HashTable'.

The 'Node' class will represent a node in a linked list. Each node will contain a key-value pair, as well as a 
pointer to the next node in the list.

The 'HashTable' class will contain the array that will hold the linked lists, as well as methods to insert, 
retrieve, and delete data from the hash table.
The  '__init__' method initializes the hash table with a given capacity. It sets the 'capacity' and 'size'
variables and initializes the array to 'None'.

  
    The ord() function in Python is a built-in function that returns the Unicode code point of 
    a given single character. It takes a single character string as an argument and returns an 
    integer representing that character's position in the Unicode table
    Trying to pass a string with more than one character will raise an error
  
 -------------------------- 
a linked list, which is composed of ListNode objects, can be iterated in Python. This can be achieved through 
a few common methods:
1. Using a while loop:
This is the most straightforward way to traverse a linked list. You start from the head of the list and move to 
the next node until you reach None. 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example linked list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))

current = head
while current is not None:
    print(current.val)
    current = current.next
2. Making the ListNode (or the linked list class) iterable:
You can implement the __iter__ and __next__ methods within your ListNode class (or a separate LinkedList class) 
to make it directly iterable using a for loop.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        current = self
        while current is not None:
            yield current.val  # Yield the value of the current node
            current = current.next

# Example linked list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))

for val in head:
    print(val)
In this example, the __iter__ method in ListNode creates a generator that yields the val of
each node as it traverses the list. This allows you to use a for loop directly on the head of your linked list.  
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity # capacity =  no of buckets
        self.size = 0  # no of ele in hash map list
        self.table = [None] * capacity
        # each key is a node

    def _hash(self, key):
        key_str = str(key)
        hash_res = 0
        for char in key_str:
            hash_res = (hash_res * 31 + ord(char)) % self.capacity # so that index is not greater than capacity
        return hash_res

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:  # empty
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            bucket = self.table[index]
            while bucket: # search each bucket for the key
                if bucket.key == key:
                    bucket.value = value
                    return
                bucket = bucket.next

            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)

        bucket = self.table[index]
        while bucket:
            if bucket.key == key:
                return bucket.value
            bucket = bucket.next

        raise KeyError(key)


    def remove(self, key):
        index = self._hash(key)
        previous = None
        bucket = self.table[index]
        while bucket:
            if bucket.key == key:
                if previous:
                    previous.next = bucket.next
                else:
                    self.table[index] = bucket.next
                self.size -= 1
                return
            previous = bucket
            bucket = bucket.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

    def put(self,key, value):  #putting new key ,val pair
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket): # check if key in hash map
            if k == key:
                bucket[i] = (key, value)
                break
        else: # if  doesnt breaks
            bucket.append((key, value))
            self.size += 1

    def get(self,key): # and get val
        index = self._hash(key)
        bucket = self.table[index]

        for k,v in bucket:
            if k == key:
                return v
        raise KeyError('key not found')

    def key(self):
        pass

    def val(self):
        pass

    def items(self): # for pairs
        pass

# Driver code
if __name__ == '__main__':


    # Create a hash table with
    # a capacity of 5
    ht = HashTable(5)

    # Add some key-value pairs
    # to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False

    # Get the value for a key
    print(ht.search("banana"))  # 2

    # Update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))  # 4

    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3

    # collision handling

    #1 by going to next free space
    #2 using bucket -list of list,linked list
    f= [[],[],[],[]]
    # all land in one bucket or list if hash gives same index like 0 or 1 and then it has to move to the desired key









"""
The time complexity of the insert, search and remove methods in a hash table using separate chaining depends on the 
size of the hash table, the number of key-value pairs in the hash table, and the length of the linked list at each 
index.
Assuming a good hash function and a uniform distribution of keys, the expected time complexity of these methods 
is O(1) for each operation. However, in the worst case, the time complexity can be O(n), where n is the number 
of key-value pairs in the hash table.
However, it is important to choose a good hash function and an appropriate size for the hash table to minimize the 
likelihood of collisions and ensure good performance.
The space complexity of a hash table using separate chaining depends on the size of the hash table and the number 
of key-value pairs stored in the hash table.
The hash table itself takes O(m) space, where m is the capacity of the hash table. Each linked list node takes O(1) 
space, and there can be at most n nodes in the linked lists, where n is the number of key-value pairs stored in the 
hash table.
Therefore, the total space complexity is O(m + n).
In practice, it is important to choose an appropriate capacity for the hash table to balance the space usage and 
the likelihood of collisions.
"""




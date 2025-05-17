

"""
Hashing in data structures is a technique for quickly storing and retrieving data using a hash function, which maps keys (often strings or numbers) to indices in a hash table (an array-like data structure). This allows for efficient lookup of values associated with specific keys, making it ideal for implementing sets and dictionaries according to GeeksforGeeks.
How Hashing Works:
1. Hash Function:
A hash function takes a key as input and returns a hash value (an index) within a specific range (e.g., the size of the hash table). This function should be designed to distribute keys evenly across the hash table to minimize collisions (where two different keys map to the same index).
2. Hash Table:
The hash table is an array (or a similar structure) where each index can store a value or a linked list of values (to handle collisions).
3. Storage:
When storing data, a key is passed to the hash function, and the resulting hash value is used as the index in the hash table to store the associated value.
4. Retrieval:
When retrieving data, the key is again passed to the hash function, the hash value is calculated, and the value stored at that index (or within the linked list) is retrieved.
Key Concepts:
Key: The data used to identify and locate a value within the hash table.
Value: The data that is stored in the hash table.
Hash Function: The algorithm that maps keys to indices.
Hash Table: The data structure that stores key-value pairs.
Hash Value: The index produced by the hash function.
Collision: When two different keys map to the same hash value.
Collision Resolution: Strategies used to handle collisions (e.g., separate chaining, open addressing).
Advantages of Hashing:
Fast Access:
Hashing provides near-constant time complexity (O(1)) for searching, insertion, and deletion operations, assuming a good hash function and minimal collisions according to Wikipedia.
Efficiency:
It's a highly efficient data structure for storing and retrieving data based on keys, making it suitable for various applications.
Wide Use:
Hashing is used in numerous applications, including database indexing, caches, and cryptography according to TechTarget.
Disadvantages of Hashing:
Collisions:
Collisions can significantly degrade performance, especially if the hash function is not well-designed or the hash table is too full according to Wikipedia.
Space Overhead:
Hash tables can require significant memory, especially if the hash function distributes keys poorly and the table is relatively sparse.
Key Distribution:
The performance of hashing heavily depends on the distribution of keys, and a poor distribution can lead to poor performance.
In summary, hashing is a powerful technique that allows for efficient data storage and retrieval based on keys, but careful consideration of hash function design, collision resolution, and key distribution is essential for optimal performance.


"""


"""
Introduction to Hashing
Last Updated : 21 Mar, 2025
Hashing refers to the process of generating a small sized output (that can be used as index in a table) from an input of typically large and variable size. Hashing uses mathematical formulas known as hash functions to do the transformation. This technique determines an index or location for the storage of an item in a data structure called Hash Table.

Introduction-to-Hashing
Introduction to Hashing
Hash Table Data Structure Overview
It is one of the most widely used data structure after arrays.
It mainly supports search, insert and delete in O(1) time on average which is more efficient than other popular data structures like arrays, Linked List and Self Balancing BST.
We use hashing for dictionaries, frequency counting, maintaining data for quick access by key, etc.
Real World Applications include Database Indexing, Cryptography, Caches, Symbol Table and Dictionaries.
There are mainly two forms of hash typically implemented in programming languages.
Hash Set : Collection of unique keys (Implemented as Set in Python, Set in JavaScrtipt, unordered_set in C++ and HashSet in Java.
Hash Map : Collection of key value pairs with keys being unique (Implemented as dictionary in Python, Map in JavaScript, unordered_map in C++ and HashMap in Java)
Situations Where Hash is not Used
Need to maintain sorted data along with search, insert and delete. We use a self balancing BST in these cases.
When Strings are keys and we need operations like prefix search along with search, insert and delete. We use Trie in these cases.
When we need operations like floor and ceiling along with search, insert and/or delete. We use Self Balancing BST in these cases.
Components of Hashing
There are majorly three components of hashing:

Key: A Key can be anything string or integer which is fed as input in the hash function the technique that determines an index or location for storage of an item in a data structure.
Hash Function: Receives the input key and returns the index of an element in an array called a hash table. The index is known as the hash index .
Hash Table: Hash table is typically an array of lists. It stores values corresponding to the keys. Hash stores the data in an associative manner in an array where each data value has its own unique index.
Components-of-Hashing
How does Hashing work?
Suppose we have a set of strings {“ab”, “cd”, “efg”} and we would like to store it in a table.

Step 1: We know that hash functions (which is some mathematical formula) are used to calculate the hash value which acts as the index of the data structure where the value will be stored.
Step 2: So, let's assign
“a” = 1,
“b”=2, .. etc, to all alphabetical characters.
Step 3: Therefore, the numerical value by summation of all characters of the string:
 “ab” = 1 + 2 = 3, 
 “cd” = 3 + 4 = 7 , 
 “efg” = 5 + 6 + 7 = 18 
Step 4: Now, assume that we have a table of size 7 to store these strings. The hash function that is used here is the sum of the characters in key mod Table size . We can compute the location of the string in the array by taking the sum(string) mod 7 .
Step 5: So we will then store
“ab” in 3 mod 7 = 3,
“cd” in 7 mod 7 = 0, and
“efg” in 18 mod 7 = 4.
Mapping-Key-with-indices-of-Array
The above technique enables us to calculate the location of a given string by using a simple hash function and rapidly find the value that is stored in that location. Therefore the idea of hashing seems like a great way to store (key, value) pairs of the data in a table.

What is a Hash function?
A hash function creates a mapping from an input key to an index in hash table, this is done through the use of mathematical formulas known as hash functions. For example: Consider phone numbers as keys and a hash table of size 100. A simple example hash function can be to consider the last two digits of phone numbers so that we have valid array indexes as output. A good hash function should have the following properties:

Efficient
Should uniformly distribute the keys to each index of hash table.
Should minimize collisions (This and the below are mainly derived from the above 2nd point)
Should have a low load factor (number of items in the table divided by the size of the table).
What is Collision in Hashing?
When two or more keys have the same hash value, a collision happens. If we consider the above example, the hash function we used is the sum of the letters, but if we examined the hash function closely then the problem can be easily visualised that for different strings same hash value is being generated by the hash function.

For example: {“ab”, “ba”} both have the same hash value, and string {“cd”,”be”} also generate the same hash value, etc. This is known as collision and it creates problem in searching, insertion, deletion, and updating of value.

collision-in-hashing
Collision in Hashing
The probability of a hash collision depends on the size of the algorithm, the distribution of hash values and the efficiency of Hash function. To handle this collision, we use Collision Resolution Techniques.

What is meant by Load Factor in Hashing?
The load factor of the hash table can be defined as the number of items the hash table contains divided by the size of the hash table. Load factor is the decisive parameter that is used when we want to rehash the previous hash function or want to add more elements to the existing hash table.

It helps us in determining the efficiency of the hash function i.e. it tells whether the hash function which we are using is distributing the keys uniformly or not in the hash table.

Load Factor = Total elements in hash table/ Size of hash table 

What is Rehashing?
As the name suggests, rehashing means hashing again. Basically, when the load factor increases to more than its predefined value (the default value of the load factor is 0.75), the complexity increases. So to overcome this, the size of the array is increased (doubled) and all the values are hashed again and stored in the new double-sized array to maintain a low load factor and low complexity.

How to Create Your Own Hash Table?
You Own Hash Table with Chaining
Your Own Hash Table with Linear Probing in Open Addressing
Your Own Hash Table with Quadratic Probing in Open Addressing

"""





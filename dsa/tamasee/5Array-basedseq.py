
"""
Chapter 5. Array-Based Sequences
Python’s various “sequence” classes, namely the built￾in list, tuple, and str classes. There is
significant commonality between these classes, most notably: each supports indexing to access an
individual element of a sequence, using a syntax such as seq[k], and each uses a low-level concept
known as an array to represent the sequence to keep track of what information is stored in what byte,
the computer uses an abstraction known as a memory address. In effect, each byte of memory is associated
with a unique number that serves as its address (more formally, the binary representation
of the number serves as the address). In this way, the computer system can refer
to the data in “byte #2150” versus the data in “byte #2157,” for example

Despite the sequential nature of the numbering system, computer hardware is designed, in theory, so
that any byte of the main memory can be efficiently accessed based upon its memory address. In this sense,
we say that a computer’s main mem￾ory performs as random access memory (RAM). That is, it is just as easy to
retrieve byte #8675309 as it is to retrieve byte #309 .In Python, each character is represented using the
Unicode character set, and on most computing systems, Python internally represents each.Unicode character with
16 bits (i.e., 2 bytes). Therefore, a six-character string, such as SAMPLE , would be stored in 12 consecutive
bytes of memory, as diagrammed

We describe this as an array of six characters, even though it requires 12 bytes
of memory. We will refer to each location within an array as a cell, and will use an
integer index to describe its location within the array, with cells numbered starting
with 0, 1, 2, and so on. For example, in Figure 5.2, the cell of the array with index 4
has contents L and is stored in bytes 2154 and 2155 of memory.

To represent such a list with an array, Python must adhere to the requirement that each cell of the
array use the same number of bytes. Yet the elements are strings,and strings naturally have different
lengths. Python could attempt to reserve enough space for each cell to hold the maximum length string
Instead, Python represents a list or tuple instance using an internal storage mechanism of an array of
object references. At the lowest level, what is stored is a consecutive sequence of memory addresses at
which the elements of the se￾quence reside In this way, Python can support constant-time access to a list
or tuple element based on its index.Note as well that a reference to the None object can be used as an
element of the list to represent an empty bed in the hospita

A single list instance may include multiple references to the same object as elements of the list,
and it is possible for a single object to be an element of two or more lists, as those lists simply
store references back to that object. As an example, when you compute a slice of a list, the result is a new
list instance, but that new list has references to the same elements that are in the original list, as portrayed in F


The same semantics is demonstrated when making a new list as a copy of an existing one, with a syntax
such as backup = list(primes). This produces a new list that is a shallow copy (see Section 2.6), in
that it references the same elements as in the first list. With immutable elements, this point is moot.
If the contents of the list were of a mutable type, a deep copy, meaning a new list with new elements,
can be produced by using the deepcopy function from the copy module.

it is a common practice in Python to initialize an array of integers using a syntax such as counters = [0] 8.
This syntax produces a list of length eight, with all eight elements being the value zero. Technically, all
eight cells of the list reference the same object

 However, we rely on the fact that the referenced integer is immutable.
Even a command such as counters[2] += 1 does not technically change the value
of the existing integer instance. This computes a new integer, with value 0+1, and
sets cell 2 to reference the newly computed value

s, we note that the extend
command is used to add all elements from one list to the end of another list. The
extended list does not receive copies of those elements, it receives references to
those elements

    Compact Arrays in Python
In the introduction to this section, we emphasized that strings are represented using
an array of characters (not an array of references). We will refer to this more direct
representation as a compact array because the array is storing the bits that represent
the primary data (characters, in the case of strings)
        S A M P L E
        0 1 2 3 4 5

Compact arrays have several advantages over referential structures in terms of computing performance.
Most significantly, the overall memory usage will be much lower for a compact structure because there
is no overhead devoted to the explicit storage of the sequence of memory references (in addition to the
primary data). That is, a referential structure will typically use 64-bits for the memory
address stored in the array, on top of whatever number of bits are used to represent
the object that is considered the element.

each Unicode character stored in a compact array within a string typically requires 2 bytes. If each
character were stored independently as a one-character string, there would be significantly more
bytes used even though a list maintains careful ordering of the sequence of memory addresses, where those
elements reside in memory is not determined by the list. Because of the workings of the cache and
memory hierarchies of computers, it is often advantageous to have data stored in
memory near other data that might be used in the same computation

The only place in which we consider alternatives will be in Chapter 15, which focuses on
the impact of memory usage on data structures and algorithms

Primary support for compact arrays is in a module named array. That module defines a class, also
named array, providing compact storage for arrays of primitive data types. , the constructor for the
array class requires a type code as a first parameter,which is a character that designates the type of
data that will be stored in the array.As a tangible example, the type code, i , designates an array of
(signed) integers,typically represented using at least 16-bits each.type code allows the interpreter to
determine precisely how many bits are needed per element of the arra.We can declare the array as
primes = array( i , [2, 3, 5, 7, 11, 13, 17, 19])
The precise number of bits for the C data types is system-dependent, but typical ranges are shown
in the table.Code C Data Type Typical Number of Bytes
b signed char 1
B unsigned char 1
u Unicode char 2 or 4
h signed short int 2
H unsigned short int 2
i signed int 2 or 4
I unsigned int 2 or 4
l signed long int 4
L unsigned long int 4
f float 4
d float 8
The array module does not provide support for making compact arrays of user￾defined data types. Compact arrays
 of such structures can be created with the lower￾level support of a module named ctypes.

Because the system might dedicate neighboring memory locations to store other data, the capacity of an
 array cannot trivially be increased by expanding into sub￾sequent cells. In the context of representing
a Python tuple or str instance, this constraint is no problem. Instances of those classes are immutable, so
the correct size for an underlying array can be fixed when the object is instantiated

Python’s list class presents a more interesting abstraction. Although a list has a
particular length when constructed, the class allows us to add elements to the list,
with no apparent limit on the overall capacity of the list. To provide this abstraction,
Python relies on an algorithmic sleight of hand known as a dynamic array.

The first key to providing the semantics of a dynamic array is that a list instance
maintains an underlying array that often has greater capacity than the current length
of the list. For example, while a user may have created a list with five elements,
the system may have reserved an underlying array capable of storing eight object
references (rather than only five). This extra capacity makes it easy to append a
new element to the list by using the next available cell of the array
If a user continues to append elements to a list, any reserved capacity will
eventually be exhausted. In that case, the class requests a new, larger array from the
system, and initializes the new array so that its prefix matches that of the existing
smaller array.At that point in time, the old array is no longer needed, so it is
reclaimed by the system


 We rely on a func￾tion named getsizeof that is available from the sys module. This function reports
the number of bytes that are being used to store an object in Python. For a list, it
reports the number of bytes devoted to the array and other instance variables of the
list, but not any space devoted to elements referenced by the list.

n particular, we see the number of bytes jump
from 72 to 104, an increase of exactly 32 bytes. Our experiment was run on a
64-bit machine architecture, meaning that each memory address is a 64-bit number
(i.e., 8 bytes). We speculate that the increase of 32 bytes reflects the allocation of
an underlying array capable of storing four object references


"""
import sys # provides getsizeof function
data = [ ]
n = len(data)
for k in range(n): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print(" Length: {0:3d}; Size in bytes: {1:4d}" .format(a, b))
    data.append(None) # increase length by one

"""
Implementing a Dynamic Array
Of course, we cannot actually grow that array, as its capacity is fixed. If an
element is appended to a list at a time when the underlying array is full, we perform
the following steps:
1. Allocate a new array B with larger capacity.
2. Set B[i] = A[i], for i = 0,...,n−1, where n denotes current number of items.
3. Set A = B, that is, we henceforth use B as the array supporting the list.
4. Insert the new element in the new array

A com￾monly used rule is for the new array to have twice the capacity of the existing array
that has been filled.
 Support for creating low-level arrays is provided by a module named
ctypes. Because we will not typically use such a low-level structure in the remain￾der of this book, we omit
a detailed explanation of the ctypes module. Instead,we wrap the necessary command for declaring the raw 
array within a private util￾ity method make array. The hallmark expansion procedure is performed in our
nonpublic resize method.
"""
# provides low-level arrays
import ctypes

class DynamicArray:  # A dynamic array class akin to a simplified Python list.
    def __init__(self): #  Create an empty array
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self): #Return number of elements stored in the array
        return self._n
    def __getitem__(self, k): # Return element at index k.
        if not 0 <= k < self._n:
            raise IndexError( "invalid index ")
        return self._A[k] # retrieve from array
    def append(self, obj): # Add object to end of the array.”””
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
            self._A[self._n] = obj
            self._n += 1
    def _resize(self, c): # nonpublic utitity Resize internal array to capacity c.
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A = B # use the bigger array
        self._capacity = c

    # nonpublic utitity Return new array with capacity c
    def _make_array(self, c):
        return (c * ctypes.py_object)()
    # see ctypes documentation
"""
    Amortized Analysis of Dynamic Array
Using an algorithmic design pattern called amortization, we can show that per￾forming a sequence of such append 
operations on a dynamic array is actually quite efficient.To perform an amortized analysis, we use an 
accounting technique where we view the computer as a coin-operated appliance that requires the payment of
one cyber-dollar for a constant amount of computing time. When an operation is executed, we should have enough 
cyber-dollars available in our current “bank account” to pay for that operation’s running time, the total amount 
of cyber￾dollars spent for any computation will be proportional to the total time spent on that computation. 
The beauty of using this analysis method is that we can overcharge some operations in order to save up 
cyber-dollars to pay for others
    Geometric Increase in Capacity
With a base of 2 (i.e., doubling the array), if the last insertion causes a resize event, the array essentially 
ends up twice as large as it needs to be. If we instead increase the array by only 25% of its current size (i.e., 
a geometric base of 1.25), we do not risk wasting as much memory in the end, but there will be more intermediate 
resize events along the way. Still it is possible to prove an O(1) amortized bound, using a constant factor
greater than the 3 cyber-dollars per operation used in the proof of Proposition 5.1(see Exercise C-5.15)

    Beware of Arithmetic Progression
To avoid reserving too much space at once, it might be tempting to implement a dynamic array with a strategy 
in which a constant number of additional cells are reserved each time an array is resized. Unfortunately, 
the overall performance of such a strategy is significantly wors Using a fixed increment for each resize, 
and thus an arithmetic progression of intermediate array sizes, results in an overall time that is quadratic 
in the number of operations, as shown in the following proposition. Intuitively, even an increase
in 1000 cells per resize will become insignificant for large data sets

However, care must be taken to ensure that the structure cannot rapidly oscillate between growing and 
shrinking the underlying array, in which case the amortized bound would not be achieved. In Exercise C-5.16, 
we explore a strategy in which the array capacity is halved whenever the number of actual element falls
below one fourth of that capacity, thereby guaranteeing that the array capacity is at most four times the number 
of elements
"""
from time import time # import time function from time module
def compute_average(n): # Perform n appends to an empty list and return average time elapsed.
    data = [ ]
    start = time( ) # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time( ) # record the end time (in seconds)
    return (end - start) / n # compute average per operation
"""
We note that tuples are typically more memory efficient than
lists because they are immutable; therefore, there is no need for an underlying
dynamic array with surplus capacity. We summarize the asymptotic efficiency of
the nonmutating behaviors of the list and tuple classes

Adding Elements to a List
In Section 5.3 we fully explored the append method. In the worst case, it requires Ω(n) time because the
underlying array is resized, but it uses O(1)time in the amor￾tized sense. Lists also support a method, with
signature insert(k, value), that inserts a given value into the list at index 0 ≤ k ≤ n while shifting all 
subsequent elements back one slot to make room

There are two complicating factors in analyzing
the efficiency of such an operation. First, we note that the addition of one element
may require a resizing of the dynamic array. That portion of the work requires Ω(n)
worst-case time but only O(1) amortized time, as per append. The other expense
for insert is the shifting of elements to make room for the new item. The time for
that process depends upon the index of the new element, and thus the number of
other elements that must be shifted. That loop copies the reference that had been
at index n− 1 to index n, then the reference that had been at index n− 2 to n− 1,
continuing until copying the reference that had been at index k to k + 1,
. Overall this leads to an amortized O(n−k +1) performance for inserting at index k.

"""
def insert(self, k, value): # Insert value at index k, shifting subsequent values rightward.
# (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity: # not enough room
        self._resize(2 *self._capacity) # so double capacity
    for j in range(self. n, k, -1): # shift rightmost first
        self._A[j] = self._A[j-1]  # 10th the new place becomes 9th ele
    self._A[k] = value # store newest element
    self._n += 1
"""

 We have repeated that
experiment with the insert method, trying three different access patterns:
• In the first case, we repeatedly insert at the beginning of a list,
for n in range(N):
data.insert(0, None)
• In a second case, we repeatedly insert near the middle of a list,
for n in range(N):
data.insert(n // 2, None)
• In a third case, we repeatedly insert at the end of the list,
for n in range(N):
data.insert(n, None)

The results of our experiment are given in Table 5.5, reporting the average time per
operation (not the total time for the entire loop). As expected, we see that inserting
at the beginning of a list is most expensive, requiring linear time per operation.
Inserting at the middle requires about half the time as inserting at the beginning,
yet is still Ω(n) time. Inserting at the end displays O(1) behavior, akin to append


Removing Elements from a List
Python’s list class offers several ways to remove an element from a list. A call to
pop( ) removes the last element from a list. This is most efficient, because all other
elements remain in their original location. This is effectively an O(1) operation,
but the bound is amortized because Python will occasionally shrink the underlying
dynamic array to conserve memo
The parameterized version, pop(k), removes the element that is at index k < n
of a list, shifting all subsequent elements leftward to fill the gap that results from
the removal. The efficiency of this operation is O(n−k), as the amount of shifting
depends upon the choice of index k
Interestingly, there is no “efficient” case for remove; every call requires Ω(n)
time. One part of the process searches from the beginning until finding the value at
index k, while the rest iterates from k to the end in order to shift elements leftward.
This linear behavior can be observed experimentally



Extending a List
Python provides a method named extend that is used to add all elements of one list
to the end of a second list. In effect, a call to data.extend(other) produces the same
outcome as the code,

for element in other:
    data.append(element)

.. Finally, increased efficiency of extend comes from
the fact that the resulting size of the updated list can be calculated in advance. If the
second data set is quite large, there is some risk that the underlying dynamic array
might be resized multiple times when using repeated calls to append. With a single
call to extend, at most one resize operation will be performed
"""
def remove(self, value):# note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
        if self._A[k] == value: # found a match!
            for j in range(k, self._n - 1): # shift others to fill gap
                self._A[j] = self._A[j+1] # shift left
            self._A[self. n - 1] = None # help garbage collection
            self._n -= 1 # we have one less item
            return # exit immediately
    raise ValueError( "value not found" ) # only reached if no match

"""
Section 1.9.2 introduces the topic of list comprehension, using an example
such as squares = [ k k for k in range(1, n+1) ] as a shorthand for

squares = [ ]
for k in range(1, n+1):
  squares.append(k k)

e list comprehension syntax is significantly faster
than building the list by repeatedly appending
Similarly, it is a common Python idiom to initialize a list of constant values
using the multiplication operator, as in [0] n to produce a list of length n with
all values equal to zero


        Python’s String Class
methods that produce a new string (e.g., capitalize, center, strip) require time that is linear in
the length of the string that is produced. Many of the behaviors that test Boolean
conditions of a string (e.g., islower) take O(n)time, examining all n characters in the
worst case, but short circuiting as soon as the answer becomes evident (e.g., islower
can immediately return False if the first character is uppercased). The comparison
operators (e.g., ==, <) fall into this category as wel

Pattern Matching
Some of the most interesting behaviors, from an algorithmic point of view, are those
that in some way depend upon finding a string pattern within a larger string; this
goal is at the heart of methods such as contains , find, index, count, replace,
and split
A naive im￾plementation runs in O(mn) time case, because we consider the n−m+1 possible
starting indices for the pattern, and we spend O(m) time at each starting position,
checking if the pattern matches

Composing Strings
Finally, we wish to comment on several approaches for composing large strings. As
an academic exercise, assume that we have a large string named document, and our
goal is to produce a new string, letters, that contains only the alphabetic characters
of the original string (e.g., with spaces, numbers, and punctuation removed)
letters = # start with empty string
for c in document:
if c.isalpha( ):
letters += c # concatenate alphabetic character

.Because strings are immutable, the command, letters += c, would
presumably compute the concatenation, letters + c, as a new string instance and
then reassign the identifier, letters, to that result. Constructing that new string
would require time proportional to its length If the final result has n characters, the
series of concatenations would take time proportional to the familiar sum 1+ 2+
3+···+n, and therefore O(n2) time.The reason that a command, letters += c, causes a new
string instance to be created is that the original string must be left unchanged if
another variable in a program refers to that string. On the other hand, if Python
knew that there were no other references to the string in question, it could imple￾ment += more efficiently 
by directly mutating the string (as a dynamic array). As
it happens, the Python interpreter already maintains what are known as reference
counts for each object; this count is used in part to determine if an object can be
garbage collected.

A more standard Python idiom to guarantee linear time composition of a string
is to use a temporary list to store individual pieces, and then to rely on the join
method of the str class to compose the final result. Using this technique with our
previous example would appear as follows:
temp = [ ] # start with empty list
for c in document:
if c.isalpha( ):
temp.append(c) # append alphabetic character
letters = .join(temp) # compose overall result

As we discussed at the end of the previous section, we can further improve
the practical execution time by using a list comprehension syntax to build up the
temporary list, rather than by repeated calls to append. That solution appears as,
letters = .join([c for c in document if c.isalpha( )])
Better yet, we can entirely avoid the temporary list with a generator comprehension:
letters = .join(c for c in document if c.isalpha( ))

"""

"""
        Using Array-Based Sequences
    5.5.1 Storing High Scores for a Game
The first application we study is storing a sequence of high score entries for a video
game. This is representative of many applications in which a sequence of objects
must be stored
we consider what information to include in an object representing a
high score entry. Obviously, one component to include is an integer representing
the score itself, which we identify as score. Another useful thing to include is
the name of the person earning this score, which we identify as name.

"""

class GameEntry:#Represents one entry of a list of high scores.”””

    def init (self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})' .format(self._name, self._score)

"""
A Class for High Scores
To maintain a sequence of high scores, we develop a class named Scoreboard. A
scoreboard is limited to a certain number of high scores that can be saved; once that
limit is reached, a new score only qualifies for the scoreboard if it is strictly higher
than the lowest “high score” on the board. The length of the desired scoreboard may
depend on the game, perhaps 10, 50, or 500

The command
self. board = [None] capacity
creates a list with the desired length, yet all entries equal to None. We maintain
an additional instance variable, n, that represents the number of actual entries
currently in our table.s the getitem method
to retrieve an entry at a given index with a syntax board[i] (or None if no such entry
exists), and we support a simple str method that returns a string representation
of the entire scoreboard, with one entry per line


"""
class Scoreboard:#Fixed-length sequence of high scores in nondecreasing order.”””

    def __init__ (self, capacity=10): # Initialize scoreboard with given maximum capacity.
        self._board = [None] * capacity # reserve space for future scores
        self._n=0 # number of actual entries

    def __getitem__(self, k):#Return entry at index k.”””
        return self._board[k]
    def __str__(self): # Return string representation of the high score list.”””
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    def add(self, entry):#Consider adding entry to high scores.”””
        score = entry.get_score( )
        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board): # no score drops from list
                self._n += 1 # so overall number increases
        # shift lower scores rightward to make room for new entry
        j = self._n - 1
        while j > 0 and self._board[j-1].get_score( ) < score:
            self._board[j] = self._board[j-1] # shift entry from j-1 to j
            j -= 1 # and decrement j
        self._board[j] = entry # when done, add new entry

"""
. If the board is not yet full,
any new entry will be retained. Once the board is full, a new entry is only retained
if it is strictly better than one of the other scores, in particular, the last entry of the
scoreboard, which is the lowest of the high scores.
When a new score is considered, we begin by determining whether it qualifies
as a high score. If so, we increase the count of active scores, n, unless the board
is already at full capacity. In that case, adding a new high score causes some other
entry to be dropped from the scoreboard, so the overall number of entries remains
the same.

final task is to shift any in￾ferior scores one spot lower (with the least score being dropped entirely when the
scoreboard is full). This process is quite similar to the implementation of the insert
method of the list class

 starting with an unordered sequence of elements and rearranging
them into nondecreasing order.-insertion-sort->. The algorithm proceeds as follows for an array￾based sequence. 
We start with the first element in the array. One element by itself
is already sorted. Then we consider the next element in the array. If it is smaller
than the first, we swap them. Next we consider the third element in the array. We
swap it leftward until it is in its proper order with the first two elements. We then
consider the fourth element, and swap it leftward until it is in the proper order with
the first three. W
The nested loops of insertion-sort lead to an O(n2) running time in the worst
case. The most work is done if the array is initially in reverse order. On the other
hand, if the initial array is nearly sorted or perfectly sorted, insertion-sort runs in
O(n) time because there are few or no iterations of the inner loop


Simple Cryptography
An interesting application of strings and lists is cryptography, the science of secret
messages and their applications. This field studies ways of performing encryp￾tion, which takes a message, 
called the plaintext, and converts it into a scrambled
message, called the ciphertext. Likewise, cryptography also studies corresponding
ways of performing decryption, which takes a ciphertext and turns it back into its
original plaintext

we can write the Caesar cipher with a rotation of r as a simple
formula: Replace each letter i with the letter (i + r) mod 26, where mod is the
modulo operator, which returns the remainder after performing an integer division.
This operator is denoted with % in Python, and it is exactly the operator we need
to easily perform the wrap around at the end of the alphabet. For 26 mod 26 is
0, 27 mod 26 is 1, and 28 mod 26 is 2.
In order to find a replacement for a character in our Caesar cipher, we need to
map the characters A to Z to the respective numbers 0 to 25. The formula for
doing that conversion is j = ord(c) − ord( A ).


"""

def insertion_sort(A): # Sort list of comparable elements into nondecreasing order.”””
    for k in range(1, len(A)): # from 1 to n-1
        cur = A[k] # current element to be inserted
        j=k # find correct index j for current
        while j > 0 and A[j-1] > cur: # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur # cur is now in the right place

"""
In Code Fragment 5.11, we develop a Python class for performing the Caesar
cipher with an arbitrary rotational shift, and demonstrate its use. When we run this
program (to perform a simple test), we get the following output.
Secret: WKH HDJOH LV LQ SODB; PHHW DW MRH’V.
Message: THE EAGLE IS IN PLAY; MEET AT JOE’S.
The constructor for the class builds the forward and backward translation strings for
the given rotation. With those in hand, the encryption and decryption algorithms
are essentially the same, and so we perform both by means of a nonpublic utility
method named transform.
"""
class CaesarCipher: # Class for doing encryption and decryption using a Caesar cipher.”””

    def __init__(self, shift): # Construct Caesar cipher using given integer shift for rotation.”””
        encoder = [None] * 26 # temp array for encryption
        decoder = [None] * 26 # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder) # will store as string
        self._backward = ''.join(decoder) # since fixed

    def encrypt(self, message):  # Return string representing encripted message.”””
        return self._transform(message, self._forward)

    def decrypt(self, secret):  # Return decrypted message given encrypted secret.”””
        return self._transform(secret, self._backward)
    def _transform(self, original, code): # Utility to perform transformation based on given code string
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper( ):
                j = ord(msg[k]) - ord( 'A' ) # index from 0 to 25
                msg[k] = code[j] # replace this character
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)

    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."

    coded = cipher.encrypt(message)

    print('Secret:', coded)

    answer = cipher.decrypt(coded)

    print('Message:', answer)


"""
Multidimensional Data Sets
Lists, tuples, and strings in Python are one-dimensional. We use a single index to
access each element of the sequence. Many computer applications involve mul￾tidimensional data sets. For example, 
computer graphics are often modeled in
either two or three dimensions. Geographic information may be naturally repre￾sented in two dimensions, medical 
imaging may provide three-dimensional scans
of a patient, and a company’s valuation is often based upon a high number of in￾dependent financial measures that 
can be modeled as multidimensional data. A
two-dimensional array is sometimes also called a matrix

A common representation for a two-dimensional data set in Python is as a list
of lists. In particular, we can represent a two-dimensional array as a list of rows,
with each row itself being a list of value
data = [ [22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61] ]

If our
goal were to create the equivalent of a two-dimensional list of integers, with r rows
and c columns, and to initialize all values to zero, a flawed approach might be to
try the command
data = ([0] * c) * r
While([0] c) is indeed a list of c zeros, multiplying that list by r unfortunately cre￾ates a single list with 
length r· c, just as [2,4,6] 2 results in list [2, 4, 6, 2, 4, 6].

A better, yet still flawed attempt is to make a list that contains the list of c zeros
as its only element, and then to multiply that list by r. That is, we could try the
command
data = [ [0] * c ] * r

To properly initialize a two-dimensional list, we must ensure that each cell of
the primary list refers to an independent instance of a secondary list. This can be
accomplished through the use of Python’s list comprehension syntax.
data = [ [0] * c for j in range(r) ]
[ [ O , X , O ], [ , X , ], [ , O , X ] ]

"""
class TicTacToe: # Management of a Tic-Tac-Toe game (does not do strategy).”””
    def init (self): # Start a new game.”””
     self.board = [ [' '] * 3 for j in range(3) ]
     self.player = 'X'
    def mark(self, i, j): # Put an X or O mark at position (i,j) for next player s turn.”””
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError( 'Invalid board position ')
        if self.board[i][j] != ' ':
            raise ValueError( 'Board position occupied' )
        if self.winner( ) is not None:
            raise ValueError(' Game is already complete ')
        self.board[i][j] = self.player
        if self.player == 'X' :
            self.player = 'O'
        else:
            self.player = 'X'

    def _is_win(self,mark): # Check whether the board configuration is a win for the given player.”””
        board = self.board # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
                mark == board[0][2] == board[1][1] == board[2][0]) # rev diag
    def winner(self): # Return mark of winning player, or None to indicate a tie.”””
        for mark in 'XO' :
            if self._is_win(mark):
                return mark
        return None
    def __str__(self): #Return string representation of current game board.”””
        rows = [' | '.join(self.board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)


"""
temp = [ ] # start with empty list
for c in document:
    if c.isalpha( ):
    temp.append(c) # append alphabetic character
letters =" ".join(temp) # compose overall result
"""























class _DoublyLinkedBase:
    class _Node:
        __slots__ = "_element" , "_prev" , "_next" # streamline memory
        def __init__(self, element, prev, next): # initialize node’s fields
            self._element = element # user’s element
            self._prev = prev # previous node reference
            self._next = next # next node reference

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer # trailer is after header
        self._trailer._prev = self._header # header is before trailer
        self._size = 0 # number of elements

    def __len__(self):
        return self._size
    def is_empty(self): # Return True if list is empty.”””
        return self._size == 0
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor) # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    def _delete_node(self, node): # Delete nonsentinel node from the list and return its element.”””
        predecessor = node._prev  # prev of node deleted is named predecessor
        successor = node._next  # next of node deleted is named successor
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element # record deleted element
        node._prev = node._next = node._element = None # deprecate node
        return element # return deleted element


# the following code fragment prints all elements of a positional list named data.
data = []
cursor = data.first( )
while cursor is not None:
    print(cursor.element( )) # print the element stored at the position
    cursor = data.after(cursor) # advance to the next position (if any)


class PositionalList(_DoublyLinkedBase):

    def __init__(self):
        self._header = _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    # ... methods like add_first, add_before, delete, etc.
    # These methods would interact with _Node objects and return Position objects.

#--------------------
class _Node:
    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next

class Position:
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
        return not (self == other)

    def _validate(self, p):
        # Helper to ensure p is a valid Position for this list
        if not isinstance(p, Position):
            raise TypeError("p must be a Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node.next is None: # Convention for a removed node
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        # Helper to create a Position instance from a node
        if node is self._header or node is self._trailer:
            return None
        return Position(self, node)

    def add_between(self, e, predecessor, successor):
        new_node = _Node(e, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return self._make_position(new_node)

    # ... (other methods like addFirst, addLast, before, after, remove, etc.)

#------------------------------- utility method -------------------------------
    def make_position(self, node): # Return Position instance for given node (or None if sentinel).”””
        if node is self._header or node is self._trailer:
            return None # boundary violation
        else:
            return self.Position(self, node) # legitimate position
#------------------------------- accessors -------------------------------
    def first(self):  # Return the first Position in the list (or None if list is empty)
        return self._make_position(self._header._next)

    def last(self): #Return the last Position in the list (or None if list is empty)
        return self._make_position(self._trailer._prev)

    def before(self, p): # Return the Position just before Position p (or None if p is first
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p): # Return the Position just after Position p (or None if p is last).”””
        node = self._validate(p)
        return self._make_position(node. next)

    def iter (self): # Generate a forward iteration of the elements of the list.”””
        cursor = self.first( )
        while cursor is not None:
            yield cursor.element( )
            cursor = self.after(cursor)

#------------------------------- mutators -------------------------------
# override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor): # Add element between existing nodes and return new Position.”””
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e): # Insert element e at the front of the list and return new Position.”””
        return self._insert_between(e, self._header, self. _header._next)

    def add_last(self, e): # Insert element e at the back of the list and return new Position.”””
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e): # Insert element e into list before Position p and return new Position.”””
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e): # Insert element e into list after Position p and return new Position.”””
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p): # Remove and return the element at Position p.”””
        original = self._validate(p)
        return self._delete_node(original) # inherited method returns element

    def replace(self, p, e): #Replace the element at Position p with e.,Return the element formerly at Position p.
        original = self._validate(p)
        old_value = original._element # temporarily store old element
        original._element = e # replace with new element
        return old_value # return the old element value
"""
for example, an air-traffic control center that has to decide which flight to clear for
landing from among many approaching the airport. This choice may be influenced by factors
such as each plane’s distance from the runway, time spent waiting in a holding pattern,
or amount of remaining fuel. It is unlikely that the landing decisions are based purely
on a FIFO policy
To use another airline
analogy, suppose a certain flight is fully booked an hour prior to departure. Be￾cause of
the possibility of cancellations, the airline maintains a queue of standby passengers hoping
to get a seat. Although the priority of a standby passenger is influenced by the check-in
time of that passenger, other considerations include the fare paid and frequent-flyer status.
So it may be that an available seat is given to a passenger who has arrived later

we introduce a new abstract data type known as a priority queue.
This is a collection of prioritized elements that allows arbitrary element insertion,and
allows the removal of the element that has first priority. When an element is added to a
priority queue, the user designates its priority by providing an associated key. The element
with the minimum key will be the next to be removed from the queue (thus, an element with key
1 will be given priority over an element with key 2).

we model an element and its priority as a key-value pair. We define the priority queue ADT
to support the following methods for a priority queue P:

P.add(k, v): Insert an item with key k and value v into priority queue P.
P.min( ): Return a tuple, (k,v), representing the key and value of an item in priority
queue P with minimum key (but do not re￾move the item); an error occurs if the priority
queue is empty.
P.remove min( ): Remove an item with minimum key from priority queue P,and return a tuple,
(k,v), representing the key and value of the removed item; an error occurs if the priority
queue is empty.
P.is empty( ): Return True if priority queue P does not contain any items.
len(P): Return the number of items in priority queue P.

A priority queue may have multiple entries with equivalent keys, in which case
methods min and remove min may report an arbitrary choice of item having mini￾mum key.
Values may be any type of object.

Implementing a Priority Queue
-----------------------------
One challenge in implementing a priority queue is that we must keep track of both an element
and its key, even as items are relocated within our data structure. we introduced the
composition design pattern,defining an Item class that assured that each element remained
paired with its associated count in our primary data structure

to store items internally as pairs consisting of a key k and a value v. To implement this
concept for all priority queue implementations, we provide a PriorityQueueBase class

that includes a definition for a nested class named Item.

"""
from pyparsing import Empty


class PriorityQueueBase: # Abstract base class for a priority queue.”””

    class _Item: #Lightweight composite to store priority queue items.”””
        __slots__ = '_key' , '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys
        def is_empty(self): # concrete method assuming abstract len
            #Return True if the priority queue is empty.
            return len(self) == 0

"""
These items are stored within a PositionalList, identified as the data member of our class. 
We assume that the positional list is implemented with a doubly-linked list, so that all
operations of that ADT execute in O(1) time

At all times, the size of the list equals the number of key-value pairs currently stored in
the priority queue. For this reason, our priority queue len method simply returns the length 
of the internal data list
Each time a key-value pair is added to the priority queue, via the add method,
we create a new Item composite for the given key and value, and add that item to
the end of the list. Such an implementation takes O(1) time

when min or remove min is called, we must locate the item with minimum key. Because the items 
are not sorted, we must inspect all entries to find one with a minimum key. For convenience, 
we define a nonpublic find min utility that returns the position of an item with minimum key

Knowledge of the position allows the remove min method to invoke the delete method on the 
positional list
Due to the loop for finding the minimum key, both min and remove min methods run in O(n).


"""
class UnsortedPriorityQueue(PriorityQueueBase,Position): # base class defines Item
    # A min-oriented priority queue implemented with an unsorted list
    def _find_min(self):
        if self.is_empty():
            raise Empty( 'Priority queue is empty' )
        small = self._data.first( )
        walk = self._data.after(small)
        while walk is not None:
            if walk.element( ) < small.element( ):
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self): # Create a new empty Priority Queue.
        self._data = PositionalList() #  doubly-linked list

    def __len__(self): # Return the number of items in the priority queue.
        return len(self._data)

    def add(self, key, value): # Add a key-value pair.”””
        self._data.add_last(self._Item(key, value))

    def min(self):  # Return but do not remove (k,v) tuple with minimum key.”””
        p = self._find_min( )
        item = p.element( )
        return (item._key,item._value)

    def remove_min(self): # Remove and return (k,v) tuple with minimum key.”””
        p = self._find_min( )
        item = self._data.delete(p)
        return (item._key, item._value)

#  Implementation with a Sorted List
"""
We rely on the first method of the posi￾tional list to find the position of the first item, 
and the delete method to remove the entry from the list. Assuming that the list is implemented 
with a doubly linked list, operations min and remove min take O(1) time
This benefit comes at a cost, however, for method add now requires that we scan
the list to find the appropriate position to insert the new item. Our implementation
starts at the end of the list, walking backward until the new key is smaller than
an existing item; in the worst case, it progresses until reaching the front of the
list. Therefore, the add method takes O(n)
"""
class SortedPriorityQueue(PriorityQueueBase,Position): # base class defines Item
     # A min-oriented priority queue implemented with a sorted list.”””
    def __init__(self): # Create a new empty Priority Queue
        self._data = PositionalList( )

    def __len__(self): # Return the number of items in the priority queue.”””
        return len(self._data)

    def add(self, key, value): # Add a key-value pair.”””
        newest = self._Item(key, value) # make new item instance
        walk = self._data.last() # walk backward looking for smaller key
        while walk is not None and newest < walk.element( ):
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest) # new key is smallest
        else:
            self._data.add_after(walk, newest) # newest goes after walk

    def min(self): # Return but do not remove (k,v) tuple with minimum key.”””
        if self.is_empty( ):
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element( )
        return (item._key, item._value)

    def remove_min(self): # Remove and return (k,v) tuple with minimum key.
        if self.is_empty( ):
            raise Empty( 'Priority queue is empty.' )
        item = self._data.delete(self._data.first( ))
        return (item._key, item._value)

"""
When using an unsorted list to store entries,we can perform insertions in O(1) time, but 
finding or removing an element with minimum key requires an O(n)-time loop through the 
entire collection. In contrast,if using a sorted list, we can trivially find or remove the 
minimum element in O(1)time, but adding a new element to the queue may require O(n) time 
to restore the sorted order.

a more efficient realization of a priority queue using a data structure called a binary heap
This data structure allows us to perform both insertions and removals in logarithmic time

using the structure of a binary tree that stores a collection of items at its
positions and that satisfies two additional properties: a relational property defined
in terms of the way keys are stored in T and a structural property defined in terms
of the shape of T itself

relational property :
Heap-Order Property: In a heap T, for every position p other than the root, the
key stored at p is greater than or equal to the key stored at p’s parent.the keys encountered on a path from
the root(min) to a leaf of T are in nondecreasing order.

For the sake of efficiency, we want the heap T to have as small a height as possible
Complete Binary Tree Property: A heap T with height h is a complete binary tree if levels
0,1,2,...,h− 1 of T have the maximum number of nodes possible(namely, level i has 2i nodes
,for 0 ≤ i ≤ h− 1) and the remaining nodes at level h reside in the leftmost possible 
positions at that level

A heap T storing n entries has height h = [log n],number of nodes in level h is at least 1 and at most 2h
2^0(level) = 1   ,   2^(h+1) - 1   max no of ele

Implementing a Priority Queue with a Heap

if we can perform update operations on a heap in time proportional to its height, then those
opera￾tions will run in logarithmic time. Let us therefore turn to the problem of how to efficiently
perform various priority queue methods using a heap


"""






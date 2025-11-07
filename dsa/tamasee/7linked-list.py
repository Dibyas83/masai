


"""

Python’s list class is highly optimized, and often a great choice for storage. With that said, there are
some notable disadvantages:
1. The length of a dynamic array might be longer than the actual number of
elements that it stores.
2. Amortized bounds for operations may be unacceptable in real-time systems.
3. Insertions and deletions at interior positions of an array are expensive.

A linked list, in contrast, relies on a more distributed representation in which a lightweight object,
known as a node, is allocated for each element. Each node maintains a reference to its element and one
or more references to neighboring nodes in order to collectively represent the linear order of the sequence.

A singly linked list, in its simplest form, is a collection of nodes that collectively
form a linear sequence. Each node stores a reference to an object that is an element
of the sequence, as well as a reference to the next node of the list

                    ele|next        ele|next    ele|next
Thenode’s element member references an arbitrary object that is an element of the se￾quence (the airport
code MSP, in this example), while the next member referencesthe subsequent node of the linked list (or
None if there is no further node
                x                y              z
          ele(head) | next        ele | next    ele(tail) | next ->   Ø
list instance maintains a member named head that identifies the first node of the list, and in some
applications another member named tail that identifies the last node of the list. The None object is
denoted as Ø
By starting at the head, and moving from one node to another by following each node’s next reference,
we can reach the tail of the list. We can identify the tail as the node having None as its next reference,
next reference of a node can be viewed as a link or pointer to another node, the process of traversing
a list is also known as link hopping or pointer hopping.

Each node is represented as a unique object, with that instance storing a
reference to its element and a reference to the next node (or None). Another object
represents the linked list as a whole. Minimally, the linked list instance must keep
a reference to the head of the list
we continue to illustrate nodes as objects, and each node’s “next” reference as a pointer. However,
for the sake of simplicity,we illustrate a node’s element embedded directly within the node structure,
 even though the element is, in fact, an independent object.

 insertion(at the head)
The main idea is that we create a new node, set its element to the new element, set its next link to
refer to the current head, and then set the list’s head to point to the new node.

Algorithm add first(L,e):
newest = Node(e) {create new node instance storing reference to element e}
newest.next = L.head {set new node’s next to reference the old head node}
L.head = newest {set variable head to reference the new node}
L.size = L.size+1 {increment the node count}

insertion(at the tail)
In this case, we create a new
node, assign its next reference to None, set the next reference of the tail to point to
this new node, and then update the tail reference itself to this new node

Algorithm add last(L,e):
newest = Node(e) {create new node instance storing reference to element e}
newest.next = None {set new node’s next to reference the None object}
L.tail.next = newest {make old tail node point to new node}
L.tail = newest {set variable tail to reference the new node}
L.size = L.size+1 {increment the node count}

 we set the next pointer for the old tail node before we make variable tail point
to the new node

remove

Algorithm remove first(L):
if L.head is None then
Indicate an error: the list is empty.
L.head = L.head.next {make head point to next node (or None)}
L.size = L.size−1 {decrement the node count}

Code Fragment 7.3: Removing the node at the beginning of a singly linked list.

Unfortunately, we cannot easily delete the last node of a singly linked list. Even
if we maintain a tail reference directly to the last node of the list, we must be able
to access the node before the last node in order to remove the last node. But we
cannot reach the node before the tail by following next links from the tail. The only
way to access this node is to start from the head of the list and search all the way
through the list. But such a sequence of link-hopping operations could take a long
time. If we want to support such an operation efficiently, we will need to make our
list doubly linked (as we do in Section 7.3)


"""
from pyparsing import Empty


# stack
class LinkedStack:

    class _Node: #  Lightweight, nonpublic class for storing a singly linked node.”””
        __slots__ = "_element ", "_next" # streamline memory usage

        def __init__(self,element,next): # initialize node’s fields
            self._element = element # reference to user’s element
            self._next = next # reference to next node

#------------------------------- stack methods -------------------------------
    def __init__(self): # Create an empty stack.
        self._head = None # reference to the head node
        self._size = 0 # number of stack elements
    def __len__(self): # Return the number of elements in the stack.
        return self._size
    def is_empty(self): # Return True if the stack is empty.
        return self._size == 0
    def push(self, e): # Add element e to the top of the stack.
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1
        # Note that the next field of the new node is set to the existing top node, and then
        # self. head is reassigned to the new node.
    def top(self): # Return (but do not remove) the element at the top of the stack .Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element # top of stack is at head of list

    def pop(self): #Remove and return the element from the top of the stack (i.e., LIFO).Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next # bypass the former top node
        self._size -= 1
        return answer

"""
there may potentially be many node instances in a single list.
The constructor of the Node class is designed for our convenience

The implementation of push essentially mirrors the pseudo-code for insertion
at the head of a singly linked list as outlined in Code Fragment 7.1. When we push
a new element e onto the stack, we accomplish the necessary changes to the linked
structure by invoking the constructor of the Node class as follows:

Note that the next field of the new node is set to the existing top node, and then
self. head is reassigned to the new node.
"""

# Node structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Stack implementation using linked list
class myStack:
    def __init__(self):
        # initially stack is empty
        self.top = None
        self.count = 0

    # push operation
    def push(self, x):
        temp = Node(x)
        temp.next = self.top    # already existing top or none
        self.top = temp

        self.count += 1

    # pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return -1
        temp = self.top
        self.top = self.top.next  # self.top.next stores the address of 2nd element
        val = temp.data

        self.count -= 1
        return val

    # peek operation
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return -1
        return self.top.data

    # check if stack is empty
    def isEmpty(self):
        return self.top is None

    # size of stack
    def size(self):
        return self.count


if __name__ == "__main__":
    st = myStack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())
"""

"""
# que

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.currSize = 0

        # Check if the queue is empty

    def isEmpty(self):
        return self.front is None

    # Add element to the queue
    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        # increment size
        self.currSize += 1

        # Remove element from the queue and return it

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return -1
        removedData = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        # decrement size
        self.currSize -= 1
        return removedData

    # Return the front element
    def getfront(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.front.data

    # Return size in O(1)
    def size(self):
        return self.currSize


if __name__ == "__main__":
    q = myQueue()

    q.enqueue(10)
    q.enqueue(20)

    print("Dequeue:", q.dequeue())

    q.enqueue(30)

    print("Front:", q.getfront())
    print("Size:", q.size())

"""
stack -  add,remove from head - lifo
que - rem head,add tail -fifo

round robin scheduler

 One node is removed from the list, with
appropriate adjustments to the head of the list and the size decremented, and then a
new node is created to reinsert at the tail of the list and the size is incremented.
If using a circularly linked list, the effective transfer of an item from the “head”
of the list to the “tail” of the list can be accomplished by advancing a reference
that marks the boundary of the queue. We will next provide an implementation
of a CircularQueue class that supports the entire queue ADT, together with an ad￾ditional method, rotate( ), that moves the first element of the queue to the back.
(A similar method is supported by the deque class of Python’s collections module;
see Table 6.4.) With this operation, a round-robin schedule can more efficiently be
implemented by repeatedly performing the following steps:
1. Service element Q.front()
2. Q.rotate()

there is no need for us to explicitly store references to both the head and the tail; as long 
as we keep a reference to the tail, we can always find the head by following the tail’s next reference.

Code Fragments 7.9 and 7.10 provide an implementation of a CircularQueue
class based on this model. The only two instance variables are tail, which is a
reference to the tail node (or None when empty), and size, which is the current
number of elements in the queue. When an operation involves the front of the
queue, we recognize self. tail. next as the head of the queue. When enqueue is
called, a new node is placed just after the tail but before the current head, and then
the new node becomes the tail.

In addition to the traditional queue operations, the CircularQueue class supports
a rotate method that more efficiently enacts the combination of removing the front
element and reinserting it at the back of the queue. With the circular representation,
we simply set self. tail = self. tail. next to make the old head become the new tail
(with the node after the old head becoming the new head

"""

class CircularQueue:
        class _Node:  # Lightweight, nonpublic class for storing a singly linked node.”””
            __slots__ = "_element ", "_next"  # streamline memory usage

            def __init__(self, element, next):  # initialize node’s fields
                self._element = element  # reference to user’s element
                self._next = next  # reference to next node



        # ------------------------------- stack methods -------------------------------
        def __init__(self):  # Create an empty que.
            self._tail = None  # will represent tail of queue
            self._size = 0  # number of queue elements

        def __len__(self):  # Return the number of elements in the stack.
            return self._size

        def is_empty(self):  # Return True if the stack is empty.
            return self._size == 0

        def first(self): # Return (but do not remove) the element at the front of the queue.
            if self.is_empty( ):
                raise Empty( "Queue is empty" )
            head = self._tail._next
            return head._element

        def dequeue(self): #Remove and return the first element of the queue (i.e., FIFO).
            # Raise Empty exception if the queue is empty.
            if self.is_empty():
                raise Empty( "Queue is empty" )
            oldhead = self._tail._next
            if self._size == 1: # removing only element
                self._tail = None # queue becomes empty
            else:
                self._tail._next = oldhead._next # bypass the old head
            self._size -= 1
            return oldhead._element

        def enqueue(self, e): #Add an element to the back or tail of queue.”””
            newest = self._Node(e, None) # node will be new tail node
            if self.is_empty( ):
                newest._next = newest # initialize circularly
            else:
                newest._next = self._tail._next # new node points to head
                self._tail._next = newest # old tail points to new node
            self._tail = newest # new node becomes the tail
            self._size += 1
        def rotate(self): # Rotate front element to the back of the queue.
            if self._size > 0:
                self._tail = self._tail._next # old head becomes new tail
        # Implementation of a CircularQueue class, using a circularly linked list as storage










# ai
class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid  # Process ID
        self.burst_time = burst_time  # Total execution time
        self.remaining_time = burst_time  # Remaining execution time

class Node:
    def __init__(self, process):
        self.process = process
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_process(self, process):
        new_node = Node(process)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Points to itself for circularity
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def is_empty(self):
        return self.head is None

    def remove_process(self, process_to_remove):
        if self.is_empty():
            return

        current = self.head
        prev = None

        # Handle case where the head is the process to remove
        if current.process == process_to_remove:
            if self.head == self.tail:  # Only one element in the list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return

        # Traverse to find the process to remove
        while current.next != self.head:
            if current.next.process == process_to_remove:
                prev = current
                break
            current = current.next

        if prev: # Found the process
            if prev.next == self.tail: # If the tail is being removed
                self.tail = prev
            prev.next = prev.next.next


def round_robin_scheduler(processes_list, time_quantum):
    ready_queue = CircularLinkedList()
    for p in processes_list:
        ready_queue.add_process(p)

    current_node = ready_queue.head
    time = 0

    print(f"Starting Round Robin Scheduling with Time Quantum: {time_quantum}")

    while not ready_queue.is_empty():
        if not current_node: # If the current_node was removed and the list is not empty
            current_node = ready_queue.head
            if not current_node: # If the list became empty after removal
                break

        process = current_node.process

        if process.remaining_time > 0:
            execution_time = min(process.remaining_time, time_quantum)
            process.remaining_time -= execution_time
            time += execution_time
            print(f"Time {time}: Process {process.pid} executed for {execution_time} units. Remaining: {process.remaining_time}")

            if process.remaining_time == 0:
                print(f"Time {time}: Process {process.pid} completed.")
                # Remove completed process from the ready queue
                next_node = current_node.next
                ready_queue.remove_process(process)
                current_node = next_node # Move to the next process in the cycle
            else:
                current_node = current_node.next # Move to the next process in the cycle
        else: # Should not happen if processes are removed upon completion
            current_node = current_node.next


# Example Usage
if __name__ == "__main__":
    processes = [
        Process("P1", 10),
        Process("P2", 5),
        Process("P3", 8)
    ]
    quantum = 3
    round_robin_scheduler(processes, quantum)

"""
 we are unable to efficiently delete a node at the tail of the list. More generally, we cannot efficiently 
delete an arbitrary node from an interior position of the list if only given a reference to that node, because
we cannot determine the node that immediately precedes the node to be deleted(yet, that node needs to have its 
next reference updated).To provide greater symmetry, we define a linked list in which each node keeps
an explicit reference to the node before it and a reference to the node after it. Such
a structure is known as a doubly linked list

In order to avoid some special cases when operating near the boundaries of a doubly linked list, it helps to 
add special nodes at both ends of the list: a header node at the beginning of the list, and a trailer node at
the end of the list. These “dummy” nodes are known as sentinels (or guards), and they do not store elements 
of the primary sequence

When using sentinel nodes, an empty list is initialized so that the next field of the header points to the 
trailer, and the prev field of the trailer points to the header;the remaining fields of the sentinels are 
irrelevant (presumably None, in Python).For a nonempty list, the header’s next will refer to a node containing 
the first real element of a sequence, just as the trailer’s prev references the node containing the last element of
a sequence

Advantage of Using Sentinels
Although we could implement a doubly linked list without sentinel nodes (as we
did with our singly linked list in Section 7.1), the slight extra space devoted to the
sentinels greatly simplifies the logic of our operations. Most notably, the header and
trailer nodes never change—only the nodes between them change.

when a new element is inserted at the front of the sequence, we will simply add the new node
between the header and the node that is currently after the header

    header BWI JFK SFO trailer
    
    header BWI JFK "PVD" SFO trailer
    
    header BWI JFK "PVD" SFO trailer

an index is not convenient for linked lists as there is no efficient way to find the jth element; 
it would seem to require a traversal of a portion of the list., the most direct way to describe the location
of an operation is by identifying a relevant node of the list. However, we prefer
to encapsulate the inner workings of our data structure to avoid having users di￾rectly access nodes of a list. In the remainder of this chapter, we will develop
two public classes that inherit from our DoublyLinkedBase class to provide more
coherent abstractions

The constructor instantiates the two sentinel nodes and links them directly to each
other.

"""
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

"""
    double-ended queue (deque) ADT
    
With the use of sentinels, the key to our implementation is to remember that
the header does not store the first element of the deque—it is the node just after the
header that stores the first element (assuming the deque is nonempty). Similarly,
the node just before the trailer stores the last element of the deque

We use the inherited insert between method to insert at either end of the
deque. To insert an element at the front of the deque, we place it immediately
between the header and the node just after the header. An insertion at the end of
deque is placed immediately before the trailer node

"""


class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance

    def first(self): # ”Return (but do not remove) the element at the front of the deque
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element # real item just after header

    def last(self): #Return (but do not remove) the element at the back of the deque.”””
        if self.is_empty( ):
            raise Empty("Deque is empty")
        return self._trailer._prev._element # real item just before trailer

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next) # after header

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev,self._trailer) # before trailer

    def delete_first(self):
        if self.is_empty( ):
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next) # use inherited method

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev) # use inherited method
    # Implementation of a LinkedDeque class that inherits from the DoublyLinkedBase class.

"""
What if a waiting customer decides to hang up before reaching the front of the customer
service queue? Or what if someone who is waiting in line to buy tickets allows a friend to “cut” into line 
at that position? We would like to design an abstract data type that provides a user a way to refer to 
elements anywhere in a sequence, and to perform arbitrary insertions and deletions

finding an element at a given index within a linked list requires traversing the list incrementally from its
beginning or end, counting elements as we go. Furthermore, indices are not a good abstraction for describing 
a local position in some applications, because the index of an entry changes over time due to inser￾tions or 
deletions that happen earlier in the sequence

A word processor uses the abstraction of a cursor to describe a position within the document without explicit 
use of an integer index, allowing operations such as “delete the character at the cursor” or “insert a new 
character just after the cursor.” Furthermore, we may be able to refer to an inherent position within a doc￾ument, 
such as the beginning of a particular section, without relying on a character index (or even a section number) 
that may change as the document evolves.

the following code fragment prints all elements of a positional list named data.
"""
data = []
cursor = data.first( )
while cursor is not None:
    print(cursor.element( )) # print the element stored at the position
    cursor = data.after(cursor) # advance to the next position (if any)


"""
A PositionalList class, built upon a doubly linked list, offers a robust way to manage ordered collections of 
elements while providing stable "positions" that remain valid even as the list undergoes modifications. This is 
in contrast to traditional array-based lists where element indices can shift after insertions or deletions.
Core Components:

_Node Class:
Represents an individual element within the doubly linked list.
Stores _element (the actual data), _prev (reference to the previous node), and _next (reference to the next node).

Position Class:
A lightweight wrapper around a _Node that provides a stable reference to a location within the PositionalList.
Stores a reference to the _node it represents and the _container (the PositionalList instance it belongs to) 
to ensure validity.Offers a method element() to retrieve the data stored at that position.

PositionalList Class:
Initialization:
Maintains _header and _trailer sentinel nodes, which simplify boundary conditions for insertions and deletions.
Keeps track of _size (number of elements).

Internal Utilities:
_validate(p): Ensures a given Position p is valid and belongs to this list.
_make_position(node): Converts a _Node into a Position object (or None if it's a sentinel).
_insert_between(e, predecessor, successor): A core helper for inserting a new element e between two existing nodes.

Public Interface (Key Methods):
__len__(): Returns the number of elements.
is_empty(): Checks if the list is empty.
first(): Returns the Position of the first element.
last(): Returns the Position of the last element.
before(p): Returns the Position immediately preceding p.
after(p): Returns the Position immediately following p.
add_first(e): Inserts element e at the beginning.
add_last(e): Inserts element e at the end.
add_before(p, e): Inserts element e before Position p.
add_after(p, e): Inserts element e after Position p.
delete(p): Removes the element at Position p, returning its value.
replace(p, e): Replaces the element at Position p with e, returning the old value.
__iter__(): Allows iteration through the elements of the list.

Advantages:
Stable Positions: Positions remain valid even with insertions/deletions elsewhere in the list, unlike indices 
in array-based lists.Efficient Insertions/Deletions: Operations like add_before, add_after, and delete can be 
performed in O(1) time given a Position.
Flexibility: Useful when maintaining references to specific elements in a dynamic list is crucial.

Advantages:
Efficient Operations: Insertions and deletions at any Position take constant time, as only a few pointer updates 
are required.
Stable References: Position objects remain valid even if the list undergoes modifications, unlike integer indices 
which can become invalid after insertions/deletions.
Bidirectional Traversal: The underlying doubly linked list allows for traversal in both forward and backward directions.
Example (Conceptual Python-like structure):
Python

"""

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
        new_node = Node(e, predecessor, successor)
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













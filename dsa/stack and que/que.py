
"""
The first element inserted is the first one to be removed.
Think of a queue like a line at a checkout counter

A queue is open at both ends:
Insertion (Enqueue) ➡ happens at the rear.
Deletion (Dequeue) ⬅ happens at the front

Applications of Queues:
✔ Scheduling tasks (CPU scheduling, printer queue).
✔ Handling requests in web servers.
✔ Breadth-First Search (BFS) in graph algorithms.

1️⃣ Enqueue(Q, x): Inserts element x at the rear.
2️⃣ Dequeue(Q): Removes the element from the front.
3️⃣ isEmpty(Q): Checks if the queue is empty.
4️⃣ isFull(Q): Checks if the queue is full (for fixed-size implementations).




"""
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
q.append('t')
q.append('u')
q.append('k')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.pop())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
#-------------------
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full())
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
"""
A queue can be implemented using an array with two indices:
Front (points to the first element).
Rear (points to the last element).

0-based indexing is used (common in Python).
Initial state: front = rear = -1 (empty queue).
Queue is empty when front == -1 .
Queue is full when rear == max_size - 1 (for non-circular arrays).

def ENQUEUE(Q, x):
    MAX-SIZE = 7
    if rear == MAX-SIZE:
        Error OVERFLOW
    else if rear == -1:
        front = rear = 1
    else:
        rear = rear + 1
    Q[rear] = x

"""
#enque
class Arrayque:
    def __init__(self,max_size):
        self.que = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def enque(self,x):
        if self.rear == self.max_size - 1:
            print("error:overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.que[self.rear] = x

"""
Queue Implementation Using Circular Arrays 🔄
A limitation of linear arrays is that dequeued spaces cannot be reused.
✔ Solution: Use a circular array where elements wrap around!

Key Details:
Initial state: front = -1 , rear = -1 (empty queue).
Queue is empty when front == -1 .
Queue is full when (rear + 1) % max_size == front

ENQUEUE(Q, x)
if (rear % N) +1 == front
Error OVERFLOW
else if rear == 0
front = rear = 1
else
rear = (rear % N)+1
Q[rear] = x
"""

class Circularque:
    def __init__(self,max_size):
        self.que = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def enque(self,x):
        if (self.rear + 1) % self.max_size == self.front:
            print("error:overflow")
        else:
            if self.front == -1: # first element
                self.front = 0
            self.rear = (self.rear + 1) % self.max_size # wrap around
            self.que[self.rear] = x

#-------
class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.max_size:
            print("Overflow! Queue is full.")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size  # Wrap rear pointer
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Underflow! Queue is empty.")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size  # Wrap front pointer
        self.size -= 1
        return item

"""
Queue Implementation Using Linked Lists 🔗
A linked list allows dynamic memory allocation, avoiding fixed-size limitations.

Advantages:
✅ No fixed size.
✅ Memory-efficient (allocates as needed).
✅ No unused space.

            
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedque:
    def __init__(self):
        self.front = None
        self.rear = None

    def enque(self,x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def deque(self):
        if self.front is None:
            print("underflow")  # cannot be removed
            return None # explicit reurn for empty que
        else:
            data = self.front.data
            self.front = self.front.next # after 1st item is deleted the next item becomes 1st item or front
            if self.front is None:
                self.rear = None
            return data

"""
Once we dequeue an element from the array, the associated cell space is 
wasted:
• The above space cannot be reused until the queue is empty (front = rear =0)
• Possible way to solve that?
– Using a circular array
– If the current rear = i then next element to be inserted at (i % N) +1
• N = size of the array (MAX-SIZE)
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item) # O(1) time

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) # O(n) time (slow for large queues)
        return "Queue is empty!"

    def is_empty(self):
        return len(self.items) == 0








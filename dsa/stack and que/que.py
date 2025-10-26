
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
# Simulate a queue with a Python list
que_list = []
que_list.append('a')
que_list.append('b')
que_list.append('c')
que_list.append('d')
print(que_list.pop(0))  # not pop only but 0
print('que_list',que_list)

# deque (double-ended queue) is preferred over a list for queues because both append()
# and popleft() run in O(1) time.popleft() efficiently removes the first element without
# shifting, making deque ideal for queues
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
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Python’s queue module provides a thread-safe FIFO queue. You can specify a maxsize. Key Methods are:
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
print(q.empty())
print(q.full())
print(q.qsize())

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

"""
#enque
class myQueue:
    def __init__(self, capacity):
        # Maximum number of elements the queue can hold.
        self.capacity = capacity
        #  Array to store queue elements.
        self.arr = [0] * capacity
        #  Current number of elements in the queue.
        self.size = 0

    # Check if queue is empty
    def isEmpty(self):
        return self.size == 0

    # Check if queue is full
    def isFull(self):
        return self.size == self.capacity

    # Enqueue
    def enqueue(self, x):
        if self.isFull():
            print("Queue is full!")
            return
        self.arr[self.size] = x
        # self.arr.append(item)
        self.size += 1

    # Dequeue-removes the front ele of the que by shifting all remaining ele one postion to left and then dec the size.
    # Wasted space: The elements before the front pointer are never reused, so memory can be wasted if many elements are dequeued
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1


    # Get front element
    def getFront(self):
        if self.isEmpty():
            print("Queue is empty!")
            return -1
        return self.arr[0]

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty!")
            return -1
        return self.arr[self.size - 1]

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.arr)


# Driver code
if __name__ == '__main__':
    q = myQueue(3)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front:", q.getFront())

    q.dequeue()
    print("Front:", q.getFront())
    print("Rear:", q.getRear())

    q.enqueue(40)

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
class myQueue:
    def __init__(self, cap):
         # fixed-size array
        self.arr = [0]*cap
           # index of front element
        self.front = 0
          # current number of elements
        self.size = 0
         # maximum capacity
        self.capacity = cap

    # Insert an element at the rear
    def enqueue(self, x):
        if self.size == self.capacity:
            print("Queue is full!")
            return
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x # self.arr[3] = x is the 4th ele added
        self.size += 1

    # Remove an element from the front
    def dequeue(self):
        if self.size == 0:
            print("Queue is empty!")
            return -1
        res = self.arr[self.front]
        self.arr[self.front] = None  # Optional: clear the dequeued slot
        self.front = (self.front + 1) % self.capacity # front moving toward rear creating vacum
        # if cap = 4,once dequed so front is in 1,size is 3 ,so the next ele if added willgo to index 0, as (1+ 3) % 4 = 0
        self.size -= 1
        return res

    # Get the front element
    def getFront(self):
        if self.size == 0:
            return -1
        return self.arr[self.front]

    # Get the rear element
    def getRear(self):
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

if __name__ == "__main__":
    q = myQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.getFront(), q.getRear())
    q.dequeue()
    print(q.getFront(), q.getRear())
    q.enqueue(40)
    print(q.getFront(), q.getRear())


"""
Queue Implementation Using Linked Lists 🔗
A linked list allows dynamic memory allocation, avoiding fixed-size limitations.

Advantages:
✅ No fixed size.
✅ Memory-efficient (allocates as needed).
✅ No unused space.
t can be implemented using a linked list, where each element of the queue is represented as a node.
Two pointers/references:

front → points to the first node (head of the queue).
rear → points to the last node (tail of the queue).          
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.currSize = 0

    # Check if the queue is empty
    def isEmpty(self):
        return self.front is None

    """
    A new node is created with the given value.If the queue is empty (front == null and rear == null), both front 
    and rear are set to this new node.Otherwise, the current rear’s next pointer is set to the new node.
    The rear pointer is updated to point to the new node.
    """
    def enque(self,x):
        new_node = Node(x)
        if self.rear is None:  # or if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        # increment size
        self.currSize += 1

    """
    dequeue operation removes an element from the front of the queue.

    If the queue is empty (front == null), return underflow (queue is empty).
    Otherwise, store the current front node in a temporary pointer.
    Move the front pointer to the next node (front = front.next).
    If the front becomes null, also set rear = null (queue becomes empty).
    """
    def deque(self):
        if self.front is None:
            print("underflow")  # cannot be removed
            return None # explicit reurn for empty que
        else:
            data = self.front.data
            self.front = self.front.next # after 1st item is deleted the next item becomes 1st item or front
            if self.front is None:
                self.rear = None
                # decrement size
            self.currSize -= 1
            return data

    # Return the front element
    def get_front(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.front.data

    # Return size in O(1)
    def size(self):
        return self.currSize

if __name__ == "__main__":

    q = Linkedque()

    q.enque(10)
    q.enque(20)

    print("Dequeue:", q.deque())

    q.enque(30)

    print("Front:", q.get_front())
    print("Size:", q.size())
    """
    Once we dequeue an element from the array, the associated cell space is 
    wasted:
    • The above space cannot be reused until the queue is empty (front = rear =0)
    • Possible way to solve that?
    – Using a circular array
    – If the current rear = i then next element to be inserted at (i % N) +1
    • N = size of the array (MAX-SIZE)
    """










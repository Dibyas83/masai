"""
Max Heap in Python
Last Updated : 11 Feb, 2025
A Max-Heap is a Data Structure with the following properties:

It is a Complete Binary Tree.
The value of the root node must be the largest among all its descendant nodes, and the same thing must be
done for its left and right sub-tree also.
max-heap-1.webpmax-heap-1.webp
How is Max Heap represented?
A max Heap is a Complete Binary Tree. A max heap is typically represented as an array. The root element
 will be at Arr[0]. Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:

Arr[(i-1)/2] Returns the parent node.
Arr[(2*i)+1] Returns the left child node.
Arr[(2*i)+2] Returns the right child node.
Operations on Max Heap:
getMax(): It returns the root element of Max Heap. Time Complexity of this operation is O(1).
extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(log n) as this operation needs to maintain the heap property (by calling heapify()) after removing the root.
insert(): Inserting a new key takes O(log n) time. We add a new key at the end of the tree. If the new key is smaller than its parent, then we don&#x2019t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
Note: In the below implementation, we do indexing from index 1 to simplify the implementation.




1
import sys
2
​
3
class MaxHeap:
4
    def __init__(self, cap):
5
        self.cap = cap
6
        self.n = 0
7
        self.a = [0] * (cap + 1)
8
        self.a[0] = sys.maxsize
9
        self.root = 1
10
​
11
    def parent(self, i):
12
        return i // 2
13
​
14
    def left(self, i):
15
        return 2 * i
16
​
17
    def right(self, i):
18
        return 2 * i + 1
19
​
20
    def isLeaf(self, i):
21
        return i > (self.n // 2) and i <= self.n
22
​
23
    def swap(self, i, j):
24
        self.a[i], self.a[j] = self.a[j], self.a[i]
25
​
26
    def maxHeapify(self, i):
27
        if not self.isLeaf(i):
28
            largest = i
29
            if self.left(i) <= self.n and self.a[i] < self.a[self.left(i)]:
30
                largest = self.left(i)
31
            if self.right(i) <= self.n and self.a[largest] < self.a[self.right(i)]:
32
                largest = self.right(i)
33
            if largest != i:
34
                self.swap(i, largest)
35
                self.maxHeapify(largest)
36
​
37
    def insert(self, val):
38
        if self.n >= self.cap:
39
            return
40
        self.n += 1
41
        self.a[self.n] = val
42
        i = self.n
43
        while self.a[i] > self.a[self.parent(i)]:
44
            self.swap(i, self.parent(i))
45
            i = self.parent(i)
46
​
47
    def extractMax(self):
48
        if self.n == 0:
49
            return None
50
        max_val = self.a[self.root]
51
        self.a[self.root] = self.a[self.n]
52
        self.n -= 1
53
        self.maxHeapify(self.root)
54
        return max_val
55
​
56
    def printHeap(self):
57
        for i in range(1, (self.n // 2) + 1):
58
            print(f"PARENT: {self.a[i]}", end=" ")
59
            if self.left(i) <= self.n:
60
                print(f"LEFT: {self.a[self.left(i)]}", end=" ")
61
            if self.right(i) <= self.n:
62
                print(f"RIGHT: {self.a[self.right(i)]}", end=" ")
63
            print()
64
​
65
# Example
66
if __name__ == "__main__":
67
    print("The maxHeap is:")
68
    h = MaxHeap(15)
69
    vals = [5, 3, 17, 10, 84, 19, 6, 22, 9]
70
    for val in vals:
71
        h.insert(val)
72
​
73
    h.printHeap()
74
    print("The Max val is", h.extractMax())
Output:

The maxHeap is
PARENT : 84 LEFT CHILD : 22 RIGHT CHILD : 19
PARENT : 22 LEFT CHILD : 17 RIGHT CHILD : 10
PARENT : 19 LEFT CHILD : 5 RIGHT CHILD : 6
PARENT : 17 LEFT CHILD : 3 RIGHT CHILD : 9
The Max val is 84
Using Library functions:
We use heapq class to implement Heap in Python. By default Min Heap is implemented by this class. But we multiply each value by -1 so that we can use it as MaxHeap.




1
# Python3 program to demonstrate heapq (Max Heap)
2
​
3
from heapq import heappop, heappush, heapify
4
​
5
# Create an empty heap
6
h = []
7
heapify(h)
8
​
9
# Add elements (multiplying by -1 to simulate Max Heap)
10
heappush(h, -10)
11
heappush(h, -30)
12
heappush(h, -20)
13
heappush(h, -400)
14
​
15
# Print max element
16
print("Max:", -h[0])
17
​
18
# Print heap elements
19
print("Heap:", [-i for i in h])
20
​
21
# Pop max element
22
heappop(h)
23
​
24
# Print heap after removal
25
print("Heap after pop:", [-i for i in h])

Output
Max: 400
Heap: [400, 30, 20, 10]
Heap after pop: [30, 10, 20]
Using Library functions with dunder method for Numbers, Strings, Tuples, Objects etc
We use heapq class to implement Heaps in Python. By default Min Heap is implemented by this class.

To implement MaxHeap not limiting to only numbers but any type of object(String, Tuple, Object etc) we should

Create a Wrapper class for the item in the list.
Override the __lt__ dunder method to give inverse result.
Following is the implementation of the method mentioned here.




1
"""
2
Python3 program to implement MaxHeap using heapq
3
for Strings, Numbers, and Objects
4
"""
5
from functools import total_ordering
6
import heapq
7
​
8
@total_ordering
9
class Wrap:
10
    def __init__(self, v):
11
        self.v = v
12
​
13
    def __lt__(self, o):
14
        return self.v > o.v  # Reverse for Max Heap
15
​
16
    def __eq__(self, o):
17
        return self.v == o.v
18
​
19
# Max Heap for numbers
20
h = [10, 20, 400, 30]
21
wh = list(map(Wrap, h))
22
​
23
heapq.heapify(wh)
24
print("Max:", heapq.heappop(wh).v)
25
​
26
# Max Heap for strings
27
h = ["this", "code", "is", "wonderful"]
28
wh = list(map(Wrap, h))
29
heapq.heapify(wh)
30
​
31
print("Heap:", end=" ")
32
while wh:
33
    print(heapq.heappop(wh).v, end=" ")

Output
Max: 400
Heap: wonderful this is code 
Using internal functions used in the heapq library
This is by far the most simple and convenient way to apply max heap in python.

DISCLAIMER - In Python, there's no strict concept of private identifiers like in C++ or Java. Python trusts developers and allows access to so-called "private" identifiers. However, since these identifiers are intended for internal use within the module, they are not officially part of the public API and may change or be removed in the future.

Following is the implementation.




1
from heapq import _heapify_max, _heappop_max, _siftdown_max
2
​
3
# Implementing heappush for max heap
4
def hpush(h, v): 
5
    h.append(v)
6
    _siftdown_max(h, 0, len(h)-1)
7
​
8
def maxh(a):
9
    c = a.copy()  # Copy for later use
10
    
11
    _heapify_max(a)  # Convert to max heap
12
    
13
    while a:
14
        print(_heappop_max(a))  # Pop elements
15
​
16
    a = c  # Restore array
17
    h = []
18
​
19
    for v in a:
20
        hpush(h, v)  # Insert elements back into heap
21
​
22
    print("Max Heap Ready!")
23
    
24
    while h:
25
        print(_heappop_max(h))  # Pop elements
26
​
27
# Example 
28
a = [6, 8, 9, 2, 1, 5]
29
maxh(a)

Output
9
8
6
5
2
1
Max Heap Ready!
9
8
6
5
2
1
Using Priority Queue



1
from queue import PriorityQueue 
2
​
3
q = PriorityQueue() 
4
​
5
# Insert elements into the queue (negate values to simulate Max Heap)
6
q.put(-10)  
7
q.put(-20)  
8
q.put(-5)   
9
​
10
# Remove and return the highest priority item (convert back to positive)
11
print(-q.get())  # 20 (highest value)
12
print(-q.get())  # 10 
13
​
14
# Check queue size
15
print('Items in queue:', q.qsize())  
16
​
17
# Check if queue is empty
18
print('Is queue empty:', q.empty())  
19
​
20
# Check if queue is full
21
print('Is queue full:', q.full())

Output
20
10
Items in queue: 1
Is queue empty: False
Is queue full: False


"""
"""
Min Heap in Python
Last Updated : 08 Feb, 2025
A Min-Heap is a Data Structure with the following properties.

It is a complete Complete Binary Tree.
The value of the root node must be the smallest among all its descendant nodes and the same thing must be done for its left and right sub-tree also.
min-heap-2.webpmin-heap-2.webp
Table of Content

Example of Min Heap
Min Heap Representation as an Array
Operations on Min Heap
Implementation of Min Heap in Python
Implementation of Min Heap Using Python’s heapq Library
Implementation of Min Heap using Priority Queue
The elements of a heap can be mapped into an array using the following rules:

If a node is stored at index k:

Left child is stored at index 2k + 1 (for 0-based indexing) or 2k (for 1-based indexing).
Right child is stored at index 2k + 2 (for 0-based indexing) or 2k + 1 (for 1-based indexing).
Example of Min Heap
Tree Representation:
            5                      13
          /   \                  /    \  
        10     15              16      31
       /                      /  \     /  \
     30                     41    51  100  41
Array Representation:
For the first tree:

[5, 10, 15, 30]

For the second tree:

[13, 16, 31, 41, 51, 100, 41]

Min Heap Representation as an Array
Since a Min Heap is a Complete Binary Tree, it is commonly represented using an array. In an array representation:

The root element is stored at Arr[0].
For any i-th node (at Arr[i]):
Parent Node → Arr[(i - 1) / 2]
Left Child → Arr[(2 * i) + 1]
Right Child → Arr[(2 * i) + 2]
Operations on Min Heap
getMin(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).
extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
Implementation of Min Heap in Python
Please refer Min-Heap for details.




1
class MinHeap:
2
    def __init__(self):
3
        self.a = []
4
​
5
    """Insert a new element into the Min Heap."""
6
    def insert(self, val):
7
        self.a.append(val)
8
        i = len(self.a) - 1
9
        while i > 0 and self.a[(i - 1) // 2] > self.a[i]:
10
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
11
            i = (i - 1) // 2
12
​
13
    """Delete a specific element from the Min Heap."""
14
    def delete(self, value):
15
        i = -1
16
        for j in range(len(self.a)):
17
            if self.a[j] == value:
18
                i = j
19
                break
20
        if i == -1:
21
            return
22
        self.a[i] = self.a[-1]
23
        self.a.pop()
24
        while True:
25
            left = 2 * i + 1
26
            right = 2 * i + 2
27
            smallest = i
28
            if left < len(self.a) and self.a[left] < self.a[smallest]:
29
                smallest = left
30
            if right < len(self.a) and self.a[right] < self.a[smallest]:
31
                smallest = right
32
            if smallest != i:
33
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
34
                i = smallest
35
            else:
36
                break
37
​
38
    """Heapify function to maintain the heap property.""" 
39
    def minHeapify(self, i, n):
40
        smallest = i
41
        left = 2 * i + 1
42
        right = 2 * i + 2
43
​
44
        if left < n and self.a[left] < self.a[smallest]:
45
            smallest = left
46
        if right < n and self.a[right] < self.a[smallest]:
47
            smallest = right
48
        if smallest != i:
49
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
50
            self.minHeapify(smallest, n)
51
​
52
    """Search for an element in the Min Heap."""
53
    def search(self, element):
54
        for j in self.a:
55
            if j == element:
56
                return True
57
        return False
58
​
59
    def getMin(self):
60
        return self.a[0] if self.a else None
61
​
62
    def printHeap(self):
63
        print("Min Heap:", self.a)
64
​
65
# Example Usage
66
if __name__ == "__main__":
67
    h = MinHeap()
68
    values = [10, 7, 11, 5, 4, 13]
69
    for value in values:
70
        h.insert(value)
71
    h.printHeap()
72

73
    h.delete(7)
74
    print("Heap after deleting 7:", h.a)
75

76
    print("Searching for 10 in heap:", "Found" if h.search(10) else "Not Found")
77
    print("Minimum element in heap:", h.getMin())

Output
Min Heap: [4, 5, 11, 10, 7, 13]
Heap after deleting 7: [4, 5, 11, 10, 13]
Searching for 10 in heap: Found
Minimum element in heap: 4
Implementation of Min Heap Using Python’s heapq Library
Python’s heapq module implements a Min Heap by default.




1
# Python3 program to demonstrate working of heapq
2
​
3
from heapq import heapify, heappush, heappop
4
​
5
# Creating empty heap
6
heap = []
7
heapify(heap)
8
​
9
# Adding items to the heap using heappush function
10
heappush(heap, 10)
11
heappush(heap, 30)
12
heappush(heap, 20)
13
heappush(heap, 400)
14
​
15
# printing the value of minimum element
16
print("Head value of heap : "+str(heap[0]))
17
​
18
# printing the elements of the heap
19
print("The heap elements : ")
20
for i in heap:
21
    print(i, end = ' ')
22
print("\n")
23
​
24
element = heappop(heap)
25
​
26
# printing the elements of the heap
27
print("The heap elements : ")
28
for i in heap:
29
    print(i, end = ' ')

Output
Head value of heap : 10
The heap elements :
10 30 20 400

The heap elements :
20 30 400
Implementation of Min Heap using queue.PriorityQueue
Please refer queue.PriorityQueue for details.




1
from queue import PriorityQueue
2
​
3
q = PriorityQueue()
4
​
5
# insert into queue
6
q.put(10)
7
q.put(20)
8
q.put(5)
9
​
10
# remove and return
11
# lowest priority item
12
print(q.get())
13
print(q.get())
14
​
15
# check queue size
16
print('Items in queue :', q.qsize())
17
​
18
# check if queue is empty
19
print('Is queue empty :', q.empty())
20
​
21
# check if queue is full
22
print('Is queue full :', q.full())

Output
5
10
Items in queue : 1
Is queue empty : False
Is queue full : False


"""

"""
Heap queue or heapq in Python
Last Updated : 17 Mar, 2025
A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap) or largest (max-heap) element. A heap is typically implemented as a binary tree, where each parent node's value is smaller (for a min-heap) or larger (for a max-heap) than its children. However, in Python, heaps are usually implemented as min-heaps which means the smallest element is always at the root of the tree, making it easy to access.

heapq module allows us to treat a list as a heap, providing efficient methods for adding and removing elements.

Creating a Heap Queue
To use a heap queue in Python, we first need to import the heapq module. A heap queue is created from a list by calling the heapq.heapify() function, which rearranges the elements of the list into a valid heap structure.

Example of creating a heap queue:




1
import heapq
2
​
3
# Creating a list
4
li = [10, 20, 15, 30, 40]
5
​
6
# Convert the list into a heap
7
heapq.heapify(li)
8
​
9
print("Heap queue:", li)

Output
Heap queue: [10, 20, 15, 30, 40]
Explanation:

heapq.heapify(li) rearranges the elements of the list into a valid heap in-place.
Output list represents the heap structure and its first element will always be the smallest element (in a min-heap).
Key operations of a heap:
Push (heappush): Adds an element to the heap while maintaining the heap property.
Pop (heappop): Removes and returns the smallest element in the heap, again maintaining the heap property.
Peek: View the smallest element without removing it.
Heapify: Convert a regular list into a valid heap in-place.
Appending and Popping Elements from a Heap Queue
Heap queues allow us to efficiently append elements and remove the smallest element. heappush() function is used to add an element to the heap while maintaining the heap property and heappop() is used to remove the smallest element. To append and pop elements from a heap queue we can use the following two functions:

heapq.heappush() function adds a new element to the heap while maintaining the heap order.
heapq.heappop() function removes the smallest element from the heap and returns it.
Example:




1
import heapq
2
​
3
# Creating an initial heap
4
h = [10, 20, 15, 30, 40]
5
heapq.heapify(h)
6
​
7
# Appending an element
8
heapq.heappush(h, 5)
9
​
10
# Pop the smallest element from the heap
11
min = heapq.heappop(h)
12
​
13
print(h)
14
​
15
print("Smallest:", min)
16
print(h)

Output
[10, 20, 15, 30, 40]
Smallest: 5
[10, 20, 15, 30, 40]
Explanation:

Element 5 is pushed into the heap and after the operation, it gets placed at the root because it is the smallest element.
heappop() function removes the smallest element (5) from the heap and returns it.
After popping, the next smallest element (10) becomes the root.
Appending and Popping Simultaneously
Python’s heapq module provides an efficient way to do this using the heappushpop() function. This function allows us to push an element onto the heap and pop the smallest element in one combined operation. It is faster than performing these operations separately, as it maintains the heap property in one go.

heappushpop() function takes two arguments:

A heap (list).
An element to push onto the heap.
Example of appending and popping simultaneously:




1
import heapq
2
​
3
# Creating a heap
4
h = [10, 20, 15, 30, 40]
5
heapq.heapify(h)
6
​
7
# Push a new element (5) and pop the smallest element at the same time
8
min = heapq.heappushpop(h, 5)
9
​
10
print(min)
11
print(h)

Output
5
[10, 20, 15, 30, 40]
Explanation:

Element 5 is appended to the heap using heappush().
Then, heappop() is used to remove the smallest element (5), which was just added.
Finding the Largest and Smallest Elements in a Heap Queue
Although a heap allows for efficient access to the smallest element, it doesn’t directly support finding the largest element. However, the heapq module provides two handy functions, nlargest() and nsmallest(), to retrieve the largest and smallest elements from the heap, respectively.

nlargest() and nsmallest()
These functions allow us to easily find the n largest or n smallest elements in a heap. They do this by efficiently scanning the heap and sorting the required number of elements.

heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.
Example of finding the largest and smallest elements using nlargest() and nsmallest():




1
import heapq
2
​
3
# Creating a heap
4
h = [10, 20, 15, 30, 40]
5
heapq.heapify(h)
6
​
7
# Find the 3 largest elements
8
maxi = heapq.nlargest(3, h)
9
print("3 largest elements:", maxi)
10
​
11
# Find the 3 smallest elements
12
min = heapq.nsmallest(3, h)
13
print("3 smallest elements:", min)

Output
3 largest elements: [40, 30, 20]
3 smallest elements: [10, 15, 20]
Note that the heapq module in Python provides functions for performing heap operations on lists in-place, without creating a separate data structure for the heap. The heapq module is efficient and easy to use, making it a popular choice for implementing priority queues and other data structures in Python.

Replace and Merge Operations on Heapq
Python’s heapq module provides additional useful operations for heaps like replace and merge.

Replace Operation
heapq.heapreplace() function is a combination of pop and push. It pops the smallest element from the heap and inserts a new element into the heap, maintaining the heap property. This operation is useful when we want to replace the smallest element with a new value in a heap.

It returns the smallest element before replacing it.
It is more efficient than using heappop() followed by heappush() because it performs both operations in one step.
Merge Operation
heapq.merge() function is used to merge multiple sorted iterables into a single sorted heap. It returns an iterator over the sorted values, which we can then iterate through.

This operation is efficient because it avoids sorting the elements from scratch. Instead, it merges already-sorted iterables in a way that maintains the heap property.

Example of replace and merge operations:




1
import heapq
2
​
3
# Creating a heap
4
h1 = [10, 20, 15, 30, 40]
5
heapq.heapify(h1)
6
​
7
# Replacing the smallest element (10) with 5
8
min = heapq.heapreplace(h1, 5)
9
​
10
print(min)
11
print(h1)
12
​
13
# Merging Heaps
14
h2 = [2, 4, 6, 8]
15
​
16
# Merging the lists
17
h3 = list(heapq.merge(h1, h2))
18
print("Merged heap:", h3)

Output
10
[5, 20, 15, 30, 40]
Merged heap: [2, 4, 5, 6, 8, 20, 15, 30, 40]
Explanation:

We use heapreplace() to replace the smallest element (10) with 5. The smallest element is popped and 5 is inserted into the heap.
We use heapq.merge() to merge these heaps into a single sorted heap while maintaining the heap property.
Advantages of using a heap queue (or heapq) in Python:
Efficient: A heap queue is a highly efficient data structure for managing priority queues and heaps in Python. It provides logarithmic time complexity for many operations, making it a popular choice for many applications.
Space-efficient: Heap queues store elements in a list-like format. This means they don't take up unnecessary extra space, making them more memory-friendly than some other options, like linked lists.
Easy to use: The heapq module provides easy-to-understand functions that let us quickly add, remove or get elements without much hassle.
Flexible: Heap queues in Python can be used to implement various data structures like priority queues, heaps and binary trees, making them a versatile tool for many applications.
Disadvantages of using a heap queue (or heapq) in Python:
Limited functionality: Heap might not work well for more complex operations or data structures that require different features.
No random access: Heap queues do not support random access to elements, making it difficult to access elements in the middle of the heap or modify elements that are not at the top of the heap.
No sorting: Heap queues do not support sorting, so if we need to sort elements in a specific order, we will need to use a different data structure or algorithm.
Not thread-safe: Heap queues are not designed to handle multiple threads accessing the data at the same time.
Overall, heap queues are a highly efficient and flexible data structure for managing priority queues and heaps in Python, but may have limited functionality and may not be suitable for all applications.

"""









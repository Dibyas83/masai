"""
While you cannot directly implement a heap using a Python dictionary as the underlying data structure, you can use a list to represent the heap and store dictionaries within it. The heapq module in Python operates on lists, and if you want to heapify a list of dictionaries, you need to ensure that the dictionaries are comparable.
Here's how you can achieve this:
1. Storing Dictionaries in a Heap:
To store dictionaries in a heap, you need to define a basis for comparison. This is typically done by including a comparable element (like a priority or a key) as the first element of a tuple, with the dictionary itself as the second element. The heapq module will then use the first element of the tuple for comparison.
"""

import heapq

# Example list of dictionaries with a 'priority' key
items = [
    {'name': 'Task A', 'priority': 5},
    {'name': 'Task B', 'priority': 1},
    {'name': 'Task C', 'priority': 3},
]

# Convert dictionaries into tuples (priority, dictionary) for heap operations
# For a min-heap, smallest priority comes first.
# For a max-heap, negate the priority.
heap = []
for item in items:
    heapq.heappush(heap, (item['priority'], item))

print(f"Heap after pushing elements: {heap}")

# Pop the element with the highest priority (smallest priority value)
lowest_priority_item = heapq.heappop(heap)
print(f"Popped item (priority, dictionary): {lowest_priority_item}")
print(f"Heap after popping: {heap}")
"""
2. Implementing a Max-Heap with Dictionaries:
For a max-heap, where you want to retrieve the item with the highest priority, you can negate the priority value when pushing it onto the min-heap.
"""

import heapq

items = [
    {'name': 'Task A', 'priority': 5},
    {'name': 'Task B', 'priority': 1},
    {'name': 'Task C', 'priority': 3},
]

max_heap = []
for item in items:
    # Negate priority for max-heap behavior
    heapq.heappush(max_heap, (-item['priority'], item))

print(f"Max-Heap after pushing elements: {max_heap}")

# Pop the element with the highest priority (largest priority value, smallest negative value)
highest_priority_item = heapq.heappop(max_heap)
print(f"Popped item (negated priority, dictionary): {highest_priority_item}")
print(f"Original priority of popped item: {-highest_priority_item[0]}")

"""
Explanation:
The heapq module in Python implements a min-heap.
When you use heapq.heappush or heapq.heapify with a list containing tuples, it compares elements based 
on the first item of the tuple.
By placing the priority (or a comparable key) as the first element of the tuple, you allow the heap to 
be ordered according to that value.
To simulate a max-heap, you invert the sign of the priority value, so that the largest original priority
becomes the smallest (most negative) value in the heap.
"""


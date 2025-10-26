

"""
A priority queue is an abstract data type that functions like a queue but prioritizes elements based on a
defined priority. Instead of a First-In, First-Out (FIFO) retrieval order, elements are retrieved based on
their priority, with the highest priority element being removed first.
In Python, a common and efficient way to implement a priority queue is using a heap, specifically a binary
heap. The heapq module in Python provides an implementation of the min-heap data structure, which is a binary
tree with the heap property: for every node i, the value of i is less than or equal to the values of its
children. This means the smallest element is always at the root of the heap.

heapq.heappush(heap, item): Inserts an item into the heap while maintaining the heap property.
heapq.heappop(heap): Removes and returns the smallest item from the heap, then reorganizes the heap
to maintain the heap property.
heapq.heapify(x): Transforms a regular list x into a heap in-place.

queue.PriorityQueue class: For thread-safe priority queues, Python's queue module provides the PriorityQueue
class, which internally uses heapq to manage priorities.

hashmap + heap(priority que)

if we want top 3 create a priority que of size 3,that add and remove according to freq they have from the dictionary
so that we dont have to store all if all are unique
heapq.heappush() to add elements: This function takes two arguments: the heap (your list) and the element you
want to add. It automatically maintains the min-heap property, ensuring the smallest element is always at the
root (index 0).
"""

import heapq
from collections import Counter


class Solution:
  def topKFrequent(self, nums, k): # k is size of priority que required
    if k == len(nums): # length of list
      return nums

    count = Counter(nums)
    print(count)
    heap = []

    for n in count:

        print(count[n],n)
        heapq.heappush(heap, (count[n], n)) # freq , no
        if len(heap) > k:
            heapq.heappop(heap)  # root - the lowest occurrence ele will be deleted and new added to last of list

    ans = []
    while heap:
      ans.append(heapq.heappop(heap)[1])  # start adding by poping the root in heap which is smallest

    return ans[::-1]

g = Solution()
nums = [1,1,2,2,3,2,4,4,4,4,5,5,6,5,5]
print(g.topKFrequent(nums,3))

"""

import heapq



my_dict = {'task_A': 5, 'task_B': 2, 'task_C': 8, 'task_D': 1}
heap_data = [(value, key) for key, value in my_dict.items()]
heapq.heapify(heap_data)

# Pop the highest priority item
highest_priority_item = heapq.heappop(heap_data)
print(f"Highest priority item: {highest_priority_item}")

# Add a new item
heapq.heappush(heap_data, (3, 'task_E'))
print(f"Heap after push: {heap_data}")


my_dict = {'task_A': 5, 'task_B': 2, 'task_C': 8, 'task_D': 1}
max_heap_data = [(-value, key) for key, value in my_dict.items()]
heapq.heapify(max_heap_data)

# Pop the highest priority (largest or min  original value) item  that is root
highest_min_value_item = heapq.heappop(max_heap_data)
print(f"Highest or min  value item (from max-heap simulation): {(-highest_value_item[0], highest_value_item[1])}")

----------------------------------
# Sort by values in ascending order
sorted_by_value_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(f"Sorted by value (ascending): {sorted_by_value_asc}")

# Sort by values in descending order
sorted_by_value_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted by value (descending): {sorted_by_value_desc}")

# Get the top 2 elements
top_2_items = sorted_by_value_desc[:2]

# If you need the result as a dictionary, you can convert it back
top_2_dict = dict(top_2_items)
-------
my_dict = {'vegetables': ['carrot']}
if 'fruits' not in my_dict:
    my_dict['fruits'] = []
my_dict['fruits'].append('apple')

if 'vegetables' not in my_dict:
    my_dict['vegetables'] = []
my_dict['vegetables'].append('broccoli')
print(my_dict)


"""




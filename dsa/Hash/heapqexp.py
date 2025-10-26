

import heapq

# Create an empty list to represent the heap
priority_queue = []

# Add elements with priorities (lower number = higher priority)
heapq.heappush(priority_queue, (3, "Task C"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (2, "Task B"))

# Retrieve elements in order of priority
print(heapq.heappop(priority_queue))
print(heapq.heappop(priority_queue))
print(heapq.heappop(priority_queue))
print(priority_queue)











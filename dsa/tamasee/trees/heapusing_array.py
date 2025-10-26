
"""
A heap can be implemented using an array in Python by leveraging the mathematical relationships between parent and child node indices. The root is at index 0. For any node at index i:
Its left child is at 2 * i + 1.
Its right child is at 2 * i + 2.
Its parent is at (i - 1) // 2 (using integer division).

Last non-leaf node = parent of last-node.
or, Last non-leaf node = parent of node at (n-1)th index.
or, Last non-leaf node = Node at index ((n-1) - 1)/2 = (n/2) - 1.

"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def _heapify_down(self, i):
        n = len(self.heap)
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

# Example Usage
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(3)
    max_heap.insert(1)
    max_heap.insert(4)
    max_heap.insert(1)
    max_heap.insert(5)
    max_heap.insert(9)
    max_heap.insert(2)
    max_heap.insert(6)

    print("Heap elements:", max_heap.heap) # Expected: [9, 6, 5, 4, 1, 3, 2, 1] (or similar valid max-heap structure)
    print("Max element:", max_heap.peek_max()) # Expected: 9

    print("Extracted max:", max_heap.extract_max()) # Expected: 9
    print("Heap elements after extraction:", max_heap.heap) # Expected: [6, 4, 5, 1, 1, 3, 2] (or similar)

    max_heap.insert(7)
    print("Heap elements after inserting 7:", max_heap.heap) # Expected: [7, 6, 5, 4, 1, 3, 2, 1] (or similar)


print("------------------Building Heap from Array")


# To heapify a subtree rooted with node i which is
# an index in arr[]. N is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


# Function to build a Max-Heap from the given array
def buildHeap(arr, n):
    # Index of last non-leaf node
    startIdx = (n // 2) - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)


# A utility function to print the array
# representation of Heap
def printHeap(arr, n):
    print("Array representation of Heap is:")

    for i in range(n):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    # Binary Tree Representation
    # of input array
    #             1
    #           /    \
    #         3        5
    #       /  \     /  \
    #     4      6  13  10
    #    / \    / \
    #   9   8  15 17
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

    n = len(arr)

    # Function call
    buildHeap(arr, n)
    printHeap(arr, n)

    # Final Heap:
    #              17
    #            /    \
    #          15      13
    #         /  \     / \
    #        9     6  5   10
    #       / \   / \
    #      4   8 3   1






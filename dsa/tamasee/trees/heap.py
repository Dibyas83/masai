from __future__ import annotations

"""
priority que - get the top ele and replace it with last element,- check which is the smallest among 3 shift-down
when inserting at the end , we do the shift up or swim operation to move th small no up.to get the min heap
"""

"""
peek (or find-minimum): returns the smallest key stored in constant time
add: insert an element in the heap in its appropriate location
poll (or extract-min): removes the smallest key stored in the heap

Applications and Usages
We model several processes in our daily-basis with a priority queue, an example would be patients waiting in
line at a hospital, where the severity of the injury could be used as the priority rule. Another great example
 is given by Skiena:

Dating is the process of extracting the most desirable person from the data structure (Find-Maximum), spending
an evening to evaluate them better, and then reinserting them into the priority queue with a possibly revised score.

Other than that, they are widely used in other algorithms such as:

Sorting: heapsort has O(n*logn) time complexity at worst
Greedy Graph Search — A* and Djikstra: greedy algorithms, such as the Djikstra’s shortest path, can use heaps to
store priority-node pairs
Huffman Coding: heaps can be used to store and retrieve the two lowest-frequency trees

    Abstracting the node data as Int but could be Any, given a custom comparison
    function to guide ourselves on how to compare the nodes.
   
        The peek operation needs to return the smallest key from the heap, in our case, this is the 
        first element of the heap — given in constant time.

    Inserting a key into a heap is always a 2-step approach. First, we want to add the incoming key into 
    the array as fast as possible, which means appending to the end. Then, we want to heapify-up (or bubble up) 
    this newly-added element to its correct position.
    The process of moving the new element to its appropriate position is going to be defined by the heapify-up 
    function, which will recursively execute the following:
    
    Get the element (starting with the last one)
    Check if it disobeys the priority rule, in this case (min-heap), check if its key value is smaller than the parent
    If smaller, then swap with its parent
    Recurse in the index of the parent
    Keep bubbling up until reaching the root


    
    Deleting from the MinHeap
    Similar to the insertion, deleting from the heap is a 2-step process consisting of first removing the 
    highest-priority key, then reorganizing the heap. The first process is simply removing the first element of 
    the array, which is tricky since for large arrays it involves a big memory shift, thus complexity can go up 
    to O(n). Due to that, we do not simply remove the first one, what we actually do is copy the last element to 
    the first position and then shrink the size of the array by 1.
    
    After moving the last element to the first position and shrinking, we proceed to heapify-down (or bubble-down) 
    the first element to its correct position in the heap. This is done recursively by executing the following steps:
    
    Get the element key (starts with the first element)
    Check if the key is greater than any of the children (left or right)
    If greater, than it is in the wrong position, swap with the smallest between left and right
    Continue to heapify down with the smallest child index
    Repeat until no more children
    The heapify down process takes O(log n) time complexity since as we navigate through the heap we always split 
    in half the number of paths — by choosing one of the children.
"""


"""
    Heapsort
    Sorting with heaps then becomes very straightforward, first, we add the unsorted elements to the heap and 
    keep polling. In each iteration of the polling loop, we are extracting the smallest key and re-organizing the heap.

    The time complexity of this operation is O(n*log n), since each time for each element that we want to sort we need 
    to heapify down, after polling.

    Advantages

    O(n * log n) time complexity in the worst case
    In-place algorithm
    Disadvantages

    Not stable
    Very difficult to parallelize compared to other algorithms such as Merge Sort and Quick Sort   
    For the in-place variation, we want to heapify the children so that the left child is always smaller than the right child. By doing that, we enforce that the array will be sorted at the end — this operation will take O(n) time complexity and still makes our algorithm O(n * log n)
"""

from typing import List, Optional

import sys


class MinHeap:
    """
    Abstracting the node data as Int but could be Any, given a custom comparison
    function to guide ourselves on how to compare the nodes.
    """
    nodes: List[int]

    def __init__(self, nodes: List[int] = []):
        self.nodes = []
        for node in nodes:
            self.add(node)

    def __len__(self) -> int:
        return len(self.nodes)

    def __get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def __has_left_child(self, parent_index: int) -> bool:
        return self.__get_left_child_index(parent_index) < len(self.nodes)

    def __has_right_child(self, parent_index: int) -> bool:
        return self.__get_right_child_index(parent_index) < len(self.nodes)

    def __has_parent(self, index: int) -> bool:
        return self.__get_parent_index(index) >= 0

    def __left_child(self, index: int) -> Optional[int]:
        if not self.__has_left_child(index):
            # Virtual -inf
            return -sys.maxsize
        return self.nodes[self.__get_left_child_index(index)]

    def __right_child(self, index: int) -> Optional[int]:
        if not self.__has_right_child(index):
            # Virtual -inf
            return -sys.maxsize
        return self.nodes[self.__get_right_child_index(index)]

    def __parent(self, index: int) -> Optional[int]:
        if not self.__has_parent(index):
            return None
        return self.nodes[self.__get_parent_index(index)]

    def __swap(self, first_idx: int, second_idx: int):
        if first_idx >= len(self.nodes) or second_idx >= len(self.nodes):
            print(f'first ({first_idx}) or second ({second_idx}) are invalid')
            return
        tmp = self.nodes[first_idx]
        self.nodes[first_idx] = self.nodes[second_idx]
        self.nodes[second_idx] = tmp

    def is_empty(self) -> bool:
        return not self.nodes

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return None
        return self.nodes[0]

    def heapify_down(self, index: Optional[int] = 0):
        """Move root to proper position in heap"""
        if index >= len(self.nodes) or not self.__has_left_child(index):
            return self.nodes
        # Check if greater than left or right
        smaller_child_idx = self.__get_left_child_index(index)
        if self.__has_right_child(index) and \
                self.__right_child(index) < self.__left_child(index):
            smaller_child_idx = self.__get_right_child_index(index)

        if self.nodes[index] < self.nodes[smaller_child_idx]:
            # Lower than both, do nothing
            return self.nodes

        if self.nodes[index] > self.nodes[smaller_child_idx]:
            # Swap with smaller child
            self.__swap(index, smaller_child_idx)
            return self.heapify_down(smaller_child_idx)

    def heapify_up(self, child: Optional[int] = None):
        """Move last added element to correct position in heap"""
        if not child:
            # Start with last
            child = len(self.nodes) - 1
        # Check if smaller than parent
        parent_idx = self.__get_parent_index(child)
        if self.__parent(child) and self.nodes[child] < self.__parent(child):
            # Swap child <> parent
            self.__swap(child, parent_idx)
            # Recurse on parent index now (should have child value)
            self.heapify_up(child=parent_idx)

        # If its not smaller, leave as it is
        return self.nodes

    def poll(self) -> Optional[int]:
        """
        Polls lowest element from the heap (usually root). To avoid memory shift
        of first-element removal, we copy the last element to the first
        position, shrink the size by 1 and heapify down.
        """
        if self.is_empty():
            print('Empty, not polling')
            return None

        # Remove first and insert the last one added as the root
        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        # Could've also used self.nodes = self.nodes[:-1]
        del self.nodes[-1]

        self.heapify_down()
        return removed_node

    def add(self, item: int):
        self.nodes.append(item)
        self.heapify_up()

    def heapify_children(self, index: int):
        """
        Heapify children of a node to obey left < right.
        """
        if not self.__has_left_child(index):
            return
        if not self.__has_right_child(index):
            return
        if self.__right_child(index) < self.__left_child(index):
            self.__swap(
                self.__get_right_child_index(index),
                self.__get_left_child_index(index))
        self.heapify_children(self.__get_left_child_index(index))
        self.heapify_children(self.__get_right_child_index(index))


def heapsort_in_place(unsorted_input: List[int]) -> List[int]:
    """ Heapsort in-place: heap.nodes is unsorted_input == True """
    heap = MinHeap()
    heap.nodes = unsorted_input
    size = len(unsorted_input)
    print(f'identity check: {heap.nodes is unsorted_input}')
    for idx in range(size // 2, -1, -1):
        heap.heapify_down(idx)
    heap.heapify_children(0)
    return heap.nodes


def heapsort_aux(unsorted_input: List[int]) -> List[int]:
    """ Heapsort using O(n) space """
    heap = MinHeap(unsorted_input)
    sorted_input = []
    for _ in range(len(unsorted_input)):
        sorted_input.append(heap.poll())
    print(f'identity check: {sorted_input is unsorted_input}')
    return sorted_input


if __name__ == '__main__':
    heap = MinHeap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(17)
    heap.add(8)

    print(f'heap elements: {heap.nodes}')

    heap.poll()
    heap.add(100)
    heap.poll()
    print(f'heap after poll: {heap.nodes}')

    unsorted_array = [10, 15, 8, 20, 17]
    print(f'unsorted_array: {unsorted_array}')
    print(f'heapsort with aux space: {heapsort_aux(unsorted_array)}')
    print(f'heapsort in place: {heapsort_in_place(unsorted_array)}')










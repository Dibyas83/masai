
"""
        4 9 3 1 0 5 2 7 6 8
        1 2 3 4 5 6 7 8 9 10

Number of comparisons are n.
Each comparison take constant time, lets say c.
Thus total time is n.c = O(n)

1 comparison if x = 4
2 comparisons if x = 9
3 comparisons if x = 3 and so on.
n comparisons if x = 8.
Total comparisons = 1 + 2 + 3 . . . n =n(n+1)/2
Average number of comparisons = n(n+1)/2/n = n+1/2 = O(n)





"""


def LS(A, n, x):

    for i in range (1,n):
        if A[i] == x:
            return i
        return -1

"""
comparisons is same as finding the number of terms in G.P
series ,
n,(n/2),(n/2^2). . . 1

Let N denotes the number of elements in the given series.
Notice it is G.P series with common ratio 1/2
Acc, to formulae,
1 = n.1/2^(N−1)
n = 2^(N−1)
After taking logarithm,
N − 1 = log n
N = 1 + log n = O(log n)

For an array of n elements, maximum no. of comparisons =
log n
Each comparison takes constant time.
Thus time complexity = c. log n = O(log n)

Algorithm  TimeComplexity SpaceComplexity  RequiresSortedData?
Linear
Search          O(n)            O(1)             No
Binary
Search          O(log n)        O(1)            Yes


Summary of Time Complexities:array,list,set
Operation              Time Complexity
get(index)               O(1)
add(element) (at end)    O(1) (amortized) / O(n) (worst-case)

add(index, element)      O(n)

remove(element) 
/ remove(index)          O(n)

indexOf(element) 
/ contains(element)      O(n)

size(), isEmpty(), 
set(index, element)       O(1)

Key takeaway: While the average case for core set operations (membership,
add, remove) is O(1) due to the hash table implementation, it's important to be
aware of the potential for O(n) worst-case scenarios, especially in situations
with many hash collisions or when performing operations involving multiple sets.

Important Note: Because tuples are immutable, operations that would modify a list (like append,
extend, insert, remove, pop, or clear) are not available for tuples. Attempting such operations 
will result in a TypeError. When you "modify" a tuple, you are effectively creating a new tuple
with the desired changes, which will have a time complexity dependent on the creation and copying of elements.
=========

Applying binary search to a linked list, even a sorted one, will result in a time complexity that is effectively
no better than a linear search. While binary search inherently reduces the search space by half in each step 
(leading to O(log N) comparisons), the fundamental issue lies in the access time for elements in a linked list.
Here's why: 
Random Access vs. Sequential Access: Binary search relies on the ability to efficiently access the "middle" 
element of a sub-list. In an array, this is a constant-time operation (O(1)) because elements are stored 
contiguously in memory and their addresses can be calculated directly. In a linked list, however, elements 
are not stored contiguously. To reach the middle element, you must traverse the list sequentially from the 
beginning (or from a known point, if it's a doubly linked list and you're moving from a known node). This 
traversal takes O(N) time in the worst case to reach the middle of a list of N elements.

Dominating Factor: Each step of a binary search on a linked list would involve finding the middle element,
 which itself takes O(N) time. While the number of comparisons is O(log N), the time spent accessing the 
 elements in each step becomes the dominant factor. Therefore, the overall time complexity for binary 
 searching a linked list becomes O(N).
 
In summary:
Binary Search on Array: O(log N) due to O(1) element access.
Binary Search on Linked List: O(N) due to O(N) element access in each step to find the middle
"""










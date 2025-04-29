
"""
K-th Element of Merged Two Sorted Arrays
Last Updated : 03 Mar, 2025
Given two sorted arrays of sizes m and n respectively, the task is to find the element that would be at the k-th position in the final sorted array formed by merging these two arrays.

Examples:

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final sorted array is [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element is 6.


Input: a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: The final sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element is 256.


Try it on GfG Practice
redirect icon
Table of Content

Using Sorting – O((m + n) * log(m + n)) Time and O(m + n) Space
Using Priority Queue – O((m + n + k) * log(m + n)) Time and O(m + n) Space
Using Merge Step of Merge Sort – O(m + n) Time and O(m + n) Space
Using Optimized Merge of Merge Sort – O(k) Time and O(1) Space
Using Binary Search – O(log(min(n, m)) Time and O(1) Space
Using Sorting – O((m + n) * log(m + n)) Time and O(m + n) Space
The idea is to create a new array by merging elements from both arrays (a[] and b[]), then sort the new array, and finally return the kth smallest element from the sorted array.





# Function for finding kth element
def kthElement(a, b, k):

    # to merge both the arrays
    arr = []

    # add the elements of array a
    for i in a:
        arr.append(i)

    # add the elements of array b
    for i in b:
        arr.append(i)

    # sort the merged array
    arr.sort()

    # return the kth element
    return arr[k - 1]

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(kthElement(a, b, k))

Output
6
Using Priority Queue – O((m + n + k) * log(m + n)) Time and O(m + n) Space
The idea is to build a min heap to store all the elements of both the arrays in sorted order, and then extract the first k elements to get the kth smallest element of the merge array.





# Function for finding kth element
import heapq

def kthElement(a, b, k):

    # to store the elements of both
    # the arrays in sorted order
    pq = []

    # add the elements of array a
    for i in a:
        heapq.heappush(pq, i)

    # add the elements of array a
    for i in b:
        heapq.heappush(pq, i)

    # pop the elements from the heap
    # till k-1 elements are popped
    while k > 1:
        heapq.heappop(pq)
        k -= 1

    # return the kth element
    return pq[0]

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(kthElement(a, b, k))

Output
6
Using Merge Step of Merge Sort – O(m + n) Time and O(m + n) Space
The basic idea here is to merge the given two arrays into a single sorted array and then simply return the element at the kth position. This approach is straightforward because it directly uses the merging process of two sorted arrays, similar to the merge step in the merge sort algorithm.


Step-by-step approach:

We initialize three pointers: two pointers to traverse each array and one to keep track of the position in the merged array.
By comparing the elements pointed to by the two array pointers, we place the smaller element into the merged array and move the respective pointer forward.
This continues until one of the arrays is fully traversed.
If any elements remain in either array, they are directly appended to the merged array.
Finally, the k-th element of this merged array is returned.



# Python Program to find K-th Element of Merged Two Sorted Arrays
# Using merge step of merge sort

def kthElement(a, b, k):
    n = len(a)
    m = len(b)

    # array to store the merged sorted array
    arr = [0] * (n + m)
    i = 0
    j = 0
    d = 0
    while i < n and j < m:

        # If the element of a[] is smaller, insert the
        # element to the sorted array
        if a[i] < b[j]:
            arr[d] = a[i]
            i += 1

        # If the element of b[] is smaller, insert the
        # element to the sorted array
        else:
            arr[d] = b[j]
            j += 1
        d += 1

    # Push the remaining elements of a[]
    while i < n:
        arr[d] = a[i]
        i += 1
        d += 1

    # Push the remaining elements of b[]
    while j < m:
        arr[d] = b[j]
        j += 1
        d += 1

    return arr[k - 1]

if __name__ == "__main__":
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    k = 5

    print(kthElement(arr1, arr2, k))

Output
6
Using Optimized Merge of Merge Sort – O(k) Time and O(1) Space
This approach optimizes the space complexity of the above approach by avoiding the creation of an additional array. Instead, we use two pointers to traverse the input arrays and count the elements until we reach the kth element. This method is more efficient in terms of space since it only uses a constant amount of extra memory.


We start with two pointers at the beginning of each array and another counter to keep track of the number of elements processed. By comparing the current elements of both arrays, the smaller one is considered as part of the merged sequence, and the pointer for that array would be incremented by 1. This process continues until we have processed k elements. The kth element encountered in this process is the result.





# Python program to find K-th Element of Merged Two Sorted Arrays
# Using optimized merge step of merge sort

def kthElement(a, b, k):
    n, m = len(a), len(b)

    # last element added to the merged sorted array
    last = 0
    i, j = 0, 0

    for _ in range(k):
        if i < n:
            # If a[i] > b[j] then increment j
            if j < m and a[i] > b[j]:
                last = b[j]
                j += 1
            # Otherwise increment i
            else:
                last = a[i]
                i += 1

        # If reached end of first array then increment j
        elif j < m:
            last = b[j]
            j += 1

    # Return the last (kth) element
    return last

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(kthElement(a, b, k))

Output
6
Using Binary Search – O(log(min(n, m)) Time and O(1) Space
The approach is similar to the Binary Search approach of Median of two sorted arrays of different sizes.


Consider the first array is smaller. If first array is greater, then swap the arrays to make sure that the first array is smaller.


We mainly maintain two sets in this algorithm by doing binary search in the smaller array. Let mid1 be the partition of the smaller array. The first set contains elements from 0 to (mid1 – 1) from smaller array and mid2 = (k – mid1) elements from the greater array to make sure that the first set has exactly k elements. The second set contains remaining elements.
Our target is to find a point in both arrays such that all elements in the first set are smaller than all elements in the other set (set that contains elements from right side). For this we validate the partitions using the same way as we did in Median of two sorted arrays of different sizes.
K-th-Element-of-Merged-Two-Sorted-Arrays-Using-Binary-Search-01.webpK-th-Element-of-Merged-Two-Sorted-Arrays-Using-Binary-Search-01.webp





# Python program to find K-th Element of Merged Two Sorted Arrays
# using Binary Search

def kthElement(a, b, k):
    n = len(a)
    m = len(b)

    # If a[] has more elements, then call kthElement
    # with reversed parameters
    if n > m:
        return kthElement(b, a, k)

    # Binary Search on the number of elements we can
    # include in the first set from a[]
    lo = max(0, k - m)
    hi = min(k, n)

    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = k - mid1

        # Find elements to the left and right of partition in a[]
        l1 = (mid1 == 0 and float('-inf') or a[mid1 - 1])
        r1 = (mid1 == n and float('inf') or a[mid1])

        # Find elements to the left and right of partition in b[]
        l2 = (mid2 == 0 and float('-inf') or b[mid2 - 1])
        r2 = (mid2 == m and float('inf') or b[mid2])

        # If it is a valid partition
        if l1 <= r2 and l2 <= r1:

            # Find and return the maximum of l1 and l2
            return max(l1, l2)

        # Check if we need to take lesser elements from a[]
        if l1 > r2:
            hi = mid1 - 1

        # Check if we need to take more elements from a[]
        else:
            lo = mid1 + 1

    return 0

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5

    print(kthElement(a, b, k))

"""












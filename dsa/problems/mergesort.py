
"""
Count Inversions of an Array
Last Updated : 01 Dec, 2024
Given an integer array arr[] of size n, find the inversion count in the array. Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Note: Inversion Count for an array indicates that how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in reverse order, the inversion count is maximum.

Examples:

Input: arr[] = {4, 3, 2, 1}
Output: 6
Explanation:


inversion-count
Input: arr[] = {1, 2, 3, 4, 5}
Output: 0
Explanation: There is no pair of indexes (i, j) exists in the given array such that arr[i] > arr[j] and i < j


Input: arr[] = {10, 10, 10}
Output: 0


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Two Nested Loops – O(n^2) Time and O(1) Space
[Expected Approach] Using Merge Sort – O(n*log n) Time and O(n) Space
[Naive Approach] Using Two Nested Loops – O(n^2) Time and O(1) Space
Traverse through the array, and for every index, find the number of smaller elements on its right side in the array. This can be done using a nested loop. Sum up the inversion counts for all indices in the array and return the sum.

"""


# Python program to Count Inversions in an array
# using nested loop

# Function to count inversions in the array
def inversionCount(arr):
    n = len(arr)
    invCount = 0

    for i in range(n - 1):
        for j in range(i + 1, n):

            # If the current element is greater than the next,
            # increment the count
            if arr[i] > arr[j]:
                invCount += 1
    return invCount

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(inversionCount(arr))


"""
Expected Approach] Using Merge Step of Merge Sort – O(n*log n) Time and O(n) Space
We can use merge sort to count the inversions in an array. First, we divide the array into two halves: left half and right half. Next, we recursively count the inversions in both halves. While merging the two halves back together, we also count how many elements from the left half array are greater than elements from the right half array, as these represent cross inversions (i.e., element from the left half of the array is greater than an element from the right half during the merging process in the merge sort algorithm). Finally, we sum the inversions from the left half, right half, and the cross inversions to get the total number of inversions in the array. This approach efficiently counts inversions while sorting the array.


Let’s understand the above intuition in more detailed form, as we get to know that we have to perform the merge sort on the given array. Below images represents dividing and merging steps of merge sort.

merge-sort-copy
During each merging step of the merge sort algorithm, we count cross inversions by comparing elements from the left half of the array with those from the right half. If we find an element arr[i] in the left half that is greater than an element arr[j] in the right half, we can conclude that all elements after i in the left half will also be greater than arr[j]. This allows us to count multiple inversions at once. Let’s suppose if there are k elements remaining in the left half after i, then there are k cross inversions for that particular arr[j]. The rest of the merging process continues as usual, where we combine the two halves into a sorted array. This efficient counting method significantly reduces the number of comparisons needed, enhancing the overall performance of the inversion counting algorithm.

Below Illustration represents the cross inversion of a particular step during the merging process in the merge sort algorithm:

count-inversions-of-an-array-1.webpcount-inversions-of-an-array-1.webp


"""


# Python program to Count Inversions in an array using merge sort

# This function merges two sorted subarrays arr[l..m] and arr[m+1..r]
# and also counts inversions in the whole subarray arr[l..r]
def countAndMerge(arr, l, m, r):

    # Counts in two subarrays
    n1 = m - l + 1
    n2 = r - m

    # Set up two lists for left and right halves
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    # Initialize inversion count (or result)
    # and merge two halves
    res = 0
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:

        # No increment in inversion count
        # if left[] has a smaller or equal element
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1

    # Merge remaining elements
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return res

# Function to count inversions in the array
def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (r + l) // 2

        # Recursively count inversions
        # in the left and right halves
        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)

        # Count inversions such that greater element is in
        # the left half and smaller in the right half
        res += countAndMerge(arr, l, m, r)
    return res

def inversionCount(arr):
    return countInv(arr, 0, n - 1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split(" ")))
    #arr = [4, 3, 2, 1]
    print(inversionCount(arr))

"""
Output
6
Note: The above code modifies (or sorts) the input array. If we want to count only inversions, we need to create a copy of the original array and perform operation on the copy array
"""















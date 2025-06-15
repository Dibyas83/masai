

"""
Implement Upper Bound
Last Updated : 17 Oct, 2024
Given a sorted array arr[] and a number target, the task is to find the upper bound of the target in this given array. The upper bound of a number is defined as the smallest index in the sorted array where the element is greater than the given number.

Note: If all the elements in the given array are smaller than or equal to the target, the upper bound will be the length of the array.

Examples:

Input: arr[] = {2, 3, 7, 10, 11, 11, 25}, target = 9
Output: 3
Explanation: 3 is the smallest index in arr[], at which element (arr[3] = 10) is larger than 9.

Input: arr[] = {2, 3, 7, 10, 11, 11, 25}, target = 11
Output: 6
Explanation: 6 is the smallest index in arr[], at which element (arr[6] = 25) is larger than 11.

Input: arr[] = {2, 3, 7, 10, 11, 11, 25}, target = 100
Output: 7
Explanation: As no element in arr[] is greater than 100, return the length of array.

Table of Content

[Naive Approach] Using Linear Search - O(n) Time and O(1) Space
[Expected Approach] Using Binary Search - O(log n) Time and O(1) Space
[Naive Approach] Using Linear Search - O(n) Time and O(1) Space
The idea is to use linear search. We compare each element of the given array with the target and find the first index where the element is greater than target.

"""
# Python program to find the upper bound of a number
# using linear search

# Function to find the upper bound of a number
def upperBound(arr, target):
    n = len(arr)

    # Compare target with each element in array
    for i in range(n):

        # If larger value found, return its index
        if arr[i] > target:
            return i

    # If all elements are smaller, return length
    return n

if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 11
    print(upperBound(arr, target))

"""
[Expected Approach] Using Binary Search - O(log n) Time and O(1) Space
The idea is to use the fact that the given array is sorted. We can apply binary search to find the index of the element just larger than the target. 

Step-by-step implementation:

Set variables lo and hi to the starting and ending of array.
Find mid = (lo + hi) / 2 and compare arr[mid] with target
if arr[mid] <= target, then all elements in the range arr[lo...mid] will also be <= target, so update lo = mid+1.
if arr[mid] > target, then upper bound will lie in the range arr[lo...mid], so update result to mid and update hi = mid - 1.
Continue step 2 till lo <= hi.
Return result as the upper bound.

"""


# Python program to find the upper bound of a number
# using binary search

# Function to find the upper bound of a number
def upperBound(arr, target):
    lo, hi = 0, len(arr) - 1
    res = len(arr)

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print(mid,"mid")
        print(lo,hi,"lo hi")

        # If arr[mid] > target, then arr[mid] can be
        # the upper bound so store mid in result and
        # search in left half, i.e. arr[lo...mid-1]
        if arr[mid] > target:
            res = mid
            hi = mid - 1

        # If arr[mid] <= target, then upper bound
        # cannot lie in the range [lo...mid], so
        # search in right half, i.e. arr[mid+1...hi]
        else:
            lo = mid + 1

    return res


if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 11

    print(upperBound(arr, target))

"""
3 mid
0 6 lo hi
5 mid
4 6 lo hi
6 mid
6 6 lo hi
6
"""




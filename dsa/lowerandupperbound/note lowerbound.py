
"""
Implement Lower Bound
Last Updated : 17 Oct, 2024
Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array. The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.

Note: If all the elements in the given array are smaller than the target, the lower bound will be the length of the array.

Examples:

Input: arr[] = {2, 3, 7, 10, 11, 11, 25}, target = 9
Output: 3
Explanation: 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.

Input: arr[] = {2, 3, 7, 10, 11, 11, 25}, target = 11
Output: 4
Explanation: 4 is the smallest index in arr[] where element (arr[4] = 11) is greater than or equal to 11.

Input: arr[] = {2, 3, 7, 10, 11, 11, 25}, target = 100
Output: 6
Explanation: As no element in arr[] is greater than 100, return the length of array.

Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Linear Search - O(n) Time and O(1) Space
[Expected Approach] Using Binary Search - O(log n) Time and O(1) Space
[Naive Approach] Using Linear Search - O(n) Time and O(1) Space
The idea is to use linear search. We compare each element of the given array with the target and find the first index where the element is greater than or equal to the target.
"""


# Python program to find the lower bound of a number
# using linear search

def lowerBound(arr, target):
    n = len(arr)

    # compare target with each element in array
    for i in range(n):

        # if equal or larger value found
        # return its index
        if arr[i] >= target:
            return i

    # if all elements are smaller, return length
    return n


if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 9
    print(lowerBound(arr, target))


"""
Output
3
[Expected Approach] Using Binary Search - O(log n) Time and O(1) Space
The idea is to use the fact that the given array is sorted. We can apply binary search to find the index of the element greater than or equal to the target. 

Step-by-step implementation:

Set variables lo and hi to the starting and ending of array.
Find mid = (lo + hi) / 2 and compare arr[mid] with target
if a[mid] >= target, then lower bound will be in the range arr[lo...mid], so update result to mid and hi to mid - 1.
if a[mid] < target, then all elements in the range [lo...mid] will also be less than target, so update lo to mid + 1.
Continue step 2 till lo <= hi.
Return result as the lower bound.
"""


# Python program to find the lower bound of a number
# using Binary Search

def lowerBound(arr, target):
    lo = 0
    hi = len(arr) - 1
    res = len(arr)

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # If arr[mid] >= target, then mid can be the
        # lower bound, so update res to mid and
        # search in left half, i.e. [lo...mid-1]
        if arr[mid] >= target:
            res = mid
            hi = mid - 1

        # If arr[mid] < target, then lower bound
        # cannot lie in the range [lo...mid] so
        # search in right half, i.e. [mid+1...hi]
        else:
            lo = mid + 1

    return res


if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 9

    print(lowerBound(arr, target))










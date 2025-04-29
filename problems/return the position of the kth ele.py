
"""
Sort the array:
The initial step involves sorting the input array in ascending order. This can be achieved using various
sorting algorithms like merge sort, quicksort, or heapsort.

Return the element at index k-1:
After sorting, the kth smallest element will be located at the index k-1 (since arrays are typically
zero-indexed). Return the element at this index.
"""


def find_kth_element(arr, k):
    """
    Returns the kth smallest element in the array.

    Args:
        arr: The input array.
        k: The position of the element to return (1-based index).

    Returns:
        The kth smallest element in the array.
    """
    arr.sort()
    return arr[k - 1]

"""
To find the position of the k-th element after a stable sort, you can either simulate the sorting process while keeping track of original indices or use a more efficient approach by leveraging properties of stable sorts.
Approach 1: Simulate Stable Sort
Create a copy: Make a copy of the input array to avoid modifying the original.
Maintain indices: Create a list of tuples, where each tuple contains the element and its original index.
Sort: Sort the list of tuples based on the element values, ensuring that the sort is stable (maintains the original order of equal elements).
Find the k-th element: Find the k-th element in the sorted list of tuples. 
Return the position: The original index of the k-th element is the position of that element after the stable sort. 
Approach 2: Efficient Solution
1. Stable sort property:
A stable sort maintains the relative order of elements with equal values. Therefore, the k-th element's position after sorting will be determined by the number of elements smaller than or equal to it, and the order of these elements based on their original positions.
2. Count elements:
Iterate through the array and count the number of elements smaller than the k-th element. Also, keep track of the number of elements equal to the k-th element encountered before the k-th element.
3. Calculate the position:
The position of the k-th element will be the count of smaller elements plus the number of equal elements before it.
Example
Python
"""
def find_kth_element_position(arr, k):
    n = len(arr)

    # Approach 1: Simulate Stable Sort
    temp_arr = [(val, i) for i, val in enumerate(arr)]
    temp_arr.sort(key=lambda x: x[0])

    kth_element = temp_arr[k-1][0]

    # Approach 2: Efficient Solution
    count_smaller = 0
    count_equal_before = 0

    for i in range(n):
        if arr[i] < arr[k-1]:
            count_smaller += 1
        elif arr[i] == arr[k-1] and i < k-1:
            count_equal_before += 1

    return count_smaller + count_equal_before + 1

# Example Usage
arr = [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
k = 5
position = find_kth_element_position(arr, k)
print(f"The position of the {k}-th element after stable sort is: {position}") # Output: 4

arr = [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
k = 2
position = find_kth_element_position(arr, k)
print(f"The position of the {k}-th element after stable sort is: {position}") #

#------------------
"""
One easy way to solve this problem is to use any stable sorting algorithm like Insertion Sort, Merge Sort etc and then get the new index of given element but we can solve this problem without sorting the array. 

As position of an element in a sorted array is decided by only those elements which are smaller than given element. We count all array elements smaller than given element and for those elements which are equal to given element, elements occurring before given elements’ index will be included in count of smaller elements this will insure the stability of the result’s index. 

"""



# Python program to get index of array element in
# sorted array
# Method returns the position of arr[idx] after
# performing stable-sort on array

def getIndexInSortedArray(arr, n, idx):
       # Count of elements smaller than current
       # element plus the equal element occurring
       # before given index
    result = 0
    for i in range(n):
        # If element is smaller then increase
        # the smaller count
        if (arr[i] < arr[idx]):
            result += 1

        # If element is equal then increase count
        # only if it occurs before
        if (arr[i] == arr[idx] and i < idx):
            result += 1
    return result;

# Driver code to test above methods
arr = [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
n = len(arr)

idxOfEle = 5
print (getIndexInSortedArray(arr, n, idxOfEle))

# Contributed by: Afzal Ansari













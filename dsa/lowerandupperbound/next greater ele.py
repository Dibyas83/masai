

"""
Next Greater Element | Set 2 (Using Upper Bound)
Last Updated : 26 Nov, 2021
Given an array arr[ ] of n integers. The task is to find the first greater element for every array element in the array using upper_bound( ) function. If there is no greater element possible for any array element return -1.
Examples :



Input: n = 7, arr[ ] = {4, 7, 3, 1, 3, 2, 5}
Output: 7 -1 4 4 4 4 7
Explanation : First greater element for first, third, fourth, fifth, sixth and last element are 7, 4, 4, 4, 4, and 7 . Second element of arr[ ] do not have it's first greater element of itself.





Input : n = 4, arr[ ] = {2, 8,  8, 1}
Output : 8 -1 -1 2
Explanation : First greater element for first and last element are 8 and 2 . Second and third element of arr[ ] do not have it's first greater element of itself .





Naive Approach: The Naive Approach and the stack approach are discussed in Set 1 of this article. Here, we have discussed the method to solve it using upper_bound().

Approach: Since upper_bound( ) cannot be applied in an unsorted array. The idea is to try to modify the array so that it becomes sorted. Thus, create an array let's name it copy[], which will have its elements in a sorted manner. First initialize copy[ ] with 0 and update every element of copy [ ] as : copy[i] = max(copy[i-1], arr[i]). Now, upper_bound( ) can be applied in the copy [ ] and find first greater element for every arr[i]. Follow the steps below to solve the problem:

Initialize an array copy[n] with values 0.
Iterate over the range [1, n) using the variable i and perform the following steps:
Set the value of copy[i] as the maximum of copy[i-1] or arr[i].
Iterate over the range [0, n) using the variable i and perform the following steps:
Initialize the variable high as the upper bound of arr[i] in the copy[] array.
If high equals n then print -1 otherwise print arr[high].
Below is the implementation of the above approach:

"""
# Python 3 implementation of  the above approach
import bisect

# Function to find first greater
# element for every element of array
def FirstGreater(arr, n):

    # Creating copy array
    copy = [0]*n

    copy[0] = arr[0]

    for i in range(1, n):

        # Updating element of copy[]
        copy[i] = max(copy[i - 1], arr[i])

    for i in range(n):

        # High stores the index of first greater
        # for every element of arr[]
        high = bisect.bisect_right(copy, arr[i], 0, n)

        # If there no element
        # is greater than arr[i]
        # print -1
        if (high == n):
            print("-1", end=" ")

        # Otherwisw print the first element
        # which is greater than arr[i]
        else:
            print(arr[high], end=" ")

# Driver Code
if __name__ == "__main__":

    arr = [4, 7, 3, 1, 3, 2, 5]
    n = len(arr)
    FirstGreater(arr, n)

    # This code is contributed by ukasp.









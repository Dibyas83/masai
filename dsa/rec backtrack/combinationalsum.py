

"""
Combination Sum
Last Updated : 28 Jan, 2025
Given an array of distinct integers arr[] and an integer target, the task is to find a list of all unique combinations of array where the sum of chosen element is equal to target.

Note: The same number may be chosen from array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Examples:

Input: arr[] = [2, 4, 6, 8], target = 8
Output: [[2, 2, 2, 2],
                [2, 2, 4],
                [2, 6],
                [4, 4],
                [8]]


Input: arr[] = [2, 7, 6, 5], target = 16
Output: [[2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 6],
                [2, 2, 2, 5, 5],
                [2, 2, 5, 7],
                [2, 2, 6, 6],
                [2, 7, 7],
                [5, 5, 6]]


Try it on GfG Practice
redirect icon
Approach: Using backtracking
The idea is to use backtracking and recursively explore all possible combinations of elements, of the given array that sums up to given target value. If the remaining sum becomes less than 0 then backtrack to explore other possible combinations.


Step by step implementation

To perform recursion, create an array cur[] to store the current combination and a 2D array res[] to store all valid combinations. Start from the 0th element and for each element arr[i], there are two choices:
Include the element: Add it to array cur and reduce remSum by arr[i] and move to the same index as we can choose same element multiple times.
Skip the element: Move to the next element without adding the current.
If the remaining sum becomes 0, add the current combination cur to res else backtrack to previous element by removing the element from the last index of cur.



# Python program to find all combinations that
# sum to a given target

# Function to generate all combinations
# of arr that sums to target.
def makeCombination(arr, remSum, cur, res, index):

    # If remSum is 0 then add the combination to the result
    if remSum == 0:
        res.append(list(cur))
        return

    # Invalid Case: If remSum is less than 0 or if index >= len(arr)
    if remSum < 0 or index >= len(arr):
        return

    # Add the current element to the combination
    cur.append(arr[index])

    # Recur with the same index
    makeCombination(arr, remSum - arr[index], cur, res, index)

    # Remove the current element from the combination
    cur.pop()

    # Recur with the next index
    makeCombination(arr, remSum, cur, res, index + 1)

# Function to find all combinations of elements
# in array arr that sum to target.
def combinationSum(arr, target):
    arr.sort()

    # List to store combinations
    cur = []

    # List to store valid combinations
    res = []
    makeCombination(arr, target, cur, res, 0)

    return res

if __name__ == "__main__":
    arr = [2, 4, 6, 8]
    target = 8

    res = combinationSum(arr, target)

    for v in res:
        print(" ".join(map(str, v)))

Output
2 2 2 2
2 2 4
2 6
4 4
8
Time Complexity: O(K * 2k), where K is average size of a valid combination and k = Target​ / min(arr), depth of the recursion tree.
Auxiliary Space: O(k), considering the recursive stack and neglecting the space required to store the combinations.



"""










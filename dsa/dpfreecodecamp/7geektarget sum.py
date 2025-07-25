"""

Target Sum
Last Updated : 13 Nov, 2023
Given an array arr[] of length N and an integer target. You want to build an expression out of arr[] by adding one of the symbols '+' and '-' before each integer in arr[] and then concatenate all the integers. Return the number of different expressions that can be built, which evaluates to target.

Example:

Input : N = 5, arr[] = {1, 1, 1, 1, 1}, target = 3
Output: 5
Explanation:
There are 5 ways to assign symbols to
make the sum of array be target 3.





-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3



Input: N = 1, arr[] = {1}, target = 1
Output: 1



Try it on GfG Practice
redirect icon
Target Sum using Recursion:
The problem can be solved by recursively exploring all possible ways to combine the integers in the array while adding or subtracting them to reach the target sum. At each step, there are two choices: either add the current element to the running total or subtract it.
Let's findTotalWays(arr, i, s, target) tells us number of ways to reach target, if first i elements have been considered and current sum is s.

Recurrence Relation:
 findTotalWays(arr, i, s, target) =  findTotalWays(arr, i+1,s +arr[i], target) +  findTotalWays(arr, i+1, s-arr[i], target)



For each element, there are 2 options.

Add the current element: If we add the current element to running total then current sum will become s+arr[i]. Call the findTotalWays() function recursively with the updated current sum and the remaining elements of array i.e., findTotalWays(arr, i+1,s +arr[i], target)
Subtract the current element: If we subtract the current element from running total then current sum will become s-arr[i]. Call the findTotalWays() function recursively with the updated current sum and the remaining elements of array i.e., findTotalWays(arr, i+1,s -arr[i], target)
Base case:

If the target sum is reached (i.e., s becomes equal to target sum) and all elements in the array have been processed, return 1. This represents a valid way to form the target sum.
If all elements in the array have been processed but the target sum has not been reached (i.e., s is not equal to target sum), return 0. This indicates expression does not evaluates to target.






"""
# Function to find the number of ways to calculate
# a target number using only array elements and
# addition or subtraction operator.
def findTotalWays(arr, i, s, target):
    # If target is reached, return 1
    if s == target and i == len(arr):
        return 1

    # If all elements are processed and
    # target is not reached, return 0
    if i >= len(arr):
        return 0

    # Return total count of two cases:
    # 1. Consider the current element and add it to the current sum target
    # 2. Consider the current element and subtract it from the current sum.
    return findTotalWays(arr, i + 1, s + arr[i], target) + findTotalWays(arr, i + 1, s - arr[i], target)

# Driver Program
if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1]

    # target number
    target = 3

    print(findTotalWays(arr, 0, 0, target))


#--------------------------
"""
Target Sum using Dynamic Programming (Memoization):
The above recursive solution has Optimal Substructure and Overlapping Subproblems so Dynamic programming (Memoization) can be used to solve the problem. So, 2D array can be used to store results of previously calculated subproblems. 



Follow the below steps to Implement the idea:

Create a 2D dp array to store the results of previously solved subproblems.
dp[i][j] will represent the number of distinct expressions to make the target sum if first i elements have even considered and the current sum is j.
During the recursion call, if the same state is called more than once, then we can directly return the answer stored in dp for that state instead of calculating again.
Notice that total_sum is added to current sum in recursive function to ensure that the memoization table can handle both positive and negative sums.

"""

# Function to find the number of ways to calculate
# a target number using only array elements and
# addition or subtraction operator.
def find_total_ways(arr, dp, i, s, target, total_sum):
    # If target is reached, return 1
    if s == target and i == len(arr):
        return 1

    # If all elements are processed and
    # target is not reached, return 0
    if i >= len(arr):
        return 0

    # If the result for the current state (i, s +
    # total_sum) has already been computed,
    # return it from the DP table to avoid redundant
    # calculations.
    if dp[i][s + total_sum] != -1:
        return dp[i][s + total_sum]

    # Return the total count of two cases:
    # 1. Consider the current element and add it to the current sum target.
    # 2. Consider the current element and subtract it from the current sum.
    dp[i][s + total_sum] = find_total_ways(arr, dp, i + 1, s + arr[i], target, total_sum) + \
                           find_total_ways(arr, dp, i + 1, s - arr[i], target, total_sum)

    return dp[i][s + total_sum]


# Driver Program
if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1]
    total_sum = sum(arr)

    # Target number
    target = 3

    # Create a DP table
    dp = [[-1] * (2 * total_sum + 1) for _ in range(len(arr))]

    # Calculate and print the result
    print(find_total_ways(arr, dp, 0, 0, target, total_sum))













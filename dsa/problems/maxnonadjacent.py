

def maxSum(arr):
    n = len(arr)

    # Create a dp array to store the maximum sum at each element
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    dp[1] = arr[0]

    # Fill the dp array using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = max(arr[i - 1] + dp[i - 2], dp[i - 1])

    return dp[n]
def inpt():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split(" ")))
        sum = maxSum(arr)
        print(sum)
inpt()

"""
Maximum sum such that no two are adjacent
Last Updated : 07 Apr, 2025
Given an array of positive numbers, find the maximum sum of a subsequence such that no two numbers in the subsequence should be adjacent in the array.

Examples: 

Input: arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: Pick the subsequence {5, 100, 5}.
The sum is 110 and no two elements are adjacent. This is the highest possible sum.


Input: arr[] = {3, 2, 7, 10}
Output: 13
Explanation: The subsequence is {3, 10}. This gives the highest possible sum = 13.


Input: arr[] = {3, 2, 5, 10, 7}
Output: 15
Explanation: Pick the subsequence {3, 5, 7}. The sum is 15.


[Naive Approach] Using Recursion- O(2^n) Time and O(n) Space
The idea is to explore all the possibilities for each element using Recursion. We can start from the last element and for each element, we have two choices:


Pick the current element and skip the element just before it.
Skip the current element and move to the element just before it.
So, the recurrence relation will be: 


maxSumRec(n) = max(arr[n – 1] + maxSumRec(n – 2),   
                                          maxSumRec(n – 1)), 
where maxSumRec(n) returns the maximum sum if n elements are left.





# Python Program to find maximum sum with no two adjacent using Recursion

# Calculate the maximum Sum value recursively
def maxSumRec(arr, n):
    
    # If no elements are left, return 0.
    if n <= 0:
        return 0
  
    # If only 1 element is left, pick it. 
    if n == 1:
        return arr[0]

    # Two Choices: pick the nth element and do not pick the nth element 
    pick = arr[n - 1] + maxSumRec(arr, n - 2)
    notPick = maxSumRec(arr, n - 1)

    # Return the max of two choices
    return max(pick, notPick)

# Function to calculate the maximum Sum value
def maxSum(arr):
    n = len(arr)
  
    # Call the recursive function for n elements
    return maxSumRec(arr, n)

if __name__ == "__main__":
    arr = [6, 7, 1, 3, 8, 2, 4]
    print(maxSum(arr))

Output
19
Time Complexity: O(2n). Every element has 2 choices to pick and not pick.
Auxiliary Space: O(n). For recursion stack space

[Better Approach] Using Memoization – O(n) Time and O(n) Space
The above solution has optimal substructure and overlapping subproblems. 


Recursion-Tree
We can optimize this solution using a memo array of size (n + 1), such that memo[i] represents the maximum value that can be collected from first i elements. Please note that there is only one parameter that changes in recursion and the range of this parameter is from 0 to n.





# Python Program to find maximum sum with no two adjacent

def maxSumRec(arr, n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return arr[0]

    # Check if the result is already computed
    if memo[n] != -1:
        return memo[n]

    pick = arr[n - 1] + maxSumRec(arr, n - 2, memo)
    notPick = maxSumRec(arr, n - 1, memo)

    # Store the max of two choices in the memo array and return it
    memo[n] = max(pick, notPick)
    return memo[n]

def maxSum(arr):
    n = len(arr)
  
    # Initialize memo array with -1
    memo = [-1] * (n + 1)
    return maxSumRec(arr, n, memo)

if __name__ == "__main__":
    arr = [6, 7, 1, 3, 8, 2, 4]
    print(maxSum(arr))

Output
19
Time Complexity: O(n). Every element is computed only once.
Auxiliary Space: O(n). For recursion stack space and memo array.

[Expected Approach 1] Using Tabulation – O(n) Time and O(n) Space
The idea is to build the solution in bottom-up manner. We create a dp[] array of size n+1 where dp[i] represents the maximum sum that can be obtained with first i elements. We first fill the known values, dp[0] and dp[1] and then fill the remaining values using the formula: dp[i] = max(arr[i] + dp[i – 2], dp[i – 1]). The final result will be stored at dp[n].





def maxSum(arr):
    n = len(arr)
  
    # Create a dp array to store the maximum sum at each element
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    dp[1] = arr[0]

    # Fill the dp array using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = max(arr[i - 1] + dp[i - 2], dp[i - 1])

    return dp[n]

arr = [6, 7, 1, 3, 8, 2, 4]
print(maxSum(arr))

Output
19
Time Complexity: O(n), Every element is computed only once.
Auxiliary Space O(n), We are using a dp array of size n.

[Expected Approach 2] Space-Optimized DP – O(n) Time and O(1) Space
On observing the dp[] array in the previous approach, it can be seen that the answer at the current index depends only on the last two values. In other words, dp[i] depends only on dp[i – 1] and dp[i – 2]. So, instead of storing the result in an array, we can simply use two variables to store the last and second last result.





# Function to calculate the maximum Sum value
def maxSum(arr):
    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # Set previous 2 values
    secondLast = 0
    last = arr[0]

    # Compute current value using previous two values
    # The final current value would be our result
    res = 0
    for i in range(1, n):
        res = max(arr[i] + secondLast, last)
        secondLast = last
        last = res

    return res

arr = [6, 7, 1, 3, 8, 2, 4]
print(maxSum(arr))
"""











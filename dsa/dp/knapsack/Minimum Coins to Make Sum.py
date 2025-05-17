
"""

Given an array of coins[] of size n and a target value sum, where coins[i] represent the coins of different denominations. You have an infinite supply of each of the coins. The task is to find the minimum number of coins required to make the given value sum. If it is not possible to form the sum using the given coins, return -1.

Examples:

Input: coins[] = [25, 10, 5], sum = 30
Output: 2
Explanation : Minimum 2 coins needed, 25 and 5


Input: coins[] = [9, 6, 5, 1], sum = 19
Output: 3
Explanation: 19 = 9 + 9 + 1


Input: coins[] = [5, 1], sum = 0
Output: 0
Explanation: For 0 sum, we do not need a coin


Input: coins[] = [4, 6, 2], sum = 5
Output: -1
Explanation: Not possible to make the given sum.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach ] Using Recursion – O(n^sum) Time and O(sum) Space
[Better Approach 1] Using Top-Down DP (Memoization) – O(n*sum) Time and O(n*sum) Space
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(n*sum) Time and O(n*sum) Space
[Expected Approach] Using Space Optimized DP – O(n*sum) Time and O(sum) Space
[Naive Approach ] Using Recursion – O(n^sum) Time and O(sum) Space
This problem is a variation of the problem Coin Change Problem. Here instead of finding the total number of possible solutions, we need to find the solution with the minimum number of coins.


The idea is to find the minimum number of coins required to reach the target sum by trying each coin denomination in the coins[] array. Starting from the target sum, for each coin coins[i], we can either include it or exclude it. If we include it, we subtract its value from sum and recursively try to make the remaining amount with the same coin denominations. If we exclude it, we move to the next coin in the list.


Mathematically the recurrence relation will look like the following:

minCoins(i, sum, coins) = min(1 + minCoins(i, sum-coins[i], coins), minCoins(i+1, sum, coins))


Base cases:


minCoins(i, sum, coins) = 0, if sum = 0.
minCoins(i, sum, coins) = INTEGER MAX, if sum < 0 or i == size of coins.



1
# Python program to find minimum of coins
2
# to make a given change sum
3
​
4
def minCoinsRecur(i, sum, coins):
5

6
    # base case
7
    if sum == 0:
8
        return 0
9
    if sum < 0 or i == len(coins):
10
        return float('inf')
11

12
    take = float('inf')
13

14
    # take a coin only if its value
15
    # is greater than 0.
16
    if coins[i] > 0:
17
        take = minCoinsRecur(i, sum - coins[i], coins)
18
        if take != float('inf'):
19
            take += 1
20
    #not taking the coin
21
    noTake = minCoinsRecur(i + 1, sum, coins)
22

23
    return min(take, noTake)
24
​
25
def minCoins(coins, sum):
26
    ans = minCoinsRecur(0, sum, coins)
27
    return ans if ans != float('inf') else -1
28
​
29
if __name__ == "__main__":
30
    coins = [9, 6, 5, 1]
31
    sum = 19
32
    print(minCoins(coins, sum))

Output
3
[Better Approach 1] Using Top-Down DP (Memoization) – O(n*sum) Time and O(n*sum) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:

1. Optimal Substructure:


Minimum number of ways to make sum at index i, i.e., minCoins(i, sum, coins), depends on the optimal solutions of the subproblems minCoins(i, sum-coins[i], coins) , and minCoins(i+1, sum, coins). By comparing these optimal substructures, we can efficiently calculate the minimum number of coins to make target sum at index i.


2. Overlapping Subproblems:


While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times.


There are only are two parameters: i and sum that changes in the recursive solution. So we create a 2D matrix of size n*(sum+1) for memoization.
We initialize this matrix as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to find minimum of coins
2
# to make a given change sum
3
​
4
def minCoinsRecur(i, sum, coins, memo):
5

6
    # base case
7
    if sum == 0:
8
        return 0
9
    if sum < 0 or i == len(coins):
10
        return float('inf')
11

12
    if memo[i][sum] != -1:
13
        return memo[i][sum]
14

15
    take = float('inf')
16

17
    # take a coin only if its value
18
    # is greater than 0.
19
    if coins[i] > 0:
20
        take = minCoinsRecur(i, sum - coins[i], coins, memo)
21
        if take != float('inf'):
22
            take += 1
23
    #not take the coins
24
    noTake = minCoinsRecur(i + 1, sum, coins, memo)
25

26
    memo[i][sum] = min(take, noTake)
27
    return memo[i][sum]
28
​
29
def minCoins(coins, sum):
30
    memo = [[-1] * (sum + 1) for _ in range(len(coins))]
31
    ans = minCoinsRecur(0, sum, coins, memo)
32
    return ans if ans != float('inf') else -1
33
​
34
if __name__ == "__main__":
35
    coins = [9, 6, 5, 1]
36
    sum = 19
37
    print(minCoins(coins, sum))

Output
3
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(n*sum) Time and O(n*sum) Space
 The idea is to fill the DP table based on previous values. For each coin, we either include it or exclude it to compute the minimum number of coins needed for each sum. The table is filled in an iterative manner from i = n-1 to i = 0 and for each sum from 1 to sum.


The dynamic programming relation is as follows:


if (sum-coins[i]) is greater than 0, then dp[i][sum] = min(1+dp[i][sum-coins[i]], dp[i+1][sum])
else dp[i][sum] = dp[i+1][sum].



1
# Python program to find minimum of coins
2
# to make a given change sum
3
​
4
def minCoins(coins, sum):
5
    dp = [[0] * (sum + 1) for _ in range(len(coins))]
6
​
7
    for i in range(len(coins) - 1, -1, -1):
8
        for j in range(1, sum + 1):
9
            dp[i][j] = float('inf')
10
            take = float('inf')
11
            noTake = float('inf')
12
​
13
            # If we take coins[i] coin
14
            if j - coins[i] >= 0:
15
                take = dp[i][j - coins[i]]
16
                if take != float('inf'):
17
                    take += 1
18
​
19
            if i + 1 < len(coins):
20
                #not take the coins
21
                noTake = dp[i + 1][j]
22
​
23
            dp[i][j] = min(take, noTake)
24
​
25
    if dp[0][sum] != float('inf'):
26
        return dp[0][sum]
27
    return -1
28
​
29
if __name__ == "__main__":
30
    coins = [9, 6, 5, 1]
31
    sum = 19
32
    print(minCoins(coins, sum))

Output
3
[Expected Approach] Using Space Optimized DP – O(n*sum) Time and O(sum) Space
In previous approach of dynamic programming we have derive the relation between states as given below:


if (sum-coins[i]) is greater than 0, then dp[i][sum] = min(1+dp[i][sum-coins[i]], dp[i+1][sum])
else dp[i][sum] = dp[i+1][sum].
If we observe that for calculating current dp[i][sum] state we only need previous row dp[i-1][sum] or current row dp[i][sum-coins[i]]. There is no need to store all the previous states just one previous state is used to compute result.





1
# Python program to find minimum of coins
2
def minCoins(coins, sum):
3

4
    # Initialize a list to store the minimum
5
    # number of coins for each amount
6
    dp = [float('inf')] * (sum + 1)
7

8
    # Base case: 0 coins are needed to make the sum of 0
9
    dp[0] = 0
10

11
    # Iterate over each coin in reverse order
12
    for i in range(len(coins) - 1, -1, -1):
13

14
        # Iterate through all amounts from 1 to sum
15
        for j in range(1, sum + 1):
16

17
            #  take variable for the current coin
18
            take = float('inf')
19

20
            #  noTake variable for the current amount
21
            noTake = float('inf')
22

23
            # If we can take the current coin
24
            if j - coins[i] >= 0 and coins[i] > 0:
25

26
                # Get the minimum coins needed
27
                # for the remaining amount
28
                take = dp[j - coins[i]]
29

30
                # Increment the count if it's a valid take
31
                if take != float('inf'):
32
                    take += 1
33

34
            # If there are coins left to consider
35
            if i + 1 < len(coins):
36

37
                # Get the minimum coins needed without
38
                # taking the current coin
39
                noTake = dp[j]
40

41
            # Store the minimum of taking or not
42
            # taking the current coin
43
            dp[j] = min(take, noTake)
44

45
    # Return the result for the given sum,
46
    # or -1 if it's not possible
47
    return dp[sum] if dp[sum] != float('inf') else -1
48
​
49
if __name__ == "__main__":
50
    coins = [9, 6, 5, 1]
51
    sum = 19
52
    print(minCoins(coins, sum))

Output
3
"""








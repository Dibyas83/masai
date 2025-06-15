"""


class Solution:
    def combine(self,n: int,k: int) -> list[list[int]]:
        result = []

        def comb(beg,curr):
            if len(curr) == k:
                result.append(curr)
                return
            if len(curr) > k:
                return
            for ind in range(beg,n+1):
                comb(ind +1, curr + [ind])
        comb(1,[])
        return result

    n = 3
    k = 2
"""
#--------------
def find_combinations(numbers, k, target):
    result = []

    def backtrack(combination, remaining_target, start_index):
        if remaining_target == 0 and len(combination) == k:
            result.append(combination.copy())
            return

        if remaining_target < 0 or len(combination) > k:
            return

        for i in range(start_index, len(numbers)):
            combination.append(numbers[i])
            backtrack(combination, remaining_target - numbers[i], i + 1)
            combination.pop()

    backtrack([], target, 0)
    return result

numbers = [1,2,3,4,5,6,7,8,9]
k = 4
target = 20
print(find_combinations(numbers, k, target))

#-----------dp
def combinations_sum_k(n, k, x):
    """
    Finds combinations of k numbers from 1 to n that sum up to x using dynamic programming.

    Args:
        n: The upper bound of the numbers to choose from (inclusive).
        k: The number of numbers to choose.
        x: The target sum.

    Returns:
        A list of combinations (lists) that sum up to x, or an empty list if no such combination exists.
    """

    dp = {}

    def solve(remaining_sum, remaining_count, current_num):
        if (remaining_sum, remaining_count, current_num) in dp:
            return dp[(remaining_sum, remaining_count, current_num)]

        if remaining_sum == 0 and remaining_count == 0:
            return [[]]

        if remaining_sum <= 0 or remaining_count <= 0 or current_num > n:
            return []

        include_current = []
        if remaining_sum >= current_num:
            include_current = [
                [current_num] + comb
                for comb in solve(remaining_sum - current_num, remaining_count - 1, current_num + 1)
            ]

        exclude_current = solve(remaining_sum, remaining_count, current_num + 1)

        dp[(remaining_sum, remaining_count, current_num)] = include_current + exclude_current
        return dp[(remaining_sum, remaining_count, current_num)]

    return solve(x, k, 1)

n,k,x = 9, 4, 20
print(combinations_sum_k(n,k,x))

#---------------
def GFG(N, K, target, coins, dp):
    # Base cases
    if K == 0 and target == 0:
        return True
    if K <= 0 or target <= 0:
        return False
    if dp[K][target] != -1:
        # Return memoized result if available
        return dp[K][target] == 1
    ans = False
    for i in range(N):
        # Try using each coin and recursively
        # check if it leads to a solution
        ans |= GFG(N, K - 1, target - coins[i], coins, dp)
    # Memoize the result and return it
    dp[K][target] = 1 if ans else 0
    return ans
# Function to make change using a given number of coins
def make_changes(N, K, target, coins):
    # Create a memoization table 'dp' to
    # store computed results
    dp = [[-1] * (target + 5) for _ in range(K + 5)]
    # Call the solve function with the initial parameters
    return GFG(N, K, target, coins, dp)
# Drivers code
if __name__ == "__main__":
    n1, k1, target1 = 4, 2, 9
    coins1 = [2, 3, 5, 7]
    print(make_changes(n1, k1, target1, coins1))
    n2, k2, target2 = 3, 4, 12
    coins2 = [1, 2,4, 6]
    print(make_changes(n2, k2, target2, coins2))





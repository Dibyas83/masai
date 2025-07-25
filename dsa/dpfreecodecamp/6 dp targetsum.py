
def subset_sum_recursive_dp(arr, n):
    """
    Finds if a subset of numbers in 'arr' sums to 'n' using dynamic programming
    with a recursive approach (memoization).

    Args:
        arr: The input array of numbers.
        n: The target sum.

    Returns:
        True if a subset sums to 'n', False otherwise.
    """
    memo = {}  # Dictionary to store results of subproblems (memoization)

    def solve(index, current_sum):
        # Base case 1: If the current_sum equals the target n, a subset is found.
        if current_sum == n:
            return True
        # Base case 2: If the current_sum exceeds n or all elements have been considered,
        # and the sum does not equal n, then no valid subset is found from this path.
        if current_sum > n or index == len(arr):
            return False

        # Check if the result for this subproblem is already memoized.
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        # Recursive step:
        # Option 1: Include the current element arr[index] in the sum.
        include_current = solve(index + 1, current_sum + arr[index])
        # Option 2: Exclude the current element arr[index] from the sum.
        exclude_current = solve(index + 1, current_sum)

        # Store the result in memoization table and return it.
        memo[(index, current_sum)] = include_current or exclude_current
        return memo[(index, current_sum)]

    # Start the recursive process from the first element and an initial sum of 0.
    return solve(0, 0)

# Example usage:
arr1 = [3, 34, 4, 12, 5, 2]
target1 = 9
print(f"Can a subset of {arr1} sum to {target1}? {subset_sum_recursive_dp(arr1, target1)}")

arr2 = [1, 5, 11, 5]
target2 = 10
print(f"Can a subset of {arr2} sum to {target2}? {subset_sum_recursive_dp(arr2, target2)}")

arr3 = [1, 2, 3]
target3 = 7
print(f"Can a subset of {arr3} sum to {target3}? {subset_sum_recursive_dp(arr3, target3)}")


#------------------------------------------

def subset_sum_dp(nums, target_sum):
    """
    Finds if a subset of numbers in 'nums' sums to 'target_sum' using dynamic programming,
    and returns one such subset if found.

    Args:
        nums (list): A list of integers.
        target_sum (int): The target sum to achieve.

    Returns:
        list: A list representing a subset that sums to target_sum, or None if no such subset exists.
    """

    # dp[i][j] will be True if a sum of j can be formed using elements from nums[0...i-1]
    # dp[j] will be True if a sum of j can be formed using elements considered so far
    dp = [False] * (target_sum + 1)
    dp[0] = True  # A sum of 0 can always be formed by choosing no elements

    # To reconstruct the path (subset), we'll store which element allowed us to reach a sum
    path = {}

    for num in nums:
        # Iterate backwards to avoid using the same element multiple times in the current iteration
        for current_sum in range(target_sum, num - 1, -1):
            if dp[current_sum - num]:
                if not dp[current_sum]:  # Only store path if this is the first time reaching current_sum
                    path[current_sum] = num
                dp[current_sum] = True

    if not dp[target_sum]:
        return None  # No subset found

    # Reconstruct the subset
    subset = []
    current_reconstruct_sum = target_sum
    while current_reconstruct_sum > 0:
        if current_reconstruct_sum in path:
            element = path[current_reconstruct_sum]
            subset.append(element)
            current_reconstruct_sum -= element
        else:
            # This case should ideally not be reached if dp[target_sum] is True
            # It implies an issue in path reconstruction logic or problem constraints
            break
    return sorted(subset) # Sort for consistent output


# Example Usage:
numbers = [2, 3, 7, 8, 10]
target = 11

result = subset_sum_dp(numbers, target)

if result:
    print(f"A subset summing to {target} is: {result}")
else:
    print(f"No subset found in {numbers} that sums to {target}")

numbers2 = [1, 5, 11, 5]
target2 = 11

result2 = subset_sum_dp(numbers2, target2)

if result2:
    print(f"A subset summing to {target2} is: {result2}")
else:
    print(f"No subset found in {numbers2} that sums to {target2}")

#-----------------------------------

def subset_sum(arr, target_sum):
    """
    Finds if a subset of numbers in arr sums to target_sum and returns one such subset.

    Args:
        arr (list): The input array of numbers.
        target_sum (int): The target sum to achieve.

    Returns:
        list: A list containing the numbers that form the target_sum, or None if no such subset exists.
    """
    n = len(arr)

    # dp[i][j] will be True if a subset of arr[:i] sums to j
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: an empty set can sum to 0
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current number is greater than the current sum j,
            # we cannot include it, so we take the value from the row above.
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # We can either exclude the current number (dp[i-1][j])
                # or include it (dp[i-1][j - arr[i-1]]).
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    # If dp[n][target_sum] is False, no subset sums to target_sum
    if not dp[n][target_sum]:
        return None

    # Reconstruct the subset
    result = []
    i, j = n, target_sum
    while i > 0 and j > 0:
        # If the sum was achieved without including arr[i-1], move to the previous row
        if dp[i - 1][j]:
            i -= 1
        # If the sum was achieved by including arr[i-1], add it to the result
        # and reduce the target sum
        else:
            result.append(arr[i - 1])
            j -= arr[i - 1]
            i -= 1

    return result[::-1]  # Return the subset in original order

# Example Usage:
# arr = [3, 34, 4, 12, 5, 2]
# target_sum = 9
# subset = subset_sum(arr, target_sum)
# if subset:
#     print(f"Numbers that sum to {target_sum}: {subset}")
# else:
#     print(f"No subset found that sums to {target_sum}")












def totalCost(mask, curr, n, cost, memo):
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)
    if mask == (1 << n) - 1:
        return cost[curr][0]

    # If the value has already been computed, return it
    # from the memo table
    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0:
            # If city i is not visited
            # Visit city i and update the mask
            ans = min(ans, cost[curr][i] +
                      totalCost(mask | (1 << i), i, n, cost, memo))

    # Memoize the result
    memo[curr][mask] = ans
    return ans


def tsp(cost):
    n = len(cost)

    # Initialize memoization table with -1
    # (indicating uncomputed states)
    memo = [[-1] * (1 << n) for _ in range(n)]

    # Start from city 0, with only city 0 visited initially (mask = 1)
    return totalCost(1, 0, n, cost, memo)


cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
res = tsp(cost)
print(res)




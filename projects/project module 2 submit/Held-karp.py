
N = 4
INF = float('inf')

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

dp = [[-1] * N for _ in range(1 << N)]

def tsp(mask, pos):
    if mask == (1 << N) - 1:  # 1111 = 4*4 - 1 = base case or end position
        return dist[pos][0]

    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = INF
    for city in range(N):
        if not (mask & (1 << city)):
            newAns = dist[pos][city] + tsp(mask | (1 << city), city)
            ans = min(ans, newAns)

    dp[mask][pos] = ans
    return ans

print(f"The minimum cost is {tsp(1, 0)}")








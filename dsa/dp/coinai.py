
def combinations_sum(n, k):
    dp = [([[] for _ in range(n + 1)]) for _ in range(k + 1)]

    dp[0][0] = [[]]

    for i in range(1, k + 1):
        for j in range(n + 1):
            for x in range(1, min(j, 9) + 1):
                for comb in dp[i - 1][j - x]:
                    dp[i][j].append(comb + [x])

    result = []
    for i in range(1, k + 1):
        result.extend(dp[i][n])

    return result

n= 10
k = 4
print(combinations_sum(n,k))

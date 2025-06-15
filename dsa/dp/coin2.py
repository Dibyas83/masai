def ways(n,c):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(len(c)):
        for j in range(c[i],n+1):
            dp[j] += dp[j-c[i]]

        print(c[i],dp)
    return dp[n]

n = 20
c = [i for i in range(1,10)]
print(ways(n,c))





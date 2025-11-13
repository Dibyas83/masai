
# n=3,len= 4   0,1,2,4 binary representation = 0,1,10,11  - count 1
# 011 - % 2 = 1 1 0=2

# using dp 1 = 01 = 1 + dp[0] = 1 + dp[n-1]
# using dp 2 = 10 = 1 + dp[0] = 1 + dp[n-2]
# using dp 3 = 10 = 1 + dp[1] = 1 + dp[n-2]

# using dp 4 = 0100 = 1 + dp[0] = 1 + dp[n-4]
# using dp 5 = 0101 = 1 + dp[1] = 1 + dp[n-4]
# using dp 6 = 0101 = 1 + dp[2] = 1 + dp[n-4]
# using dp 7 = 0101 = 1 + dp[3] = 1 + dp[n-4]

# using dp 8 = 1000 = 1 + dp[0] = 1 + dp[n-8]

# offset are imp points when they double like [1,2,4,8,16 ]

class Solut:
    def countbit(self, n: int) -> int:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp







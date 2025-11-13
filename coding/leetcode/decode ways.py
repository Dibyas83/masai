
# given a string of int ->ways to-> decode it into string of char
# 26 int are mapped 26 char
# 11106 can be mapped into aajf(1 1 10 6) and kjf(11 10 6)
# 06 != 6 or f, 10 = 10 or 1 j or i
"""
12131                          1               2              1
                         1          12
                    2     21            1
                1                   3       (31>26)

"""
# using cache of size n and store dp[i] = dp[i+1] + dp[i+2]
# method 1 recursive caching sol

class Sol:
    def numDecoding(self, s: str) -> int:

        dp = {len(s): 1}  # initialize cache mapped to one if their is empty string

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":  # base case
                dp[i] = 0
            else:
                dp[i]=dp[i+1]

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[
                i + 1] in "0123456")):  # it is double digit val if 1 and <=len(s)(0-9) or 2 and <= 6
                dp[i] += dp[i + 2]  # sub problem is double digit val
        return dp[0]

    def numDecoding2(self, s: str) -> int: # recursive
        dp = {len(s): 1}  # initialize cache mapped to one if their is empty string
        def dfs(i):  # the current position in list
            if i in dp: # i is in cache or it is the last no-base case
                return dp[i]
            if s[i] =="0": # base case
                return 0
            res = dfs(i+1) # currently we are within range and take the next combination
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")): # it is double digit val if 1 and <=len(s)(0-9) or 2 and <= 6
                res += dfs(i+2) # sub problem is double digit val
            dp[i] = res # caching it
            return res
        return dfs[0]










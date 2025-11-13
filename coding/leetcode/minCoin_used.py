

# use any given coin many times to reach target with min no of coin used
# 1 - using greedy by using max value of coin
# 2- using dfs backtracking  ,and keep record of repeating sub-pproblems so that we dont re-calculate it


#  if  [1,3,4,6] given and target is 8 . 8-6=2 if in list solved if not add to list remainder[],if not 8-4=4 if in list solved,

# target = list[8] from coins = [1,3,4,6] 8-6=2 if in list solved if not pop initial target, add to list target[],if not 8-4=4 if in list solved,
# target = [8,7,5,4,2] for i in target: if i in coins: yes ,else target.pop(i) target.append(i-(coins))

# method 3 use dp to store coins required to get  starting from min values


class Solut:
    def maxprodsubarr(self, coins: list[int],amt: int) -> int:
        dp = [amt + 1] * (amt * 1) # amt + 1 is the default val
        dp[0] = 0 # base for 0 val 0 coins

        for a in range(1, amt+1):
            for c in coins:
                if a -c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c]) # c and dp[3] if targ = 7 and coin is 4

        return dp[amt] if dp[amt] != amt + 1 else -1














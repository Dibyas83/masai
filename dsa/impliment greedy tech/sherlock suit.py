

def solve(coins,amt):
    dp = [amt+1] * (amt+1)
    # initialize with maximum ans
    print([amt + 1])
    print((amt + 1))
    dp[0] = 0
    for i in range(amt + 1): # price in first or curr shop
        for coin in coins:
            if coin <= i:
                print(coin,"coin")

                dp[i] = min(dp[i], 1 + dp[i - coin])

            else:
                break # if coin exceeds curr amt
    return dp

def main():
    t = int(input())
    coins = [1,2,5,10,20,50,100,200,500,2000]
    amt_dp = solve(coins,1000) # min coins needed for amts up to 10000
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split(" ")))
        ans = -1
        min_coins = float('inf')
        print(min_coins)
        print(amt_dp)
        for val in a:
            if amt_dp[val] < min_coins:
                ans = val
                min_coins = amt_dp[val]
            elif amt_dp[val] == min_coins:
                ans = min(ans,val) # in case of tie
        print(ans)

if __name__== "__main__":
    main()














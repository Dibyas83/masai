import math

def max_profit(prices):
    min_price = math.inf

    max_prof = 0
    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price
        if profit > max_prof:
            max_prof = profit
    return max_prof
def inpt():
    t = int(input())
    for _ in range(t):
        n = int(input())
        prics = list(map(int, input().split(" ")))
        print(max_profit(prics))

inpt()




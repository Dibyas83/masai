
# best time to buy a stock to maximize profits from a list of day prices
# two pointer, left - buy ,right - sell, right must be > left

class Solut:
    def maximize_profit(self,n: int, prices: list[int]) -> int:
        l,r = 0, # initialize
        maxprofit = 0
        while r < len(prices): # right pointr not passed the list of prices
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit,profit)
            else:
                l = r # if prices fall more below ,buy it from day after curr
            r += 1 # if increasing check to sell on next day
        return maxprofit






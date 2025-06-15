
val = [1,4,5,7]
wts = [1,3,4,5]

c = 5
cap =c+1
table = [[0 for _ in range(cap)] for _ in range(len(val))]


for ind in range(len(val)): #val is const
    for weight in range(1,cap): # for different capacity
        # differentiating-each cell gives max for cap of that col or cell
        if wts[ind] > weight:
            table[ind][weight] = table[ind-1][weight]
            continue
        # if the vlue is still less than the cap
        prior_val = table[ind-1][weight]
        #val of curitem +val of remaining weight
        # what we add to curr val is remaining weight as index that gives the value of prev row and remaining weight
        # in each cell we have values corresponding to that cap when col representing cap against the weight of items in wts

        newbestoption = val[ind] + table[ind-1][weight-wts[ind]]# for ind 0 it is 3 + (tab[-1][(0-5)-1]) for ind 1 its 6 + (tab[0][(0-5)-2])
        table[ind][weight] = max(prior_val, newbestoption)

sol_arr = []
for x in table:
    for y in x:
        sol_arr.append(y)
print(max(sol_arr))
"""
       
        if j == 0:
            table[ind][j] = 0
        elif ind == 0:
            table[ind][j] = table[ind][j-1] + w[j-1]
        else:
            table[ind][j] = max(table[ind-1][j], table[ind-1][j-1] + w[j-1])
"""

#cs dojo-----------------


def knsak(n,c1,arr,val,wts):


    if n == 0 or c1 == 0: # no items left or capacity over
        arr[n][c1]= 0
    if arr[n][c1] != -1:
        return arr[n][c1]
    tmp1 = 0

    if wts[n-1] <= c1:
        tmp1 = val[n - 1] + knsak(n - 1, c1 - wts[n - 1], arr, val,wts)  # val[n] means currr item is added to sack and capacity is reduced and
        # items to consider is lessened
    tmp2 = knsak(n-1,c1,arr,val,wts) # not puting in sack so item to consider is lessened ,capacity dont changes
    arr[n][c1] = max(tmp1,tmp2)
    return arr[n][c1]
    #arr[n][c1] = result
    #return result
def knapsack2(c1, val, wts):
    n = len(val)

    # Memoization table to store the results
    arr = [[-1] * (c1 + 1) for _ in range(n + 1)]

    return knsak(n,c1,arr,val,wts)

if __name__ == "__main__":
    val = [1, 4, 5, 7]
    n = len(val)
    wts = [1, 3, 4, 5]
    c1 = 5

    print(knapsack2(c1, val, wts))


#geek-----------
# Returns the maximum value that
# can be put in a knapsack of capacity c1
def knapsackRec(W, val, wt, n, memo):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # Check if we have previously calculated the same subproblem
    if memo[n][W] != -1:
        return memo[n][W]

    pick = 0

    # Pick nth item if it does not exceed the capacity of knapsack
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1, memo)

    # Don't pick the nth item
    notPick = knapsackRec(W, val, wt, n - 1, memo)

    # Store the result in memo[n][c1] and return it
    memo[n][W] = max(pick, notPick)
    return memo[n][W]

def knapsack(W, val, wt):
    n = len(val)

    # Memoization table to store the results
    memo = [[-1] * (W + 1) for _ in range(n + 1)]

    return knapsackRec(W, val, wt, n, memo)

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    c1 = 4

    print(knapsack(c1, val, wt))


# space optimized sinle dimensional
# Function to find the maximum profit
def knapsack(W, val, wt):
    # Initializing dp list
    dp = [0] * (W + 1)

    # Taking first i elements
    for i in range(1, len(wt) + 1):

        # Starting from back, so that we also have data of
        # previous computation of i-1 items
        for j in range(W, wt[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])
        print(dp)

    return dp[W]


if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))

#----------------------------

# Function to find the maximum profit
def knapsack(W, val, wt):
    # Initializing dp list
    dp = [0] * (W+1) # starts from index W  in loopso 1 is added

    # Taking first i elements
    for i in range(1, len(wt) + 1):

        # Starting from back, so that we also have data of
        # previous computation of i-1 items
        for j in range(W, wt[i - 1] - 1, -1): # -1 for making it reach beg element or last element
            print(dp[j],"dpj") # every row gives max val for using available weight of that index and before
            dp[j] = max(dp[j], val[i - 1] + dp[j - wt[i - 1]]) # val0= 1 + dp[4]=0 ,it will start find value when
            # j is min,exp i=2 ,j=5,4,3 when j=3
            print(dp[j])
        print("---------")
        print(dp)
        print(dp[W]) # w is the last index
    #print("----------------")
    #print(dp)


    return dp[W]


if __name__ == "__main__":
    val = [1, 4, 5, 7]
    wt = [1, 3, 4, 5]
    W = 5

    print(knapsack(W, val, wt))




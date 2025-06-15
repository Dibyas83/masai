def s(arr, n, sum):
    def subset_sum(n, sum):  # n changes ,sum or cap changes
        if sum == 0:  # bag is full sum reached 0 or no bag
            return True
        if n == 0 and sum != 0:  # no of items remaining is 0 and sum not reached
            return False
        else:  # not reached base condition
            currnum = arr[n - 1]
            if currnum <= sum:
                used_curr = subset_sum(n - 1, sum - currnum)
                notused_curr = subset_sum( n - 1, sum)
                return used_curr or notused_curr  # can we get answer from any route
            else:
                return subset_sum(n - 1, sum)

    return subset_sum(n, sum)

n= 5
arr = [1, 2, 3, 4, 5]
sum = 10
if s(arr, n, sum):
    print("Yes")

# dp ---------------------

def s(arr, n, sum):
    dp = {}
    def subset_sum(n, sum):  # n changes ,sum or cap changes
        if sum == 0:  # bag is full sum reached 0 or no bag
            return True
        if n == 0 and sum != 0:  # no of items remaining is 0 and sum not reached
            return False
        elif (n,sum) in dp:
            return dp[(n,sum)]
        else:  # not reached base condition
            currnum = arr[n - 1]
            if currnum <= sum:
                used_curr = subset_sum(n - 1, sum - currnum)
                notused_curr = subset_sum( n - 1, sum)
                c = used_curr or notused_curr  # can we get answer from any route
            else:
                c = subset_sum(n - 1, sum)
            dp[(n,sum)] = c
            return c

    return subset_sum(n, sum)

n= 5
arr = [1, 2, 3, 4, 5]
sum = 10
if s(arr, n, sum):
    print("Yes")

#optimize - by sorting num in asc or desc and seeing if any num not able to  form then rest
# nums after it will not be able to also

def s(arr, n, sum):
    dp = {}
    arr.sort(reverse=True)
    def subset_sum(n, sum):  # n changes ,sum or cap changes
        if sum == 0:  # bag is full sum reached 0 or no bag
            return True
        if n == 0 and sum != 0:  # no of items remaining is 0 and sum not reached
            return False
        elif (n,sum) in dp:
            return dp[(n,sum)]
        else:  # not reached base condition
            currnum = arr[n - 1]
            if currnum <= sum:
                used_curr = subset_sum(n - 1, sum - currnum)
                notused_curr = subset_sum( n - 1, sum)
                c = used_curr or notused_curr  # can we get answer from any route
            else: # items bigger will not give result
                c = 0
            dp[(n,sum)] = c
            return c

    return subset_sum(n, sum)

n= 5
arr = [1, 2, 3, 4, 5]
sum = 10
if s(arr, n, sum):
    print("Yes")


# using table iteration

def s(arr, n, sum):
    dp = [[0]*(sum + 1)  for _ in range(n)]
    for i in range(n):
        for j in range(sum + 1):
            curnum = arr[i]
            cursum = j
            if i == 0: # first row
                if cursum == 0 or curnum == cursum: # first cell or col
                    dp[i][j] = 1 # if cap is 0 ,by not including we can make it possible. but
                    # rest all will  be 0. ex we have weight 5 - 0 1 2 3 4 5 6 - gives - 1 0 0 0 0 1 0

            else:
                if curnum <= cursum:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curnum] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
    return dp[n - 1][sum]

n= 5
arr = [1, 2, 3, 4, 5]
sum = 10
if s(arr, n, sum):
    print("Yes")









# recuursive - we keep breaking big to small from which sol comes
def capsolve(n,cap,val,wt): # asuming these things wil give answer = global

    def solve(n,cap):
        if n==0 or cap == 0:
            return 0
        else:
            cwt = wt[n-1]
            cv = val[n-1]
            # condition 1-if cwt < cap, 2 - if to keep the curr item in bag or not
            if cwt <= cap:
                keep = cv + solve(n-1,cap-cwt)
                notkeep = solve(n-1,cap)
                return max(keep,notkeep)
            else:
                return solve(n-1,cap) # n-1 becuse items to consider has decreased
    return solve(n,cap)
# lets dp this

def capsolve(n, cap, val, wt):  # asuming these things wil give answer = global
    dp = {}

    def solve(n, cap):
        if n == 0 or cap == 0:
            return 0
        elif (n,cap) in dp:
            return dp[(n,cap)]
        else:
            cwt = wt[n - 1]
            cv = val[n - 1]
            # condition 1-if cwt < cap, 2 - if to keep the curr item in bag or not
            if cwt <= cap:
                keep = cv + solve(n - 1, cap - cwt)
                notkeep = solve(n - 1, cap)
                c =  max(keep, notkeep)
            else:
                c = solve(n - 1, cap)  # n-1 becuse items to consider has decreased
            dp[(n,cap)] = c # a tuple is created to store
            return c

    return solve(n, cap)


# iterative approach by tabulation in which we solve from small peices  to bigger like fibnaci
# make 2d array

def cap_iter_solve(n, cap, val, wt):  # asuming these things wil give answer = global
    dp = [[0]* (cap+1) for _ in range(n)]

    for i in range(n):
        for j in  range(cap+1):
            cap = j
            cwt = wt[i]
            cv = val[i]
            if i == 0:
                if j == 0:
                    dp[i][j] = 0
                else:
                    if cwt <= cap:
                        dp[i][j] = cv
                    else:
                        dp[i][j] = 0
            else:
                if cwt <= cap:
                    c1 = cv + dp[i-1][j-cwt]
                    c2 = 0 + dp[i-1][j]
                    dp[i][j] = max(c1,c2)
                else:
                    dp[i][j] = dp[i-1][j]
    return dp[n-1][cap]





















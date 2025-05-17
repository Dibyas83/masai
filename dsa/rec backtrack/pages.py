
def solve(n,m):
    if n <0:
        return float('inf')
    if n== 0: # no more moves needed
        return 0
    if m[n] != -1: # -1 for invalid path, no of moves on that page no,add nth no untill -1,per n has 10 or 12pages

        #print(m,"m")
        return m[n]  #  m store 10 or 12,returns page no after page turnover of 10 0r 12 pages
    print(solve(n-10,m),"10")
    print(solve(n-12,m),"12")
    m[n] = min(solve(n-10,m), solve(n-12,m)) + 1
    #print(n ,"min")
    return m[n]

tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())
    m = [-1]*(n+1)
    res = solve(n,m)
    print("ans",res if res != float('inf') else -1) # if result is infinity print -1













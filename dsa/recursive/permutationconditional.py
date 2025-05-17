

def masai_packers(k,n,arr,memo):
    if k== 0:
        return 1 #  if exact sum is acheived we found a valid combination
    if k < 0:
        return 0 # the sum becomes negetive
    if memo[k]!= -1:

        return memo[k] # if already computed, eturn the stored result

    ans = 0
    for i in range(n):
        ans += masai_packers(k - arr[i], n, arr, memo)
        print(ans) # 1 is minused 5 times
    print(memo[k])
    print(k)
    memo[k] = ans # store result in memorization array
    print(memo)
    return memo[k]
k,n = list(map(int,input().split(" ")))
arr = list(map(int,input().split(" ")))
memo = [-1]* (k+1)  # mememorization array initialized to -1
ans = masai_packers(k, n, arr, memo)
print(ans)











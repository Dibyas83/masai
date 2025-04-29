
def check(a,b,c,mid,k):
    return a*mid*mid + b*mid + c >= k

def solve(a,b,c,k):
    low = 0
    high = k

    ans = -1

    while low <= high:
        mid = (low + high) // 2
        print(high)
        print(low)
        print(mid)

        if check(a,b, c, mid, k):
            high = mid - 1
            ans = mid
        else:
            low = mid + 1

    if ans == 0:
        return -1
    else:
        return ans

def inp():
    t = int(input())
    for _ in range(t):

        a,b,c,k = list(map(int,input().strip().split(" ")))
        print(solve(a,b,c,k))

inp()







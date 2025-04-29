
def check(a,b,c,mid,k):
    return a*mid*mid + b*mid + c >= k

def solve(a,b,c,k):
    low = 0
    high = k
    ans =1
    if c > k:
        ans = -1

    while low < high:
        mid = low + ((high - low) // 2)
        print(high)
        print(low)
        print(mid)

        if a*mid*mid + b*mid + c > k:
            high = mid - 1
        else:
            low = mid + 1
            mid2 = low + ((high - low) // 2)
            if a * mid2 * mid2 + b * mid2 + c >= k:
                print(mid2)
                ans = mid2

    return ans


def inp():
    t = int(input())
    for _ in range(t):

        a,b,c,k = list(map(int,input().strip().split(" ")))
        print(solve(a,b,c,k))

inp()

"""

def check(a,b,c,mid,k):
    return a**mid + b*mid + c >= k
    
        if low == 1 and high == 2:
            ans = mid
            
            3 4 5 6
            2 7 6 3
"""

#-----------------------













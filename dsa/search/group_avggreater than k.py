


def avgchoc(n,k,arr,avg):
    if k <= avg[0]:
        return 0
    elif k > avg[n-1]:
        return n

    low = 0
    high = n-1
    while low <= high:
        mid = low + ((high-low)) // 2
        if avg[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return low

def inp():
    n = int(input())
    q = int(input())
    arr = list(map(int,input().split(" ")))
    arr.sort()
    sm = 0
    avg = [-1] * n

    for i in range(n):
        sm += arr[i]
        avg[i] = (sm / (i+1))

    for _ in range(q):
        k = int(input())
        print(avgchoc(n,k,arr,avg))
inp()











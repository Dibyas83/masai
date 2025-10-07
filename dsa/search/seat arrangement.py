
def ispossible(n,m,arr,mid):
    person = 1
    curr = arr[0] # 1st customer
    for i in range(n):
        if arr[i] - curr >= mid:
            person += 1
            curr = arr[i]
            if person >= m: # c is required no of people seats
                break
    return person >= m

def seatsavail(arr,m,n):
    low = 0
    high = arr[n-1] - arr[0] # max dist bet 1st and last seat
    while low <= high:
        mid = low + ((high-low)) // 2
        if ispossible(n,m,arr,mid):
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

def inp():
    n,m = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    arr.sort()
    print(seatsavail(arr, m, n))

inp()
"""
9 4
1 2 3 4 5 6 7 8 9
ans 2
9 6
1 2 3 4 5 6 7 8 9
a 1
"""















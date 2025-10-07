"""
n -machines = len(arr)
m items needed
arr = time req to produce 1 item by n machines
low = min time req
high = highest time req=slowest machine time * m items = end of array item
or

1,2,3,4,5,6,7 time taken
in 1 min they produce 1,1//2,1//3 items
m be 10
in 5 min they produce 5+5//2 + 5//3 + 5//4 + 5//5
"""
def ispossible(n,m,arr,mid):
    sm = 0
    for i in range(n):
        sm += mid // arr[i]  # how many items machine i  can produce in mid time  5//1= 5, 5//2= 2.5
    if sm == m:
        return mid
    elif sm > m:
        return sm >= m

def totaltime(arr,m,n):
    low = 1
    high = max(arr) * m
    while low <= high:
        mid = low + ((high-low)) // 2
        if ispossible(n,m,arr,mid): # sm >= m, more is produced
            high = mid -1 # to use less time
        else:
            low = mid + 1 # to inc time req
    print(high + 1)

def inp():
    n,m = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    totaltime(arr, m, n)


inp()



















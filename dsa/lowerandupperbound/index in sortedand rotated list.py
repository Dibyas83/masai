
def solve(n,arr):
    left = 0
    right = n-1
    while left < right:
        mid = left + (right -left) // 2
        if arr[mid] > arr[right]:  # 4567123 then this side has min in it
            le = mid + 1
        else:
           right = mid # or min is mid or to the left
    index = left
    if index == 0 and arr[0] < arr[n-1]: # if rotated
        return "NO"
    for i in range(1,index):
        if arr[i-1] > arr[i]: # if not in ascending
            return "NO"
    for i in range(index+1,n):
        if arr[i-1] > arr[i]:
            return "NO"
    if index > 0 and arr[-1] > arr[0]: # if rotated arr0> arr-1 ,inc order
        return "NO"
    return "YES"

n = int(input())
arr = list(map(int,input().split(" ")))
res = solve(n,arr)
print(res)












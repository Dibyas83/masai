
def solve(n,k,arr):
    low = 0
    high = n-1
    while low < high:
        mid = low + (high -low) // 2
        if arr[mid] > arr[high]:  # 4567123 then this side has min in it
            low = mid + 1
        else:
            high = mid # or min is mid or to the left
    return arr[low]













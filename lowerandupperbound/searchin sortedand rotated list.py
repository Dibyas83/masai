
def solve(n,k,arr):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        if arr[0] <= arr[mid]:  # then this side has max sorted nos
            if arr[0] <= k and k <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:   # then this side has max sorted nos
            if arr[mid] <= k and k <= arr[n-1]:
                high = mid - 1
            else:
                low = mid + 1
    return -1 # not found













pos = -1


def binary_search(arr1, n):
    low, high = 0, len(arr1) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr1[mid] == n:
            globals()['pos'] = mid
            print(pos)
            return True
        else:
            if arr1[mid] > n:
                low = mid+1
            else:
                high = mid-1
    return False


arr1 = [2,3,4,5,6,7,11,13,15,23,25,27,34,36,37]
n = 11
if binary_search(arr1,n):
    print( "found at-",pos+1)
else:
    print("not found")








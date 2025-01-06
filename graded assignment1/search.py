

def binary_search(arr1,key):

    low, high = 0, arr1[-1]
    while low <= high:
        mid = (low + high) // 2
        if mid == key:
            return mid

        if mid < key:
            low, high = (mid + 1, high)

        else:
            low,high = low,mid-1
    return -1


arr1 = [1, 2, 3, 4, 5, 6, 8, 11, 33, 66, 88, 89, 90, 777]
print(binary_search(arr1,66))





def find_first_last_count(arr, key):
    key = 8
    lst = [2, 4,5, 6, 8, 11, 22, 25, 31]
    low  , high = 0  , len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return - 1 # if not found after processes


nums_s = [1,2,3,4,5,6,8]
print(find_first_last_count(nums_s ,4))
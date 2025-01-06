key = 22
c=0
arr = [2, 4,5, 6,8, 8, 11, 16,22,22,22, 25,31]
low  , high = 0  , len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(mid)

    if arr[mid+1] == key:
        c += 1
        break

    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid -1


print(mid,mid+c,c)

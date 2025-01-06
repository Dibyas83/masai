target2 = 8
lst = [2, 4,5, 6, 8, 11, 16, 22, 25, 31]
low  , high = 0  , len(lst) - 1
while low <= high:
    mid = (low + high)//2
    if lst[mid] == target2:
        print(mid)
    elif lst[mid] < target2:
        low = mid + 1
    else:
        high = mid - 1
print("not")
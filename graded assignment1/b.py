cou = 0
target2 = 8
ind =0
lst = [2, 4,5, 6,8, 8, 11, 16, 22, 25,31]
low  , high = 0  , len(lst) - 1
 low <= high:
    mid = (low + high)//2
    if lst[mid] == target2:
        ind= mid

    elif lst[mid] < target2:
        low = mid + 1
    else:
        high = mid - 1
for i in range(len(lst)):
    if lst[ind+1] == target2:
        cou += 1
    else:
        break
print(ind,ind+cou,cou)
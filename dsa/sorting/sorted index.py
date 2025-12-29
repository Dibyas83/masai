def quicks(arr):
    if len(arr) <= 0:
        return arr
    else:
        mid = arr[0]
        less = [x for x in arr[1:] if x < mid]
        high = [x for x in arr[1:] if x >= mid]
        return quicks(less) + [mid] + quicks(high)


def sort_inde(ar1, K):
    arr_with_indices = list(enumerate(ar1))
    sorted_arr_with_indices = sorted(arr_with_indices,key=lambda x: x[1])
    sorted_indices = [index for index, value in sorted_arr_with_indices]
    pos = sorted_indices.index(K)
    return pos
T = int(input())
for i in range(T):
    N, K = map(int, input().split(" "))
    arr1 = list(map(int, input().split(" ")))
    res = sort_inde(arr1,K)
    print(res)


    print(arr1)
    num = arr1[K]
    li = quicks(arr1)
    print(li)
    index = li.index(num)
    print(index)
    ct = 0
    for i in range(N):
        if li[i] == num:
            print(ct)
        else:
            ct += 1



"""
1
7 2
4 2 5 6 1 8 4

"""

# nuss1 = [1, 2, 3, 5, 6, 11,15,22,26,34,46,54, 55,58,77,80,90, 100]
nuss1 = [1, 2, 3, 5, 55, 58, 77, 80, 90, 100]
target = 2
low, high = nuss1[0], nuss1[-1]
mid = len(nuss1) // 2
ind = mid
while True:
    print(mid)
    if nuss1[0] == target:
        print(0)
    if nuss1[-1] == target:
        print(-1)

    if nuss1[mid] == target:
        print(ind)
        break
    if nuss1[mid] < target:
        nuss1 = nuss1[(mid+1)::1]
        mid = len(nuss1) // 2
        print(mid)
        ind += mid
    elif nuss1[mid] > target:
        nuss1 = nuss1[0:(mid):1]  # 0,1,2,3,4    0,1
        mid = len(nuss1) // 2
        print(mid)
        ind -= mid  # 5-2 = 3  3-1=2

    else:
        print(-1)
        break
print("------------------------------------------------------2")
    # nuss1 = [1, 2, 3, 5, 6, 11,15,22,26,34,46,54, 55,58,77,80,90, 100]
nuss2 = [1, 2, 3, 5,10,11, 55, 58, 77, 80, 90, 100]
target = 80
low, high = nuss2[0], nuss2[-1]
# if len(nuss2)%2 == 0:

mid = len(nuss2) // 2
ind = mid
while low<high:
    print(mid)
    if nuss2[0] == target:
        print(0)
    if nuss2[-1] == target:
        print(-1)

    if nuss2[mid] == target:
        print(ind )
        break
    if nuss2[mid] < target:
        nuss2 = nuss2[(mid + 1)::1]
        mid = len(nuss2) // 2
        print(mid)
        ind += mid
    elif nuss2[mid] > target:
        nuss2 = nuss2[0:(mid-1):1]  # 0,1,2,3,4    0,1
        mid = len(nuss2) // 2
        print(mid)
        ind -= mid  # 5-2 = 3  3-1=2

    else:
        print(-1)
        break



























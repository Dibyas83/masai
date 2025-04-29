
def solve(arr,key):
    low = 0
    high = len(arr) -1
    sumv = 0
    ans = 0
    while low<= high:
        mid = int((low + high) / 2)
        print(low)
        print(high)
        print(mid)
        midval = arr[mid]
        if midval <= key:
            ans = mid + 1  # when  low > high it stops and ans of previous itr is ans
            low = mid + 1  # search in higher places

        else:
            high = mid - 1

    for i in range(0,ans):
        sumv += arr[i]

    print(str(ans) + " with total power" + str(sumv))
n = int(input())
array = []
while n:
    val = int(input())
    array.append(val)
    n = n-1
q = int(input())
array.sort()
print(array)
while q:
    keyx = int(input())
    solve(array,keyx) # test cases input
    q= q-1












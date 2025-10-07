
def binary(arr,k):
    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + (high - low)) // 2
        if arr[mid] == k:
            print("index = ",mid)
            return 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid+1
    return -1

def inpu():
    k = int(input())
    arr = list(map(int,input().split(" ")))
    print(binary(arr,k))

inpu()











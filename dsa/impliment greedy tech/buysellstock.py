
def solve(arr,n):
    left = 0
    right = 1
    maxprice = 0
    while right < n:
        if arr[left] < arr[right]:
            profit = arr[right] - arr[left]
            maxprice = max(profit,maxprice)
            print(arr[left],arr[right],"less") # if left is less only right increases
        else:# when more small is found
            left = right # two pointer
            print(arr[left], arr[right],"more")
        right += 1
    return maxprice

def inp():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split(" ")))
        print(solve(arr,n))
inp()











def solve(n,k,arr):
    mx = max(arr)
    mn = min(arr)
    minc = float('inf') # min overall cost
    print(minc,"init")
    minv = -1
    for i in range(mn,mx + 1):
        cost =  []
        for j in range(n):
            print(i,"i")
            print(arr[j],"arr[j")
            if arr[j]  > i:
                cost.append((arr[j]-i)*5)
            else:
                cost.append((i-arr[j])*3)
        print(cost,"unsorted")
        cost.sort()
        print(cost,"cost")
        sm = 0
        for a in range(k):
            sm += cost[a]
        print(sm,"sm")
        print(minc,"2")
        if sm < minc:
            minc = sm
            print(minc,"3")
        print(arr,"arr")
    print(minc,"minc")
def inp():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split(" "))
        arr = list(map(int,input().split(" ")))
        solve(n,k,arr)
inp()\











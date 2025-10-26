

m,n = list(map(int,input().split(" ")))
arr = list(map(int,input().split(" ")))
ct = 0
i = 0

while i < m:
    if arr[i] == 0:
        left = (i==0 or arr[i-1] == 0)
        right = (i==m or arr[i+1] == 0)
        if left and right:
            arr[i] = 1
            ct += 1
            i += 2
        else:
            i += 1
    else:
        i += 1

if ct >= n:
    print("yes")
else:
    print("no")











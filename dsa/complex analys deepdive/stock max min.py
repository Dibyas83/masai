

n = int(input())
arr = list(map(int,input().split(" ")))
max1 = 0
curr = 0
max_change = []
for i in range(n):
    curr += arr[i]
    if curr > max1:
        max1 = curr
print(max1)









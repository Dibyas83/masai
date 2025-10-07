
tot_sum = 0
n,m = map(int,input().split(" "))
for i in range(n):
    arr1 = list(input().strip())
    for j in range(m):
        if arr1[j] == "-":
            tot_sum += 1
        elif arr1[j] == "/":
            tot_sum += 2
print(tot_sum)











n,m =map(int,input().split(" "))
for i in range(n):
    arr1 = list(map(str,input()))
    for j in arr1:
        if j== "-":
            print("1", end= " ")
        elif j == "*":
            print("0", end= " ")
        else:
            print("2", end=" ")
    print()







n = int(input())
for i in range(n):
    arr1 = list(map(int,input().split(" ")))
    for j in range(n-1,-1,-1):  # flipping
        if arr1[j] == 0:
            print("1", end= " ")
        else:
            print("0", end= " ")
    print()










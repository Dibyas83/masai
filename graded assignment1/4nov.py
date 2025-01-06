N = 2
M = 2
arr = [[2,3],[6,7]]
# multi_list = [[0 for j in range(M+2)] for i in range(N+2)]
a = [[0] * M] * N
for i in range(M):
    sam = " "
    for j in range(N):
        sam += str(arr[i][j])+" "
    print(sam)

print("------------------------=================1")

M,N=2,3
arr = [[2,3,4],[6,7,5]]
for i in range(M):
    sam = 0
    for j in range(N):
        if arr[i][j]%2 == 1:
            sam += arr[i][j]
    print(sam)
print("----------------------2")
for i in range(N):
    bag = ""
    for j in range(M):
        bag += str(i+j)+" "
    print(bag)

print("---------------------3")
j=4
k=3
matrix= [[2,3,4],[4,5,6],[6,7,4],[5,3,4]]
for i in range(j):
    if i%2 == 0:
        for j in range(k-1,-1,-1):
            print(matrix[i][j],end=" ")
    else:
        for j in range(0,k):
            print(matrix[i][j],end=" ")

print("-----------------------4")




# level 2
#
print("==============")



# 2
arr = [[2,3,4],[6,7,5]]
N,M=2,2
sum1 = 0
for i in range(N):
    for j in range(M+1):
        if j == 0 or j == M:
            sum1 += arr[i][j]
            print(sum1)
print(sum1)
print("-------------------------------88")
# 3

print("-------------------5")
#4















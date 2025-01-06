

arr = [3,5,1,10,8]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]*2 == arr[j]:

            print("yes")
            break
        else:
            print("no")

N = 3
M = 2
# multi_list = [[j for j in range(M+1)] for i in range(N+1)]
res = [0][0]
bag = [[0,0],[0,0],[0,0]]
for i in range(N):
    bag = ""
    for j in range(M):
        res += str(res[i][j]) + " "
    print(res)
print()











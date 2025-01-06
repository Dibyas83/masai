N =4
M = 3
matrix = []
count = 0
for j in range(1,N):
    for i in range(1,M):
        count += 1
        matrix.append(count)

       # matrix.append(count)
    #print(count ,end=" ")
    print(matrix)
print()

N =3
M = 2
bag = ""
count = 0
arr = [[1,2],[3,4],[7,8]]
for i in range(N):
    bag = ""
    for j in range(M):

        bag += str(arr[i][j])+" "
        print(bag)
    print(bag)

        #print(bag)

N =3
M = 2
bag = 0
count = 0
arr = [[1,2],[3,4],[7,8]]
for i in range(N):
    bag = 0
    for j in range(M):

        bag += arr[i][j]
        #print(bag)
    print(bag)


arr = [[2,3,4],[6,7,5]]
N,M=2,2
sum1 = 0
for i in range(N):
    for j in range(M+1):
        if j == 0 or j == M:
            sum1 += arr[i][j]
            print(sum1)
print(sum1)






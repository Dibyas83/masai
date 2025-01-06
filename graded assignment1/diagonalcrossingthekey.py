

matrix= [[2,3,4],
         [4,5,6],
         [6,7,4],
         [5,3,4]]
r = 4
c =3
k= 6
row = -1 # indexes of k
col =-1
d2row = -1
d2col = -1
for i in range(r):
    for j in range(c):
        if matrix[i][j] == k:
            row = i # found k indixes
            col = j
            d2col = j # for right to left dia indexes
            d2row = i
print(row,col)
while row != 0 and col != 0:# from key to top right ,untill both col and row will be 0
    row -= 1
    col -= 1
while row != r and col != c: # from key to bottom right
    print(matrix[row][col],end=" ")
    row += 1
    col += 1
print()
while d2row!=0 and d2col!=c-1: # find top right corner element , from where we start
    d2row -= 1
    d2col += 1
print(d2row,d2col)
while d2row!=r and d2col!=-1: # from above point to bottom left
    print(matrix[d2row][d2col],end=" ")
    d2row += 1 # starts traveling to bottom left
    d2col -= 1
print(matrix[0][-1])
print(matrix[0][c-1])

print("---------------------------")

# def dag_cross(matrix,ro,co,ik):








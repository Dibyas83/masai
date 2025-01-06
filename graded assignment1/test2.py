





rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter the entries rowwise:")

for i in range(rows):
    a =[]
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)
    print(a)
print(matrix)
print("The Matrix is:")
for i in range(rows-1):
    for j in range(cols):
        print(matrix[i][j], end = " ")
    print()


"""Add Two Matrices in Python Using User Input
To add two matrices in Python using user input, you first need to take two matrices as input and then add them element-wise:
"""

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the entries for the first matrix:")
matrix1 = [[int(input()) for x in range(cols)] for y in range(rows)]
print("Enter the entries for the second matrix:")
matrix2 = [[int(input()) for x in range(cols)] for y in range(rows)]

result = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print("Resultant Matrix:")
for r in result:
    print(r)

input_list11 = [1,2,8,4,5,2,5,4,1]
mydict = {}
for v in input_list11:
    if v not in mydict.keys():
        mydict[v] = 1
        print(mydict[v])
    else:
        mydict[v] += 1
print(mydict)





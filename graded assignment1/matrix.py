Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix1 = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row):
    a = []
    # A for loop for column entries
    for column in range(Column):
        a.append(int(input()))
    matrix1.append(a)
print(matrix1)


matrix2 = [][]
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix2[row][column], end=" ")
    print()

matrix2 = [[column for column in range(4)] for row in range(4)]

print(matrix2)
















# A basic code for matrix input from user

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
grid = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(input())
    grid.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(grid[i][j], end = "")
    print()


"""

# A basic code for matrix input from user

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    b = map(str,input().split(" "))
    a.append(b)

    matrix.append(a)
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end="")
        print()

"""












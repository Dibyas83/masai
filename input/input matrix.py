
"""
MATRIX a user input matrix in different ways. Some of the methods
for user input matrix in Python are shown below:
"""
# A basic code for matrix input from user

R = int(input("Enter the number of rows"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

"""
Using map() function and Numpy. In Python, there exists a popular library called NumPy. 
"""
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

        # User input of entries in a 
        # single line separated by space
entries = list(map(int, input().split(" ")))

        # For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)

"""
To take an input matrix from a user in Python, you can use nested lists and take input using a loop. 
Here’s an example of how to take a matrix input from a user:
"""

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter the entries rowwise:")

for i in range(rows):
    a =[]
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)

print("The Matrix is:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end = " ")
    print()









# one-liner logic to take input for rows and columns
mat = [[int(input()) for x in range (C)] for y in range(R)]
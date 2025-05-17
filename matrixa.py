

# Using nested lists
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
element = matrix_a[1][2] # Accesses the element in the 2nd row and 3rd column (value is 6)

# Modifying elements
matrix_a[0][0] = 10 # Changes the element in the 1st row and 1st column to 10

# Matrix operations using nested loops
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = []

for i in range(len(matrix_a)):
    row_sum = []
    for j in range(len(matrix_a[0])):
        row_sum.append(matrix_a[i][j] + matrix_b[i][j])
    result_matrix.append(row_sum)

# Using NumPy
import numpy as np

matrix_np_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_np_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix addition
result_matrix_np_add = matrix_np_a + matrix_np_b

# Matrix multiplication
result_matrix_np_multiply = np.dot(matrix_np_a, matrix_np_b)
"""
Creating a simple matrix using Python
Method 1: Creating a matrix with a List of list
A Matrix is fundamentally a 2D list therefore we can create a Matrix by creating a 2D list (list of lists).

"""


mat = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

print("Matrix =", mat)
"""
Output
Matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Method 2: Take Matrix input from user in Python
In this example we are going to take user inputs for rows and columns for the matrix and then print the complete matrix.
"""

rows = int(input("rows: "))
col = int(input("columns: "))

matrix = []
print("entries row-wise:")

for i in range(rows):
    row = []
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix.append(row)  # adding rows to the matrix

print("\n2D matrix is:")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
"""
Output:

Enter the number of rows: 2
Enter the number of columns: 2
Enter the entries row-wise:
1
2
3
4

The 2D matrix is:
1 2
3 4
Method 3: Create a matrix using list comprehension
List comprehension is an elegant way to define and create a list in Python, we are using the range function for printing 4 rows and 4 columns.
"""



matrix = [[col for col in range(4)] for row in range(4)]
print(matrix)
"""
Output
[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
Explanation:

Outer loop (for row in range(4)) runs 4 times to create 4 rows.
Inner loop (for col in range(4)) fills each row with values 0 to 3.
Assigning Value in a matrix
Method 1: Assign value to an individual cell in Matrix
Here we are replacing and assigning value to an individual cell (1 row and 1 column = 11) in the Matrix.
"""



x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x[1][1] = 11

print(x)
"""
Output
[[1, 2, 3], [4, 11, 6], [7, 8, 9]]
Method 2: Using Negative Indexing
We are assigning a value to an individual cell using negative indexing in this example (-2 row and -1 column = 21) in the Matrix.

"""


x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x[-2][-1] = 21  # row = -2 , column = -1
print(x)
"""
Output:

[[1, 2, 3], [4, 5, 21], [7, 8, 9]]
Accessing Value in a matrix
Method 1: Direct Indexing
We can access elements of a Matrix by using its row and column index.
"""

print("Element at (1,3):", x[0][2])
print("Element at (3,3):", x[2][2])
"""
Output:

Element at (1,3): 3
Element at (3,3): 9
Method 2: Negative Indexing
Here, we are accessing elements of a Matrix by passing its row and column on negative indexing.
"""

print(x[-1][-2])
"""
Output:

8
Mathematical Operations with Matrix in Python
Example 1: Addition Using Loops
Let’s see how we can add two matrices using for-loop in Python.
"""

x = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
y = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
res = [[0]*3 for _ in range(3)]

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] + y[i][j]

for r in res:
    print(r)
"""

[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
Example 2: Addition & Subtraction with List Comprehension
Performing the Basic addition and subtraction using list comprehension.

"""
x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

y = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]

# Matrix addition
add_res = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

# Matrix subtraction
sub_res = [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


print("Matrix Addition:")
for row in add_res:
    print(row)

print("\nMatrix Subtraction:")
for row in sub_res:
    print(row)
"""
Output:

Matrix Addition
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]


Matrix Subtraction
[-8, -6, -4]
[-2, 0, 2]
[4, 6, 8]
Example 3: Python program to multiply and divide two matrices
Performing the basic multiplication and division of two matrices using Python loop.
"""

x = [[2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]]

y = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Element-wise multiplication
mult_res = [[x[i][j] * y[i][j] for j in range(3)] for i in range(3)]

# Element-wise integer division
div_res = [[x[i][j] // y[i][j] for j in range(3)] for i in range(3)]

print("Matrix Multiplication:")
for row in mult_res:
    print(row)

print("\nMatrix Division:")
for row in div_res:
    print(row)
"""
Output:

Matrix Multiplication:
[2, 8, 18]
[32, 50, 72]
[98, 128, 162]

Matrix Division:
[2, 2, 2]
[2, 2, 2]
[2, 2, 2]
Transpose of a Matrix
Example 1: Using loop
Transpose of a matrix is obtained by changing rows to columns and columns to rows. In other words, transpose of A[][] is obtained by changing A[i][j] to A[j][i].
"""



x = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
transpose = [[0]*3 for _ in range(3)]

for i in range(len(x)):
    for j in range(len(x[0])):
        transpose[j][i] = x[i][j]

for r in transpose:
    print(r)
"""
Output
[9, 6, 3]
[8, 5, 2]
[7, 4, 1]
Example 2: Using List Comprehension
Here’s how to Transpose a matrix using list comprehension.
"""



transpose = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
for row in transpose:
    print(row)
"""
Output:

[9, 6, 3]
[8, 5, 2]
[7, 4, 1]
NumPy Matrix Operations
Creating a Matrix with Random Values
Here we are creating a Numpy array using numpy.random and a random module.
"""

import numpy as np

arr = np.random.randint(10, size=(3, 3))
print(arr)
"""
Output:

[[2 7 5]
 [8 5 1]
 [8 4 6]]
Explanation:

The numpy.random module is used to generate random numbers.
np.random.randint(10, size=(3, 3)) creates a 3×3 matrix with random integers from 0 to 9.
Basic Math Operations with NumPy
Here we are covering different mathematical operations such as addition, subtraction, multiplication, and division using Numpy.


"""

import numpy as np

x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

print("Addition:\n", np.add(x, y))
print("Subtraction:\n", np.subtract(x, y))
print("Multiplication:\n", np.multiply(x, y))
print("Division:\n", np.divide(x, y))
"""
Output
Addition:
 [[ 8 10]
 [13 15]]
Subtraction:
 [[-6 -6]
 [-5 -5]]
Multiplication:
 [[ 7 16]
 [36 50]]
Division:
 [[0.14285714 0.25      ]
 [0.44444444 0.5       ]]
Dot and cross product with Matrix
In this example, we are going to discuss how we can calculate the dot and the cross products of two matrices using NumPy, it provides built in functions to calculate them. First, let’s discsuss what are dot and cross products in short:

Dot Product: Calculates the sum of the products of corresponding elements, often used to find projections or perform matrix multiplication.
Cross Product: Produces a vector perpendicular to two 3D vectors, useful in physics for torque, angular momentum, etc.

"""

import numpy as np

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Dot Product:\n", np.dot(x, y))
print("Cross Product:\n", np.cross(x, y))
"""
Output
Dot Product:
 [[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
Cross Product:
 [[-10  20 -10]
 [-10  20 -10]
 [-10  20 -10]]
Transpose Using NumPy
To perform transpose operation in matrix we can use the numpy.transpose() method.

"""


import numpy as np

matrix = [[1, 2, 3], [4, 5, 6]]
print(np.transpose(matrix))
"""
Output
[[1 4]
 [2 5]
 [3 6]]
Creating Empty Matrices
Initializing an empty array, using the np.zeros().
"""



import numpy as np

a = np.zeros((2, 2), dtype=int)
print("2x2 Matrix:\n", a)

b = np.zeros((3, 3))
print("3x3 Matrix:\n", b)
"""
Output
2x2 Matrix:
 [[0 0]
 [0 0]]
3x3 Matrix:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Slicing in Matrix using Numpy
Slicing is the process of choosing specific rows and columns from a matrix and then creating a new matrix by removing all of the non-selected elements.

"""


import numpy as np

x = np.array([[6, 8, 10],
              [9, -12, 15],
              [12, 16, 20],
              [15, -20, 25]])

print("Full Matrix:\n", x)
print("Third Row, Second Column:", x[2:3, 1])
print("Third Row, Third Column:", x[2:3, 2])
"""
Output
Full Matrix:
 [[  6   8  10]
 [  9 -12  15]
 [ 12  16  20]
 [ 15 -20  25]]
Third Row, Second Column: [16]
Third Row, Third Column: [20]
Deleting Rows with NumPy
Here, we are trying to delete rows using the np.delete() function. In the code, we first tried to delete the 0th row, then we tried to delete the 2nd row, and then the 3rd row.
"""



import numpy as np

a = np.array([[6, 8, 10],
              [9, -12, 15],
              [12, 16, 20],
              [15, -20, 25]])

print("Delete 0th Row:\n", np.delete(a, 0, axis=0))
print("Delete 1st Row:\n", np.delete(a, 1, axis=0))
"""
Output
Delete 0th Row:
 [[  9 -12  15]
 [ 12  16  20]
 [ 15 -20  25]]
Delete 1st Row:
 [[  6   8  10]
 [ 12  16  20]
 [ 15 -20  25]]
Add Rows or Columns to a NumPy Array
We can easily add a new row or column to an existing NumPy array using stacking functions like np.hstack() (horizontal stack) and np.vstack() (vertical stack).

Here’s how to add a column to an existing 2D array:

"""


import numpy as np

x = np.array([[6, 8, 10],
              [9, -12, 15],
              [15, -20, 25]])

# new column to be added
col = np.array([1, 2, 3])

# add the column (after reshaping it into a column vector)
res = np.hstack((x, np.atleast_2d(col).T))

print("Resultant Array:\n", res)
"""
Output
Resultant Array:
 [[  6   8  10   1]
 [  9 -12  15   2]
 [ 15 -20  25   3]]

#-----------------
numpy.matrix() in Python
Last
Updated: 0
9
Mar, 2022
This


class returns a matrix from a string of data or array-like object.Matrix obtained is a specialised 2D array.


Syntax:

numpy.matrix(data, dtype=None):
Parameters:

data: data
needs
to
be
array - like or string
dtype: Data
type of returned
array.

Returns:

data
interpreted as a
matrix
"""
# Python Program illustrating
# numpy.matrix class

import numpy as geek

# string input
a = geek.matrix('1 2; 3 4')
print("Via string input : \n", a, "\n\n")

# array-like input
b = geek.matrix([[5, 6, 7], [4, 6]])
print("Via array-like input : \n", b)
"""
Output:

Via
string
input:
[[1 2]
 [3 4]]


Via
array - like
input:
[[[5, 6, 7][4, 6]]]

References:
https: // docs.scipy.org / doc / numpy / reference / generated / numpy.mat.html  # numpy.mat

Note:
These
codes
won’t
run
on
online
IDE’s.Please
run
them
on
your
systems
to
explore
the
working

#----------------
"""
"""
Adding and Subtracting Matrices in Python
Last Updated : 25 Apr, 2023
In this article, we will discuss how to add and subtract elements of the matrix in Python. 

Example:

Suppose we have two matrices A and B.
A = [[1,2],[3,4]]
B = [[4,5],[6,7]]

then we get
A+B = [[5,7],[9,11]]
A-B = [[-3,-3],[-3,-3]]
Now let us try to implement this using Python 

1. Adding elements of the matrix

In the above code, we have used np.add() method to add elements of two matrices. If shape of two arrays are not same, that is arr1.shape != arr2.shape, they must be broadcastable to a common shape (which may be the shape of one or the other).


"""

# importing numpy as np
import numpy as np
 
 
# creating first matrix
A = np.array([[1, 2], [3, 4]])
 
# creating second matrix
B = np.array([[4, 5], [6, 7]])
 
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
 
# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))
"""
Output:

Printing elements of first matrix
[[1 2]
 [3 4]]
Printing elements of second matrix
[[4 5]
 [6 7]]
Addition of two matrix
[[ 5  7]
 [ 9 11]]
2. Subtracting elements of matrices

In the above code, we have used np.subtract() to subtract elements of two matrices. It returns the difference of arr1 and arr2, element-wise.

"""


# importing numpy as np
import numpy as np
 
 
# creating first matrix
A = np.array([[1, 2], [3, 4]])
 
# creating second matrix
B = np.array([[4, 5], [6, 7]])
 
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
 
# subtracting two matrix
print("Subtraction of two matrix")
print(np.subtract(A, B))
"""
Output:

Printing elements of first matrix
[[1 2]
 [3 4]]
Printing elements of second matrix
[[4 5]
 [6 7]]
Subtraction of two matrix
[[-3 -3]
 [-3 -3]]
METHOD 3:Using nested loops

APPROACH:

The given task is to subtract two matrices in Python and print their elements. Approach 2 uses nested loops to subtract the two matrices. It prints the elements of both matrices using nested loops and then subtracts the corresponding elements of the matrices to get the result matrix.

ALGORITHM:

1. Define two matrices matrix1 and matrix2.
2.Print the elements of matrix1 and matrix2 using nested loops.
3. Define an empty matrix result of the same size as matrix1.
4. Subtract the corresponding elements of matrix1 and matrix2 using nested loops and store the result in the result matrix.
5. Print the result matrix.

"""


# Input matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
 
# Printing elements of matrix1
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
 
# Printing elements of matrix2
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
 
# Subtracting two matrices
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
 
# Printing the result
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()
"""
Output
Printing elements of first matrix
1 2 
3 4 
Printing elements of second matrix
4 5 
6 7 
Subtraction of two matrix
-3 -3 
-3 -3 
Time complexity:

1. The time complexity of printing the matrices using nested loops is O(n^2), where n is the size of the matrices.
2. The time complexity of subtracting two matrices using nested loops is also O(n^2).
3. Therefore, the overall time complexity of this approach is O(n^2).
 

Space complexity:

1.The space complexity of this approach is O(n^2), as it requires three matrices of size n^2. The input matrices matrix1 and matrix2 require a space of n^2 each, and the result matrix requires a space of n^2.
"""

"""
Python

# Using nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using list comprehension
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
Accessing Elements
Elements in a 2-D array are accessed using two indices: the row index and the column index.
Python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])  # Output: 2 (element at row 0, column 1)
print(matrix[2][0])  # Output: 7 (element at row 2, column 0)
Iterating Through 2-D Arrays
Nested loops are commonly used to iterate through all elements of a 2-D array.
Python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9
Modifying 2-D Arrays
Elements in a 2-D array can be modified by assigning new values to specific positions.
Python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][2] = 10  # Change element at row 1, column 2 to 10
print(matrix)  # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
"""





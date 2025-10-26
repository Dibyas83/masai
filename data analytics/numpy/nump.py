

# it is written in c so it is fast

import numpy

import numpy as np

print(np.__version__)

lii = [1,2,3,4,5]
lii = np.array(lii) # numpy.array(lii)
print(lii,type(lii))
print(lii.ndim)
lii = lii * 5
print(lii)
print("----------------------3d")
li = [1,2,3,4]
li2d =  np.array([[1,2,3,4,5],[3,4,5,6,7],[4,7,9,11,22]])
li3d =  np.array([[['A','B','C','D','Y'],['A','U','M','D','N']],
                  [[1,2,3,4,5],[3,4,5,6,7]],
                  [[1,2,3,4,5],[3,4,5,6,7]]])
print(li3d.shape)   # 3d, 2 row, 5 col
print(li3d[0][1][4]) # chain indexing
print(li3d[0,0,3]) # multidimensional indexing
WORD = li3d[0,0,1] + li3d[0,0,4] + li3d[0,1,1]
print(WORD)
# row selection
print(li2d[1])
print(li2d[-1])
print(li2d[1:4])
print(li2d[0:4:2])   # 2 is steps
print(li2d[::2])   # 2 is steps
print(li2d[::-1])   # reversed
print(li2d[::-2])   # reversed
print("------------------------col")
# col selection
print(li2d[1,1]) # row 1,col 1
print(li2d[:,1]) # row all,col 1
print(li2d[:,-2]) # row all,col -2
print(li2d[:,0:3]) # row all,col 0 t0  3
print(li2d[:,1:]) # row all,col 1 t0  .....
print(li2d[:,::2]) # row all, every 2nd col 1st, 3rd,5th
print(li2d[:,1::2]) # row all, every 2nd col from col 1 2nd, 4th
print(li2d[:,::-1]) # row all, reverse
print(li2d[:,::-2]) # row all, reverse every 2nd col
print(li2d[0:2,0:2]) #firsy 2 col of first two rows
print(li2d[0:2,2:]) #last 2 col of first two rows
print(li2d[2:, 0:2]) # 1st 2 col of last two rows
print(li2d[2:, 2:]) # last 2 col of last two rows

# scaler math

#print(li + 2)
print(lii + 4)
print(lii - 2)
print(lii * 6)
print(lii / 2)
print(lii ** 2)

# vectorised math func
# vector is single dimensional
print(np.sqrt(lii))
print(np.round(lii))
print(np.pi) # constant
radius1 =  np.array([1,2,3])
print(np.pi * radius1 ** 2)

# element-wise arithmetic

rad1 =  np.array([1,2,3])
rad3 =  np.array([2,2,2])
rad2 =  np.array([3,8,9])
print(rad1 + rad2)
print(rad1 - rad2)
print(rad1 * rad2)
print(rad1 / rad2)
print(rad1 ** rad3) # [1 4 9]

# comparison operator

print(lii == 4) # boolean
print(lii >= 4)
lii[lii < 3] = 0  # if less than 3 it is assigned 0

# broadcasting allows numpy to perform operations on arrays with different shapes
# by virtually expanding dimensions,so they match the larger arrays shape.
# no of rows or col match or either of them is 1
ar1  = np.array([[1,2,3,4]]) # 2d array
ar2  = np.array([[1],[2],[3],[4]])
print(ar1.shape)  # 1,4
print(ar2.shape) # 4,1
print(ar1 * ar2)

print("-------------------------------broadcasting")

# aggregate func - summarize data and typically return a single value


li = li * 5
print(li)

lii2 = [3,4,5,6,7]
lii3 = [3,4,5,6,7]
print(lii2+lii3)
print(lii2+lii)  # lii is already numpy

print(np.array(lii3) + np.array(lii2))

list1 = []
for i in range(len(lii3)):
    list1.append(lii3[i] + lii2[i])

print(np.array([1,2,3]))
print(np.zeros((2,2)))
print(np.arange(5)) # can use floating point value
print(list(np.arange(5))) # can use floating point value
print(list(np.arange(1,5.5,0.5)))#print(f)
print(list(np.arange(1,5.5,0.5)))#print(f)
print(np.arange(1, 5.5,0.5))#print(f)
arr1 = np.array([10,20,30])
print(arr1)

l4 = []
for i in list1:
    l4.append(i*2)
print(l4)
print(np.std(lii))  # standard deviation - measure of spread
print(np.var(lii))  # square of standard deviation
print(np.argmin(lii))  # gives position or index no of min
print(np.argmax(lii))  # gives position or index no of max
li2d2 =  np.array([[1,2,3,4,5],[3,4,5,6,7],[4,7,9,11,22]])
print(np.sum(li2d2, axis=0)) # sum by col
print(np.sum(li2d2, axis=1)) # sum by row

# filtering - that match a given condition
ages =  np.array([[21,12,13,14,15],[23,24,25,26,17],[14,17,19,11,22]]) # ages of 3 groups

teens = ages[ages < 18] # boolean indexing
senio = ages[(ages >= 18) & (ages < 25)] # boolean indexing
adu = ages[(ages < 18) & (ages >= 25)] # boolean indexing
print("teens",teens)
evensage = ages[ages % 2 == 0]
print(evensage)

adults = np.where(ages >= 18, ages, 0) # 0 fill value if condition not satisfying
print(adults)
# random no generator

rng1 = np.random.default_rng(seed=1) # will generate same random no
print(rng1.integers(1,7,size=4))
print(rng1.integers(1,7,size=(4,2))) # 2d array 4 rows 2 cols

# floatin point no
print(np.random.uniform(low=-1,high=1, size =(3,2))) # uniform means uniform distribution each ele has equal chance of being selected
# gives a random floating point no bet 0-1,can give range,size
np.random.seed(seed=1)

# shuffling array
print("-----------------------------shufle")
l1 =  np.array([1,2,3,4,5])
randno = rng1.choice(l1,size = 2)
randno = rng1.choice(l1,size = (3,2))
rng1.shuffle(l1)
print(l1)
print(randno)



a = np.ones((3,3)) # 3/3 array
b = a + [3,4,5]
print("b",b)
print(np.max(b,axis = 0)) # max o each col
print(numpy.max(b,axis = 1)) # max of row
print(numpy.max(b))

n = np.zeros((3,3))
n[1,1] = 1
print(n)
kk = np.sum(b)
kk1 = np.max(b)
kk11 = np.max(b,axis = 0)
kk12 = np.max(b,axis=1) # max of row
kk2 = np.mean(b)
print(kk,kk1,kk2)
print(kk11,kk12)


x = np.matrix(np.arange(12).reshape((3,4)));
print(x)

print(x.getA())

"""
NumPy is a fundamental library in Python for numerical computing, providing powerful tools for working with 
arrays and matrices. While NumPy offers a dedicated np.matrix class, it is generally recommended to use np.ndarray 
for matrix operations due to its broader applicability and the potential deprecation of np.matrix in future versions.
Here are some common matrix operations using NumPy's np.ndarray:


1. Creating Matrices:
Matrices are typically created as 2D NumPy arrays using np.array().
Python
"""

# Create a 2x2 matrix
matrix_a = np.array([[1, 2], [3, 4]])

# Create a 3x3 matrix
matrix_b = np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
"""
2. Basic Arithmetic Operations (Element-wise):
These operations apply to corresponding elements of matrices of the same shape.
Python
"""
# Addition
result_add = matrix_a + matrix_a

# Subtraction
result_sub = matrix_a - matrix_a

# Element-wise multiplication
result_elem_mul = matrix_a * matrix_a

# Element-wise division
result_elem_div = matrix_a / matrix_a
"""
3. Matrix Multiplication:
NumPy offers several ways to perform matrix multiplication, adhering to the rules of linear algebra.
Python
"""
# Using np.dot()
result_dot = np.dot(matrix_a, matrix_a)

# Using np.matmul()
result_matmul = np.matmul(matrix_a, matrix_a)

# Using the @ operator (Python 3.5+)
result_at_op = matrix_a @ matrix_a
"""
4. Transpose:
The transpose of a matrix can be obtained using the .T attribute.
Python
"""
transpose_a = matrix_a.T
"""
5. Inverse:
The inverse of an invertible square matrix can be found using np.linalg.inv().
Python
"""
inverse_a = np.linalg.inv(matrix_a)
"""
6. Determinant:
The determinant of a square matrix can be calculated using np.linalg.det().
Python
"""
determinant_a = np.linalg.det(matrix_a)
"""
7. Other Useful Operations:
np.zeros(): Create a matrix filled with zeros.
np.ones(): Create a matrix filled with ones.
np.identity(): Create an identity matrix.
np.max(), np.min(), np.sum(), np.mean(): Statistical operations.
flatten(): Return a flattened copy of the matrix.
"""
print("=================================================")

# importing numpy for matrix operations
import numpy

# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (numpy.add(x,y))

# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (numpy.subtract(x,y))

# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (numpy.divide(x,y))

# using multiply() to multiply matrices element wise
print ("The element wise multiplication of matrix is : ")
print (numpy.multiply(x,y))

# using dot() to multiply matrices
print ("The product of matrices is : ")
print (numpy.dot(x,y))

"""
6. sqrt() :- This function is used to compute the square root of each element of matrix. 
7. sum(x,axis) :- This function is used to add all the elements in matrix. Optional "axis" argument 
computes the column sum if axis is 0 and row sum if axis is 1. 
8. "T" :- This argument is used to transpose the specified matrix. 
"""
# using sqrt() to print the square root of matrix
print ("The element wise square root is : ")
print (numpy.sqrt(x))

# using sum() to print summation of all elements of matrix
print ("The summation of all matrix element is : ")
print (numpy.sum(y))

# using sum(axis=0) print summation of each column of matrix
print ("The column wise summation of all matrix is : ")
print (numpy.sum(y,axis=0))

# using sum(axis=1) print summation of each row of matrix
print ("The row wise summation of all matrix is : ")
print (numpy.sum(y,axis=1))

# using "T" to transpose the matrix
print ("The transpose of given matrix is : ")
print (x.T)

print("======================================================loop")

"""
Using nested loops:
Approach:

Define matrices A and B.
Get the number of rows and columns of the matrices using the len() function.
Initialize matrices C, D, and E with zeros using nested loops or list comprehension.
Use nested loops or list comprehension to perform the element-wise addition, subtraction, and division of matrices.
Print the resulting matrices C, D, and E.

"""
A = [[1,2],[4,5],[1,1]]
B = [[7,8],[9,10],[1,1]]
rows = len(A)
cols = len(A[0])
print("cols = ",cols)

# Element wise addition
C = [[0 for i in range(cols)] for j in range(rows)] # starting from 0
for i in range(rows):
	for j in range(cols):
		C[i][j] = A[i][j] + B[i][j]
print("Addition of matrices: \n", C)

# Element wise subtraction
D = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
	for j in range(cols):
		D[i][j] = A[i][j] - B[i][j]
print("Subtraction of matrices: \n", D)

# Element wise division
E = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
	for j in range(cols):
		E[i][j] = A[i][j] / B[i][j]
print("Division of matrices: \n", E)

print("======================================================")
A = [[1,2],[4,5]]
B = [[7,8],[9,10]]
rows = len(A)
cols = len(A[0])

# Element wise addition
C = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
	for j in range(cols):
		C[i][j] = A[i][j] + B[i][j]
print("Addition of matrices: \n", C)

# Element wise subtraction
D = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
	for j in range(cols):
		D[i][j] = A[i][j] - B[i][j]
print("Subtraction of matrices: \n", D)

# Element wise division
E = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
	for j in range(cols):
		E[i][j] = A[i][j] / B[i][j]
print("Division of matrices: \n", E)

















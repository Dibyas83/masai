How
to
inverse
a
matrix
using
NumPy
Last
Updated: 05
May, 2023
In
this
article, we
will
see
NumPy
Inverse
Matrix in Python
before
that
we
will
try to understand the concept of it.The inverse of a matrix is just a reciprocal of the matrix as we do in normal arithmetic for a single number which is used to solve the equations to find the value of unknown variables.The inverse of a matrix is that matrix which when multiplied with the original matrix will give an identity matrix.

The
inverse
of
a
matrix
exists
only if the
matrix is non - singular
i.e., the
determinant
should
not be
0.
Using
determinant and adjoint, we
can
easily
find
the
inverse
of
a
square
matrix
using
the
below
formula,

if det(A) != 0
    A - 1 = adj(A) / det(A)
else
    "Inverse doesn't exist"
Matrix
Equation:



= > Ax = B\\ = > A ^ {-1}
Ax = A ^ {-1}
B\\ = > x = A ^ {-1}
B

where,

A - 1: The
inverse
of
matrix
A

x: The
unknown
variable
column

B: The
solution
matrix

Inverse
Matrix
using
NumPy
Python
provides
a
very
easy
method
to
calculate
the
inverse
of
a
matrix.The
function
numpy.linalg.inv() is available in the
NumPy
module and is used
to
compute
the
inverse
matrix in Python.

Syntax: numpy.linalg.inv(a)

Parameters:

a: Matrix
to
be
inverted

Returns: Inverse
of
the
matrix
a.

Example
1: In
this
example, we
will
create
a
3
by
3
NumPy
array
matrix and then
convert
it
into
an
inverse
matrix
using
the
np.linalg.inv()
function.

# Import required package
import numpy as np

# Taking a 3 * 3 matrix
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
Output:

[[0.17647059 - 0.00326797 - 0.02287582]
 [0.05882353 - 0.13071895  0.08496732]
[-0.11764706
0.1503268
0.05228758]]
Example
2: In
this
example, we
will
create
a
4
by
4
NumPy
array
matrix and then
convert
it
using
np.linalg.inv()
function
into
an
inverse
Matrix in Python.

# Import required package
import numpy as np

# Taking a 4 * 4 matrix
A = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
Output:

[[0.13368984  0.10695187  0.02139037 - 0.09090909]
 [-0.00229183  0.02673797  0.14820474 - 0.12987013]
[-0.12987013
0.18181818
0.06493506 - 0.02597403]
[0.11000764 - 0.28342246 - 0.11382735  0.23376623]]
Example
3: In
this
example, we
will
create
multiple
NumPy
array
matrices and then
convert
them
into
their
inverse
matrices
using
np.linalg.inv()
function.

# Import required package
import numpy as np

# Inverses of several matrices can
# be computed at once
A = np.array([[[1., 2.], [3., 4.]],
              [[1, 3], [3, 5]]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
Output:

[[[-2.    1.]
  [1.5 - 0.5]]

 [[-1.25  0.75]
    [0.75 - 0.25]]]

Python | Numpy
matrix.transpose()
Last
Updated: 0
9
Jan, 2024
With
the
help
of
Numpy
matrix.transpose()
method, we
can
find
the
transpose
of
the
matrix
by
using
the
matrix.transpose()
method in Python.

Numpy
matrix.transpose()
Syntax

Syntax: matrix.transpose()

Parameter: No
parameters;
transposes
the
matrix
it is called
on.

Return: Return
transposed
matrix

What is Numpy
matrix.transpose()?
`numpy.matrix.transpose()` is a
function in the
NumPy
library
that
computes
the
transpose
of
a
matrix.It
swaps
the
rows and columns
of
the
matrix, effectively
reflecting
it
along
its
main
diagonal.The
function is called
on
a
NumPy
matrix
object, and it
does
not take
any
parameters.The
result is a
new
matrix
representing
the
transposed
version
of
the
original
matrix.

NumPy
Matrix
transpose() – Transpose
of
an
Array in Python
There
are
numerous
examples
of
`numpy.matrix.transpose()`.Here, we
illustrate
commonly
used
instances
of
`numpy.matrix.transpose()`
for clarity.

Matrix
Transformation
Matrix
Multiplication
NumPy
Matrix
Transformation
Example
1: In
this
example, the
code
uses
the
NumPy
library
to
create
a
2×3
matrix.It
then
calculates
the
transpose
of
the
original
matrix
using
the
`transpose()`
function.Finally, it
prints
both
the
original and transposed
matrices
to
the
console.

import numpy as np

# Original matrix
original_matrix = np.matrix([[1, 2, 3], [4, 5, 6]])

# Transposed matrix
transposed_matrix = original_matrix.transpose()

print("Original Matrix:")
print(original_matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)
Output:

Original
Matrix:
[[1 2 3]
 [4 5 6]]
Transposed
Matrix:
[[1 4]
 [2 5]
[3
6]]
Example
2: In
this
example
This
Python
code
uses
the
NumPy
library
to
create
a
3×3
matrix
named ‘gfg’.It
then
applies
the
transpose()
method
to
the
matrix and assigns
the
result
to ‘geek’.Finally, it
prints
the
transposed
matrix ‘geek’.

# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

# applying matrix.transpose() method
geek = gfg.transpose()

print(geek)
Output:

[[4 12  4]
 [1  3  5]
[9
1
6]]
Transpose
of
an
Array
Like
Object
In
this
example
code
uses
NumPy
to
create
two
2×2
matrices, `matrix_a` and `matrix_b`.It
then
transposes
`matrix_b`
using
the
`transpose()`
function and performs
matrix
multiplication
between
`matrix_a` and the
transposed
`matrix_b`.The
result is printed
to
the
console.

import numpy as np

# Matrices for multiplication
matrix_a = np.matrix([[1, 2], [3, 4]])
matrix_b = np.matrix([[5, 6], [7, 8]])

# Transpose one matrix before multiplication
result = matrix_a * matrix_b.transpose()

print("Result of Matrix Multiplication:")
print(result)
Output:

Result
of
Matrix
Multiplication:
[[17 23]
 [39 53]]

#-----------------------
Matrix
Transpose
Without
Numpy
In
Python
Last
Updated: 26
Feb, 2024
Matrix
transpose is a
fundamental
operation in linear
algebra
where
the
rows
of
a
matrix
are
swapped
with its columns.This operation is denoted by A ^ T, where A is the original matrix.The transposition of a matrix has various applications, such as solving systems of linear equations, computing the inner product of matrices, and more

What is Matrix
Transpose?
A
transpose
of
a
matrix is an
operation
that
switches
the
positions
of
its
rows and columns.If
you
have
a
matrix
A
with dimensions m×n, the transpose A ^ T will have dimensions n×m, and the elements of A ^ T will be such that the i-th row of A ^ T is the i-th column of A.Here, I'll provide a general explanation using mathematical notation and Python syntax:

A
T
=
[
    a
    11
    a
    21
    a
    12
    a
    22
]
A
T
=[
    a
    11
​

a
12
​

​

a
21
​

a
22
​

​
]



Matrix
Transpose
Without
Numpy in Python
Below, are
the
methods
of
Matrix
Transpose
Without
Numpy
In
Python.

Using
Nested
Loops
Using
List
Comprehension
Using
zip()
Function
Matrix
Transpose
Without
Numpy
Using
Nested
Loops
In
this
example, below
Python
code
transposes
a
given
matrix
by
initializing
an
empty
matrix
'transposed'
with dimensions swapped.It then iterates through the original matrix, assigning the transposed values to the new matrix.Finally, it prints both the original and transposed matrices for comparison.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

transposed = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transposed[j][i] = matrix[i][j]

print( & quot;
Original
Matrix: & quot;)
for row in matrix:
    print(row)

print( & quot;\nTransposed
Matrix: & quot;)
for row in transposed:
    print(row)

Output
Original
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Transposed
Matrix:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
Matrix
Transpose
Without
Numpy
Using
List
Comprehension
In
this
example, below
Python
code
efficiently
transposes
a
given
matrix
using
list
comprehension and zip.It
creates
the
transposed
matrix
by
extracting
columns
from the original

matrix.The
code
then
prints
both
the
original and transposed
matrices
for comparison.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print( & quot;
Original
Matrix: & quot;)
for row in matrix:
    print(row)

print( & quot;\nTransposed
Matrix: & quot;)
for row in transposed:
    print(row)

Output
Original
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Transposed
Matrix:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
Matrix
Transpose
Without
Numpy
Using
zip()
Function
In
this
example, below
Python
code
efficiently
transposes
a
given
matrix
using
the
zip
function
with the unpacking operator ( * ).It creates the transposed matrix by unpacking columns from the original matrix.The code then prints both the original and transposed matrices for comparison.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [list(row) for row in zip(*matrix)]

print( & quot;
Original
Matrix: & quot;)
for row in matrix:
    print(row)

print( & quot;\nTransposed
Matrix: & quot;)
for row in transposed:
    print(row)

Output
Original
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Transposed
Matrix:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
Conclusion
In
Conclusion, above
Python
processes
efficiently
achieve
matrix
transposition
without
relying
on
NumPy.The
first
uses
nested
loops
to
swap
rows and columns.The
second
employs
nested
list
comprehension
for a more compact solution.The third utilizes the zip function with unpacking, offering a concise and elegant approach.Despite their implementation differences, all approaches effectively manipulate matrices, catering to various preferences for readability and brevity.

#-------------------------
"""
Matrix Multiplication in NumPy
Last Updated : 02 Sep, 2020
Let us see how to compute matrix multiplication with NumPy. We will be using the numpy.dot() method to find the product of 2 matrices.

For example, for two matrices A and B.
A = [[1, 2], [2, 3]]
B = [[4, 5], [6, 7]]

So, A.B = [[1*4 + 2*6, 2*4 + 3*6], [1*5 + 2*7, 2*5 + 3*7]
So the computed answer will be: [[16, 26], [19, 31]]
In Python numpy.dot() method is used to calculate the dot product between two arrays.

Example 1 : Matrix multiplication of 2 square matrices.




# importing the module 
import numpy as np 
  
# creating two matrices 
p = [[1, 2], [2, 3]] 
q = [[4, 5], [6, 7]] 
print("Matrix p :") 
print(p) 
print("Matrix q :") 
print(q) 
  
# computing product 
result = np.dot(p, q) 
  
# printing the result 
print("The matrix multiplication is :") 
print(result) 
Output :

Matrix p :
[[1, 2], [2, 3]]
Matrix q :
[[4, 5], [6, 7]]
The matrix multiplication is :
[[16 19]
 [26 31]]
Example 2 : Matrix multiplication of 2 rectangular matrices.




# importing the module 
import numpy as np 
  
# creating two matrices 
p = [[1, 2], [2, 3], [4, 5]] 
q = [[4, 5, 1], [6, 7, 2]] 
print("Matrix p :") 
print(p) 
print("Matrix q :") 
print(q) 
  
# computing product 
result = np.dot(p, q) 
  
# printing the result 
print("The matrix multiplication is :") 
print(result) 
Output :

Matrix p :
[[1, 2], [2, 3], [4, 5]]
Matrix q :
[[4, 5, 1], [6, 7, 2]]
The matrix multiplication is :
[[16 19  5]
 [26 31  8]
 [46 55 14]]
"""














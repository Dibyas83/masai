
"""
To inverse a matrix using NumPy, the numpy.linalg.inv() function is utilized. This function is part of NumPy's
linear algebra module. Here is a step-by-step guide:
Import NumPy: Begin by importing the NumPy library, commonly aliased as np.


    import numpy as np
Define the Matrix: Create a square matrix using np.array(). It is crucial that the matrix is square (equal number of rows and columns) and non-singular (its determinant is not zero) for an inverse to exist.


    matrix = np.array([[1, 2], [3, 4]])
Calculate the Inverse: Use the np.linalg.inv() function, passing the matrix as an argument.


    inverse_matrix = np.linalg.inv(matrix)
Verify (Optional but Recommended): To confirm the inversion, multiply the original matrix by its inverse. The result should be an identity matrix (with ones on the diagonal and zeros elsewhere), although minor floating-point inaccuracies might be present.


    identity_check = np.matmul(matrix, inverse_matrix)
Print Results: Display the original matrix, its inverse, and the identity check.


    print("Original Matrix:\n", matrix)
    print("Inverse Matrix:\n", inverse_matrix)
    print("Identity Check (Matrix * Inverse):\n", identity_check)


Note: If the matrix is singular (determinant is zero), np.linalg.inv() will raise a LinAlgError.

"""
import numpy as np

matrix = np.array([[1, 2], [3, 4]])

inverse_matrix = np.linalg.inv(matrix)
identity_check = np.matmul(matrix, inverse_matrix)
print("Original Matrix:\n", matrix)
print("Inverse Matrix:\n", inverse_matrix)
print("Identity Check (Matrix * Inverse):\n", identity_check)


# Define a 3x3 matrix
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

# Print the inverse
print("Inverse of A:\n", A_inv)

# Verify the inverse by multiplying A and A_inv
identity_result = np.matmul(A, A_inv)
print("\nVerification (A * A_inv):\n", identity_result)




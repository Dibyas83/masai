
def sum_boundary_and_diagonals(matrix, n):
    matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    n = 5

    boundary_sum = 0
    diagonal_sum = 0
    boundary_elements = set()  # To store unique boundary elements
    diagonal_elements = set()  # To store unique diagonal elements
# Add boundary elements
    for i in range(n):

    # First and last row
        boundary_elements.add((0, i)) # Top row
        boundary_elements.add((n - 1, i)) # Bottom row
        # First and last column (excluding corners already added by rows)
        boundary_elements.add((i, 0)) # Left column as set no duplicate
        boundary_elements.add((i, n - 1)) # Right column
        # Calculate the boundary sum
    for row, col in boundary_elements:
        boundary_sum += matrix[row][col] # making matrix
# Add diagonal elements
    for i in range(n):

# Primary diagonal
        diagonal_elements.add((i, i))
        diagonal_elements.add((i,n-i-1))
# Secondary diagonal
        diagonal_elements.add((i, n - i - 1))
# Calculate the diagonal sum, excluding duplicates with boundary
    for row, col in diagonal_elements:
        if (row, col) not in boundary_elements:
            diagonal_sum += matrix[row][col]
# Total sum is the sum of boundary and unique diagonal elements
    print(boundary_sum + diagonal_sum)

matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
sum_boundary_and_diagonals(matrix,5)




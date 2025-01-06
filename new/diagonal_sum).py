matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
n = 5

boundary_sum = 0
diagonal_sum = 0
boundary_elements = set()  # To store unique boundary elements row and col
diagonal_elements = set()  # To store unique diagonal elements
# Add boundary elements
for i in range(n):  # it is set so duplicates deleted automatically
    # First and last row
    boundary_elements.add((0, i))  # Top row
    boundary_elements.add((n - 1, i))  # Bottom row
    # First and last column (excluding corners already added by rows)
    boundary_elements.add((i, 0))  # Left column
    boundary_elements.add((i, n - 1))  # Right column
    # Calculate the boundary sum
for row, col in boundary_elements:
    boundary_sum += matrix[row][col]
# Add diagonal elements
for i in range(n):
    # Primary diagonal
    diagonal_elements.add((i, i))
    # Secondary diagonal
    diagonal_elements.add((i, n - i - 1))
# Calculate the diagonal sum, excluding duplicates with boundary
for row, col in diagonal_elements:
    if (row, col) not in boundary_elements:
        diagonal_sum += matrix[row][col]
        print(diagonal_sum)
# Total sum is the sum of boundary and unique diagonal elements
print(boundary_sum + diagonal_sum)

matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
n = 5

boundary_sum = 0
diagonal_sum = 0
boundary_elements = set()  # To store unique boundary elements
diagonal_elements = set()
for i in range(n):
    boundary_elements.add((0,i))
    boundary_elements.add((n-1,i))
    boundary_elements.add((i,0))
    boundary_elements.add((i,n-1))
for row,col in boundary_elements:
    boundary_sum += matrix[row][col]

for i in range(n):
    diagonal_elements.add((i,i))
    diagonal_elements.add((i,n-i-1))
for row ,col in diagonal_elements:
    if (row,col) not in boundary_elements:
        diagonal_sum += matrix[row][col]
print(boundary_sum + diagonal_sum)

for i in range(5):
    for j in range(5):
        print(matrix[i][j])
    print()

matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
n = 5
boun_ele = set()
dia_ele = set()
boun_sum = 0
dia_sum = 0
for i in range(n):
    boun_ele.add((0,1))
    boun_ele.add((n-1,i))
    boun_ele.add((i,0))
    boun_ele.add((i,n-1))
for r,c in boun_ele:
    boun_sum += matrix[r][c]
for i in range(n):
    dia_ele.add((i,i))
    dia_ele.add((i,n-i-1))
for r,c in dia_ele:
    if (r,c) not in boun_ele:
        dia_sum += matrix[r][c]
print(boun_sum+ dia_sum)













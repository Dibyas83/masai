

# all possible paths

# Function to print the path taken to reach destination
def printPath(path):
    for i in path:
        print(i, end=", ")
    print()

# Function to find all possible paths in a matrix
# from the top-left cell to the bottom-right cell


def findPaths(arr, path, i, j):
    global M, N

    # If the bottom-right cell is reached, print the path
    if i == M - 1 and j == N - 1:
        path.append(arr[i][j])
        printPath(path)
        path.pop()
        return

    # Boundary cases: Check if we are out of the matrix
    if i < 0 or i >= M or j < 0 or j >= N:
        return

    # Include the current cell in the path
    path.append(arr[i][j])

    # Move right in the matrix
    if j + 1 < N:
        findPaths(arr, path, i, j + 1)

    # Move down in the matrix
    if i + 1 < M:
        findPaths(arr, path, i + 1, j)

    # Backtrack: Remove the current cell from the current path
    path.pop()


# Driver code
if __name__ == "__main__":
    # Input matrix
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # To store the path
    path = []

    # Starting cell (0, 0)
    i, j = 0, 0

    M = len(arr)
    N = len(arr[0])

    # Function call
    findPaths(arr, path, i, j)








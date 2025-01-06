N = 3
M = 2

for i in range(N):
    bag = ""
    for j in range(M):
        bag += str(i+j) + " "
    print(bag)


# Python3 implementation of the approach

# Function to return the sum of those columns
# of a given matrix that start with an odd element
def sumColumns(arr, r, c):
    # Initialize sum to 0
    sum = 0

    # Traverse through all the elements of the first row
    for j in range(c):

        # If the element is odd
        if (arr[0][j] % 2 != 0):

            # Add all the elements of that column
            for i in range(r):
                sum += arr[i][j]

    # Return the sum
    return sum


# Driver code
arr = [[8, 2, 3, 5], [9, 8, 7, 6], [1, 2, 5, 5]]
r = len(arr)
c = len(arr[0])
print(sumColumns(arr, r, c))

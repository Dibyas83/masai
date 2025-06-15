
# Python program for the above approach

# Function to find and print pair
def chkPair(A, x):
    size = len(A)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if A[i] + A[j] == x:
                return True
    return False

# Driver code
if __name__ == "__main__":
    A = [0, -1, 2, -3, 1]
    x = -2

    if chkPair(A, x):
        print("Yes")
    else:
        print("No", x)

# This code is contributed by Susobhan Akhuli













# Python implementation of the above approach

# Recursive function to find
# all the required combinations
def Recurrence(N, K, sub_vector, vis, output, last):
    # Base case
    if N == 0 and K == 0:
        # Push the current subset
        # in the array output[][]
        output.append(sub_vector[:])
        return

    # If N or K is less than 0
    if N <= 0 or K <= 0:
        return

    # Traverse the range [1, 9]
    for i in range(last, 10):
        # If current number is
        # not marked visited
        if not vis[i]:
            # Mark i visited
            vis[i] = True

            # Push i into the vector
            sub_vector.append(i)

            # Recursive call
            Recurrence(N - 1, K - i, sub_vector, vis, output, i + 1)

            # Pop the last element
            # from sub_vector
            sub_vector.pop()

            # Mark i unvisited
            vis[i] = False


# Function to check if required
# combination can be obtained or not
def combinationSum(N, K):
    # If N * 9 is less than K
    if N * 9 < K:
        print("Impossible")
        return

    # Stores if a number can
    # be used or not
    vis = [False] * 10

    # Stores a subset of numbers
    # whose sum is equal to K
    sub_vector = []

    # Stores list of all the
    # possible combinations
    output = []

    # Recursive function call to
    # find all combinations
    Recurrence(N, K, sub_vector, vis, output, 1)

    # Print the output array
    for i in range(len(output)):
        for x in output[i]:
            print(x, end=" ")
        print()
    return


# Driver Code
if __name__ == "__main__":
    N, K = 3, 9
    combinationSum(N, K)









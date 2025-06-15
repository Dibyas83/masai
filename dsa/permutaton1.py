
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    # Base case
    if l == r:
        print("".join(a))
    else:
        # Permutations made
        for i in range(l, r + 1):
            # Swapping done
            a[l], a[i] = a[i], a[l]
            #print("a".join(a))

            # Recursion called
            permute(a, l + 1, r)
            #print("b".join(a))

            # backtrack
            a[l], a[i] = a[i], a[l]
            #print("c".join(a))

# Driver Code
if __name__ == "__main__":
    str = list("ABC")
    n = len(str)

    # Function call
    permute(str, 0, n - 1)
#this code is contribuited by Utkarsh



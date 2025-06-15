
# Python program for the above approach

# A recursive binary search function. It returns
# location of x in the given array arr[l..r] if present,
# otherwise returns -1
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid, then
        # it can only be present in the left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in the right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    # We reach here when the element is not
    # present in the array
    return -1

# Driver code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

# Print the result
if result == -1:
    print("Element is not present in array")
else:
    print(f"Element is present at index {result}")

# This code is contributed by Susobhan Akhuli








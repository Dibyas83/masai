
"""
sorts from beg ,max goes to end then sorting array size decreases
Core Idea: “Compare neighbors, swap if wrong, repeat until no swaps!”
Why “Bubble” Sort? Larger elements "bubble up" like fizzy drinks! 🥤
Step-by-Step Walkthrough (using [5, 1, 4, 2, 8] ):
Pass 1:
Swap 5↔1 → [1, 5, 4, 2, 8]
Swap 5↔4 → [1, 4, 5, 2, 8]


"""

def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for i in range(len(arr) - 1, 0, -1):

        # Initialize swapped to track if any swaps occur
        swapped = False

        # Inner loop to compare adjacent elements
        for j in range(i): # loops lesser by lesser
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr[i])

                # Mark that a swap has occurred
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped: # already sorted
            break
    return arr

# Sample list to be sorted
arr = [6, 6, 2]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)







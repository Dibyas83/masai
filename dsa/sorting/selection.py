"""
Core Idea: “Find the max, swap it to the end, repeat!”
Step-by-Step Walkthrough (using [29, 10, 14, 37, 13] ):
1st Iteration: Find max ( 37 ), swap with last element → [29, 10, 14, 13, 37]
2nd Iteration: Find max in unsorted part ( 29 ), swap with second last → [13, 10, 14, 29, 37]

"""
def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1): # Start from the end
        max_index = 0 # Assume first item is the largest
        for j in range(1, i+1): # compare with next  with decreasing list size
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i] # Swap with end
    return arr

# Always O(n²): Even if the array is sorted, it checks every element every time.Use max_index for ascending order.
# Flip the comparison to sort descending!
#---------------
# min sorted first

def SelectionSort2(arr1):
    n = len(arr1) # 5
    for i in range(n-1): # 0 - 4 Start from the begin
        min_index = i  # 0
        for j in range(i+1, n):# 1,2,3,4 - 5 #  compare with next
            if arr1[j] < arr1[min_index]:
                min_index = j # 1
        arr1[i], arr1[min_index] = arr1[min_index], arr1[i] # Swap with end
    return arr1

"""
Key Points to Remember ✓
✅ Time Complexity: Always O(n²) → Inefficient for large lists (e.g., sorting 1000 items takes ~500k operations).
✅ Use When: The list is small (e.g., less than 20 items).
✅ Stability: Not stable → Equal items might swap places.
"""

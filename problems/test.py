

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
"""

rows, cols = 3, 3  # Example dimensions
grid = [[input() for _ in range(cols)] for _ in range(rows)]
print(grid,end=" ")
"""
rows, cols = map(int,input().split(" "))  # Example dimensions
for _ in range(cols):
    for _ in range(rows):
        u = input().join(" ")
        print(u)









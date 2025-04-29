
"""
After stably sorting a list using merge sort in Python, the position of a specific element can be determined by iterating through the sorted list and comparing each element with the target element. Because merge sort is stable, elements with the same value maintain their original relative order. Thus, the first occurrence of the target element in the sorted list corresponds to its final position if duplicates are present.
Python
"""
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def find_element_position(arr, element):
    sorted_arr = merge_sort(arr)
    for index, value in enumerate(sorted_arr):
        if value == element:
            return index
    return -1  # Element not found

# Example usage:
def inpt():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split(" "))
        my_list = list(map(int,input().split(" ")))
        target_element = my_list[k]
        position = find_element_position(my_list,target_element)
        #print(my_list[k])
        print(position)

inpt()

"""

if position != -1:
    print(f"The element {target_element} is at position {position} after sorting.")
else:
    print(f"The element {target_element} is not in the list.")
"""






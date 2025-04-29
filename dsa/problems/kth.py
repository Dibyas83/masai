
###------------------------
"""
Here's how to find the position of the k-th element after stably sorting an array using Merge Sort in Python:
Implement Merge Sort: A standard, stable implementation of Merge Sort is required. Stability ensures that elements with equal values maintain their original order.
Python
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Stability is maintained here
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
#Track Original Indices: To determine the original position of the k-th element, create a list of tuples, where each tuple contains the element's value and its original index.

def track_index(arr):
    indexed_arr = []
    for i, value in enumerate(arr):
        indexed_arr.append((value, i))
    return indexed_arr
#Sort and Retrieve: Apply Merge Sort to the indexed array and then retrieve the index of the k-th element.

def find_kth_position(arr, k):
    indexed_arr = track_index(arr)
    sorted_indexed_arr = merge_sort(indexed_arr)
    return sorted_indexed_arr[k - 1][1] #adjust k to be 1-based



arr = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3
original_position = find_kth_position(arr, k)
print(f"The original position of the {k}-th element is: {original_position}")









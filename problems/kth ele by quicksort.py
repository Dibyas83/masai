
smaller_count = 0
def count(arr,k):
    n = len(arr)
    k = int(input())
    kth_element = arr[k]
    for y in arr[0:k]:
        if y == kth_element:
            global smaller_count
            smaller_count += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def solve(arr):
    global k
    sorted_arr = quick_sort(arr)

    for x in sorted_arr:
        if x < y:
            smaller_count += 1
    return smaller_count

# Example usage:
def inpt():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split(" "))
        arr = list(map(int, input().split(" ")))
        position = quick_sort(arr,k)
        print(f"Position of the {k}-th element after sorting: {position}")

inpt()

"""
def inpt():
  t = int(input())
  for _ in range(t):
    n,k = map(int,input().split(" "))
    my_list = list(map(int,input().split(" ")))
    target_element = my_list[k]
    position = insertion_sort_with_kth_position(my_list,target_element)
    print(position)
inpt()
"""








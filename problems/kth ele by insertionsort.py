
def insertion_sort_with_kth_position(arr, k):
    n = len(arr)
    kth_element = arr[k]
    smaller_count = 0
    for y in arr[0:k]:
        if y == kth_element:
            smaller_count += 1

    # Perform insertion sort
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Find the position of the k-th element
    #kth_element = arr[k]
    #smaller_count = 0
    for x in arr:
        if x < kth_element:
            smaller_count += 1

    return smaller_count


# Example usage:
def inpt():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split(" "))
        arr = list(map(int, input().split(" ")))
        position = insertion_sort_with_kth_position(arr, k)
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








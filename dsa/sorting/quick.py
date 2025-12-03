def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        print("pivot",pivot)
        print("array[j]",array[j])
        print("i",i)  # i is also increasing due to low inc

        if array[j] <= pivot:
            print(array[j], pivot,array[high], "bef ari,piv")
            i = i + 1
            print(array[i], array[j],"before")
            (array[i], array[j]) = (array[j], array[i])
            print(array[i], array[j],"after")

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
print("--------------------------------------")
#--------------
def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort2(left) + [pivot] + quicksort2(right)

# Example
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort2(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)

def quicks(list):
    if len(list) <= 0:
        return list
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x <= pivot]
        high = [x for x in list[1:] if x > pivot]
        return quicks(less) + [pivot] + quicks(high)
list1 = [1,0,2,1,4,7,3,8,5]

list2 = list(map(int, input().split(' ')))
u2 = quicks(list2)
u = quicks(list1)
print(' '.join(map(str,u)))
print(' '.join(map(str,u2)))








def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position


# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

def count_pairs_with_sum(arr, target_sum):
    count = 0
    seen = {}
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += seen[complement] # seeen compliment is boolean 0/1
            print(seen[complement],"sc")
            print(seen,"s")
            print(count,"c")
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    print(count)

arr = [12, 11, 13, 5, 6, 15]
target_sum = 18
count_pairs_with_sum(arr, target_sum)

#---------------
def solve(n,arr,k):
    arr.sort(key=lambda x: x%k)
    print(" ".join(map(str,arr)))



arr1 = [1,22,3,44,5,6,7,8,9]
arr2 = sorted(set(arr1))
print(arr2,"i")
print(arr2[-3:])

def two_sum(n, arr, target):

# Two pointers approach
    left = 0
    right = n - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        # Check if the current sum equals the target
        if current_sum == target:
            print(left, right)
            return
        elif current_sum < target:
            left += 1 # Move left pointer to the right to increase the sum
        else:
            right -= 1 # Move right pointer to the left to decrease the sum
    print(-1, -1)

arr=[2,3,4,6,7,8,9]
target = 9
n=7
print(two_sum(n,arr,target))

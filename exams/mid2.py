"""
max of three
"""
def maximum_of_three(a, b, c):
    # Initialize the maximum value as the first number
    max_val = a
    # Compare with the second number
    if b > max_val:
        max_val = b # max changes
    # Compare with the third number
    if c > max_val:
        max_val = c # max changes
    print(max_val) # after determining printed

maximum_of_three(4,7,2)

print("----------------2")
"""
s = input("string").split(" ")
print(" ".join(word[::-1] for word in s))
"""
# Reverse the string but maintain the relative order of the words and the spaces in between.

def reverse_words_in_string(s):
    # Split the string into words, reverse each word, and join them back
    print(' '.join(word[::-1] for word in s.split(' ')))


print("----------------3")
def solve(N):
    # Initialize the factorial to 1
    factorial = 1  # Loop through numbers from 1 to N (inclusive)
    for i in range(1, N + 1):
        factorial *= i  # Multiply factorial by the current number
    # Print the final factorial value
    print(factorial)
solve(4)
"""

Description:
Given a sorted array of integers, return indices of two numbers such that they add up to a target value.
If no such pair exists, print (-1 -1).

"""
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
            left += 1  # Move left pointer to the right to increase the sum
        else:
            right -= 1  # Move right pointer to the left to decrease the sum

    print(-1, -1)

# Find the length of the longest subarray which is strictly increasing.
# ie every element is increasing
def longest_increasing_subarray(n, arr):
    max_length = 1  # Initialize the maximum length
    current_length = 1  # Length of the current increasing subarray
    for i in range(1, n):

        # Check if the current element is greater than the previous one
        if arr[i] > arr[i - 1]:
            current_length += 1  # Increment the current length
            max_length = max(max_length, current_length)  # Update max_length
        else:
            current_length = 1  # Reset current_length if sequence breaks
    print(max_length)






























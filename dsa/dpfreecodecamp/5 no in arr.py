
def find_combinations_recursive(arr, target_sum, current_index, current_combination, result):
    """
    Recursively finds combinations of numbers in an array that sum to a target.

    Args:
        arr (list): The input array of numbers.
        target_sum (int): The target sum to achieve.
        current_index (int): The current index in the array to consider.
        current_combination (list): The combination of numbers built so far.
        result (list): A list to store all valid combinations found.
    """
    # Base case 1: If target_sum is 0, a valid combination is found
    if target_sum == 0:
        result.append(list(current_combination))  # Append a copy to avoid modification issues
        return

    # Base case 2: If target_sum becomes negative or we've exhausted the array
    if target_sum < 0 or current_index == len(arr):
        return

    # Recursive step 1: Include the current element
    current_combination.append(arr[current_index])
    find_combinations_recursive(arr, target_sum - arr[current_index], current_index, current_combination, result)
    current_combination.pop()  # Backtrack: remove the current element for the next path

    # Recursive step 2: Exclude the current element
    find_combinations_recursive(arr, target_sum, current_index + 1, current_combination, result)

def find_sum_combinations(arr, target_sum):
    """
    Initiates the recursive search for combinations that sum to the target.

    Args:
        arr (list): The input array of numbers.
        target_sum (int): The target sum to achieve.

    Returns:
        list: A list of lists, where each inner list is a combination
              that sums to the target.
    """
    result = []
    find_combinations_recursive(arr, target_sum, 0, [], result)
    return result

# Example Usage:
numbers = [2, 3, 6, 7]
target = 7
combinations = find_sum_combinations(numbers, target)
print(f"Combinations that sum to {target}: {combinations}")

numbers_with_duplicates = [1, 2, 1, 3]
target_duplicate = 3
combinations_duplicate = find_sum_combinations(numbers_with_duplicates, target_duplicate)
print(f"Combinations for {numbers_with_duplicates} that sum to {target_duplicate}: {combinations_duplicate}")






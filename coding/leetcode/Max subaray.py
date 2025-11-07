"""# [1,-2,3,4,-5,1,2,-2,4]  fin sum of contiguous subarray with max val. 1,-2,3,4 after this it will not increase
# 3,4 is max
class Solu:
    def maxsub(self,arr: list[int]):
        n = len(arr)
        max_sum = 0
        s = 0
        e = 0
        for i in range(n):   # starting index

            for j in range(i, n): # ending index
                sum = 0

                print('max_sum ,sum',max_sum ,sum)
                for k in range(i, j+1):  # sum from start to end index
                    sum += arr[k]
                    s = i
                    e = k
                if sum > max_sum:
                    max_sum = sum

                    return s, e




arr12 = [1,-2,3,4,-5,1,2,-2,4]
h = Solu()
print(h.maxsub(arr12))"""

# using sliding window
class Solut:
    def maxsubarr(self, nums: list[int]) -> int:
        maxsub = nums[0]
        cursumm  = 0
        l = len(nums)
        y = []
        for n in range(l):
            if cursumm < 0:
                cursumm = 0 # rejecting past facts
                y=[]
            print(y)
            cursumm += nums[n] # starting fresh
            if cursumm > maxsub:
                y.append(n)
            maxsub = max(maxsub,cursumm)


        return maxsub,y[0],y[-1]

h=Solut()
print(h.maxsubarr(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print("oooooooooooooooooooooooooooooooooooooooooo")

def max_subarray_sum_with_indices(arr):
    max_so_far = arr[0]  # Stores the overall maximum sum found
    current_max = arr[0]  # Stores the maximum sum ending at the current position

    start_index = 0  # Start index of the maximum subarray
    end_index = 0    # End index of the maximum subarray
    s = 0            # Temporary start index for tracking current_max

    for i in range(1, len(arr)):
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            s = i  # New start for the current_max subarray
        else:
            current_max += arr[i]

        if current_max > max_so_far:
            max_so_far = current_max
            start_index = s
            end_index = i

    return max_so_far, start_index, end_index

# Example usage:
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum1, start1, end1 = max_subarray_sum_with_indices(arr1)
print(f"Array: {arr1}")
print(f"Maximum Subarray Sum: {max_sum1}")
print(f"Start Index: {start1}, End Index: {end1}")

arr2 = [1,-2,3,4,-5,1,2,-2,4]
max_sum2, start2, end2 = max_subarray_sum_with_indices(arr2)
print(f"\nArray: {arr2}")
print(f"Maximum Subarray Sum: {max_sum2}")
print(f"Start Index: {start2}, End Index: {end2}")

arr3 = [-5, -2, -8, -1]
max_sum3, start3, end3 = max_subarray_sum_with_indices(arr3)
print(f"\nArray: {arr3}")
print(f"Maximum Subarray Sum: {max_sum3}")
print(f"Start Index: {start3}, End Index: {end3}")
print("==============================================")

def max_subarray_sum_brute_force(arr):
    n = len(arr)
    max_so_far = float('-inf')  # Initialize with negative infinity

    for i in range(n):  # Outer loop for start index
        for j in range(i, n):  # Inner loop for end index
            current_sum = 0
            for k in range(i, j + 1):  # Innermost loop to calculate sum
                current_sum += arr[k]
                print('current_sum,max_so_far', current_sum, max_so_far)
            print("------------------------------------------")
            print('current_sum,max_so_far',current_sum,max_so_far)
            if current_sum > max_so_far:
                max_so_far = current_sum

    return max_so_far


# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum_brute_force(arr)
print(f"The maximum subarray sum is: {result}")

print("========================================")
def max_subarray_sum_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')  # Initialize with negative infinity
    start_index = -1
    end_index = -1

    # Outer loop for the starting index of the subarray
    for i in range(n):
        current_sum = 0
        # Inner loop for the ending index of the subarray
        for j in range(i, n):
            current_sum += arr[j]

            # If the current subarray sum is greater than the maximum sum found so far
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j

    return max_sum, start_index, end_index

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray_sum_brute_force(arr)
print(f"Maximum subarray sum: {max_sum}")
print(f"Start index: {start}")
print(f"End index: {end}")
print(f"Subarray: {arr[start:end+1]}")


def max_subarray_sumind_brute_force2(arr):
    n = len(arr)
    max_sum = float('-inf')  # Initialize with negative infinity
    start_index = 0
    end_index = 0

    # Outer loop for the starting index of the subarray
    for i in range(n):

        # Inner loop for the ending index of the subarray
        for j in range(i, n):
            current_sum = 0
            for k in range(i,j+1):
                current_sum += arr[k]

                # If the current subarray sum is greater than the maximum sum found so far
                if current_sum > max_sum:
                    max_sum = current_sum
                    start_index = i
                    end_index = j

    return max_sum, start_index, end_index

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray_sumind_brute_force2(arr)
print(f"Maximum subarray sum: {max_sum}")
print(f"Start index: {start}")
print(f"End index: {end}")
print(f"Subarray: {arr[start:end+1]}")






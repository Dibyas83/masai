my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(len(my_dict))

def solve(n, arr):
    freq = {}  # Dictionary to store the frequency of each element
    # Count frequency of each element in the array
    for num in arr:
        if num in freq:
            freq[num] += 1
            print(freq[num])
        else:
            freq[num] = 1
    print(freq.items())
    # Sum all elements that appear exactly once
    # num is key, count is values
    unique_sum = sum(num for num, count in freq.items() if count == 1)
    print(unique_sum)


n=8
arr = [1,2,3,4,4,3,6,7]
solve(n,arr)
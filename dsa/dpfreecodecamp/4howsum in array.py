
# element in array should be non-negetive, can_sum(targe_tsum,(array))
"""
it is combination
#can_sum(7,(5,3,4,7))      7

      2(5)        4(3)          3(4)       0(7)      new target sum after using the respective elements in array,2 does not have more valid option as it will give negative values

    - - -     - 1(3) 0(4) -       - 0(3) -               negetive                 0 means target sum found

m,n  - n is the length of the array,m is levels in worst case there may be 1, m-1,will take m levels
The combinations of the numbers 1, 3, and 3, where order doesn't matter, are {1, 3}. If the order of selection matters (permutations), the possibilities are 133, 313, and 331.
123 - 1,2,3,12,23,13,123
"""
def how_sum(n,arr,cur_ind,cur_comb,res):
    #base case 1
    if n == 0:
        res.append(list(cur_comb))
        return  # return to next iteration
    # base case 2
    if n < 0 or cur_ind == len(arr):
        return  # return to next iteration
    #recursive step 1:include the curr element
    cur_comb.append(arr[cur_ind])
    how_sum(n-arr[cur_ind],arr,cur_ind,cur_comb, res) #allows for multiple uses
    cur_comb.pop() #backtrack - remove the curr ele for the next path.after it was found < 0 or curindex=len(arr) it returned.like for loop
    #start again rec step2-exclude curr ele so that curr element is not included again
    how_sum(n, arr, cur_ind+1, cur_comb, res)

def start_search(n,arr): # This function initializes an empty result list
    result = []
    how_sum(n,arr,0,[],result)
    return result

# Example Usage:
numbers = [2, 3, 6,1, 7]
target = 7
combinations = start_search(target,numbers)
print(f"Combinations that sum to {target}: {combinations}")

numbers_with_duplicates = [1, 2, 1, 3]
target_duplicate = 3
combinations_duplicate = start_search( target_duplicate,numbers_with_duplicates)
print(f"Combinations for {numbers_with_duplicates} that sum to {target_duplicate}: {combinations_duplicate}")
# tc = n**m , space = height = m
"""
def how_sum(n,arr,ar):
    if n>0:
        return []
    if n == 0:
        return [].append(n)
    if n < 0:
        return None
    for i in arr:
        n = n - i
        remainder_res = how_sum(n, arr)
        if  remainder_res != None:
            return remainder_res.append(i)
    return None

"""

def memo_target_sum(n,arr,dict):
    if n in dict: # only n changing
        return dict[n]
    if n == 0:
        return True
    if n < 0:
        return False
    for i in arr:
        n = n - i  # element in array not mutable
        if  memo_target_sum(n, arr,dict) == True:
            dict[n] = True
            return True
    dict[n] = False
    return False

# its permutation not combination
dict={}
print(memo_target_sum(7,[4,5],dict),"memo")
print(memo_target_sum(5,[2,3,6],dict))
# tc = m*n,space m









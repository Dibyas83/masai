
# element in array should be non-negetive, can_sum(targe_tsum,(array))
"""
#can_sum(7,(5,3,4,7))      7

      2(5)        4(3)          3(4)       0(7)      new target sum after using the respective elements in array,2 does not have more valid option as it will give negative values

    - - - -   - 1(3) 0(4) -   - 0(3) - - negetive                 0 means target sum found

m,n  - n is the length of the array,m is levels in worst case there may be 1, m-1,will take m levels
"""
def target_sum(n,arr):
    if n == 0:
        return True
    if n < 0:
        return False
    for i in arr:
        remainder = n - i  # element in array not mutable
        if target_sum(remainder, arr) == True:
            return True
    return False
# its permutation not combination
arr = [2,3]
arr1 = [2,3,6]
arr2 = [2,3,6,1]
print(target_sum(7,[4,5]))
print(target_sum(5,arr1))
print(target_sum(8,arr2))
# tc = n**m , space = height = m
"""
def target_sum(n,arr):
    if n == 0:
        return True

    for i in arr:
        remainder = n - i  # element in array not mutable
        if remainder >= 0:
            return target_sum(remainder, arr.remove(i))
        return target_sum(n, arr)
    return False

arr = [2,3]
arr1 = [2,3,6]
arr2 = [2,3,6,1]
print(target_sum(7,[2,3]))
print(target_sum(5,arr1))
print(target_sum(8,arr2))

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










def solve(price,no_of,arr,cur_sum,ans,res,idx):
    print(cur_sum,len(ans),"currsum,len")

    if cur_sum > price:
        print("grater")
        return # returns to previous ans  and index which was smaller and enters loop with that prev values
    if cur_sum == price and len(ans) == no_of:
        print(ans,"suceess")
        res.append(ans[:])
        return # returns to previous ans and index and enters loop below solve
    for i in range(len(ans),len(arr)):
        print(idx, "index in loop")
        print(ans,"beg")
        print(i,"i")
        ans.append(arr[i])
        solve(price, no_of, arr, cur_sum + arr[i], ans, res, i + 1) # if fails again loops
        print(ans[-1],"ans[-1]") # if meets condition comes here pops and loops again
        ans.pop()# when solve breaks it pops ans and breaked when loop finished

        print(ans,"anspoped")
        print(i,"iserial",end=" ")

if __name__== "__main__":
    price, no_of =map(int,input().split(" "))
    arr = [1,2,3,4,5,6,7,8,9]
    ans = []
    res = []
    solve(price,no_of,arr,0,ans,res,0)
    if not res:
        print(-1)
    else:
        res = sorted(res)
        for combination in res:
            print(" ".join(map(str,combination)))

#--------------
def combinationofcoin(amt,coins,arr1,cursum,anss,combs,ind):
    print(cursum,len(anss))
    l = len(arr1)

    if cursum > amt:
        return
    if cursum == amt and len(anss)== coins:
        combs.append(anss[:])
        return
    for i in range(ind,l):
        print(ind,"ind")
        anss.append(arr1[i])
        combinationofcoin(amt, coins, arr1, cursum + arr1[i], anss, combs, i+1)
        anss.pop()

if __name__ == "__main__":
    amt,coins = map(int,input().split(" "))
    arr1 = [1,2,3,4,5,6,7,8,9]
    anss = []
    combs = []
    combinationofcoin(amt, coins, arr1,0 , anss, combs, 0)
    if not combs:
        print(-1)
    else:
        combs = sorted(combs)
        for comb in combs:
            print(" ".join(map(str,comb)))

#-------------------------
"""

Find all valid combinations of at most K numbers that sum up to N
Last Updated : 20 Feb, 2023
Given two numbers N and K, the task is to find all valid combinations of at most K numbers that sum up to N such that the following conditions are true: 

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations

Examples:



Input: K = 3, N = 7
Output: 
1 2 4
1 6
2 5
3 4
7 





Input: K = 3, N = 9
Output: 
1 2 6
1 3 5
1 8
2 3 4
2 7
3 6
4 5
9



 
Naive Approach: The idea is to create an array of numbers from 1 to 9, and find all subsequences of length at most K with sum N.

Time Complexity: O(10^2) 
Auxiliary Space: O(10^2)

Recursive Approach: The problem can also be solved using Recursion as follows:

Create an array of digits 1-9 in arr.
Create a recursive function that iterates the array with current index as i, current sum as sum, current count as c, current selection as temp, and current resultant vector as ans.
Base case 1: if (sum == n && c <= k)
Insert temp vector into ans vector
Return the ans vector
Base case 2: if (i >= arr.size() || sum > n || c > k)
Return the ans vector as the current constraints have been violated
Else
Push current array element into temp vector
Call the recursive function
Pop the current element from the vector
Call the recursive function
"""
# python3 code to solve the above problem

# Recursive program to find
# all combinations of at most K
# digits with sum N
def rec(arr, i, k, c, n, ans, temp, sum):

    # Base case 1
    if (sum == n and c <= k):
        ans.append(temp.copy())
        return ans

    # Base case 2
    if (i >= len(arr) or sum > n or c > k):
        return ans

    # Insert arr[i] into current selection
    # //and call recursive function
    temp.append(arr[i])
    ans = rec(arr, i + 1, k, c + 1, n, ans, temp,
              sum + arr[i])

    # Remove arr[i] from current selection
    # and call recursive function
    temp.pop()
    ans = rec(arr, i + 1, k, c, n, ans, temp, sum)

    return ans

# Function to solve the problem
# and print the list of combinations
def combinationSum(k, n):

    arr = [0 for _ in range(9)]
    for i in range(1, 10):
        arr[i - 1] = i

    ans = []
    temp = []

    # Recursive function call
    ans = rec(arr, 0, k, 0, n, ans, temp, 0)

    # Print the output[][] array
    for i in range(0, len(ans)):

        for x in ans[i]:
            print(x, end=" ")
        print()

# Driver Code
if __name__ == "__main__":

    N, K = 7, 3
    combinationSum(K, N)




#-------------------------

# python3 code to solve the above problem

# Recursive program to find count of
# all combinations of at most K
# digits with sum N
def rec(arr, i, k, c, n, ans, sum):
    # Base case 1
    if (sum == n and c <= k):
        ans += 1
        return ans

    # Base case 2
    if (i >= len(arr)
            or sum > n or c > k):
        return ans

    # Consider arr[i] into current selection
    # and call recursive function
    ans = rec(arr, i + 1, k, c + 1,
              n, ans, sum + arr[i])

    # Do not consider arr[i] into current
    # selection and call recursive function
    ans = rec(arr, i + 1, k, c, n, ans, sum)

    return ans


# Function to solve the problem
# and print the count of combinations
def combinationSum(k, n):
    arr = [0 for _ in range(9)]
    for i in range(1, 10):
        arr[i - 1] = i

    ans = 0

    # Recursive function call
    ans = rec(arr, 0, k, 0, n, ans, 0)

    return ans


# Driver Code
if __name__ == "__main__":
    N, K = 9, 3
    print(combinationSum(K, N))


#--------------youtube

class Solution:
    def combin(self, amnt: int, k: int) -> List[List[int]]:
        res1 = []
        def backtrack1(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            # (start,amnt-(k-len(comb))+1)
            for i in range(start, amnt + 1):
                comb.append(i)
                backtrack1(i + 1, comb)
                comb.pop()
        backtrack1(1, [])
        return res1

"""
There's an optimization you can do. Instead of looping till n+1, which results in some branches that don't have enough height to make a k-combination, you loop till the last number from which it is possible to make a k-combination.
```
# Number of elements still needed to make a k-combination.
need = k - len(comb)
# The range of numbers is [i, n], therefore, size=n - i + 1
remaining = n - i + 1
# This is the last offset from which we can still make a k-combination.
offset = remaining - need
for i in range(start, start + offset + 1):
"""









































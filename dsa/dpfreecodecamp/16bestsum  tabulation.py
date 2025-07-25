
"""
cansum(7,[4,5,3])
there will be repetition use of array elements,so create an array > n
|0|1|2|3|4|5 6 7
ans in arr

cansum(0,[_])  if combination is 0 then return null ,if multiple combi return one
[] N N [3] [4] [5] [3,3] [3,4][4,3] - array     N = Null asume cannot be generated . if target is 0 then comb is [] empty arr
|0|1|2| 3|  4   5    6    7    - 7(4,5,3) - if currently i is true after 4 steps i can reach 4 so also true,similarly after 5 , and 3 steps
---------  4
-------3
-----------    5
       3---------        4
       3-------      3
       3-----------5      5 going outside array but 3,4 still in array reaching 6,7 making them true or constructable,if end is true then 7 is constructable
            4-------3
tc = m**2*n space = m**2  = due to combination findings

"""
def bestsum(targetsum, nums):
    table = [None] * (targetsum + 1)
    table[0] = []

    for i in range(targetsum + 1):
        if table[i] is not None:
            for num in nums:
                combination = table[i] + [num]
                if i + num <= targetsum and (table[i + num] is None or len(table[i + num]) > len(combination)):
                    table[i + num] = combination

    return table[targetsum]

print(bestsum(7, [5, 3, 4]))
"""
def howsum(n,arr):
    table = ["None"] * (n+1)
    table[0] = []

    for i in range(n+1):
        x=table[i]
        if table[i] != "None":
            for j in arr:
                if (i+j) <= n:
                    table[i+j] = [x,j]

    return table[n]

print(howsum(7,[4,5,3]))
print(howsum(7,[4,2]))
print(howsum(8,[2,5,3]))

"""












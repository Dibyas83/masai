
"""
cansum(7,[4,5,3])
there will be repetition use of array elements,so create an array > n
|0|1|2|3|4|5 6 7
ans in true or false

cansum(0,[_])  if target is 0 its  always possible without taking any elements
 t f f t t t t t- array
|0|1|2|3|4|5 6 7    - 7(4,5,3) - if currently i is true after 4 steps i can reach 4 so also true,similarly after 5 , and 3 steps
---------4
-------3
-----------5
       ---------4
       -------3
       -----------5      5 going outside array but 3,4 still in array reaching 6,7 making them true or constructable,if end is true then 7 is constructable

tc = m*n space = m

"""

def cansum(n,arr):
    table = [False] * (n+1)
    table[0] = True

    for i in range(n+1):
        if table[i] == True:
            for j in arr:
                if (i+j) <= n:
                    table[i+j] = True

    return table[n]

print(cansum(7,[4,5,3]))
print(cansum(7,[4,2]))
print(cansum(8,[2,5,3]))
















"""

Permutation and Combination in Python
Last Updated : 08 Mar, 2023
Python provides direct methods to find permutations and combinations of a sequence. These methods are present in itertools package.

Permutation
First import itertools package to implement the permutations method in python. This method takes a list as an input and returns an object list of tuples that contain all permutations in a list form.





# A Python program to print all
# permutations using library function
from itertools import permutations


# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])

# Print the obtained permutations
for i in list(perm):
    print (i)
Output:

(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
Time complexity: O(n!), where n is the length of the input list. This is because there are n! permutations of n elements, and the program generates and prints all of them.
Auxiliary space: O(n!), as the program needs to store all n! permutations in memory before printing them out. Specifically, the perm variable created by calling permutations([1, 2, 3]) stores all n! permutations in memory as a list.

It generates n! permutations if the length of the input sequence is n.
If want  to get permutations of length L then implement it in this way.




# A Python program to print all
# permutations of given length
from itertools import permutations

# Get all permutations of length 2
# and length 2
perm = permutations([1, 2, 3], 2)

# Print the obtained permutations
for i in list(perm):
    print (i)
Output:

(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
The time complexity of this program is O(n^r) where n is the length of the input array and r is the length of permutations to be generated.

The space complexity is also O(n^r) as all permutations are stored in memory before printing.

It generates nCr * r! permutations if the length of the input sequence is n and the input parameter is r.

Combination
This method takes a list and an input r as an input and return an object list of tuples which contain all possible combination of length r in a list form.





# A Python program to print all
# combinations of given length
from itertools import combinations

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)

# Print the obtained combinations
for i in list(comb):
    print (i)
Output:

(1, 2)
(1, 3)
(2, 3)


1. Combinations are emitted in lexicographic sort order of input. So, if the input list is sorted, the combination tuples will be produced in sorted order.





# A Python program to print all
# combinations of a given length
from itertools import combinations

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)

# Print the obtained combinations
for i in list(comb):
    print (i)
Output:

(1, 2)
(1, 3)
(2, 3)


2. Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each combination.





# A Python program to print all combinations
# of given length with unsorted input.
from itertools import combinations

# Get all combinations of [2, 1, 3]
# and length 2
comb = combinations([2, 1, 3], 2)

# Print the obtained combinations
for i in list(comb):
    print (i)
Output:

(2, 1)
(2, 3)
(1, 3)


3. If we want to make a combination of the same element to the same element then we use combinations_with_replacement.





# A Python program to print all combinations
# with an element-to-itself combination is
# also included
from itertools import combinations_with_replacement

# Get all combinations of [1, 2, 3] and length 2
comb = combinations_with_replacement([1, 2, 3], 2)

# Print the obtained combinations
for i in list(comb):
    print (i)
"""

"""
Combinations in Python without using itertools
Last Updated : 21 Jun, 2022
Itertools in Python is a module that produces complex iterators with the help of methods that work on iterators. This module works as a fast, memory-efficient tool that is used either by itself or in combination to form iterator algebra.

Printing Combinations Using itertools
Using Itertools we can display all the possible combinations of the string in a quite optimized way. To display the combination requires 2 parameters. First is the string and the second is the length of substrings needed. The following example makes all combinations for the string ‘abc’ using itertools. 

Example: 




# Import combinations from itertools
from itertools import combinations 
   
     
def n_length_combo(arr, n): 
     
    # using set to deal 
    # with duplicates  
    return list(combinations(arr, n)) 
   
# Driver Function 
if __name__ == "__main__": 
    arr = 'abc'
    n = 2
    print (n_length_combo([x for x in arr], n) )
Output
[('a', 'b'), ('a', 'c'), ('b', 'c')]
Printing Combinations Without using itertools
A. Using recursion
To create combinations without using itertools, iterate the list one by one and fix the first element of the list and make combinations with the remaining list. Similarly, iterate with all the list elements one by one by recursion of the remaining list.




# Function to create combinations 
# without itertools
def n_length_combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        remainlst_combo = n_length_combo(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])
           
    return l
 
# Driver code
if __name__=="__main__":
    arr ="abc"
    print(n_length_combo([x for x in arr], 2))
Output
[['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b']]
B. By using iterations
In this, return the first combination of n elements from the string as it is, then other combinations are made by considering each element by its position. Each element is treated as unique based on its position, not on its value. So if the input elements are unique, there will be no repeat values in each combination. 




import numpy
 
 
def n_length_combo(iterable, r):
     
    char = tuple(iterable)
    n = len(char)
     
    if r > n:
        return
     
    index = numpy.arange(r)
     
    # returns the first sequence 
    yield tuple(char[i] for i in index)
     
    while True:
         
        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return
         
        index[i] += 1
         
        for j in range(i + 1, r):
             
            index[j] = index[j-1] + 1
             
        yield tuple(char[i] for i in index)
         
# Driver code
print([x for x in n_length_combo("abc", 2)])
"""

def perm(arr,n,k):
    k = [1,2,3]
    l = len(k)
    arr = []*n
    curr = 0
    ct = 0
    for i in range(l):
        for j in range(l-i):
            for j in range(l-i):
                if k[i] + curr <= n:
                    curr = k[i] + curr


def perm(arr,n,k):
    k = [1,2,3]
    l = len(k)
    arr = []*n
    curr = 0
    ct = 0
    for i in range(l):
        n // k[i] = x
        n // k[i+1] = y
        n // k[i+2] = z

        if n%k[i] == 0:
            ct += 1
        if n%k[i]%k[i+1] == 0:
            ct += 1
        if n%k[i]%k[i+1]%k[i+2] == 0:
            ct += 1
        for j in range(l-i):




from functools import reduce
a = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x + y, a)

print(res)

import functools

# importing operator for operator functions
import operator

# initializing list
a = [1, 3, 5, 6, 2]

# using reduce with add to compute sum of list
print(functools.reduce(operator.add, a))

# using reduce with mul to compute product
print(functools.reduce(operator.mul, a))

# using reduce with add to concatenate string
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))


from itertools import accumulate
from operator import add

# Cumulative sum with accumulate
a = [1, 2, 3, 4, 5]
res = accumulate(a, add)

print(list(res))















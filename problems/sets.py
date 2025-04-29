
"""
In Python, a set cannot directly contain another set as an element because sets are mutable, and their elements must be immutable. Attempting to add a mutable object like a set into another set will result in a TypeError. To achieve a set containing other sets, the inner sets must be converted to frozenset objects, which are immutable.
Python

set1 = frozenset({1, 2, 3})
set2 = frozenset({4, 5, 6})
main_set = {set1, set2}
print(main_set)
# Expected output: {frozenset({1, 2, 3}), frozenset({4, 5, 6})}
Operations on these sets are similar to regular sets, but the immutability of frozenset must be considered. For instance, you cannot add or remove elements from a frozenset after it's created.
Python

set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})

# Union
union_set = set1 | set2
print(union_set)
# Expected output: frozenset({1, 2, 3, 4, 5})

# Intersection
intersection_set = set1 & set2
print(intersection_set)
# Expected output: frozenset({3})

# Difference
difference_set = set1 - set2
print(difference_set)
# Expected output: frozenset({1, 2})

"""



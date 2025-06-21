
# list is a dynamic array

import sys

l = []
print(sys.getsizeof(l))  # how space it is taking in ram
l.append("hello")
print(sys.getsizeof(l))
l.append('world')
print(sys.getsizeof(l))
l.append(1)
print(sys.getsizeof(l))
l.append(2)
print(sys.getsizeof(l))
l.append(3)
print(sys.getsizeof(l))
l.append(4)
print(sys.getsizeof(l))
l.append(5)
print(sys.getsizeof(l))
l.append(6)
print(sys.getsizeof(l))
l.append(7)
print(sys.getsizeof(l))
l.append(8)
print(sys.getsizeof(l))
"""
56
88
88
88
88
120
120
120
120
184
184
the array size is inc by 8 bytes
"""











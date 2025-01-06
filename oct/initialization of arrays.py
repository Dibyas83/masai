n = 3
m = 2
multi_list = [[0 for j in range(m+1)] for i in range(n+1)]
for i in range(n):
    bag = ""
    for j in range(m):
        bag += str(multi_list[i][j]) + " "
    print(bag)
""" # initializes all the 10 spaces with 0’s
a = [0] * 10 
print("Intitialising empty list with zeros: ", a)

# initializes all the 10 spaces with None
b = [None] * 10
print("Intitialising empty list of None: ", b)

# initializes a 4 by 3 array matrix all with 0's
c =  [[0] * 4] * 3
print("Intitialising 2D empty list of zeros: ", c)

# empty list which is not null, it's just empty.
d = []
print("Intitialising empty list of zeros: ", d)
"""

""" # initialize the spaces with 0’s with 
# the help of list comprehensions
a = [0 for x in range(10)]
print(a)

b = [[0] * 4 for i in range(3)]
print(b)
"""
""" b= []
for x in range(5):
    b.append([[]])
          
print(b)

c = []
for x in range(5):
    c.append(0)
    
print(c)
"""

""" import numpy

# create a simple array with numpy empty()
a = numpy.empty(5, dtype=object)
print(a)

# create multi-dim array by providing shape
matrix = numpy.empty(shape=(2, 5), dtype='object')
print(matrix)
"""

""" import itertools

#Initialize empty array with length 10 filled with 0's
a = list(itertools.repeat(0, 10))
print(a)

#Initialize 2D empty array with 3 rows and 4 columns filled with 0's
b = [list(itertools.repeat(0, 4)) for i in range(3)]
print(b)
"""

























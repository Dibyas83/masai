"""
rows = 3
cols = 2

mat = [[0 for _ in range(cols)] for _ in range(rows)]
print(f'matrix of dimension {rows} x {cols} is {mat}')

# editing the individual elements
mat[0][0], mat[0][1] = 1,2
mat[1][0], mat[1][1] = 3,4
mat[2][0], mat[2][1] = 5,6
print(f'modified matrix is {mat}')

# checking the memory address of first element of a row
print(f'addr(mat[0][0]) = {id(mat[0][0])}, addr(mat[0][1]) = {id(mat[0][1])}')
print(f'addr(mat[1][0]) = {id(mat[1][0])}, addr(mat[1][1]) = {id(mat[1][1])}')
print(f'addr(mat[2][0]) = {id(mat[2][0])}, addr(mat[2][1]) = {id(mat[2][1])}')

"""
"""
import numpy as np

rows = 3
cols = 2
size = rows*cols

mat = np.array([0]*size).reshape(rows,cols)

"""
"""
rows = 3
cols = 2

mat = [[0 for _ in range(cols)]]*rows
print(f'matrix with dimension {rows} x {cols} is {mat}')

# editing the individual elements 
mat[0][0], mat[0][1] = 1,2
mat[1][0], mat[1][1] = 3,4
mat[2][0], mat[2][1] = 5,6
print(f'modified matrix is {mat}')

# checking the memory address of first element of a row
print(f'addr(mat[0][0]) = {id(mat[0][0])}, addr(mat[0][1]) = {id(mat[0][1])}')
print(f'addr(mat[1][0]) = {id(mat[1][0])}, addr(mat[1][1]) = {id(mat[1][1])}')
print(f'addr(mat[2][0]) = {id(mat[2][0])}, addr(mat[2][1]) = {id(mat[2][1])}')

"""
"""
rows = 3
cols = 2
 
mat = [[0]*cols for _ in range(rows)]
print(f'matrix with dimension {rows} x {cols} is {mat}')
 
# editing the individual elements 
mat[0][0], mat[0][1] = 1,2
mat[1][0], mat[1][1] = 3,4
mat[2][0], mat[2][1] = 5,6
print(f'modified matrix is {mat}')
 
# checking the memory address of first element of a row
print(f'addr(mat[0][0]) = {id(mat[0][0])}, addr(mat[0][1]) = {id(mat[0][1])}')
print(f'addr(mat[1][0]) = {id(mat[1][0])}, addr(mat[1][1]) = {id(mat[1][1])}')
print(f'addr(mat[2][0]) = {id(mat[2][0])}, addr(mat[2][1]) = {id(mat[2][1])}')
"""
"""
rows = 3
cols = 2

mat = [[0]*cols]*rows
print(f'matrix with dimension {rows} x {cols} is {mat}')

# editing the individual elements 
mat[0][0], mat[0][1] = 1,2
mat[1][0], mat[1][1] = 3,4
mat[2][0], mat[2][1] = 5,6
print(f'modified matrix is {mat}')

# checking the memory address of first element of a row
print(f'addr(mat[0][0]) = {id(mat[0][0])}, addr(mat[0][1]) = {id(mat[0][1])}')
print(f'addr(mat[1][0]) = {id(mat[1][0])}, addr(mat[1][1]) = {id(mat[1][1])}')
print(f'addr(mat[2][0]) = {id(mat[2][0])}, addr(mat[2][1]) = {id(mat[2][1])}')

"""
















"""
# Python3 code to demonstrate working of
# Initialize list with empty dictionaries
# using {} + "*" operator

# Initialize list with empty dictionaries
# using {} + "*" operator
res = [{}] * 6

print("The list of empty dictionaries is : " + str(res))

"""

"""
# Python3 code to demonstrate working of
# Initialize list with empty dictionaries
# using {} + list comprehension

# Initialize list with empty dictionaries
# using {} + "*" operator
res = [{} for sub in range(6)]

print("The list of empty dictionaries is : " + str(res))

"""
"""
import itertools

def init_list_dict(n):
	# using itertools.repeat to repeat the empty dictionary n times
	return list(itertools.repeat({}, n))

res = init_list_dict(6)
print("The list of empty dictionaries is : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy

"""
"""
# Initialize list with empty dictionaries using a for loop
n = 6
res = []
for i in range(n):
	res.append({})
print("The list of empty dictionaries is : " + str(res))

"""
"""
res = [{} for _ in range(6)]
print("The list of empty dictionaries is: " + str(res))

"""
"""
# Initialize list with empty dictionaries using dict() function
res = [dict() for i in range(6)]

print("The list of empty dictionaries is : " + str(res))

"""
"""
# Python3 code to demonstrate working of 
# Convert Dictionaries List to Order Key Nested dictionaries
# Using loop + enumerate()

# initializing lists
test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8, "Good" : 2}, {"Best": 10, "CS" : 1}]

# printing original list
print("The original list : " + str(test_list))

# using enumerate() to extract key to map with dict values 
res = dict()
for idx, val in enumerate(test_list):
	res[idx] = val
	
# printing result 
print("The constructed dictionary : " + str(res))

"""
"""
# Python3 code to demonstrate working of 
# Convert Dictionaries List to Order Key Nested dictionaries
# Using dictionary comprehension + enumerate() 

# initializing lists
test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8, "Good" : 2}, {"Best": 10, "CS" : 1}]

# printing original list
print("The original list : " + str(test_list))

# dictionary comprehension encapsulating result as one liner
res = {idx : val for idx, val in enumerate(test_list)}
	
# printing result 
print("The constructed dictionary : " + str(res))

"""
"""
# Initializing the list
test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8, "Good" : 2}, {"Best": 10, "CS" : 1}]

# Using a dictionary comprehension with enumerate() to create a dictionary
# The enumerate() function returns tuples of the form (index, value) for each element in the list
# We use these tuples to map the index to the corresponding dictionary in the list
res = {i: val for i, val in enumerate(test_list)}

# Printing the resulting dictionary
print("The constructed dictionary : " + str(res))

"""
"""
This method maps each element of the given iterable (in this case, the list test_list) to the corresponding tuple of the form (index, value) using enumerate(), and then creates a dictionary using these tuples as key-value pairs.


test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8, "Good" : 2}, {"Best": 10, "CS" : 1}]

# Using map() with enumerate() to create a dictionary
res = dict(map(lambda x: (x[0], x[1]), enumerate(test_list)))

# Printing the resulting dictionary
print("The constructed dictionary : " + str(res))

"""
"""
test_list = [{"Gfg": 3, 4: 9}, {"is": 8, "Good": 2}, {"Best": 10, "CS": 1}]

# using zip() to combine the list with a range of indices
res = {i: d for i, d in zip(range(len(test_list)), test_list)}

# printing result
print("The constructed dictionary : " + str(res))

"""

























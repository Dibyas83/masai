
# can move down or right on grid m (rows) * n(col)
# (0,0) no grid - gives 0
#if grid is (1,1) one dimensional and nothing to do anymore - which is the base case
# grid(0,1) and (1,0) are invalid - gives 0

# grid size decreases finally to 1,1,so this has overlapping conditions
"""
                             2,3 =3 ways
      down-child(reduce row)      right-child(red col)
            1,3=1                           2,2=2

      0,3       1,2=0+1             1,2=1          2,1=1

            0,2=0     1,1=1      0,2    1,1      1,1   2,0
all with 0 will return 0 and 1,1 will return 1
if there was diagonal movement then 2,3 -> 1,2
"""
def ways(m,n):
    if m == 1 and n==1:
        return 1
    if m== 0 or n == 0:
        return 0
    else:
        return ways(m-1,n) + ways(m,n-1) # this is the smallest structure with base case

print(ways(3,3))
print(ways(3,2))
print(ways(2,3))
# tc = 2**(n+m),space comp is levels n+m
#--------------------------------------
# 2,3 will give same no of ways that 3,2 will give - this will be used in memoization

def memo_ways(m1,n1,dict1):
    if (m1,n1) in dict1:
        return dict1[(m1,n1)]

    if m1 == 1 and n1==1:
        return 1
    if m1== 0 or n1 == 0:
        return 0
    else:
        dict1[(m1,n1)] = memo_ways(m1-1,n1,dict1) + memo_ways(m1,n1-1,dict1) #store
        return  dict1[(m1,n1)]# return the same
dict1 = {}
print(memo_ways(10,10,dict1),"memo")
print(memo_ways(3,2,dict1))
print(memo_ways(2,3,dict1))

#tc = m*n(duplicates removed)   ,space comp = n+m
#-----------------------------------------------------------
# Initialize an empty dictionary to represent the grid
grid_dict = {}

# Define the dimensions of your conceptual grid (optional, for reference)
rows = 3
cols = 4

# Assign values to specific cells in the grid
grid_dict[(0, 0)] = 'A'  # Row 0, Column 0
grid_dict[(0, 1)] = 'B'  # Row 0, Column 1
grid_dict[(1, 2)] = 'C'  # Row 1, Column 2
grid_dict[(2, 3)] = 'D'  # Row 2, Column 3

# Access values from the grid
print(f"Value at (0, 0): {grid_dict[(0, 0)]}")
print(f"Value at (1, 2): {grid_dict[(1, 2)]}")

# Check if a coordinate exists in the grid
if (1, 1) in grid_dict:
    print(f"Value at (1, 1): {grid_dict[(1, 1)]}")
else:
    print("No value at (1, 1).")

# Iterate through the stored grid cells
print("\nStored grid cells:")
for coord, value in grid_dict.items():
    print(f"Coordinate: {coord}, Value: {value}")

"""
Explanation:
grid_dict = {}:
An empty dictionary is initialized to hold the grid data.
grid_dict[(row, col)] = value:
Each cell in the grid is represented by a key-value pair. The key is a tuple (row, col) representing the coordinates, and the value is the data stored at that cell.
Accessing values:
You can access the value at a specific coordinate by using the tuple (row, col) as the key, e.g., grid_dict[(0, 0)].
Checking for existence:
The in operator can be used to check if a specific coordinate exists as a key in the dictionary before attempting to access its value, which helps prevent KeyError.
Iterating:
You can iterate through all the stored cells using a for loop with grid_dict.items(), which returns key-value pairs (coordinate-value pairs in this case).
This method provides a flexible and efficient way to manage 2D grid data, especially when the grid is not fully populated
"""
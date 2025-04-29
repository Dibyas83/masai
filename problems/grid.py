rows, cols = 3, 3  # Example dimensions
grid = [[None for _ in range(cols)] for _ in range(rows)]


for _ in range(rows):
    for _ in range(cols):
        row_index = int(input("Enter row index: "))
        col_index = int(input("Enter column index: "))
        value = input("Enter value for the grid: ")
        if 0 <= row_index < rows and 0 <= col_index < cols:
            grid[row_index][col_index] = value
            print("Grid updated successfully!")
        else:
            print("Invalid row or column index.")

def print_grid(grid):
    for row in grid:
        print(row)

print_grid(grid)

#-------------
class WorldMap (object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        world = []
        for i in range(self.width):
            world.append(None)
            for j in range(self.height):
                world[i].append(None)



class WorldMap2(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[None for x in range(self.width)] for y in range(self.height)]

"""
# initializing an empty matrix
matrix = []
# taking 2x2 matrix from the user
for i in range(2):
   # taking row input from the user
   row = list(map(int, input().split()))
   # appending the 'row' to the 'matrix'
   matrix.append(row)
# printing the matrix
print(matrix)

-----------

# initializing an empty matrix
matrix = []
# taking 2x2 matrix from the user
for i in range(2):
   # empty row
   row = []
   for j in range(2):
      # asking the user to input the number
      # converts the input to int as the default one is string
      element = int(input())
      # appending the element to the 'row'
      row.append(element)
   # appending the 'row' to the 'matrix'
   matrix.append(row)
# printing the matrix
print(matrix)


"""







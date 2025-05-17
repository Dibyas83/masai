
"""
Longest Possible Route in a Matrix with Hurdles
Last Updated : 04 Jun, 2023
Given an M x N matrix, with a few hurdles arbitrarily placed, calculate the length of the longest
 possible route possible from source to a destination within the matrix. We are allowed to move to
 only adjacent cells which are not hurdles. The route cannot contain any diagonal moves and a location
  once visited in a particular path cannot be visited again.

For example, the longest path with no hurdles from source to destination is highlighted below. The
length of the path is 24.



The idea is to use Backtracking. We start from the source cell of the matrix, move forward in all
four allowed directions, and recursively checks if they lead to the solution or not. If the destination
is found, we update the value of the longest path else if none of the above solutions work we return
false from our function.

Below is the implementation of the above idea

Try it on GfG Practice
redirect icon

"""

# Python program to find Longest Possible Route in a
# matrix with hurdles
import sys
R,C = 3,10

# A Pair to store status of a cell. found is set to
# True if destination is reachable and value stores
# distance of longest path
class Pair:

    def __init__(self, found, value):
        self.found = found
        self.value = value

# Function to find Longest Possible Route in the
# matrix with hurdles. If the destination is not reachable
# the function returns false with cost sys.maxsize.
# (i, j) is source cell and (x, y) is destination cell.
def findLongestPathUtil(mat, i, j, x, y, visited):

    # if (i, j) itself is destination, return True
    if i == x and j == y:
        p = Pair( True, 0 )
        return p

    # if not a valid cell, return false
    if i < 0 or i >= R or j < 0 or j >= C or mat[i][j] == 0 or visited[i][j]: # 0 is blocked and visited should not be crossed
        p = Pair( False, sys.maxsize )

        return p

    # include (i, j) in current path i.e.
    # set visited(i, j) to True
    visited[i][j] = True

    # res stores longest path from current cell (i, j) to a destination cell (x, y)
    res = -sys.maxsize -1

    # go left from current cell
    sol = findLongestPathUtil(mat, i, j - 1, x, y, visited)

    # if destination can be reached on going left from
    # current cell, update res
    if (sol.found): #  A Pair to store status of a cell. found is set to
# True if destination is reachable and value stores distance of longest path
        res = max(res, sol.value)

    # go right from current cell
    sol = findLongestPathUtil(mat, i, j + 1, x, y, visited)

    # if destination can be reached on going right from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # go up from current cell
    sol = findLongestPathUtil(mat, i - 1, j, x, y, visited)

    # if destination can be reached on going up from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # go down from current cell
    sol = findLongestPathUtil(mat, i + 1, j, x, y, visited)

    # if destination can be reached on going down from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # Backtrack
    visited[i][j] = False # could not be reached or visited in recursive move

    # if destination can be reached from current cell,
    # return True
    if (res != -sys.maxsize -1):
        p = Pair( True, 1 + res )
        print(visited)
        return p

    # if destination can't be reached from current cell,
    # return false
    else:
        p = Pair( False, sys.maxsize )
        return p

# A wrapper function over findLongestPathUtil()
def findLongestPath(mat, i, j, x,y):

    # create a boolean matrix to store info about
    # cells already visited in current route
    # initialize visited to false
    visited = [[False for i in range(C)]for j in range(R)]

    # find longest route from (i, j) to (x, y) and
    # print its maximum cost
    p = findLongestPathUtil(mat, i, j, x, y, visited)

    if (p.found):
        print("Length of longest possible route is ",str(p.value))


    # If the destination is not reachable
    else:
        print("Destination not reachable from given source")

# Driver code

# input matrix with hurdles shown with number 0
mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

# find longest path with source (0, 0) and
# destination (1, 7)
findLongestPath(mat, 0, 0, 1, 7)
"""
# This code is contributed by shinjanpatra
Output
Length of longest possible route is 24
Time Complexity: 4^(R*C), Here R and C are the numbers of rows and columns respectively. For every index we
 have four options, so our overall time complexity will become 4^(R*C).
Auxiliary Space: O(R*C), The extra space is used in storing the elements of the visited matrix.

An approach without using any extra space:
Below is the step-by-step approach:

Start from the source cell.
Explore all possible directions (right, down, left, up) from the current cell.
If a valid adjacent cell is found (within the boundaries of the matrix and has a value of 1), move 
to that cell and increment the current path length.
Recursively repeat steps 2 and 3 for the new cell.
If the destination cell is reached, compare the current path length with the longest path length found 
so far and update it if necessary.
Backtrack by undoing the move (mark the current cell as visited) and continue exploring other directions.
Repeat steps 2-6 until all possible paths are explored.
Return the longest path length as the result.
Below is the implementation:


"""

# Function for finding the longest path
# 'ans' is -1 if we can't reach
# 'cur' is the number of steps we have traversed


def findLongestPath(mat, i, j, di, dj, n, m, cur=0, ans=-1): # di,dj are destinations
    # If we reach the destination
    if i == di and j == dj:
        # If current path steps are more than previous path steps
        if cur > ans:
            ans = cur
        return ans

    # if the source or destination is a hurdle itself
    if mat[i][j]==0 or mat[di][dj]==0:
        return ans
    # Mark as visited
    mat[i][j] = 0 # as hurdle if visited

    # Checking if we can reach the destination going right
    if j != m-1 and mat[i][j+1] > 0:
        ans = findLongestPath(mat, i, j+1, di, dj, n, m, cur+1, ans)

    # Checking if we can reach the destination going down
    if i != n-1 and mat[i+1][j] > 0:
        ans = findLongestPath(mat, i+1, j, di, dj, n, m, cur+1, ans)

    # Checking if we can reach the destination going left
    if j != 0 and mat[i][j-1] > 0:
        ans = findLongestPath(mat, i, j-1, di, dj, n, m, cur+1, ans)

    # Checking if we can reach the destination going up
    if i != 0 and mat[i-1][j] > 0:
        ans = findLongestPath(mat, i-1, j, di, dj, n, m, cur+1, ans)

    # Marking visited to backtrack
    mat[i][j] = 1 # make it iterable again for backtrsck solving

    # Returning the answer we got so far
    return ans

mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
"""

mat = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
"""
# Find the longest path with source (0, 0) and destination (2, 3)
vis = [[False for _ in mat[0]] for x in mat]
print(findLongestPath(mat, 0, 0, 2, 3, len(mat), len(mat[0])))
"""
Output
9
Time Complexity: O(4^N), where N is the number of cells in the matrix. This is because, at each cell, there are four possible directions to explore (right, down, left, up), and the maximum depth of the recursion is N.
Auxiliary Space: O(1)

"""
"""
Longest Possible Route in a Matrix with Hurdles
Last Updated : 04 Jun, 2023
Given an M x N matrix, with a few hurdles arbitrarily placed, calculate the length of the longest
possible route possible from source to a destination within the matrix. We are allowed to move to
only adjacent cells which are not hurdles. The route cannot contain any diagonal moves and a location
once visited in a particular path cannot be visited again.

For example, the longest path with no hurdles from source to destination is highlighted below.
The length of the path is 24.

The idea is to use Backtracking. We start from the source cell of the matrix, move forward in
all four allowed directions, and recursively checks if they lead to the solution or not. If 
the destination is found, we update the value of the longest path else if none of the above 
solutions work we return false from our function.

Below is the implementation of the above idea 

Try it on GfG Practice
redirect icon


"""
# Python program to find Longest Possible Route in a
# matrix with hurdles
import sys
R,C = 3,10
 
# A Pair to store status of a cell. found is set to
# True of destination is reachable and value stores
# distance of longest path
class Pair:
     
    def __init__(self, found, value):
        self.found = found 
        self.value = value
 
# Function to find Longest Possible Route in the
# matrix with hurdles. If the destination is not reachable
# the function returns false with cost sys.maxsize.
# (i, j) is source cell and (x, y) is destination cell.
def find_Longest_Path_Util(mat, i, j, x, y, visited):
    # if (i, j) itself is destination, return True
    if i == x and j == y:
        p = Pair( True, 0 )
        return p
     
    # if not a valid cell, return false
    if i < 0 or i >= R or j < 0 or j >= C or mat[i][j] == 0 or visited[i][j]:
        p = Pair( False, sys.maxsize )
        return p
 
    # include (i, j) in current path i.e.
    # set visited(i, j) to True
    visited[i][j] = True
 
    # res stores longest path from current cell (i, j) to
    # destination cell (x, y)
    res = -sys.maxsize -1
 
    # go left from current cell
    sol = findLongestPathUtil(mat, i, j - 1, x, y, visited)
 
    # if destination can be reached on going left from
    # current cell, update res
    if sol.found:
        res = max(res, sol.value)
 
    # go right from current cell
    sol = findLongestPathUtil(mat, i, j + 1, x, y, visited)
 
    # if destination can be reached on going right from
    # current cell, update res
    if sol.found:
        res = max(res, sol.value)
 
    # go up from current cell
    sol = findLongestPathUtil(mat, i - 1, j, x, y, visited)
 
    # if destination can be reached on going up from
    # current cell, update res
    if sol.found:
        res = max(res, sol.value)
 
    # go down from current cell
    sol = findLongestPathUtil(mat, i + 1, j, x, y, visited)
 
    # if destination can be reached on going down from
    # current cell, update res
    if sol.found:
        res = max(res, sol.value)
 
    # Backtrack
    visited[i][j] = False
 
    # if destination can be reached from current cell,
    # return True
    if res != -sys.maxsize -1:
        p = Pair( True, 1 + res )
        return p
     
    # if destination can't be reached from current cell,
    # return false
    else:
        p = Pair( False, sys.maxsize )
        return p
 
# A wrapper function over findLongestPathUtil()
def findLongestPath(mat, i, j, x,y):
 
    # create a boolean matrix to store info about
    # cells already visited in current route
    # initialize visited to false
    visited = [[False for i in range(C)]for j in range(R)]
 
    # find longest route from (i, j) to (x, y) and
    # print its maximum cost
    p = findLongestPathUtil(mat, i, j, x, y, visited)
    if p.found:
        print("Length of longest possible route is ",str(p.value))
 
    # If the destination is not reachable
    else:
        print("Destination not reachable from given source")
 
# Driver code
 
# input matrix with hurdles shown with number 0
mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
 
# find longest path with source (0, 0) and
# destination (1, 7)
findLongestPath(mat, 0, 0, 1, 7)
"""
# This code is contributed by shinjanpatra


An approach without using any extra space:
Below is the step-by-step approach:

Start from the source cell.
Explore all possible directions (right, down, left, up) from the current cell.
If a valid adjacent cell is found (within the boundaries of the matrix and has a value of 1), move to that cell and increment the current path length.
Recursively repeat steps 2 and 3 for the new cell.
If the destination cell is reached, compare the current path length with the longest path length found so far and update it if necessary.
Backtrack by undoing the move (mark the current cell as visited) and continue exploring other directions.
Repeat steps 2-6 until all possible paths are explored.
Return the longest path length as the result.
Below is the implementation:




# Function for finding the longest path
# 'ans' is -1 if we can't reach
# 'cur' is the number of steps we have traversed
 
 
def findLongestPath(mat, i, j, di, dj, n, m, cur=0, ans=-1):
    # If we reach the destination
    if i == di and j == dj:
        # If current path steps are more than previous path steps
        if cur > ans:
            ans = cur
        return ans
 
    # if the source or destination is a hurdle itself
      if mat[i][j]==0 or mat[di][dj]==0:
      return ans
    # Mark as visited
    mat[i][j] = 0
 
    # Checking if we can reach the destination going right
    if j != m-1 and mat[i][j+1] > 0:
        ans = findLongestPath(mat, i, j+1, di, dj, n, m, cur+1, ans)
 
    # Checking if we can reach the destination going down
    if i != n-1 and mat[i+1][j] > 0:
        ans = findLongestPath(mat, i+1, j, di, dj, n, m, cur+1, ans)
 
    # Checking if we can reach the destination going left
    if j != 0 and mat[i][j-1] > 0:
        ans = findLongestPath(mat, i, j-1, di, dj, n, m, cur+1, ans)
 
    # Checking if we can reach the destination going up
    if i != 0 and mat[i-1][j] > 0:
        ans = findLongestPath(mat, i-1, j, di, dj, n, m, cur+1, ans)
 
    # Marking visited to backtrack
    mat[i][j] = 1
 
    # Returning the answer we got so far
    return ans
 
 
mat = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
 
# Find the longest path with source (0, 0) and destination (2, 3)
vis = [[False for _ in mat[0]] for x in mat]
print(findLongestPath(mat, 0, 0, 2, 3, len(mat), len(mat[0])))
"""








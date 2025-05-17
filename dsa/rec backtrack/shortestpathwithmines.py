
"""
Find shortest safe route in a path with landmines
Last Updated : 22 Dec, 2023
Given a path in the form of a rectangular matrix having few landmines arbitrarily placed (marked as 0), calculate length of the shortest safe route possible from any cell in the first column to any cell in the last column of the matrix. We have to avoid landmines and their four adjacent cells (left, right, above and below) as they are also unsafe. We are allowed to move to only adjacent cells which are not landmines. i.e. the route cannot contains any diagonal moves.

Examples:

Input:
A 12 x 10 matrix with landmines marked as 0

[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  0  1  1  1  1  1  1  1  1 ]
[ 1  1  1  0  1  1  1  1  1  1 ]
[ 1  1  1  1  0  1  1  1  1  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  1  1  1  1  0  1  1  1  1 ]
[ 1  0  1  1  1  1  1  1  0  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 0  1  1  1  1  0  1  1  1  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  1  1  0  1  1  1  1  1  1 ]

Output:
Length of shortest safe route is 13 (Highlighted in Bold)
The idea is to use Backtracking. We first mark all adjacent cells of the landmines as unsafe. Then for each safe cell of first column of the matrix, we move forward in all allowed directions and recursively checks if they leads to the destination or not. If destination is found, we update the value of shortest path else if none of the above solutions work we return false from our function.

Below is the implementation of above idea:

Try it on GfG Practice
redirect icon



# Python3 program to find shortest safe Route
# in the matrix with landmines
import sys

R = 12
C = 10

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [ -1, 0, 0, 1 ]
colNum = [ 0, -1, 1, 0 ]

min_dist = sys.maxsize

# A function to check if a given cell (x, y)
# can be visited or not
def isSafe(mat, visited, x, y):

    if (mat[x][y] == 0 or visited[x][y]):
        return False

    return True

# A function to check if a given cell (x, y) is
# a valid cell or not
def isValid(x, y):

    if (x < R and y < C and x >= 0 and y >= 0):
        return True

    return False

# A function to mark all adjacent cells of
# landmines as unsafe. Landmines are shown with
# number 0
def markUnsafeCells(mat):

    for i in range(R):
        for j in range(C):
            # If a landmines is found
            if (mat[i][j] == 0):
                # Mark all adjacent cells
                for k in range(4):
                    if (isValid(i + rowNum[k], j + colNum[k])):
                        mat[i + rowNum[k]][j + colNum[k]] = -1

    # Mark all found adjacent cells as unsafe
    for i in range(R):
        for j in range(C):
            if (mat[i][j] == -1):
                mat[i][j] = 0

    Uncomment below lines to print the path
    /*
     * for (int i = 0; i < R; i++) {
     * for (int j = 0; j < C; j++) { cout <<
     * std::setw(3) << mat[i][j]; } cout << endl; }
     *"""

# Function to find shortest safe Route in the
# matrix with landmines
# mat[][] - binary input matrix with safe cells marked as 1
# visited[][] - store info about cells already visited in
# current route
# (i, j) are coordinates of the current cell
# min_dist --> stores minimum cost of shortest path so far
# dist --> stores current path cost
def findShortestPathUtil(mat, visited, i, j, dist):

    global min_dist

    # If destination is reached
    if (j == C - 1):
        # Update shortest path found so far
        min_dist = min(dist, min_dist)
        return

    # If current path cost exceeds minimum so far
    if (dist > min_dist):
        return

    # include (i, j) in current path
    visited[i][j] = True

    # Recurse for all safe adjacent neighbours
    for k in range(4):
        if (isValid(i + rowNum[k], j + colNum[k]) and isSafe(mat, visited, i + rowNum[k], j + colNum[k])):
            findShortestPathUtil(mat, visited, i + rowNum[k], j + colNum[k], dist + 1)

    # Backtrack
    visited[i][j] = False

# A wrapper function over findshortestPathUtil()
def findShortestPath(mat):

    global min_dist

    # Stores minimum cost of shortest path so far
    min_dist = sys.maxsize

    # Create a boolean matrix to store info about
    # cells already visited in current route
    visited = [[False for i in range(C)] for j in range(R)]

    # Mark adjacent cells of landmines as unsafe
    markUnsafeCells(mat)

    # Start from first column and take minimum
    for i in range(R):
        # If path is safe from current cell
        if (mat[i][0] == 1):
            # Find shortest route from (i, 0) to any
            # cell of last column (x, C - 1) where
            # 0 <= x < R
            findShortestPathUtil(mat, visited, i, 0, 0)

            # If min distance is already found
            if (min_dist == C - 1):
                break

    # If destination can be reached
    if (min_dist != sys.maxsize):
        print("Length of shortest safe route is", min_dist)
    else:
        # If the destination is not reachable
        print("Destination not reachable from given source")

mat = [
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ] ]
""" 
# Find shortest path
findShortestPath(mat)
 
# This code is contributed by mukesh07.
Output
Length of shortest safe route is 13
Time Complexity: O(4^(R * C)), where R is number of rows and C are the number of columns in the given matrix.
Auxiliary Space: O(R * C), as we are using extra space like visted[R][C].

Another method: It can be solved in polynomial time with the help of Breadth First Search. Enqueue the cells with 1 value in the queue with the distance as 0. As the BFS proceeds, shortest path to each cell from the first column is computed. Finally for the reachable cells in the last column, output the minimum distance.

The implementation in C++ is as follows: 

"""

""" 
# Python program to find shortest safe Route in
# the matrix with landmines
import sys
 
R = 12
C = 10
 
class Key:
    def __init__(self,i, j):
        self.x = i
        self.y = j
 
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [ -1, 0, 0, 1 ]
colNum = [ 0, -1, 1, 0 ]
 
# A function to check if a given cell (x, y) is
# a valid cell or not
def isValid(x, y):
 
    if (x < R and y < C and x >= 0 and y >= 0):
        return True
 
    return False
 
# A function to mark all adjacent cells of
# landmines as unsafe. Landmines are shown with
# number 0
def findShortestPath(mat):
 
    for i in range(R):
        for j in range(C):
            # if a landmines is found
            if (mat[i][j] == 0):
                # mark all adjacent cells
                for k in range(4):
                    if (isValid(i + rowNum[k], j + colNum[k])):
                        mat[i + rowNum[k]][j + colNum[k]] = -1
             
    # mark all found adjacent cells as unsafe
    for i in range(R):
        for j in range(C):
            if (mat[i][j] == -1):
                mat[i][j] = 0
 
    dist = [[-1 for i in range(C)]for j in range(R)]
 
    q = []
 
    for i in range(R):
        if(mat[i][0] == 1):
            q.append(Key(i,0))
            dist[i][0] = 0
 
    while(len(q) != 0):
        k = q[0]
        q = q[1:]
 
        d = dist[k.x][k.y]
 
        x = k.x
        y = k.y
 
        for k in range(4):
            xp = x + rowNum[k]
            yp = y + colNum[k]
            if(isValid(xp,yp) and dist[xp][yp] == -1 and mat[xp][yp] == 1):
                dist[xp][yp] = d+1
                q.append(Key(xp,yp))
     
    # stores minimum cost of shortest path so far
    ans = sys.maxsize
 
    # start from first column and take minimum
    for i in range(R):
        if(mat[i][C-1] == 1 and dist[i][C-1] != -1):
            ans = min(ans,dist[i][C-1])
 
     
    # if destination can be reached
    if(ans == sys.maxsize):
        print("NOT POSSIBLE")
         
    else:  # if the destination is not reachable
        print(f"Length of shortest safe route is {ans}")
 
# Driver code
     
# input matrix with landmines shown with number 0
mat =[
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]
]
     
# find shortest path
findShortestPath(mat)
 
# This code is contributed by shinjanpatra
Output
Length of shortest safe route is 13
Time Complexity: O(r * c), where r and c are the number of rows and columns in the given matrix respectively.
Auxiliary Space: O(r * c)

"""











"""
Given an M x N matrix where each element can either be 0 or 1. We need to find the shortest path between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1.

Note: You can move into an adjacent cell in one of the four directions, Up, Down, Left, and Right if that adjacent cell is filled with element 1.

Example:

Input: mat[][] = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1]], source = [0, 1], destination = {2, 2}
Output: 3
Explanation: The path is (0, 1) -> (1, 1) -> (2, 1) – > (2, 2) (the same is highlighted below)
1 1 1 1
1 1 0 1
1 1 1 1
1 1 0 0
1 0 0 1


Input: mat[][] = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0 ] , [1, 0, 1, 0, 1]], source = {0, 0}, destination = {3, 4}
Output: -1
Explanation: The path is not possible between source and destination, hence return -1.


Try it on GfG Practice
redirect icon
[Naive Approach] – Using DFS
The idea for this approach is to use Recursion to explore all possible paths at every step starting from the given source cell in the matrix and backtrack if the destination is not reached and also keep track of visited cells using an array.





1
import sys
2
​
3
# User defined Pair class
4
class Pair:
5
    def __init__(self, x, y):
6
        self.first = x
7
        self.second = y
8
​
9
# Check if it is possible to go to (x, y) from the current
10
# position. The function returns false if the cell has
11
# value 0 or already visited
12
def isSafe(mat, visited, x, y):
13
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] == 1 and (not visited[x][y]))
14
​
15
def shortPath(mat, visited, i, j, x, y, min_dist, dist):
16
    if (i == x and j == y):
17
        min_dist = min(dist, min_dist)
18
        return min_dist
19
​
20
    # set (i, j) cell as visited
21
    visited[i][j] = True
22

23
    # go to the bottom cell
24
    if (isSafe(mat, visited, i + 1, j)):
25
        min_dist = shortPath(
26
            mat, visited, i + 1, j, x, y, min_dist, dist + 1)
27
​
28
    # go to the right cell
29
    if (isSafe(mat, visited, i, j + 1)):
30
        min_dist = shortPath(
31
            mat, visited, i, j + 1, x, y, min_dist, dist + 1)
32
​
33
    # go to the top cell
34
    if (isSafe(mat, visited, i - 1, j)):
35
        min_dist = shortPath(
36
            mat, visited, i - 1, j, x, y, min_dist, dist + 1)
37
​
38
    # go to the left cell
39
    if (isSafe(mat, visited, i, j - 1)):
40
        min_dist = shortPath(
41
            mat, visited, i, j - 1, x, y, min_dist, dist + 1)
42
​
43
    # backtrack: remove (i, j) from the visited matrix
44
    visited[i][j] = False
45
    return min_dist
46
​
47
# Wrapper over shortPath() function
48
def shortPathLength(mat, src, dest):
49
    if (len(mat) == 0 or mat[src.first][src.second] == 0
50
            or mat[dest.first][dest.second] == 0):
51
        return -1
52
​
53
    row = len(mat)
54
    col = len(mat[0])
55
​
56
    # construct an `M × N` matrix to keep track of visited
57
    # cells
58
    visited = []
59
    for i in range(row):
60
        visited.append([None for _ in range(col)])
61
​
62
    dist = sys.maxsize
63
    dist = shortPath(mat, visited, src.first,
64
                            src.second, dest.first, dest.second, dist, 0)
65
​
66
    if (dist != sys.maxsize):
67
        return dist
68
    return -1
69
​
70
mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
71
       [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
72
       [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
73
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
74
       [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
75
       [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
76
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
77
       [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
78
       [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
79
       ]
80
​
81
src = Pair(0, 0)
82
dest = Pair(3, 4)
83
dist = shortPathLength(mat, src, dest)
84
​
85
print(dist)

Output
11
Time complexity: O(4^MN)
Auxiliary Space:  O(M*N)

[Expected Approach] – Using BFS
The idea for this approach is inspired from Lee algorithm and uses BFS.  The BFS considers all the paths starting from the source and moves ahead one unit in all those paths at the same time which makes sure that the first time when the destination is visited, it is the shortest path.
We start from the source cell and call the BFS while maintaining a queue to store the coordinates of the matrix, and a Boolean array to keep track of the visited cells.





1
# A point in a Maze (Needed for QNode)
2
class Point:
3
    def __init__(self, x_, y_):
4
        self.x = x_
5
        self.y = y_
6
​
7
# A QNode (Needed for BFS)
8
class QNode:
9
    def __init__(self, p_, d_):
10
        self.p = p_
11
        self.d = d_
12
​
13
​
14
def is_valid(x, y, r, c):
15
    return 0 <= x < r and 0 <= y < c
16
​
17
​
18
def bfs(mat, src, dest):
19
    r, c = len(mat), len(mat[0])
20

21
    # If Source and Destination are valid
22
    if not mat[src.x][src.y] or not mat[dest.x][dest.y]: return -1
23
​
24
    # Do BFS using Queue and Visited
25
    vis = [[False] * c for _ in range(r)]
26
    from collections import deque
27
    q = deque([QNode(src, 0)])
28
    vis[src.x][src.y] = True
29
    while q:
30

31
        # Pop an item from queue
32
        node = q.popleft()
33
        p = node.p
34
        d = node.d
35
​
36
        # If we reached the destination
37
        if p.x == dest.x and p.y == dest.y: return d
38

39
        # Try all four adjacent
40
        dx = [-1, 0, 0, 1]
41
        dy = [0, -1, 1, 0]
42
        for i in range(4):
43
            nx, ny = p.x + dx[i], p.y + dy[i]
44
            if is_valid(nx, ny, r, c) and mat[nx][ny] and not vis[nx][ny]:
45
                vis[nx][ny] = True
46
                q.append(QNode(Point(nx, ny), d + 1))
47
    return -1
48
​
49
​
50
mat = [
51
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
52
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
53
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
54
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
55
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
56
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
57
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
58
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
59
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
60
]
61
​
62
print(bfs(mat, Point(0, 0), Point(3, 4)))

Output
11
Time complexity: O(M*N)
Auxiliary Space: O(M*N)

"""











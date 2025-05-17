

"""

Given a square chessboard of n x n size, the position of the Knight and the position of a target are given. We need to find out the minimum steps a Knight will take to reach the target position.

Examples:

Input:


kNIGHT
Knight

knightPosition:  (1, 3) , targetPosition: (5, 0)


Output: 3
Explanation: In above diagram Knight takes 3 step to reach
                      from (1, 3) to (5, 0)
                     (1, 3) -> (3, 4) -> (4, 2) -> (5, 0)


Try it on GfG Practice
redirect icon
This problem can be seen as the shortest path in an unweighted graph. Therefore, BFS is an appropriate algorithm to solve this problem.

Steps:

Start with the knight’s initial position and mark it as visited.
Initialize a queue for BFS, where each entry stores the knight’s current position and the distance from the starting position.
Explore all 8 possible moves a knight can make from its current position.
For each move:
Check if the new position is within the board boundaries.
Check if the position has not been visited yet.
If valid, push this new position into the queue with a distance 1 more than its parent.
During BFS, if the current position is the target position, return the distance of that position.
Repeat until the target is found or all possible positions are explored.



1
# structure for storing a cell's data
2
class Cell:
3
    def __init__(self, x=0, y=0, dis=0):
4
        self.x = x
5
        self.y = y
6
        self.dis = dis
7
​
8
# Utility method to check if (x, y) is inside the board
9
def isInside(x, y, n):
10
    return 1 <= x <= n and 1 <= y <= n
11
​
12
# Method to return the minimum steps to reach target
13
def minSteps(knightPos, targetPos, n):
14
    # x and y direction where a knight can move
15
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
16
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
17
​
18
    # queue for storing knight's states
19
    q = []
20
​
21
    # push starting position of knight with 0 distance
22
    q.append(Cell(knightPos[0], knightPos[1], 0))
23
​
24
    visit = [[False] * (n + 1) for _ in range(n + 1)]
25
​
26
    # visit starting position
27
    visit[knightPos[0]][knightPos[1]] = True
28
​
29
    # loop until queue is empty
30
    while q:
31
        t = q.pop(0)
32
​
33
        # if target is reached, return the distance
34
        if t.x == targetPos[0] and t.y == targetPos[1]:
35
            return t.dis
36
​
37
        # explore all reachable positions
38
        for i in range(8):
39
            x = t.x + dx[i]
40
            y = t.y + dy[i]
41
​
42
            # if the position is valid and not visited, push it to queue
43
            if isInside(x, y, n) and not visit[x][y]:
44
                visit[x][y] = True
45
                q.append(Cell(x, y, t.dis + 1))
46
​
47
    # if no path found, return -1
48
    return -1
49
​
50
# Driver code
51
if __name__ == '__main__':
52
    n = 30
53
    knightPos = [1, 1]
54
    targetPos = [30, 30]
55
    print(minSteps(knightPos, targetPos, n))

Output
20
Time complexity: O(n2)
Auxiliary Space: O(n2)
"""

"""
Given a square chessboard of N x N size, the position of Knight and position of a target is given, the task is to find out the minimum steps a Knight will take to reach the target position.
 



Examples : 
 

Input : (2, 4) - knight's position, (6, 4) - target cell
Output : 2

Input : (4, 5) (1, 1)
Output : 3
 

A BFS approach to solve the above problem has already been discussed in the previous post. In this a post, a Dynamic Programming solution is discussed.
Explanation of the approach : 
 

Case 1 : If target is not along one row or one column of knight’s position. 
Let a chess board of 8 x 8 cell. Now, let say knight is at (3, 3) and the target is at (7, 8). There are possible 8 moves from the current position of knight i.e. (2, 1), (1, 2), (4, 1), (1, 4), (5, 2), (2, 5), (5, 4), (4, 5). But, among these only two moves (5, 4) and (4, 5) will be towards the target and all other goes away from the target. So, for finding minimum steps go to either (4, 5) or (5, 4). Now, calculate the minimum steps taken from (4, 5) and (5, 4) to reach the target. This is calculated by dynamic programming. Thus, this results in the minimum steps from (3, 3) to (7, 8).
Case 2 : If the target is along one row or one column of knight’s position. 
Let a chess board of 8 x 8 cell. Now, let’s say knight is at (4, 3) and the target is at (4, 7). There are possible 8 moves but towards the target, there are only 4 moves i.e. (5, 5), (3, 5), (2, 4), (6, 4). As, (5, 5) is equivalent to (3, 5) and (2, 4) is equivalent to (6, 4). So, from these 4 points, it can be converted into 2 points. Taking (5, 5) and (6, 4) (here). Now, calculate the minimum steps taken from these two points to reach the target. This is calculated by dynamic programming. Thus, this results in the minimum steps from (4, 3) to (4, 7).
Exception : When the knight will be at corner and the target is such that the difference of x and y coordinates with knight’s position is (1, 1) or vice-versa. Then minimum steps will be 4.
Dynamic Programming Equation : 
 


1) dp[diffOfX][diffOfY] is the minimum steps taken from knight’s position to target’s position.
2) dp[diffOfX][diffOfY] = dp[diffOfY][diffOfX].
where, diffOfX = difference between knight’s x-coordinate and target’s x-coordinate 
diffOfY = difference between knight’s y-coordinate and target’s y-coordinate 
 


Below is the implementation of above approach: 
 




# Python3 code for minimum steps for 
# a knight to reach target position 
  
# initializing the matrix. 
dp = [[0 for i in range(8)] for j in range(8)]; 
  
  
def getsteps(x, y, tx, ty): 
      
    # if knight is on the target 
    # position return 0. 
    if (x == tx and y == ty): 
        return dp[0][0]; 
      
    # if already calculated then return 
    # that value. Taking absolute difference. 
    elif(dp[abs(x - tx)][abs(y - ty)] != 0): 
        return dp[abs(x - tx)][abs(y - ty)]; 
    else: 
  
        # there will be two distinct positions 
        # from the knight towards a target. 
        # if the target is in same row or column 
        # as of knight then there can be four 
        # positions towards the target but in that 
        # two would be the same and the other two 
        # would be the same. 
        x1, y1, x2, y2 = 0, 0, 0, 0; 
  
        # (x1, y1) and (x2, y2) are two positions. 
        # these can be different according to situation. 
        # From position of knight, the chess board can be 
        # divided into four blocks i.e.. N-E, E-S, S-W, W-N . 
        if (x <= tx): 
            if (y <= ty): 
                x1 = x + 2; 
                y1 = y + 1; 
                x2 = x + 1; 
                y2 = y + 2; 
            else: 
                x1 = x + 2; 
                y1 = y - 1; 
                x2 = x + 1; 
                y2 = y - 2; 
  
        elif (y <= ty): 
            x1 = x - 2; 
            y1 = y + 1; 
            x2 = x - 1; 
            y2 = y + 2; 
        else: 
            x1 = x - 2; 
            y1 = y - 1; 
            x2 = x - 1; 
            y2 = y - 2; 
  
        # ans will be, 1 + minimum of steps 
        # required from (x1, y1) and (x2, y2). 
        dp[abs(x - tx)][abs(y - ty)] = \ 
        min(getsteps(x1, y1, tx, ty),  
        getsteps(x2, y2, tx, ty)) + 1; 
  
        # exchanging the coordinates x with y of both 
        # knight and target will result in same ans. 
        dp[abs(y - ty)][abs(x - tx)] = \ 
        dp[abs(x - tx)][abs(y - ty)]; 
        return dp[abs(x - tx)][abs(y - ty)]; 
  
# Driver Code 
if __name__ == '__main__': 
  
    # size of chess board n*n 
    n = 100; 
  
    # (x, y) coordinate of the knight. 
    # (tx, ty) coordinate of the target position. 
    x = 4; 
    y = 5; 
    tx = 1; 
    ty = 1; 
  
    # (Exception) these are the four corner points 
    # for which the minimum steps is 4. 
    if ((x == 1 and y == 1 and tx == 2 and ty == 2) or
            (x == 2 and y == 2 and tx == 1 and ty == 1)): 
        ans = 4; 
    elif ((x == 1 and y == n and tx == 2 and ty == n - 1) or
        (x == 2 and y == n - 1 and tx == 1 and ty == n)): 
        ans = 4; 
    elif ((x == n and y == 1 and tx == n - 1 and ty == 2) or
        (x == n - 1 and y == 2 and tx == n and ty == 1)): 
        ans = 4; 
    elif ((x == n and y == n and tx == n - 1 and ty == n - 1) 
        or (x == n - 1 and y == n - 1 and tx == n and ty == n)): 
        ans = 4; 
    else: 
  
        # dp[a][b], here a, b is the difference of 
        # x & tx and y & ty respectively. 
        dp[1][0] = 3; 
        dp[0][1] = 3; 
        dp[1][1] = 2; 
        dp[2][0] = 2; 
        dp[0][2] = 2; 
        dp[2][1] = 1; 
        dp[1][2] = 1; 
  
        ans = getsteps(x, y, tx, ty); 
  
    print(ans); 
  
# This code is contributed by PrinciRaj1992 
Output: 
3
 

Time Complexity: O(N * M) where N is the total number of rows and M is the total number of columns
Auxiliary Space: O(N * M) 



"""









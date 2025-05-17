
"""
Travelling Salesman Problem (TSP) using Reduced Matrix Method
Last Updated : 21 Apr, 2024
Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point.

Examples:

Input:



Example of connections of cities
Example of connections of cities


Output: 80
Explanation: An optimal path is 1 – 2 – 4 – 3 – 1.



Dynamic Programming Approach: This approach is already discussed in Set-1 of this article.

Branch and Bound Approach: The branch and bound approach is already discussed in this article.

Reduced Matrix: This approach is similar to the Branch and Bound approach. The difference here is that the cost of the path and the bound is decided based on the method of matrix reduction. The following are the assumptions for a reduced matrix:

A row or column of the cost adjacency matrix is said to be reduced if and only if it contains at least one zero element and all remaining entries in that row or column ≥ 0.
If all rows and columns are reduced then only the matrix is reduced matrix.
Tour length (new) = Tour length (old) – Total value reduced.
We first rewrite the original cost adjacency matrix by replacing all diagonal elements from 0 to Infinity
The basic idea behind solving the problem is:

The cost to reduce the matrix initially is the minimum possible cost for the travelling salesman problem.
Now in each step, we need to decide the minimum possible cost if that path is taken i.e., a path from vertex u to v is followed.
We can do that by replacing uth row and vth column cost by infinity and then further reducing the matrix and adding the extra cost for reduction and cost of edge (u, v) with the already calculated minimum path cost.
Once at least one path cost is found, that is then used as upper bound of cost to apply the branch and bound method on the other paths and the upper bound is updated accordingly when a path with lower cost is found.
Following are the steps to implement the above procedure:

Step1: Create a class (Node) that can store the reduced matrix, cost, current city number, level (number of cities visited so far), and path visited till now.
Step2: Create a priority queue to store the live nodes with the minimum cost at the top.
Step3: Initialize the start index with level = 0 and reduce the matrix. Calculate the cost of the given matrix by reducing the row and then the column. The cost is calculated in the following way:
Row reduction – Find the min value for each row and store it. After finding the min element from each row, subtract it from all the elements in that specific row.
Column reduction – Find the min value for each column and store it. After finding the min element from each column, subtract it from all the elements in that specific column. Now the matrix is reduced.
Now add all the minimum elements in the row and column found earlier to get the cost.
Step4: Push the element with all information required by Node into the Priority Queue.
Step5: Now, perform the following operations till the priority queue gets empty.
Pop the element with the min value from the priority queue.
For each pop operation check whether the level of the current node is equal to the number of nodes/cities or not.
If yes then print the path and return the minimum cost.
If No then, for each and every child node of the current node calculate the cost by using the formula-
Child->Cost = parent_matrix_cost + cost_from_parentTochild + Child_reducedMatrix_cost.
The cost of a reduced Matrix can be calculated by converting all the values of its rows and column to infinity and also making the index Matrix[Col][row] = infinity.
Then again push the current node into the priority queue.
Step6: Repeat Step5 till we don’t reach the level = Number of nodes – 1.
Follow the illustration below for a better understanding.

Illustration:

Consider the connections as shown in the graph:



Example of connections
Example of connections

Initially the cost matrix looks like:



row/col
no	1	2	3	4
1	–	10	15	20
2	10	–	35	25
3	15	35	–	30
4	20	25	30	–
After row and column reduction the matrix will be:



row/col
no	1	2	3	4
1	–	0	5	10
2	0	–	25	15
3	0	20	–	15
4	0	5	10	–
and row minimums are 10, 10, 15 and 20.



row/col
no	1	2	3	4
1	–	0	0	0
2	0	–	20	5
3	0	20	–	5
4	0	5	5	–
and the column minimums are 0, 0, 5 and 10.
So the cost reduction of the matrix is (10 + 10 + 15 + 20 + 5 + 10) = 70



Now let us consider movement from 1 to 2: Initially after substituting the 1st row and 2nd column to infinity, the matrix will be:



row/col
no	1	2	3	4
1	–	–	–	–
2	–	–	20	5
3	0	–	–	5
4	0	–	5	–
After the matrix is reduced the row minimums will be 5, 0, 0
row/col
no	1	2	3	4
1	–	–	–	–
2	–	–	15	0
3	0	–	–	5
4	0	–	5	–
and the column minimum will be  0, 5, 0
row/col
no	1	2	3	4
1	–	–	–	–
2	–	–	10	0
3	0	–	–	5
4	0	–	0	–
So the cost will be 70 + cost (1, 2) + 5 + 5 = 70 + 0 + 5 + 5 = 80.
Continue this process till the traversal is complete and find the minimum cost.



Given below the structure of the recursion tree along with the bounds:



The recursion diagram with bounds
"""
import sys
from queue import PriorityQueue

# Define the number of vertices and infinity value
N = 4
INF = sys.maxsize

# Node class to store each node along with the cost, level, and vertex
class Node:
    def __init__(self, parentMatrix, path, level, i, j):
        self.path = path.copy()
        self.reducedMatrix = [row.copy() for row in parentMatrix]
        self.cost = 0
        self.vertex = j
        self.level = level

        # Add this edge to the path
        if level != 0:
            self.path.append((i, j))

        # Change all entries of row i and column j to infinity
        # Also change the entry for vertex k to infinity
        if level != 0:
            for k in range(N):
                self.reducedMatrix[i][k] = INF
                self.reducedMatrix[k][j] = INF
            self.reducedMatrix[j][0] = INF
    def __lt__(self, other):
        return self.cost < other.cost
# Function to perform row reduction
def rowReduction(reducedMatrix):
    row = [INF]*N

    # Row[i] contains minimum in row i
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] < row[i]:
                row[i] = reducedMatrix[i][j]

    # Reduce the minimum value from each element in each row
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] != INF and row[i] != INF:
                reducedMatrix[i][j] -= row[i]

    return row

# Function to perform column reduction
def columnReduction(reducedMatrix):
    col = [INF]*N

    # Col[j] contains minimum in col j
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] < col[j]:
                col[j] = reducedMatrix[i][j]

    # Reduce the minimum value from each element in each column
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] != INF and col[j] != INF:
                reducedMatrix[i][j] -= col[j]

    return col

# Function to calculate the cost of the path
def calculateCost(reducedMatrix):
    cost = 0
    row = rowReduction(reducedMatrix)
    col = columnReduction(reducedMatrix)

    # Calculate the cost by adding the reduction values
    for i in range(N):
        cost += (row[i] if row[i] != INF else 0)
        cost += (col[i] if col[i] != INF else 0)

    return cost

# Function to print the path
def printPath(path):
    for pair in path:
        print(f"{pair[0] + 1} -> {pair[1] + 1}")

# Function to solve the TSP problem
def solve(CostGraphMatrix):
    # Create a priority queue to store live nodes of the search tree
    pq = PriorityQueue()

    # Create a root node and calculate its cost
    root = Node(CostGraphMatrix, [], 0, -1, 0)
    root.cost = calculateCost(root.reducedMatrix)

    # Add root to the list of live nodes
    pq.put((root.cost, root))

    # Continue until the priority queue becomes empty
    while not pq.empty():
        # Find a live node with the least estimated cost
        min = pq.get()[1]

        # Get the vertex number
        i = min.vertex

        # If all the cities have been visited
        if min.level == N - 1:
            min.path.append((i, 0))
            printPath(min.path)
            return min.cost

        # Generate all the children of min
        for j in range(N):
            if min.reducedMatrix[i][j] != INF:
                child = Node(min.reducedMatrix, min.path, min.level + 1, i, j)
                child.cost = min.cost + min.reducedMatrix[i][j] + calculateCost(child.reducedMatrix)
                pq.put((child.cost, child))

    return 0

# Define the cost matrix
CostGraphMatrix = [
    [ INF, 10, 15, 20 ],
    [ 10, INF, 35, 25 ],
    [ 15, 35, INF, 30 ],
    [ 20, 25, 30, INF ]
]

# Print the total cost of the tour
print("Total cost is", solve(CostGraphMatrix))







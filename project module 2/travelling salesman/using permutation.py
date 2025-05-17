"""
Traveling Salesman Problem (TSP) Implementation
Last Updated : 26 Nov, 2024
Given a 2d matrix cost[][] of size n where cost[i][j] denotes the cost of moving from city i to city j. The task is to complete a tour from city 0 (0-based index) to all other cities such that we visit each city exactly once and then at the end come back to city 0 at minimum cost.

Note the difference between Hamiltonian Cycle and TSP. The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once. Here we know that Hamiltonian Tour exists (because the graph is complete) and in fact, many such tours exist, the problem is to find a minimum weight Hamiltonian Cycle.

Examples:

Input: cost[][] = [[0, 111], [112, 0]]
Output: 223
Explanation: We can visit 0->1->0 and cost = 111 + 112 = 223.


Input: cost[][] = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]]
Output: 3000
Explanation: We can visit 0->1->2->0 and cost = 1000 + 1000 + 1000 = 3000.


Try it on GfG Practice
redirect icon
Approach:

The given graph is a complete graph, meaning there is an edge between every pair of nodes. A naive approach to solve this problem is to generate all permutations of the nodes, and calculate the cost for each permutation, and select the minimum cost among them.


An important observation in the Traveling Salesman Problem (TSP) is that the choice of the starting node does not affect the solution. This is because the optimal path forms a cyclic tour. For example, if the optimal tour is a1→a2→a3→a4→a1, starting from any other node, such as a2, results in the equivalent tour a2→a3→a4→a1→a2 with same total cost.


To simplify the problem, we can fix one node (e.g., node 1) as the starting point and only consider permutations of the remaining nodes.


"""
# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point

from itertools import permutations

def tsp(cost):

    # Number of nodes
    numNodes = len(cost)
    nodes = list(range(1, numNodes))

    minCost = float('inf')

    # Generate all permutations of the
    # remaining nodes
    for perm in permutations(nodes):
        currCost = 0
        currNode = 0

        # Calculate the cost of the current permutation
        for node in perm:
            currCost += cost[currNode][node]
            currNode = node

        # Add the cost to return to the starting node
        currCost += cost[currNode][0]

        # Update the minimum cost if the current cost
        # is lower
        minCost = min(minCost, currCost)

    return minCost


if __name__ == "__main__":

    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    res = tsp(cost)
    print(res)


"""
Output
80
Time complexity:  O(n!) where n is the number of vertices in the graph. This is because the algorithm uses the next_permutation function which generates all the possible permutations of the vertex set. 
Auxiliary Space: O(n) as we are using a vector to store all the vertices.

"""
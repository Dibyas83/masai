"""

Given two arrays v[] and w[] that represent values and weights associated with n items respectively. Find out the maximum value subset(Maximum Profit) of v[] such that the sum of the weights of this subset is smaller than or equal to Knapsack capacity W.

Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag.

Input: N = 3, W = 4, v[] = {1, 2, 3}, w[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.


Input: N = 5, W = 10, v[] = {40, 50, 100, 95, 30}, w[] = {2, 3.14, 1.98, 5, 3}
Output: 235


Branch and Bound Algorithm:
Branch and bound is an algorithm design paradigm which is generally used for solving combinatorial optimization problems. These problems typically exponential in terms of time complexity and may require exploring all possible permutations in worst case. Branch and Bound solve these problems relatively quickly.


Firstly let us explore all approaches for this problem.

1. 0/1 Knapsack using Greedy Approach:
A Greedy approach is to pick the items in decreasing order of value per unit weight. The Greedy approach works only for fractional knapsack problem and may not produce correct result for 0/1 knapsack.


2. 0/1 Knapsack using Dynamic Programming (DP):
We can use Dynamic Programming (DP) for 0/1 Knapsack problem. In DP, we use a 2D table of size n x W. The DP Solution doesn’t work if item weights are not integers.


3. 0/1 Knapsack using Brute Force:
Since DP solution doesn’t always work just like in case of non-integer weight, a solution is to use Brute Force. With n items, there are 2n solutions to be generated, check each to see if they satisfy the constraint, save maximum solution that satisfies constraint. This solution can be expressed as tree.


Knapsack-using-Branch-and-Bound
0/1 Knapsack using Brute Force

4. 0/1 Knapsack using Backtracking:
We can use Backtracking to optimize the Brute Force solution. In the tree representation, we can do DFS of tree. If we reach a point where a solution no longer is feasible, there is no need to continue exploring. In the given example, backtracking would be much more effective if we had even more items or a smaller knapsack capacity.


0-1-Knapsack-using-Branch-and-Bound
0/1 Knapsack using Backtracking

5. 0/1 Knapsack using Branch and Bound:
The backtracking based solution works better than brute force by ignoring infeasible solutions. We can do better (than backtracking) if we know a bound on best possible solution subtree rooted with every node. If the best in subtree is worse than current best, we can simply ignore this node and its subtrees. So we compute bound (best solution) for every node and compare the bound with current best solution before exploring the node.


0-1-Knapsack-using-Branch-and-Bound3
0/1 Knapsack using Branch and Bound

How to find bound for every node for 0/1 Knapsack?
The idea is to use the fact that the Greedy approach provides the best solution for Fractional Knapsack problem. To check if a particular node can give us a better solution or not, we compute the optimal solution (through the node) using Greedy approach. If the solution computed by Greedy approach itself is more than the best so far, then we can’t get a better solution through the node.


Follow the steps to implement the above idea:

Sort all items in decreasing order of ratio of value per unit weight so that an upper bound can be computed using Greedy Approach.
Initialize maximum profit, maxProfit = 0, create an empty queue, Q, and create a dummy node of decision tree and enqueue it to Q. Profit and weight of dummy node are 0.
Do following while Q is not empty.
Extract an item from Q. Let the extracted item be u.
Compute profit of next level node. If the profit is more than maxProfit, then update maxProfit.
Compute bound of next level node. If bound is more than maxProfit, then add next level node to Q.
Consider the case when next level node is not considered as part of solution and add a node to queue with level as next, but weight and profit without considering next level nodes.
Below is the implementation of above approach:

"""



from queue import PriorityQueue

class Item:

    def __init__(self, weight, value):

        self.weight = weight

        self.value = value

class Node:

    def __init__(self, level, profit, weight):
        self.level = level      # Level of the node in the decision tree (or index in arr[])

        self.profit = profit    # Profit of nodes on the path from root to this node (including this node)

        self.weight = weight    # Total weight at the node

    def __lt__(self, other):
        return other.weight < self.weight  # Compare based on weight in descending order

def bound(u, n, W, arr):

    # Calculate the upper bound of profit for a node in the search tree

    if u.weight >= W:

        return 0

    profit_bound = u.profit

    j = u.level + 1

    total_weight = u.weight

    # Greedily add items to the knapsack until the weight limit is reached

    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    # If there are still items left, calculate the fractional contribution of the next item

    if j < n:

        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)

    return profit_bound

def knapsack(W, arr, n):

    # Sort items based on value-to-weight ratio in non-ascending order

    arr.sort(key=lambda x: x.value / x.weight, reverse=True)



    priority_queue = PriorityQueue()

    u = Node(-1, 0, 0)  # Dummy node at the starting

    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():

        u = priority_queue.get()

        if u.level == -1:

            v = Node(0, 0, 0)  # Starting node

        elif u.level == n - 1:

            continue  # Skip if it is the last level (no more items to consider)

        else:

            v = Node(u.level + 1, u.profit, u.weight)  # Node without considering the next item

        v.weight += arr[v.level].weight

        v.profit += arr[v.level].value

        # If the cumulated weight is less than or equal to W and profit is greater than previous profit, update maxProfit

        if v.weight <= W and v.profit > max_profit:

            max_profit = v.profit

        v_bound = bound(v, n, W, arr)

        # If the bound value is greater than current maxProfit, add the node to the priority queue for further consideration

        if v_bound > max_profit:

            priority_queue.put(v)

        # Node considering the next item without adding it to the knapsack

        v = Node(u.level + 1, u.profit, u.weight)

        v_bound = bound(v, n, W, arr)

        # If the bound value is greater than current maxProfit, add the node to the priority queue for further consideration

        if v_bound > max_profit:

            priority_queue.put(v)

    return max_profit

# Driver program to test the above function

W = 10
arr = [
    Item(2, 40),
    Item(3.14, 50),
    Item(1.98, 100),
    Item(5, 95),
    Item(3, 30)
]

n = len(arr)
max_profit = knapsack(W, arr, n)
print("Maximum possible profit =", max_profit)
"""
Output
Maximum possible profit = 235
Time Complexity: O(2N)
Auxiliary Space: O(N)

Branch and bound is very useful technique for searching a solution but in worst case, we need to fully calculate the entire tree. At best, we only need to fully calculate one path through the tree and prune the rest of it.
"""
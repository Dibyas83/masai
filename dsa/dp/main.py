
"""
Dynamic programming is a powerful algorithmic technique used to solve optimization problems by breaking them down into smaller, overlapping subproblems. It involves storing solutions to these subproblems to avoid redundant calculations and improve efficiency. The core idea is to leverage optimal substructure and overlapping subproblems to find the most efficient solution.
Key Concepts:
Optimal Substructure:
A problem has optimal substructure if an optimal solution can be constructed from optimal solutions to its subproblems.
Overlapping Subproblems:
These are subproblems that are solved repeatedly during the computation of the overall solution.
Memoization (Top-Down):
A technique where solutions to subproblems are stored in a memo table or cache to avoid recomputing them.
Tabulation (Bottom-Up):
A technique where solutions to subproblems are computed in a bottom-up manner, building up to the final solution.
How it Works:
Divide and Conquer: Break down the problem into smaller, overlapping subproblems.
Solve Subproblems: Solve each subproblem once and store the result.
Combine Subproblem Solutions: Combine the solutions to the subproblems to build the final solution.
Common Applications:
Fibonacci Sequence: Efficiently calculating Fibonacci numbers.
Knapsack Problem: Determining the most valuable items to include in a knapsack with limited weight capacity.
Shortest Path Problems: Finding the shortest path between two points in a graph.
Edit Distance: Calculating the minimum number of edits (insertions, deletions, substitutions) required to transform one string into another.
Matrix Chain Multiplication: Finding the most efficient order to multiply a chain of matrices.
Example: Fibonacci Sequence
Python
"""
def fibonacci_dp(n):

    # Calculates the nth Fibonacci number using dynamic programming (top-down with memoization).

    memo = {}  # Memo table to store calculated Fibonacci numbers

    def fib(i):
        print(i,"i")
        if i in memo:
            return memo[i]
        if i <= 1:
            return i
        if i == 2:
            return 1

        memo[i] = fib(i - 1) + fib(i - 2)  # Store the calculated value in memo
        print(memo)
        return memo[i]

    return fib(n)
n =int(input())
print(fibonacci_dp(n))
"""
6
6 i
5 i
4 i
3 i
2 i
1 i
{3: 2}
2 i
{3: 2, 4: 3}
3 i
{3: 2, 4: 3, 5: 5}
4 i
{3: 2, 4: 3, 5: 5, 6: 8}
8
"""











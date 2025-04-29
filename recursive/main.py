

"""

What is Recursion?
Recursion is a technique where a function calls itself to solve smaller instances of the sameproblem.
Think of it as breaking a big problem into smaller, more manageable sub-problems.
Key Components:
Base Case:
The condition that stops further recursive calls.
Recursive Case:
The part of the function that continues the recursion.
Why Learn Recursion?
It simplifies code for problems like factorials, Fibonacci numbers, and more.
Helps in understanding important concepts like the call stack and memory management.
2.
Recursive Function Examples
😊
2.1 Factorial Function
Concept:
Calculate the factorial of a non-negative integer
.
Recursive Approach:
Base Case:
and
Recursive Case:
n
f act(0) = 1 f act(1) = 1
f act(n) = n × f act(n − 1)
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
# Example usage:
print(fact(5))
# Output: 120

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
"""

"""

Understanding the Call Stack
😊
Call Stack Overview:
The call stack is a special region in memory that stores information about active functioncalls.
Stack Frames:
Each function call creates a frame that contains parameters, local variables,and the return address.

Key Points:
fib(1) = 1 f ib(2) = 1
fib(n) = f ib(n − 1) + f ib(n − 2)

Pushing:
A new stack frame is added when a function is called.
Popping:
Once a function completes, its frame is removed.
Managing the call stack is crucial to avoid issues like stack overflow.

Algorithm Analysis
😊Time Complexity Considerations:
Factorial:
Time complexity is O(n) because it makesrecursive calls.
Fibonacci:The naive recursive solution has exponential time complexity due to overlappingsubproblems.
Merge Operation Example:
Merging two sorted arrays typically involves O(n) time where n is the total number of elements.

Best, Worst, and Average Cases:
For merging, the best case might involve fewer comparisons, while the worst case requires 2n - 1
comparisons.
Understanding these cases helps in analyzing algorithm efficiency.

6.
Common Mistakes in Recursion
😊
Missing Base Case:
Forgetting the base case can lead to infinite recursion and a stack overflow.
Not Handling Edge Cases:
Ensure proper checks for edge cases such as negative numbers or empty inputs.
Overlapping Subproblems:
Problems like the Fibonacci sequence can be inefficient if not optimized (e.g., usingmemoization).
Memory Consumption:
Each recursive call adds a new frame to the stack, which can consume significant memory ifnot managed properly.
Overcomplicating Solutions:
Sometimes, iterative solutions are simpler and more efficient than their recursivecounterparts.
Keep these pitfalls in mind to write more robust and efficient recursive functions.



7.
Exercises and Practice
😊
1.
Exercise 1:
Write a recursive function to compute the sum of digits of a number.
2.
Exercise 2:
Modify the recursive Fibonacci function to use memoization for improved performance.
3.
Exercise 3:
Implement a recursive function to reverse a string.
Try these exercises on your own and experiment with different inputs to see how your functionsbehave
"""
def nos(n):
    if n <= 1:
        return n
    else:
        print(n)
        return nos(n-1)

n= 10
print(nos(n))

def rev_string(stri):
    n = len(stri)
    revst = ""
    if len(stri) < 1:
        return stri
    else:
        revst[0] = stri[n-1]











"""
Introduction to Recursion
Last Updated : 24 Apr, 2025
The process in which a function calls itself directly or indirectly is called recursion and the corresponding
 function is called a recursive function.

A recursive algorithm takes one step toward solution and then recursively call itself to further move. The
algorithm stops once we reach the solution. Since called function may further call itself, this process
might continue forever. So it is essential to provide a base case to terminate this recursion process.
Need of Recursion

Recursion helps in logic building. Recursive thinking helps in solving complex problems by breaking
them into smaller subproblems.
Recursive solutions work as a a basis for Dynamic Programming and Divide and Conquer algorithms.
Certain problems can be solved quite easily using recursion like Towers of Hanoi (TOH),
Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.
Steps to Implement Recursion

Step1 – Define a base case: Identify the simplest (or base) case for which the solution is known or trivial.
This is the stopping condition for the recursion, as it prevents the function from infinitely calling itself.

Step2 – Define a recursive case: Define the problem in terms of smaller subproblems. Break the problem down
into smaller versions of itself, and call the function recursively to solve each subproblem.

Step3 – Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base
case, and does not enter an infinite loop.

Step4 – Combine the solutions: Combine the solutions of the subproblems to solve the original problem.

How memory is allocated to different function calls in recursion?

Recursion uses more memory to store data of every recursive call in an internal function call stack.

Whenever we call a function, its record is added to the stack and remains there until the call is finished.
The internal systems use a stack because function calling follows LIFO structure, the last called function finishes first.
When any function is called from main(), the memory is allocated to it on the stack. A recursive function calls
 itself, the memory for a called function is allocated on top of memory allocated to the calling function and a
 different copy of local variables is created for each function call. When the base case is reached, the function 
 returns its value to the function by whom it is called and memory is de-allocated and the process continues

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
"""
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

print("rev a string")

def rev_string(stri):
    st = " ".join(map(str,stri))
    n1 = len(stri)
    #if not stri:
        #return ""
    if len(stri) == 1:
        return stri[0]
    else:

        return stri[n1 -1] + rev_string(stri[:n1-1])

stri= "aeiou"

print(rev_string(stri))

def reverse_string(s):
    if not s:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

# Example usage
original_string = "hello"
reversed_string = reverse_string(original_string)
print(f"Reversed string: {reversed_string}") # Output: Reversed string: olleh


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

"""
Types of Recursion in Python
Recursion can be broadly classified into two types: tail recursion and non-tail recursion. The main difference 
between them is related to what happens after the recursive call.

Tail Recursion: This occurs when the recursive call is the last operation executed in the function, with no 
additional work or calculation following the recursive call. In many programming languages, tail recursion can 
be optimized by the compiler into iterative loops to improve performance and prevent stack overflow.

Non-Tail Recursion: This occurs when there are operations or calculations that follow the recursive call. 
This type prevents the compiler or interpreter from optimizing the recursion into an iteration.
Here is a Python example that demonstrates both tail recursion and non-tail recursion:
"""

def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    # Base case
    if n == 1:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)

# Example usage
print(tail_fact(5))
print(nontail_fact(5))








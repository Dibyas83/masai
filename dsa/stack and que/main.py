


"""
Using stack
We can use a stack data structure to reverse a string due to its Last In First Out (LIFO) property.
This means that the last element added to the stack will be the first one to be removed, this effectively
 reversing the order of the elements.

Note: list can be easily used to simulate the behavior of a stack. It provides built-in methods like .append()
and .pop(), which make it suitable for stack operations.

"""


s = "GeeksforGeeks"

# Convert the string into a list to use it as a stack
stack = list(s)

# Initialize an empty string to hold the reversed result
rev = ""

# Continue looping until the stack is empty
while stack:

    # Remove the top element from the stack
    # and add it to the reversed string
    rev += stack.pop()

print(rev)














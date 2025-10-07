
"""

A stack is a type of linear data structure where:
Elements are inserted and removed only from one end (called the top).

✔️ How to implement stacks using arrays and linked lists
✔️ Applications of stacks in real-world scenarios
✔️ Expression notations (Infix, Prefix, Postfix)

Real-Life Examples of Stacks:
A pile of books 📚 → You remove the top one first.
Browser history ↩️ → The most recent page you visited is popped first when you hit "Back".
Undo/Redo in text editors 🔄 → Recent changes are stored in a stack!

push(x) Adds element x to the top of the stack.
pop() Removes and returns the top element.
SIZE() Returns the number of elements in the stack.
STACK-EMPTY() Checks if the stack is empty.
TOP-ELEMENT() Returns the top element without removing it.

3️⃣ If the stack is full, an OVERFLOW error occurs.
3️⃣ If the stack is empty, an UNDERFLOW error occurs

 Function Calls & Recursion – Each function call is pushed onto a stack.
✔️ Undo/Redo in text editors – Your actions are stored in a stack.
✔️ Balanced Parentheses Checker – Used in programming languages.
✔️ Expression Evaluation & Conversion – Used in mathematical expressions.
✔️ String Reversal – Useful in reversing text

Infix <Operand> <Operator> <Operand> A + B
Prefix (Polish Notation) <Operator> <Operand> <Operand> + A B
Postfix (Reverse Polish Notation) <Operand> <Operand> <Operator> A B +
"""


def push(arr,x,max_size_stack):
    top = len(arr)

    if top >= max_size_stack-1:
        print("overflow")
    else:
        arr.append(x)
    print(arr)

arr = list(map(int,input().split(" ")))
x = int(input())
max_size_stack = int(input())
push(arr,x,max_size_stack)


class Stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.stack = []
        self.top = -1 # curr size as it is empty

    def push(self,item):
        if self.top == self.maxsize - 1:
            raise  Exception("overflow")
        self.top += 1 # now becomes 0
        self.stack.append(item)

    def pop(self):
        if self.top == -1:
            raise  Exception("underflow")
        self.top -= 1
        return  self.stack.pop()

#------------------using linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("UNDERFLOW")
        item = self.top.data
        self.top = self.top.next
        return item




















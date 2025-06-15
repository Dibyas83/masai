
"""
Here's how to take input for a Binary Search Tree (BST) in Python:
1. Node Class:
First, define a Node class to represent each node in the BST:
Python
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
2. Insert Function:
Create an insert function to add new nodes to the BST while maintaining the BST property (left child < parent < right child):
Python
"""
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

"""
3. Input Method:
Now, you can take input from the user. This example takes space-separated integers as input:
Python
"""
def build_bst_from_input(input_str):
    root = None
    keys = list(map(int, input_str.split()))
    for key in keys:
        root = insert(root, key)
    return root

"""
4. Example Usage:
Python
"""
if __name__ == "__main__":
    input_str = input("Enter space-separated integers: ")
    bst_root = build_bst_from_input(input_str)
"""

This code will prompt the user to enter a sequence of numbers, which are then used to build a BST.
5. Inorder Traversal:
To check that the BST was built correctly, you can use an inorder traversal, which will print the nodes in sorted order:
Python
"""
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

"""
6. Example with Inorder:
Python
"""
if __name__ == "__main__":
    input_str = input("Enter space-separated integers: ")
    bst_root = build_bst_from_input(input_str)
    print("Inorder traversal of the BST:")
    inorder(bst_root)

"""
Explanation:
The Node class represents each node in the tree.
The insert function recursively finds the correct position for a new key based on the BST property.
The build_bst_from_input function takes user input, converts it to integers, and inserts them into the BST.
The inorder function recursively traverses the tree, printing the nodes in sorted order.
This approach allows you to build a BST by providing a sequence of values from user input.

"""








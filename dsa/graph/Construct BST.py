#Construct BST from its given level order traversal Using Recursion:
"""
The idea is to use recursion as the first element will always be the root of the tree and second element will be the left child and the third element will be the right child (if fall in the range), and so on for all the remaining elements.



Follow the steps below to solve the problem:

First, pick the first element of the array and make it root.
Pick the second element, if its value is smaller than the root node value make it left child,
Else make it right child
Now recursively call step (2) and step (3) to make a BST from its level Order Traversal.

"""
# Python implementation to construct a BST
# from its level order traversal

import math

# Node of a BST


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to get a new node
def getNode(data):

    # Allocate memory
    newNode = Node(data)

    # put in the data
    newNode.data = data
    newNode.left = None
    newNode.right = None
    return newNode


# Function to construct a BST from
# its level order traversal
def LevelOrder(root, data):
    if(root == None):
        root = getNode(data)
        return root

    if(data <= root.data):
        root.left = LevelOrder(root.left, data)
    else:
        root.right = LevelOrder(root.right, data)
    return root


def constructBst(arr, n):
    if(n == 0):
        return None
    root = None

    for i in range(0, n):
        root = LevelOrder(root, arr[i])

    return root


# Function to print the inorder traversal
def inorderTraversal(root):
    if (root == None):
        return None

    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)


# Driver program
if __name__ == '__main__':

    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    n = len(arr)

    root = constructBst(arr, n)

    print("Inorder Traversal: ", end="")
    root = inorderTraversal(root)


# This code is contributed by Srathore

















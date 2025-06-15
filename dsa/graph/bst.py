
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

# Creating the root node
root1 = Node(5)


# Python program to demonstrate
# insert operation in binary search tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert
# a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
            return root
    if root.val < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)

# Print inorder traversal of the BST
inorder(r)

#---------------search

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key
    # is present at root
    if root is None or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


# Creating a hard coded tree for keeping
# the length of the code small. We need
# to make sure that BST properties are
# maintained if we try some other cases.
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Searching for keys in the BST
print("Found" if search(root, 19) else "Not Found")
print("Found" if search(root, 80) else "Not Found")

#----------------deletion
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Note that it is not a generic inorder successor
# function. It mainly works when the right child
# is not empty, which is  the case we need in BST
# delete.
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


# This function deletes a given key x from the
# given BST and returns the modified root of the
# BST (if it is modified).
def del_node(root, x):
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.key > x:
        root.left = del_node(root.left, x)
    elif root.key < x:
        root.right = del_node(root.right, x)

    else:
        # If root matches with the given key

        # Cases when root has 0 children or
        # only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)

    return root


# Utility function to do inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = del_node(root, x)
    inorder(root)
    print()

#-----------------traverseal

# Python3 code to implement the approach

# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v


# Inorder Traversal
def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)

        # Visit node
        print(root.data, end=" ")

        # Traverse right subtree
        printInorder(root.right)


# Driver code
if __name__ == "__main__":
    # Build the tree
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    # Function call
    print("Inorder Traversal:", end=" ")
    printInorder(root)

    # This code is contributed by ajaymakvana.











"""
trees are directed graphs
perfect(avl) and complete tree

binary trees - 1  > (2*1) > (2*2 , 2*2 + 1),(2*1 +1) > (2*(2+3), 2*(2+3) + 1)
array representation [1 2 -1(no node) 4 5]

leafs have height 0 base case

dfs - left to down ,node(final) ,right

tree - [1 2 4 5 10] uses call stack-recursive

start by initializing a stack =[1] root but currently leaf
poped ele = stack.pop=[1]
stack = [3,2] (right and left)
stack.pop=[1,2]
stack = [3,5,4]
stack.pop=[1,2,4]
stack = [3,5]
stack.pop=[1,2,4,5]
tack = [3,]
stack.pop=[1,2,4,5]
tack = []
stack.pop=[1,2,4,5,3]
tack = [10]
stack.pop=[1,2,4,5,3,10]



preorder traversal -node,left,right  - on final node after going to bottom node
[1 2 4 5 3 10]
inorder trav  -start left ,node ,right then up , up
[4 2 5 1 10 3]
post order - left,right,node - [4 5 2 10 3 1]
------------------------
bfs traversal level by level  uses queue
tree - [1 2 3 4 5 10]

start by initializing a queue =[1] root but currently leaf
poped ele = stack.pop=[1]
stack = [2,3] (right and left)
stack.pop=[1,2]
stack = [3,4,5
stack.pop=[1,2,3]
stack = [4,5]
stack.pop=[1,2,3,4]
tack = [5,]
stack.pop=[1,2,3,4,5]
tack = [10]
stack.pop=[1,2,3,4,5,10]

time o(n) space o(n)

------------------
binary tree to bst(complete binary tree, height balanced)

5 - (2 - 1,3),(8 - 7,9)  left side small, right  side bigger
o(log n)

inorder search - 1,2,3,5,7,8,9


 root.value = 10
    root.left = 11
    root.right = 12
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if not node:
        return
    print(node.data,end=' ')
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    pre_order(node.right)


def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=' ')

# doing iteratively using stack
def pre_order_itrative(node):
    stk = []

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

"""

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(10)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

    def __str__(self):
        return str(self.val)
"""
#----------------bfs search- level order traversal
from collections import deque

def level_order(node):

    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node.data,end=' ')
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)



def search(node,val): # dfs
    if not node:
        return False
    if node.val == val:
        return True
    return search(node.left,val) or search(node.right,val)



# search using bst
def search_bst(node,target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val:
        return search_bst(node.left,target)
    else:
        return search_bst(node.right,target)


if __name__ == "__main__":
    # Creating the tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("In-order DFS: ", end='')
    in_order(root)
    print("\nPre-order DFS: ", end='')
    pre_order(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)
    print("\nLevel order: ", end='')

# insertion
from collections import deque

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to insert a new node in the binary tree
"""
2. Insertion in Binary Tree
Inserting elements means add a new node into the binary tree. As we know that there is no such ordering of elements in the binary tree, So we do not have to worry about the ordering of node in the binary tree. We would first creates a root node in case of empty tree. Then subsequent insertions involve iteratively searching for an empty place at each level of the tree. When an empty left or right child is found then new node is inserted there. By convention, insertion always starts with the left child node.
"""


def insert(root, key):
    if root is None:
        return Node(key)

    # Create a queue for level order traversal
    queue = deque([root])

    while queue:
        temp = queue.popleft()

        # If left child is empty, insert the new node here
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)

        # If right child is empty, insert the new node here
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)

    return root

# In-order traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("Inorder traversal before insertion: ", end="")
    inorder(root)
    print()

    key = 6
    root = insert(root, key)

    print("Inorder traversal after insertion: ", end="")
    inorder(root)
    print()

"""
3. Searching in Binary Tree
Searching for a value in a binary tree means looking through the tree to find a node that has that value. Since binary trees do not have a specific order like binary search trees, we typically use any traversal method to search. The most common methods are depth-first search (DFS) and breadth-first search (BFS). In DFS, we start from the root and explore the depth nodes first. In BFS, we explore all the nodes at the present depth level before moving on to the nodes at the next level. We continue this process until we either find the node with the desired value or reach the end of the tree. If the tree is empty or the value isn’t found after exploring all possibilities, we conclude that the value does not exist in the tree.

Here is the implementation of searching in a binary tree using Depth-First Search (DFS):
"""
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to search for a value in the binary tree using DFS
def searchDFS(root, value):
    # Base case: If the tree is empty or we've reached a leaf node
    if root is None:
        return False
    # If the node's data is equal to the value we are searching for
    if root.data == value:
        return True
    # Recursively search in the left and right subtrees
    left_res = searchDFS(root.left, value)
    right_res = searchDFS(root.right, value)

    return left_res or right_res

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    value = 6
    if searchDFS(root, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")

"""
4. Deletion in Binary Tree
Deleting a node from a binary tree means removing a specific node while keeping the tree’s structure. First, we need to find the node that want to delete by traversing through the tree using any traversal method. Then replace the node’s value with the value of the last node in the tree (found by traversing to the rightmost leaf), and then delete that last node. This way, the tree structure won’t be effected. And remember to check for special cases, like trying to delete from an empty tree, to avoid any issues.

Note: There is no specific rule of deletion but we always make sure that during deletion the binary tree proper should be preserved.
"""
from collections import deque

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to delete a node from the binary tree
def deleteNode(root, val):
    if root is None:
        return None

    # Use a queue to perform BFS
    queue = deque([root])
    target = None

    # Find the target node
    while queue:
        curr = queue.popleft()

        if curr.data == val:
            target = curr
            break
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    if target is None:
        return root

    # Find the deepest rightmost node and its parent
    last_node = None
    last_parent = None
    queue = deque([(root, None)])

    while queue:
        curr, parent = queue.popleft()
        last_node = curr
        last_parent = parent

        if curr.left:
            queue.append((curr.left, curr))
        if curr.right:
            queue.append((curr.right, curr))

    # Replace target's value with the last node's value
    target.data = last_node.data

    # Remove the last node
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None
    else:
        return None
    return root

# In-order traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    print("Original tree (in-order): ", end="")
    inorder(root)
    print()

    val_to_del = 3
    root = deleteNode(root, val_to_del)

    print(f"Tree after deleting {val_to_del} (in-order): ", end="")
    inorder(root)
    print()

#height

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Returns height which is the number of edges
# along the longest path from the root node down
# to the farthest leaf node.
def height(root):
    if root is None:
        return -1

    # compute the height of left and right subtrees
    lHeight = height(root.left)
    rHeight = height(root.right)

    return max(lHeight, rHeight) + 1


if __name__ == "__main__":
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)

    print(height(root))







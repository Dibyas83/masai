
"""
An AVL tree is a self-balancing binary search tree where the heights of the left and right subtrees of any
node differ by at most one. This balance factor ensures that the tree remains relatively balanced, preventing
 worst-case scenarios that can lead to O(n) time complexity for search, insertion, and deletion operations
 in a regular binary search tree.
Key Properties of AVL Trees:
Balance Factor:
For every node in an AVL tree, the balance factor (the difference in height between the left and right subtrees)
 must be -1, 0, or 1.
Self-Balancing:
After each insertion or deletion, the AVL tree rebalances itself if necessary to maintain the balance factor
 property.
Binary Search Tree Property:
Like a binary search tree, the value of each node in the left subtree is less than the value of the node,
and the value of each node in the right subtree is greater than the value of the node.
Operations on AVL Trees:
Insertion:
Perform standard BST insertion.
Trace the path from the inserted node to the root, updating the balance factors of the nodes on the path.
If any node's balance factor becomes -2 or 2, perform rotations (single or double) to rebalance the tree.
Deletion:
Perform standard BST deletion.
Trace the path from the deleted node's parent to the root, updating the balance factors of the nodes on the path.
If any node's balance factor becomes -2 or 2, perform rotations to rebalance the tree.
Search:
Perform standard BST search, which takes O(log n) time in a balanced AVL tree.
Rotations in AVL Trees:
Left Rotation: Used when the right subtree is too heavy.
Right Rotation: Used when the left subtree is too heavy.
Left-Right Rotation: A combination of left and right rotations, used in specific imbalance cases.
Right-Left Rotation: A combination of right and left rotations, used in specific imbalance cases.
Time Complexity:
Search: O(log n), Insertion: O(log n), and Deletion: O(log n).
Applications:
Databases and indexing, Efficient search and retrieval operations, and Situations where maintaining a
balanced tree is crucial for performance


"""
from input.inputsimple import height

"""
geek 

AVL Tree Data Structure
Last Updated : 10 Apr, 2025
An AVL tree defined as a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees for any node cannot be more than one.

The absolute difference between the heights of the left subtree and the right subtree for any node is known as the balance factor of the node. The balance factor for all nodes must be less than or equal to 1.
Every AVL tree is also a Binary Search Tree (Left subtree values Smaller and Right subtree values greater for every node), but every BST is not AVL Tree. For example, the second diagram below is not an AVL Tree.
The main advantage of an AVL Tree is, the time complexities of all operations (search, insert and delete, max, min, floor and ceiling) become O(Log n). This happens because height of an AVL tree is bounded by O(Log n). In case of a normal BST, the height can go up to O(n).
An AVL tree maintains its height by doing some extra work during insert and delete operations. It mainly uses rotations to maintain both BST properties and height balance.
There exist other self-balancing BSTs also like Red Black Tree. Red Black tree is more complex, but used more in practice as it is less restrictive in terms of left and right subtree height differences.
Example of an AVL Tree:
The balance factors for different nodes are : 12 :1, 8:1, 18:1, 5:1, 11:0, 17:0 and 4:0. Since all differences are less than or equal to 1, the tree is an AVL tree.

AVL tree
AVL tree
Example of a BST which is NOT AVL:
The Below Tree is NOT an AVL Tree as the balance factor for nodes 8, 4 and 7 is more than 1.

BST-Unbalanced
Not an AVL Tree
Operations on an AVL Tree:
Searching : It is same as normal Binary Search Tree (BST) as an AVL Tree is always a BST. So we can use the same implementation as BST. The advantage here is time complexity is O(Log n)
Insertion : It does rotations along with normal BST insertion to make sure that the balance factor of the impacted nodes is less than or equal to 1 after insertion
Deletion : It also does rotations along with normal BST deletion to make sure that the balance factor of the impacted nodes is less than or equal to 1 after deletion.
Please refer Insertion in AVL Tree and Deletion in AVL Tree for details.

Rotating the subtrees (Used in Insertion and Deletion)
An AVL tree may rotate in one of the following four ways to keep itself balanced while making sure that the BST properties are maintained.

Left Rotation:

When a node is added into the right subtree of the right subtree, if the tree gets out of balance, we do a single left rotation.


Left-Rotation in AVL tree
Right Rotation:

If a node is added to the left subtree of the left subtree, the AVL tree may get out of balance, we do a single right rotation.

avl-tree
Right-Rotation in AVL Tree


Left-Right Rotation:

A left-right rotation is a combination in which first left rotation takes place after that right rotation executes.


Left-Right Rotation in AVL tree
Right-Left Rotation:

A right-left rotation is a combination in which first right rotation takes place after that left rotation executes.


Right-Left Rotation in AVL tree
Advantages of AVL Tree:
AVL trees can self-balance themselves and therefore provides time complexity as O(Log n) for search, insert and delete.
It is a BST only (with balancing), so items can be traversed in sorted order.
Since the balancing rules are strict compared to Red Black Tree, AVL trees in general have relatively less height and hence the search is faster.
AVL tree is relatively less complex to understand and implement compared to Red Black Trees.
Disadvantages of AVL Tree:
It is difficult to implement compared to normal BST and easier compared to Red Black
Less used compared to Red-Black trees. Due to its rather strict balance, AVL trees provide complicated insertion and removal operations as more rotations are performed.
Applications of AVL Tree:
AVL Tree is used as a first example self balancing BST in teaching DSA as it is easier to understand and implement compared to Red Black
Applications, where insertions and deletions are less common but frequent data lookups along with other operations of BST like sorted traversal, floor, ceil, min and max.
Red Black tree is more commonly implemented in language libraries like map in C++, set in C++, TreeMap in Java and TreeSet in Java.
AVL Trees can be used in a real time environment where predictable and consistent performance is required.
Related Articles:

Insertion in an AVL Tree
Deletion in an AVL Tree
Red Black Tree

"""
# height

class Avlnode:
    root.value = 10
    root.left = 11
    root.right = 12
    def __int__(self,key):
        self.key = key
        self.left = self.right = None # currently leaf
        self.height = 1

    def height(node):
        return node.height if node else 0

# rotation

    def rotate_right(y):
        x,t2 = y.left, y.left.right
        x.right,y.left = y,t2
        y.height = 1+ max(height(y.left), height(y.right))
        x.height = 1 + max(height(x.left),height(x.right))
        return x

show = Avlnode(a)
print(show.rotate_right(a))
#--------------BFS

from collections import deque
def bfs(root):
    if not root: return
    q =deque([root])
    while q:
        node =q.popleft()
        print(node.key, end=" ")
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)









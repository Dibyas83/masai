
"""
DSA Trees
Trees
The Tree data structure is similar to Linked Lists in that each node contains data and can be linked to other nodes.

We have previously covered data structures like Arrays, Linked Lists, Stacks, and Queues. These are all linear structures, which means that each element follows directly after another in a sequence. Trees however, are different. In a Tree, a single element can have multiple 'next' elements, allowing the data structure to branch out in various directions.

The data structure is called a "tree" because it looks like a tree, only upside down, just like in the image below.

R
A
B
C
D
E
F
G
H
I
The Tree data structure can be useful in many cases:

Hierarchical Data: File systems, organizational models, etc.
Databases: Used for quick data retrieval.
Routing Tables: Used for routing data in network algorithms.
Sorting/Searching: Used for sorting data and searching for data.
Priority Queues: Priority queue data structures are commonly implemented using trees, such as binary heaps.
ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Introduction

Unmute
Duration
2:49
/
Current Time
0:01

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Next
Stay
Brand logo

Tree Terminology and Rules
Learn words used to describe the tree data structure by using the interactive tree visualization below.

The whole tree

Root node

Edges

Nodes

Leaf nodes

Child nodes

Parent nodes

Tree height (h=2)

Tree size (n=10)

R
A
B
C
D
E
F
G
H
I
The first node in a tree is called the root node.

A link connecting one node to another is called an edge.

A parent node has links to its child nodes. Another word for a parent node is internal node.

A node can have zero, one, or many child nodes.

A node can only have one parent node.

Nodes without links to other child nodes are called leaves, or leaf nodes.

The tree height is the maximum number of edges from the root node to a leaf node. The height of the tree above is 2.

The height of a node is the maximum number of edges between the node and a leaf node.

The tree size is the number of nodes in the tree.

ADVERTISEMENT

Types of Trees
Trees are a fundamental data structure in computer science, used to represent hierarchical relationships. This tutorial covers several key types of trees.

Binary Trees: Each node has up to two children, the left child node and the right child node. This structure is the foundation for more complex tree types like Binay Search Trees and AVL Trees.

Binary Search Trees (BSTs): A type of Binary Tree where for each node, the left child node has a lower value, and the right child node has a higher value.

AVL Trees: A type of Binary Search Tree that self-balances so that for every node, the difference in height between the left and right subtrees is at most one. This balance is maintained through rotations when nodes are inserted or deleted.

Each of these data structures are described in detail on the next pages, including animations and how to implement them.



"""











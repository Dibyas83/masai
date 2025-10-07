
"""
A tree is an abstract data type that stores elements hierarchically. With the excep￾tion of the top element, each element in a tree has a parent element and zero or
more children elements

A tree is usually visualized by placing elements inside
ovals or rectangles, and by drawing the connections between parents and children
with straight lines. (See Figure 8.2.) We typically call the top element the root
of the tree,

Formal Tree Definition
Formally, we define a tree T as a set of nodes storing elements such that the nodes
have a parent-child relationship that satisfies the following properties:
• If T is nonempty, it has a special node, called the root of T, that has no parent.
• Each node v of T different from the root has a unique parent node w; every
node with parent w is a child of w

- This convention also allows us to define a tree recursively such
that a tree T is either empty or consists of a node r, called the root of T, and a
(possibly empty) set of subtrees whose roots are the children of r.

-Other Node Relationships
Two nodes that are children of the same parent are siblings. A node v is external
if v has no children. A node v is internal if it has one or more children. External
nodes are also known as leaves

We see that the internal nodes of the tree are associ￾ated with directories and the leaves are associated with regular files. In the UNIX
and Linux operating systems, the root of the tree is appropriately called the “root
directory,” and is represented by the symbol “/".

A node u is an ancestor of a node v if u = v or u is an ancestor of the parent of v.
Conversely, we say that a node v is a descendant of a node u if u is an ancestor of v

An edge of tree T is a pair of nodes (u,v) such that u is the parent of v, or vice
versa. A path of T is a sequence of nodes such that any two consecutive nodes in
the sequence form an edge
                                Tree
            BinaryTree                         LinkedTree

ArrayBinaryTree   LinkedBinaryTree
Figure 8.5: Our own inheritance hierarchy for modeling various abstractions and
implementations of tree data structures

Ordered Trees
A tree is ordered if there is a meaningful linear order among the children of each
node; that is, we purposefully identify the children of a node as being the first,
second, third, and so on. Such an order is usually visualized by arranging siblings
left to right, according to their order

The Tree Abstract Data Type
As we did with positional lists in Section 7.4,we define a tree ADT using the
concept of a position as an abstraction for a node of a tree. An element is stored
at each position, and positions satisfy parent-child relationships that define the tree
structure. A position object for a tree supports the method:

p.element( ): Return the element stored at position p.

The tree ADT then supports the following accessor methods, allowing a user to
navigate the various positions of a tree

T.root( ): Return the position of the root of tree T,
or None if T is empty.
T.is root(p): Return True if position p is the root of Tree T.
T.parent(p): Return the position of the parent of position p,
or None if p is the root of T.
T.num children(p): Return the number of children of position p.
T.children(p): Generate an iteration of the children of position p.
T.is leaf(p): Return True if position p does not have any children.
len(T): Return the number of positions (and hence elements) that
are contained in tree T.
T.is empty( ): Return True if tree T does not contain any positions.
T.positions( ): Generate an iteration of all positions of tree T.
iter(T): Generate an iteration of all elements stored within tree T

If a tree T is ordered, then T.children(p) reports the children of p in the natural
order. If p is a leaf, then T.children(p) generates an empty iteration. In similar
regard, if tree T is empty, then both T.positions( ) and iter(T) generate empty iter￾ations.

A Tree Abstract Base Class in Python
In discussing the object-oriented design principle of abstraction in Section 2.1.2, we
noted that a public interface for an abstract data type is often managed in Python via
duck typing. For example, we defined the notion of the public interface for a queue
ADT in Section 6.2, and have since presented several classes that implement the
queue interface (e.g., ArrayQueue in Section 6.2.2, LinkedQueue in Section 7.1.2,
CircularQueue in Section 7.2.2). However, we never gave any formal definition of
the queue ADT in Python; all of the concrete implementations were self-contained
classes that just happen to adhere to the same public interface. A more formal
mechanism to designate the relationships between different implementations of the
same abstraction is through the definition of one class that serves as an abstract
base class, via inheritance, for one or more concrete classes.

Tree class does not define any internal representation for stor￾ing a tree, and five of the methods given in that code fragment remain abstract
(root, parent, num children, children, and len ); each of these methods raises a
NotImplementedError. (A more formal approach for defining abstract base classes
and abstract methods, using Python’s abc module, is described in Section 2.4.3.)
The subclasses are responsible for overriding abstract methods, such as children, to
provide a working implementation for each behavior, based on their chosen internal
representation.

Although the Tree class is an abstract base class, it includes several concrete
methods with implementations that rely on calls to the abstract methods of the class.
In defining the tree ADT in the previous section, we declare ten accessor methods.
Five of those are the ones we left as abstract, in Code Fragment 8.1. The other five
can be implemented based on the former.
 Code Fragment 8.2 provides concrete
implementations for methods is root, is leaf, and is empty. In Section 8.4, we will
explore general algorithms for traversing a tree that can be used to provide concrete
implementations of the positions and iter methods within the Tree class. The
beauty of this design is that the concrete methods defined within the Tree abstract
base class will be inherited by all subclasses. This promotes greater code reuse, as
there will be no need for those subclasses to reimplement such behaviors


The depth of p is the number of ancestors of p, excluding p itself
• If p is the root, then the depth of p is 0.
• Otherwise, the depth of p is one plus the depth of the parent of p

Height
The height of a position p in a tree T is also defined recursively:
• If p is a leaf, then the height of p is 0.
• Otherwise, the height of p is one more than the maximum of the heights of
p’s children.
The height of a nonempty tree T is equal to the maximum of
the depths of its leaf positions.



"""
class Tree:  # Abstract base class representing a tree structure.”””


    # ------------------------------- nested Position class -------------------------------
    class Position:  # An abstraction representing the location of a single element.”””

        def element(self):  #Return the element stored at this Position.”””
            raise NotImplementedError(' must be implemented by subclass' )
        def __eq__(self, other):  # Return True if other Position represents the same location.”””
            raise NotImplementedError( 'must be implemented by subclass ')
        def __ne__(self, other):  # Return True if other does not represent the same location.”””
            return not (self == other) # opposite of eq
    # ---------- abstract methods that concrete subclass must support ----------
    def root(self): # Return Position representing the tree s root (or None if empty).”””
        raise NotImplementedError( 'must be implemented by subclass' )
    def parent(self, p):  # Return Position representing p s parent (or None if p is root).”””

        raise NotImplementedError( 'must be implemented by subclass' )
    def num_children(self, p): # Return the number of children that Position p has.”””
        raise NotImplementedError( 'must be implemented by subclass' )
    def children(self, p): # Generate an iteration of Positions representing p s children.”””
        raise NotImplementedError( 'must be implemented by subclass' )
    def __len__(self): # Return the total number of elements in the tree.”””
        raise NotImplementedError( 'must be implemented by subclass' )

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):  # Return True if Position p represents the root of the tree.”””
        return self.root( ) == p
    def is_leaf(self, p): # Return True if Position p does not have any children.”””
        return self.num_children(p) == 0
    def is_empty(self): # Return True if the tree is empty.”””
        return len(self) == 0

"""
 Computing Depth and Height
Let p be the position of a node of a tree T. The depth of p is the number of
ancestors of p, excluding p itself. For example, in the tree of Figure 8.2, the node
storing International has depth 2. Note that this definition implies that the depth of
the root of T is 0. The depth of p can also be recursively defined as follows:
• If p is the root, then the depth of p is 0.
• Otherwise, the depth of p is one plus the depth of the parent of p.

algorithm T.depth(p) runs in O(n) worst￾case time, where n is the total number of positions of T, because a position of T
may have depth n− 1 if all nodes form a single branch

Height
The height of a position p in a tree T is also defined recursively:
• If p is a leaf, then the height of p is 0.
• Otherwise, the height of p is one more than the maximum of the heights of
p’s children.
The height of a nonempty tree T is the height of the root of T. For example, the
tree of Figure 8.2 has height 4. In addition, height can also be viewed as follow
"""

def depth(self, p):  # Return the number of levels separating Position p from the root.”””
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))


def height1(self): # works, but O(nˆ2) worst-case time .Return the height of the tree.”””
    return max(self.depth(p) for p in self.positions( ) if self.is_leaf(p))


"""
We can compute the height of a tree more efficiently, in O(n) worst-case time,
by relying instead on the original recursive definition. To do this, we will param￾eterize a function based on a position within the tree, and calculate the height of
the subtree rooted at that position. Algorithm height2, shown as nonpublic method
height2 in Code Fragment 8.5, computes the height of tree T in this way.
"""

def height2(self, p): # time is linear in size of subtree
    # Return the height of the subtree rooted at Position p.”””
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))

"""
It is important to understand why algorithm height2 is more efficient than
height1. The algorithm is recursive, and it progresses in a top-down fashion. If
the method is initially called on the root of T, it will eventually be called once for
each position of T. This is because the root eventually invokes the recursion on
each of its children, which in turn invokes the recursion on each of their children,
and so on


Although we do not yet have a concrete
implementation of children(p), we assume that such an iteration is generated in
O(cp +1) time, where cp denotes the number of children of p. Algorithm height2
spends O(cp +1) time at each position p to compute the maximum, and its overall
running time is O(∑p(cp + 1)) = O(n+ ∑p cp).

def height(self, p=None):
68 ”””Return the height of the subtree rooted at Position p.
69
70 If p is None, return the height of the entire tree.
71 ”””
72 if p is None:
73 p = self.root( )
74 return self. height2(p) # start height2 recursion
Code Fragment 8.6: Public method Tree.height that computes the height of the
entire tree by default, or a subtree rooted at given position, if specified.

                Binary Trees
A binary tree is an ordered tree with the following properties:
1. Every node has at most two children.
2. Each child node is labeled as being either a left child or a right child.
3. A left child precedes a right child in the order of children of a node.

The subtree rooted at a left or right child of an internal node v is called a left subtree
or right subtree, respectively, of v. A binary tree is proper if each node has either
zero or two children. Some people also refer to such trees as being full binary
trees

: An important class of binary trees arises in contexts where we wish
to represent a number of different outcomes that can result from answering a series
of yes-or-no questions. Each internal node is associated with a question. Starting at
the root, we go to the left or right child of the current node, depending on whether
the answer to the question is “Yes” or “No.” With each decision, we follow an
edge from a parent to a child, eventually tracing a path in the tree from the root
to a leaf. Such binary trees are known as decision trees, because a leaf position p
in such a tree represents a decision of what to do if the questions associated with
p’s ancestors are answered in a way that leads to p. A decision tree is a proper
binary tre


An arithmetic expression can be represented by a binary tree whose
leaves are associated with variables or constants, and whose internal nodes are
associated with one of the operators +, −, ×, and /. (See Figure 8.8.) Each node
in such a tree has a value associated with it.
• If a node is leaf, then its value is that of its variable or constant.
• If a node is internal, then its value is defined by applying its operation to the
values of its children.

                            -
                /                       +
        *             +            *               6
    +       3     -       2     3       -
3      1        9    5               7      4

This tree represents
the expression ((((3 + 1) × 3)/((9 − 5) + 2)) − ((3 × (7 − 4)) + 6)). The value
associated with the internal node labeled “/” is 2.

if we were to allow unary operators,
like negation (−), as in “−x,” then we could have an improper binary tree
As an abstract data type, a binary tree is a specialization of a tree that supports three
additional accessor methods:
T.left(p): Return the position that represents the left child of p,
or None if p has no left child.
T.right(p): Return the position that represents the right child of p,
or None if p has no right child.
T.sibling(p): Return the position that represents the sibling of p,
or None if p has no sibling.

7. By using inheritance, a binary tree supports all the functionality that was
defined for general trees (e.g., parent, is leaf, root). Our new class also inherits the
nested Position class that was originally defined within the Tree class definition.
In addition, the new class provides declarations for new abstract methods left and
right that should be supported by concrete subclasses of BinaryTree

The new sibling method is derived from the combination of left, right, and parent. Typ￾ically, we identify the sibling of a position p as the “other” child of p’s parent.
However, if p is the root, it has no parent, and thus no sibling. Also, p may be the
only child of its parent, and thus does not have a sibling.

 Code Fragment 8.7 provides a concrete implementation of the children
method; this method is abstract in the Tree class. Although we have still not speci-
fied how the children of a node will be stored, we derive a generator for the ordered
children based upon the implied behavior of abstract methods left and right.

In a binary tree, level 0 has at most one node (the
root), level 1 has at most two nodes (the children of the root), level 2 has at most
four nodes, and so on. (See Figure 8.9.) In general, level d has at most 2d nodes
grows exponentially as we go down the tree.

Proposition 8.8: Let T be a nonempty binary tree, and let n, nE, nI and h denote
the number of nodes, number of external nodes, number of internal nodes, and
height of T, respectively. Then T has the following properties:
1. h+1 ≤ n ≤ 2^h+1 −1
2. 1 ≤ nE ≤ 2^h
3. h ≤ nI ≤ 2^h −1
4. log(n+1)−1 ≤ h ≤ n−1
Also, if T is proper, then T has the following properties:
1. 2h+1 ≤ n ≤ 2^(h+1) −1
2. h+1 ≤ nE ≤ 2^h
3. h ≤ nI ≤ 2^h −1
4. log(n+1)−1 ≤ h ≤ (n−1)/2
"""

class BinaryTree(Tree): # Abstract base class representing a binary tree structure.”””

 # --------------------- additional abstract methods ---------------------
    def left(self, p): # Return a Position representing p s left child.Return None if p does not have a left child.

        raise NotImplementedError( 'must be implemented by subclass' )
    def right(self, p): # Return a Position representing p s right child.Return None if p does not have a right child.

        raise NotImplementedError( 'must be implemented by subclass' )

 # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):  # Return a Position representing p s sibling (or None if no sibling).”””
        parent = self.parent(p)
        if parent is None: # p must be the root
            return None # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent) # possibly None
            else:
                return self.left(parent) # possibly None
    def children(self, p):  # Generate an iteration of Positions representing p s children.”””
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
#Code Fragment 8.7: A BinaryTree abstract base class that extends the existing Tree
#abstract base class from Code Fragments 8.1 and 8.2.

"""
the following relationship exists
between the number of internal nodes and external nodes in a proper binary tree.
Proposition 8.9: In a nonempty proper binary tree T, with nE external nodes and
nI internal nodes, we have nE = nI +1.

- If T has only one node v, we remove v and place it on the external-node
pile. Thus, the external-node pile has one node and the internal-node pile is
empty.
-  T has more than one node, we remove from T an (arbitrary)
external node w and its parent v, which is an internal node. We place w on
the external-node pile and v on the internal-node pile. If v has a parent u,
then we reconnect u with the former sibling z of w, as shown in Figure 8.10.
This operation, removes one internal node and one external node, and leaves
the tree being a proper binary tree.
Repeating this operation, we eventually are left with a final tree consisting
of a single node

We have not yet defined key imple￾mentation details for how a tree will be represented internally, and how we can
effectively navigate between parents and children. Specifically, a concrete imple￾mentation of a tree must provide methods root, parent, num children, children,
len , and in the case of BinaryTree, the additional accessors left and right

 Linked Structure for Binary Trees
A natural way to realize a binary tree T is to use a linked structure, with a node
(see Figure 8.11a) that maintains references to the element stored at a position p
and to the nodes associated with the children and parent of p. If p is the root of
T, then the parent field of p is None. Likewise, if p does not have a left child
(respectively, right child), the associated field is None. The tree itself maintains an
instance variable storing a reference to the root node (if any), and a variable, called
size, that represents the overall number of nodes of T

                                    parent
                l-child ref   ref to ele at p  r-child ref      r child

                   parent                                          parent
                                                l-child ref   ref to ele at p  r-child ref 
l-child ref   ref to ele at p  r-child ref 

Python Implementation of a Linked Binary Tree Structure
We
define a simple, nonpublic Node class to represent a node, and a public Position
class that wraps a node. We provide a validate utility for robustly checking the
validity of a given position instance when unwrapping it, and a make position
utility for wrapping a node as a position to return to a caller
-------------------
In Python, __ne__ is a special method, also known as a "dunder" or "magic" method, that implements the "not equal to" (!=) operator for objects. When you use object1 != object2, Python internally calls object1.__ne__(object2).
Key aspects of __ne__:
Operator Overloading: It allows you to define how the != operator behaves for instances of your custom classes.
Comparison Logic: The method should return True if the two objects are considered not equal and False otherwise.
Signature: It typically takes two arguments: self (the instance on which the method is called) and other (the object being compared to).
Default Behavior: If __ne__ is not explicitly defined in a class, Python's default implementation will typically delegate to __eq__ (the equality method) and return the negation of its result. This means if object1 == object2 is True, then object1 != object2 will be False by default, and vice versa.
Consistency with __eq__: It is generally recommended to ensure that __ne__ and __eq__ are consistent, meaning a != b should be the logical negation of a == b.
Example:
Python

class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return self.value == other.value

    def __ne__(self, other):
        # Explicitly defining __ne__ as the negation of __eq__
        if not isinstance(other, MyClass):
            return NotImplemented
        return self.value != other.value

obj1 = MyClass(10)
obj2 = MyClass(20)
obj3 = MyClass(10)

print(obj1 != obj2) # True
print(obj1 != obj3) # False
print(obj1.__ne__(obj2)) # True (direct call)
--------------------------
with a constructor and with concrete implementations for the methods that remain abstract in the Tree and
BinaryTree classes. The constructor creates an empty tree by initializing root to
None and size to zero. These accessor methods are implemented with careful use
of the validate and make position utilities to safeguard against boundary case

Operations for Updating a Linked Binary Tree 

We chose not to declare update methods as part of the Tree or BinaryTree ab￾stract base classes for several reasons. First, although the principle of encapsula￾tion suggests that the outward behaviors of a class need not depend on the internal
representation, the efficiency of the operations depends greatly upon the representa￾tion
We prefer to have each concrete implementation of a tree class offer the most suitable options for updating a tree.

The second reason we do not provide update methods in the base class is that
we may not want such update methods to be part of a public interface. There are
many applications of trees, and some forms of update operations that are suitable
for one application may be unacceptable in another. However, if we place an update
method in a base class, any class that inherits from that base will inherit the update
method
For linked binary trees, a reasonable set of update methods to support for gen￾eral usage are the following:
T.add root(e): Create a root for an empty tree, storing e as the element,
and return the position of that root; an error occurs if the
tree is not empty.

T.add left(p, e): Create a new node storing element e, link the node as the
left child of position p, and return the resulting position;
an error occurs if p already has a left child.

T.add right(p, e): Create a new node storing element e, link the node as the
right child of position p, and return the resulting position;
an error occurs if p already has a right child.

T.replace(p, e): Replace the element stored at position p with element e,
and return the previously stored element.

T.delete(p): Remove the node at position p, replacing it with its child,
if any, and return the element that had been stored at p;
an error occurs if p has two children.

T.attach(p, T1, T2): Attach the internal structure of trees T1 and T2, respec￾tively, as the left and right subtrees of leaf position p of
T, and reset T1 and T2 to empty trees; an error condition
occurs if p is not a leaf.

We have specifically chosen this collection of operations because each can be
implemented in O(1) worst-case time with our linked representation.
The most complex of these are delete and attach, due to the case analyses involving the
various parent-child relationships and boundary conditions, yet there remains only
a constant number of operations to perform.

To avoid the problem of undesirable update methods being inherited by sub￾classes of LinkedBinaryTree, we have chosen an implementation in which none
of the above methods are publicly supported. Instead, we provide nonpublic ver￾sions of each, for example, providing the underscored delete in lieu of a public
delete


------------------------
The __slots__ attribute in Python classes is used to explicitly declare the data members (attributes) that an instance of the class will possess. This declaration has several significant implications: 
Memory Optimization: By default, Python instances store their attributes in a dictionary (__dict__). This dictionary provides flexibility, allowing new attributes to be added dynamically at runtime. However, a dictionary for each instance can consume significant memory, especially when dealing with a large number of instances. When __slots__ is defined, Python instead allocates a fixed amount of space for the specified attributes, often in a more compact structure like a hidden array of references, thereby reducing memory consumption per instance.
Attribute Access Speed: Storing attributes in a fixed-size structure can also lead to faster attribute lookup times compared to dictionary lookups.
Preventing Dynamic Attribute Creation: When __slots__ is defined, instances of that class cannot have new attributes added to them at runtime unless those attributes are explicitly listed in __slots__. Attempting to add an unlisted attribute will result in an AttributeError. This can be beneficial for enforcing a fixed structure and preventing typos or unintended attribute creation.
How to use __slots__:
To use __slots__, define a class attribute named __slots__ and assign it an iterable (e.g., a tuple or list) containing the names of the allowed instance attributes as strings.
Python

class MyClass:
    __slots__ = ('attribute1', 'attribute2', 'attribute3')

    def __init__(self, val1, val2, val3):
        self.attribute1 = val1
        self.attribute2 = val2
        self.attribute3 = val3

# Example usage
obj = MyClass(10, 20, 30)
print(obj.attribute1)  # Output: 10

# Attempting to add a new attribute not in __slots__ will raise an AttributeError
# obj.new_attribute = 40 
Important Considerations:
Inheritance: If a class with __slots__ inherits from another class, all classes in the inheritance hierarchy must also define __slots__ (or inherit from object in Python 3, which handles __slots__ implicitly for its base classes) to fully benefit from the memory and speed optimizations. If a parent class does not define __slots__ and therefore has a __dict__, then the child class instances will still have a __dict__, negating some of the benefits.
No __dict__ or __weakref__: Instances of classes using __slots__ will typically not have a __dict__ attribute or a __weakref__ attribute (unless explicitly included in __slots__). This means they cannot be directly used with functions or mechanisms that rely on these attributes, such as weakref.ref.
Flexibility Trade-off: While __slots__ offers performance benefits, it reduces the dynamic flexibility of adding attributes to instances at runtime. This trade-off should be considered based on the specific needs of the application.



----------------------

"""
class LinkedBinaryTree(BinaryTree): # Linked representation of a binary tree structure.”””

    class _Node: # Lightweight, nonpublic class for storing a node.
        __slots__ = '_element' , '_parent' , '_left' , '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position): # An abstraction representing the location of a single element.”””

        def __init__(self, container, node): # Constructor should not be invoked by user.”””
            self._container = container
            self._node = node
        def element(self): # Return the element stored at this Position.”””
            return self._node._element
        def __eq__(self, other): # Return True if other is a Position representing the same location.”””
            return type(other) is type(self) and other._node is self._node
    def _validate(self, p): # Return associated node, if position is valid.”””
        if not isinstance(p, self.Position):
            raise TypeError( 'p must be proper Position type ')
        if p._container is not self:
            raise ValueError( 'p does not belong to this container ')
        if p._node._parent is p._node: # convention for deprecated nodes
            raise ValueError( 'p is no longer valid' )
        return p._node

    def _make_position(self, node): # Return Position instance for given node (or None if no node).”””
        return self.Position(self, node) if node is not None else None
        #-------------------------- binary tree constructor --------------------------
    def __init__(self): # Create an initially empty binary tree.”””
        self._root = None
        self._size = 0

    #-------------------------- public accessors --------------------------
    def __len__(self): # Return the total number of elements in the tree.”””
        return self._size
    def root(self): # Return the root Position of the tree (or None if tree is empty).”””
        return self._make_position(self._root)
    def parent(self, p): #Return the Position of p s parent (or None if p is root).”””
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p): # Return the Position of p s left child (or None if no left child).”””
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p): # Return the Position of p s right child (or None if no right child).”””
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p): # Return the number of children of Position p.”””
        node = self._validate(p)
        count = 0
        if node._left is not None: # left child exists
            count += 1
        if node._right is not None: # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None: raise ValueError( 'Root exists' )
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """ Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError( 'Left child exists ')
        self._size += 1
        node._left = self._Node(e, node) # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """ Create a new right child for Position p, storing element e
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """

        node = self._validate(p)

        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)  # node is its parent
        return self._make_position(node._right)


    def _replace(self, p, e):
        """Replace the  element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
             Return the element that had been stored at Position p.
            Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError( 'p has two children' )
        child = node._left if node._left else node._right # might be None
        if child is not None:
            child._parent = node._parent # child s grandparent becomes parent
        if node is self._root:
            self._root = child # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError(' position must be leaf' )
        if not type(self) is type(t1) is type(t2): # all 3 trees must be same type
            raise TypeError( 'Tree types must match' )
        self._size += len(t1) + len(t2)
        if not t1.is_empty( ): # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty( ): # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None # set t2 instance to empty
            t2._size = 0
"""
root, left, right, parent, and num children are imple￾mented directly in LinkedBinaryTree and take O(1) time
and all other methods also
The depth method at position p runs in O(dp +1) time where dp is its depth; the height
method on the root of the tree runs in O(n) time

-----------
    Array-Based Representation of a Binary Tree
An alternative representation of a binary tree T is based on a way of numbering the
positions of T. For every position p of T, let f(p) be the integer defined as follows.
• If p is the root of T, then f(p) = 0.
• If p is the left child of position q, then f(p) = 2 f(q) +1.
• If p is the right child of position q, then f(p) = 2 f(q) +2.
The numbering function f is known as a level numbering of the positions in a
binary tree T, for it numbers the positions on each level of T in increasing order
from left to right. (See Figure 8.12.) Note well that the level numbering is based
on potential positions within the tree, not actual positions of a given tree, so they
are not necessarily consecutive

One advantage of an array-based representation of a binary tree is that a posi￾tion p can be represented by the single integer f(p), and that position-based meth￾ods such as root, parent, left, and right can be implemented using simple arithmetic
operations on the number f(p).
Based on our formula for the level numbering, the
left child of p has index 2 f(p) + 1, the right child of p has index 2 f(p) + 2, and
the parent of p has index (f(p)− 1)/2.

. Let n be the number of nodes of T, and let fM be the maximum value
of f(p) over all the nodes of T. The array A requires length N = 1 + fM, since
elements range from A[0] to A[ fM]. Note that A may have a number of empty cells
that do not refer to existing nodes of T. In fact, in the worst case, N = 2n − 1,
the justification of which is left as an exercise (R-8.16). In Section 9.3, we will
see a class of binary trees, called “heaps” for which N = n. Thus, in spite of the
worst-case space usage, there are applications for which the array representation
of a binary tree is space efficient.

deleting a node and promoting its child takes O(n) time because it is not just the child that moves locations within
the array, but all descendants of that child.

When representing a binary tree with a linked structure, each node explicitly main￾tains fields left and right as references to individual children. For a general tree,
there is no a priori limit on the number of children that a node may have. A natural
way to realize a general tree T as a linked structure is to have each node store a
single container of references to its children. For example, a children field of a
node can be a Python list of references to the children of the node

by using a collection to store the children of each position p, we can implement
children(p) by simply iterating that collection.
Operation                               Running Time
len, is empty                           O(1)
root, parent, is root, is leaf          O(1)
children(p)                             O(cp +1)
depth(p)                                O(dp +1)
height                                  O(n)
Table 8.2: Running times of the accessor methods of an n-node general tree im￾plemented with a linked structure. We let cp denote the number of children of a
position p. The space usage is O(n)

        Tree Traversal Algorithms
A traversal of a tree T is a systematic way of accessing, or “visiting,” all the posi￾tions of T

    Preorder and Postorder Traversals of General Trees
In a preorder traversal of a tree T, the root of T is visited first and then the sub￾trees rooted at its children are traversed recursively. If the tree is ordered, then
the subtrees are traversed according to the order of the children

Algorithm preorder(T, p):
    perform the “visit” action for position p
    for each child c in T.children(p) do
       preorder(T, c)                       {recursively traverse the subtree rooted at c}

        Postorder Traversal
it recursively traverses the subtrees rooted at the children of the root first, and
then visits the root (hence, the name “postorder”)
    
Algorithm postorder(T, p):
    for each child c in T.children(p) do
       postorder(T, c)

        BFS
A breadth-first traversal is a common approach used in software for playing
games. A game tree represents the possible choices of moves that might be made
by a player (or computer) during a game, with the root of the tree being the initial
configuration for the game. For example, Figure 8.17 displays a partial game tree
for Tic-Tac-Toe.
A breadth-first traversal of such a game tree is often performed because a computer
may be unable to explore a complete game tree in a limited amount of time. So the
computer will consider all moves, then responses to those moves, going as deep as
computational time allows
The process is not recursive, since we are not traversing entire subtrees at once. We use
a queue to produce a FIFO (i.e., first-in first-out) semantics for the order in which
we visit nodes. The overall running time is O(n), due to the n calls to enqueue and
n calls to dequeue

Algorithm breadthfirst(T):
   Initialize queue Q to contain T.root( )
   while Q not empty do
     p = Q.dequeue( ) {p is the oldest entry in the queue}
     perform the “visit” action for position p
     for each child c in T.children(p) do
       Q.enqueue(c) {add p’s children to the end of the queue for later visits}

        Inorder Traversal of a Binary Tree

During an inorder traversal, we visit a position between the recursive traver￾sals of its left and right subtrees. The inorder traversal of a binary tree T can be
informally viewed as visiting the nodes of T “from left to right.” Indeed, for every
position p, the inorder traversal visits p after all the positions in the left subtree of
p and before all the positions in the right subtree of p
starts from botom extreme left 
                                   12
                    6                             18
            /            \                    /        \
          4               10               14           19
    2          5       8      11       13     16
  /   \               /  \                   /   \
1       3           7     9                 15   17
Algorithm inorder(p):
if p has a left child lc then
inorder(lc) {recursively traverse the left subtree of p}
perform the “visit” action for position p
if p has a right child rc then
inorder(rc) {recursively traverse the right subtree of p}

the inorder
traversal visits positions in a consistent order with the standard representation of
the expression, as in 3+1×3/9−5+2... (albeit without parentheses).


                Binary Search Trees
An important application of the inorder traversal algorithm arises when we store an
ordered sequence of elements in a binary tree, defining a structure we call a binary
search tree. Let S be a set whose unique elements have an order relation. For
example, S could be a set of integers. A binary search tree for S is a binary tree T
such that, for each position p of T:
• Position p stores an element of S, denoted as e(p).
• Elements stored in the left subtree of p (if any) are less than e(p).
• Elements stored in the right subtree of p (if any) are greater than e(p).

Implementing Tree Traversals in Python
When first defining the tree ADT in Section 8.1.2, we stated that tree T should
include support for the following methods:
T.positions( ): Generate an iteration of all positions of tree T.
iter(T): Generate an iteration of all elements stored within tree T.
At that time, we did not make any assumption about the order in which these
iterations report their results. In this section, we demonstrate how any of the tree
traversal algorithms we have introduced could be used to produce these iterations.
To begin, we note that it is easy to produce an iteration of all elements of a
tree, if we rely on a presumed iteration of all positions. Therefore, support for
the iter(T) syntax can be formally provided by a concrete implementation of the
special method iter within the abstract base class Tree. We rely on Python’s
generator syntax as the mechanism for producing iterations. (See Section 1.8.) Our
implementation of Tree. iter is given in Code Fragment 8.16.
75 def iter (self):
76 ”””Generate an iteration of the tree s elements.”””
77 for p in self.positions( ): # use same order as positions()
78 yield p.element( ) # but yield each element

Preorder Traversal

def preorder(self):
80 ”””Generate a preorder iteration of positions in the tree.”””
81 if not self.is empty( ):
82 for p in self. subtree preorder(self.root( )): # start recursion
83 yield p
84
85 def subtree preorder(self, p):
86 ”””Generate a preorder iteration of positions in subtree rooted at p.”””
87 yield p # visit p before its subtrees
88 for c in self.children(p): # for each child c
89 for other in self. subtree preorder(c): # do preorder of c’s subtree
90 yield other # yielding each to our caller


Postorder Traversal
We can implement a postorder traversal using very similar technique as with a
preorder traversal. The only difference is that within the recursive utility for a post￾order we wait to yield position p until after we have recursively yield the positions
in its subtrees. An implementation is given in Code Fragment 8.19.
94 def postorder(self):
95 ”””Generate a postorder iteration of positions in the tree.”””
96 if not self.is empty( ):
97 for p in self. subtree postorder(self.root( )): # start recursion
98 yield p
99
100 def subtree postorder(self, p):
101 ”””Generate a postorder iteration of positions in subtree rooted at p.”””
102 for c in self.children(p): # for each child c
103 for other in self. subtree postorder(c): # do postorder of c’s subtree
104 yield other # yielding each to our caller
105 yield p # visit p after its subtrees


Inorder Traversal for Binary Trees
The preorder, postorder, and breadth-first traversal algorithms are applicable to
all trees, and so we include their implementations within the Tree abstract base
class. Those methods are inherited by the abstract BinaryTree class, the concrete
LinkedBinaryTree class, and any other dependent tree classes we might develop.
The inorder traversal algorithm, because it explicitly relies on the notion of a
left and right child of a node, only applies to binary trees. We therefore include its
definition within the body of the BinaryTree class. We use a similar technique to
implement an inorder traversal (Code Fragment 8.21) as we did with preorder and
postorder traversals.
www.it-ebooks.info
336 Chapter 8. Trees
106 def breadthfirst(self):
107 ”””Generate a breadth-first iteration of the positions of the tree.”””
108 if not self.is empty( ):
109 fringe = LinkedQueue( ) # known positions not yet yielded
110 fringe.enqueue(self.root( )) # starting with the root
111 while not fringe.is empty( ):
112 p = fringe.dequeue( ) # remove from front of the queue
113 yield p # report this position
114 for c in self.children(p):
115 fringe.enqueue(c) # add children to back of queue
Code Fragment 8.20: An implementation of a breadth-first traversal of a tree. This
code should be included in the body of the Tree class. 


37 def inorder(self):
38 ”””Generate an inorder iteration of positions in the tree.”””
39 if not self.is empty( ):
40 for p in self. subtree inorder(self.root( )):
41 yield p
42
43 def subtree inorder(self, p):
44 ”””Generate an inorder iteration of positions in subtree rooted at p.”””
45 if self.left(p) is not None: # if left child exists, traverse its subtree
46 for other in self. subtree inorder(self.left(p)):
47 yield other
48 yield p # visit p between its subtrees
49 if self.right(p) is not None: # if right child exists, traverse its subtree
50 for other in self. subtree inorder(self.right(p)):
51 yield other


Applications of Tree Traversals
In this section, we demonstrate several representative applications of tree traversals,
including some customizations of the standard traversal algorithms.
Table of Contents
When using a tree to represent the hierarchical structure of a document, a preorder
traversal of the tree can naturally be used to produce a table of contents for the doc￾ument

The unindented version of the table of contents, given a tree T, can be produced
with the following code:
for p in T.preorder( ):
print(p.element( ))

A preferred approach to producing an indented table of contents is to redesign
a top-down recursion that includes the current depth as an additional parameter.
Such an implementation is provided in Code Fragment 8.23. This implementation
runs in worst-case O(n) time (except, technically, the time it takes to print strings
of increasing lengths).
1 def preorder indent(T, p, d):
2 ”””Print preorder representation of subtree of T rooted at p at depth d.”””
3 print(2 d + str(p.element( ))) # use depth for indentation
4 for c in T.children(p):
5 preorder indent(T, c, d+1) # child depth is d+1

Tree Traversal Algorithms 339
1 def preorder label(T, p, d, path):
2 ”””Print labeled representation of subtree of T rooted at p at depth d.”””
3 label = . .join(str(j+1) for j in path) # displayed labels are one-indexed
4 print(2 d + label, p.element( ))
5 path.append(0) # path entries are zero-indexed
6 for c in T.children(p):
7 preorder label(T, c, d+1, path) # child depth is d+1
8 path[−1] += 1
9 path.pop( )
Code Fragment 8.24: Efficient recursion for printing an indented and labeled pre￾sentation of a preorder traversal.
---------
def parenthesize(T, p):
2 ”””Print parenthesized representation of subtree of T rooted at p.”””
3 print(p.element( ), end= ) # use of end avoids trailing newline
4 if not T.is leaf(p):
5 first time = True
6 for c in T.children(p):
7 sep = ( if first time else , # determine proper separator
8 print(sep, end= )
9 first time = False # any future passes will not be the first
10 parenthesize(T, c) # recur on child
11 print( ) , end= ) # include closing parenthesis


The recursive computation of disk space is emblematic of a postorder traversal,
as we cannot effectively compute the total space used by a directory until after we
know the space that is used by its children directories. Unfortunately, the formal
implementation of postorder, as given in Code Fragment 8.19 does not suffice for
this purpose. As it visits the position of a directory, there is no easy way to discern
which of the previous positions represent children of that directory, nor how much
recursive disk space was allocated.
We would like to have a mechanism for children to return information to the
parent as part of the traversal process. A custom solution to the disk space prob￾lem, with each level of recursion providing a return value to the (parent) caller, is
provided in Code Fragment 8.26.
1 def disk space(T, p):
2 ”””Return total disk space for subtree of T rooted at p.”””
3 subtotal = p.element( ).space( ) # space used at position p
4 for c in T.children(p):
5 subtotal += disk space(T, c) # add child’s space to subtotal
6 return subtotal
Code Fragment 8.26: Recursive computation of disk space for a tree. We assume
that a space( ) method of each tree element reports the local space used at that
position.


Euler Tours and the Template Method Pattern 
The various applications described in Section 8.4.5 demonstrate the great power
of recursive tree traversals. Unfortunately, they also show that the specific imple￾mentations of the preorder and postorder methods of our Tree class, or the inorder
method of the BinaryTree class, are not general enough to capture the range of
computations we desire.

 In some cases, we need more of a blending of the ap￾proaches, with initial work performed before recurring on subtrees, additional work
performed after those recursions, and in the case of a binary tree, work performed
between the two possible recursions

Furthermore, in some contexts it was impor￾tant to know the depth of a position, or the complete path from the root to that
position, or to return information from one level of the recursion to another.

The Euler tour traversal of a general tree T can be informally defined as a “walk” around T, where
we start by going from the root toward its leftmost child, viewing the edges of T as
being “walls” that we always keep to our left. (See Figure 8.21.)

The complexity of the walk is O(n), because it progresses exactly two times
along each of the n−1 edges of the tree—once going downward along the edge, and
later going upward along the edge. To unify the concept of preorder and postorder
traversals, we can think of there being two notable “visits” to each position p:
• A “pre visit” occurs when first reaching the position, that is, when the walk
passes immediately left of the node in our visualization.
• A “post visit” occurs when the walk later proceeds upward from that position,
that is, when the walk passes to the right of the node in our visualization.

That tour contains two contiguous subtours, one traversing that position’s left
subtree and another traversing the right subtree.

Algorithm eulertour(T, p):
perform the “pre visit” action for position p
for each child c in T.children(p) do
eulertour(T, c) {recursively tour the subtree rooted at c}
perform the “post visit” action for position p
Code Fragment 8.27: Algorithm eulertour for performing an Euler tour traversal of
a subtree rooted at position p of a tree.

The Template Method Pattern
To provide a framework that is reusable and adaptable, we rely on an interesting
object-oriented software design pattern, the template method pattern. The template
method pattern describes a generic computation mechanism that can be specialized
for a particular application by redefining certain steps. To allow customization, the
primary algorithm calls auxiliary functions known as hooks at designated steps of
the process.
In the context of an Euler tour traversal, we define two separate hooks, a pre￾visit hook that is called before the subtrees are traversed, and a postvisit hook that is
called after the completion of the subtree traversals. Our implementation will take
the form of an EulerTour class that manages the process, and defines trivial defi-
nitions for the hooks that do nothing. The traversal can be customized by defining
a subclass of EulerTour and overriding one or both hooks to provide specialized
behavior

Tree Traversal Algorithms 343
1 class EulerTour:
2 ”””Abstract base class for performing Euler tour of a tree.
3
4 hook previsit and hook postvisit may be overridden by subclasses.
5 ”””
6 def init (self, tree):
7 ”””Prepare an Euler tour template for given tree.”””
8 self. tree = tree
9
10 def tree(self):
11 ”””Return reference to the tree being traversed.”””
12 return self. tree
13
14 def execute(self):
15 ”””Perform the tour and return any result from post visit of root.”””
16 if len(self. tree) > 0:
17 return self. tour(self. tree.root( ), 0, [ ]) # start the recursion
18
19 def tour(self, p, d, path):
20 ”””Perform tour of subtree rooted at Position p.
21
22 p Position of current node being visited
23 d depth of p in the tree
24 path list of indices of children on path from root to p
25 ”””
26 self. hook previsit(p, d, path) # ”pre visit” p
27 results = [ ]
28 path.append(0) # add new index to end of path before recursion
29 for c in self. tree.children(p):
30 results.append(self. tour(c, d+1, path)) # recur on child s subtree
31 path[−1] += 1 # increment index
32 path.pop( ) # remove extraneous index from end of path
33 answer = self. hook postvisit(p, d, path, results) # ”post visit” p
34 return answer
35
36 def hook previsit(self, p, d, path): # can be overridden
37 pass
38
39 def hook postvisit(self, p, d, path, results): # can be overridden
40 pass
Code Fragment 8.28: An EulerTour base class providing a framework for perform￾ing Euler tour traversals of a tree.



A labeled version of an indented, preorder presentation, akin to Code Frag￾ment 8.24, could be generated by the new subclass of EulerTour shown in Code
Fragment 8.30.
1 class PreorderPrintIndentedLabeledTour(EulerTour):
2 def hook previsit(self, p, d, path):
3 label = . .join(str(j+1) for j in path) # labels are one-indexed
4 print(2 d + label, p.element( ))
Code Fragment 8.30: A subclass of EulerTour that produces a labeled and indented,
preorder list of a tree’s elements.
To produce the parenthetic string representation, originally achieved with Code
Fragment 8.25, we define a subclass that overrides both the previsit and postvisit
hooks. Our new implementation is given in Code Fragment 8.31.
1 class ParenthesizeTour(EulerTour):
2 def hook previsit(self, p, d, path):
3 if path and path[−1] > 0: # p follows a sibling
4 print( , , end= ) # so preface with comma
5 print(p.element( ), end= ) # then print element
6 if not self.tree( ).is leaf(p): # if p has children
7 print( ( , end= ) # print opening parenthesis
8
9 def hook postvisit(self, p, d, path, results):
10 if not self.tree( ).is leaf(p): # if p has children
11 print( ) , end= ) # print closing parenthesis
Code Fragment 8.31: A subclass of EulerTour that prints a parenthetic string repre￾sentation of a tree.
Notice that in this implementation, we need to invoke a method on the tree instance
that is being traversed from within the hooks. The public tree( ) method of the
EulerTour class serves as an accessor for that tree.

-------------------

The Euler Tour Traversal of a Binary Tree
In Section 8.4.6, we introduced the concept of an Euler tour traversal of a general
graph, using the template method pattern in designing the EulerTour class. That
class provided methods hook previsit and hook postvisit that could be overrid￾den to customize a tour. In Code Fragment 8.33 we provide a BinaryEulerTour
specialization that includes an additional hook invisit that is called once for each
position—after its left subtree is traversed, but before its right subtree is traversed.

Our implementation of BinaryEulerTour replaces the original tour utility to
specialize to the case in which a node has at most two children. If a node has only
one child, a tour differentiates between whether that is a left child or a right child,
with the “in visit” taking place after the visit of a sole left child, but before the visit
of a sole right child

class BinaryEulerTour(EulerTour):
2 ”””Abstract base class for performing Euler tour of a binary tree.
3
4 This version includes an additional hook invisit that is called after the tour
5 of the left subtree (if any), yet before the tour of the right subtree (if any).
6
7 Note: Right child is always assigned index 1 in path, even if no left sibling.
8 ”””
9 def tour(self, p, d, path):
10 results = [None, None] # will update with results of recursions
11 self. hook previsit(p, d, path) # ”pre visit” for p
12 if self. tree.left(p) is not None: # consider left child
13 path.append(0)
14 results[0] = self. tour(self. tree.left(p), d+1, path)
15 path.pop( )
16 self. hook invisit(p, d, path) # ”in visit” for p
17 if self. tree.right(p) is not None: # consider right child
18 path.append(1)
19 results[1] = self. tour(self. tree.right(p), d+1, path)
20 path.pop( )
21 answer = self. hook postvisit(p, d, path, results) # ”post visit” p
22 return answer
23
24 def hook invisit(self, p, d, path): pass # can be overridden



Case Study: An Expression Tree

Our ExpressionTree class is de-
fined as a subclass of LinkedBinaryTree, and we rely on the nonpublic mutators to
construct such trees. Each internal node must store a string that defines a binary op￾erator (e.g., + ), and each leaf must store a numeric value (or a string representing
a numeric value).
Our eventual goal is to build arbitrarily complex expression trees for compound
arithmetic expressions such as (((3+ 1)× 4)/((9− 5) + 2)). However, it suffices
for the ExpressionTree class to support two basic forms of initialization:

 In the context of an ExpressionTree
class, we support a special str method (see Section 2.3.2) that returns the
appropriate string. Because it is more efficient to first build a sequence of individ￾ual strings to be joined together (see discussion of “Composing Strings” in Sec￾tion 5.4.2), the implementation of str relies on a nonpublic, recursive method
named parenthesize recur that appends a series of strings to a list


class ExpressionTree(LinkedBinaryTree):
2 ”””An arithmetic expression tree.”””
3
4 def init (self, token, left=None, right=None):
5 ”””Create an expression tree.
6
7 In a single parameter form, token should be a leaf value (e.g., 42 ),
8 and the expression tree will have that value at an isolated node.
9
10 In a three-parameter version, token should be an operator,
11 and left and right should be existing ExpressionTree instances
12 that become the operands for the binary operator.
13 ”””
14 super( ). init ( ) # LinkedBinaryTree initialization
15 if not isinstance(token, str):
16 raise TypeError( Token must be a string )
17 self. add root(token) # use inherited, nonpublic method
18 if left is not None: # presumably three-parameter form
19 if token not in +-*x/ :
20 raise ValueError( token must be valid operator )
21 self. attach(self.root( ), left, right) # use inherited, nonpublic method
22
23 def str (self):
24 ”””Return string representation of the expression.”””
25 pieces = [ ] # sequence of piecewise strings to compose
26 self. parenthesize recur(self.root( ), pieces)
27 return .join(pieces)
28
29 def parenthesize recur(self, p, result):
30 ”””Append piecewise representation of p s subtree to resulting list.”””
31 if self.is leaf(p):
32 result.append(str(p.element( ))) # leaf value as a string
33 else:
34 result.append( ( ) # opening parenthesis
35 self. parenthesize recur(self.left(p), result) # left subtree
36 result.append(p.element( )) # operator
37 self. parenthesize recur(self.right(p), result) # right subtree
38 result.append( ) ) # closing parenthesis
Code Fragment 8.35: The beginning of an ExpressionTree class



Expression Tree Evaluation
The numeric evaluation of an expression tree can be accomplished with a simple
application of a postorder traversal. If we know the values represented by the two
subtrees of an internal position, we can calculate the result of the computation that
position designates. Pseudo-code for the recursive evaluation of the value repre￾sented by a subtree rooted at position p is given in Code Fragment 8.36.
Algorithm evaluate recur(p):
if p is a leaf then
return the value stored at p
else
let ◦ be the operator stored at p
x = evaluate recur(left(p))
y = evaluate recur(right(p))
return x ◦ y
Code Fragment 8.36: Algorithm evaluate recur for evaluating the expression rep￾resented by a subtree of an arithmetic expression tree rooted at position p.
To implement this algorithm in the context of a Python ExpressionTree class,
we provide a public evaluate method that is invoked on instance T as T.evaluate( ).
Code Fragment 8.37 provides such an implementation, relying on a nonpublic
evaluate recur method that computes the value of a designated subtree.
39 def evaluate(self):
40 ”””Return the numeric result of the expression.”””
41 return self. evaluate recur(self.root( ))
42
43 def evaluate recur(self, p):
44 ”””Return the numeric result of subtree rooted at p.”””
45 if self.is leaf(p):
46 return float(p.element( )) # we assume element is numeric
47 else:
48 op = p.element( )
49 left val = self. evaluate recur(self.left(p))
50 right val = self. evaluate recur(self.right(p))
51 if op == + : return left val + right val
52 elif op == - : return left val − right val
53 elif op == / : return left val / right val
54 else: return left val right val # treat x or as multiplication
Code Fragment 8.37: Support for evaluating an ExpressionTree instance


Building an Expression Tree
The constructor for the ExpressionTree class, from Code Fragment 8.35, provides
basic functionality for combining existing trees to build larger expression trees.
However, the question still remains how to construct a tree that represents an ex￾pression for a given string, such as (((3+1)x4)/((9-5)+2)) .
To automate this process, we rely on a bottom-up construction algorithm, as￾suming that a string can first be tokenized so that multidigit numbers are treated
atomically (see Exercise R-8.30), and that the expression is fully parenthesized.
The algorithm uses a stack S while scanning tokens of the input expression E to
find values, operators, and right parentheses. (Left parentheses are ignored.)
• When we see an operator ◦, we push that string on the stack.
• When we see a literal value v, we create a single-node expression tree T
storing v, and push T on the stack.
• When we see a right parenthesis, ) , we pop the top three items from the
stack S, which represent a subexpression (E1 ◦ E2). We then construct a
tree T using trees for E1 and E2 as subtrees of the root storing ◦, and push
the resulting tree T back on the stack.
We repeat this until the expression E has been processed, at which time the top
element on the stack is the expression tree for E. The total running time is O(n).
An implementation of this algorithm is given in Code Fragment 8.38 in the form
of a stand-alone function named build expression tree, which produces and returns
an appropriate ExpressionTree instance, assuming the input has been tokenized.


1 def build expression tree(tokens):
2 ”””Returns an ExpressionTree based upon by a tokenized expression.”””
3 S=[] # we use Python list as stack
4 for t in tokens:
5 if t in +-x*/ : # t is an operator symbol
6 S.append(t) # push the operator symbol
7 elif t not in () : # consider t to be a literal
8 S.append(ExpressionTree(t)) # push trivial tree storing value
9 elif t == ) : # compose a new tree from three constituent parts
10 right = S.pop( ) # right subtree as per LIFO
11 op = S.pop( ) # operator symbol
12 left = S.pop( ) # left subtree
13 S.append(ExpressionTree(op, left, right)) # repush tree
14 # we ignore a left parenthesis
15 return S.pop( )
Code Fragment 8.38: Implementation of a build expression tree that produces an
ExpressionTree from a sequence of tokens representing an arithmetic expression.



























































"""
















"""
Tree  for they allow us to implement a host of algorithms much faster than when
using linear data structures, such as array-based lists or linked lists. Trees also
provide a natural organization for data, and consequently have become ubiquitous
structures in file systems, graphical user interfaces, databases, Web-sites, and
other computer systems

The relationships in a tree are hierarchical, with some objects being “above” and
some “below” others. Actually, the main terminology for tree data structures comes
from family trees, with the terms “parent,” “child,“ancestor,” and “descendant” being
the most common words used to describe rela￾tionships. With the excep￾tion of the top
element, each element in a tree has a parent element and zero or more children elements

top element the root of the tree,

Formal Tree Definition
Formally, we define a tree T as a set of nodes storing elements such that the nodes
have a parent-child relationship that satisfies the following properties:
• If T is nonempty, it has a special node, called the root of T, that has no parent.
• Each node v of T different from the root has a unique parent node w; every
node with parent w is a child of w

-Note that according to our definition, a tree can be empty, meaning that it does not
have any nodes This convention also allows us to define a tree recursively such
that a tree T is either empty or consists of a node r, called the root of T, and a
(possibly empty) set of subtrees whose roots are the children of r.

-Other Node Relationships
Two nodes that are children of the same parent are siblings. A node v is external if v has
 no children.A node v is internal if it has one or more children. External nodes are also
known as leaves

We see that the internal nodes of the tree are associ￾ated with directories and the leaves
are associated with regular files. In the UNIX and Linux operating systems, the root of
the tree is appropriately called the “root directory,” and is represented by the symbol “/".
                                                                        rt
c is an ancestor of papers/, and p is a descendant of cs016/        c      cs016/
                                                                    a        b
                                                                papers/      p
An edge of tree T is a pair of nodes (u,v) such that u is the parent of v, or vice-versa.
A path of T is a sequence of nodes such that any two consecutive nodes in the sequence
form an edge
                                Tree
            BinaryTree                         LinkedTree

ArrayBinaryTree   LinkedBinaryTree


Ordered Trees
A tree is ordered if there is a meaningful linear order among the children of each
node; that is, we purposefully identify the children of a node as being the first,
second, third, and so on. Such an order is usually visualized by arranging siblings
left to right, according to their order
The components of a structured document, such as a book, are hier￾archically organized
as a tree whose internal nodes are parts, chapters, and sections,and whose leaves are
paragraphs, tables, figures, The root of the tree corresponds to the book itsel

The Tree Abstract Data Type- we define a tree ADT using the concept of a 'position' as an
abstraction for a node of a tree. An element is stored at each position, and positions
satisfy parent-child relationships that define the tree structure

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
 a public interface for an abstract data type is often managed in Python via
duck typing. For example, we defined the notion of the public interface for a queue
ADT in Section 6.2, and have since presented several classes that implement the
queue interface (e.g., ArrayQueue , LinkedQueue ,CircularQueue
A more formal mechanism to designate the relationships between different implementations
of the same abstraction is through the definition of one class that serves as an abstract
base class, via inheritance, for one or more concrete classes.

Although the Tree class is an abstract base class, it includes several concrete
methods with implementations that rely on calls to the abstract methods of the class.
In defining the tree ADT in the previous section, we declare ten accessor methods.
Five of those are the ones we left as abstract, in Code Fragment 8.1. The other five
can be implemented based on the former.
"""
"""
Abstract Base Classes (ABCs) in object-oriented programming can indeed contain concrete methods 
alongside abstract methods.
Concrete methods in an ABC are:
Fully implemented: Unlike abstract methods, which only declare a signature and require implementation in subclasses, 
concrete methods within an ABC have a complete implementation within the abstract class itself.
Inheritable: Subclasses that extend or implement the ABC automatically inherit these concrete methods. 
They can use them directly without needing to redefine them.
Overridable (with conditions): Subclasses can choose to override concrete methods inherited from an ABC to provide 
a specialized implementation, as long as the concrete method is not marked as final (or equivalent in the 
specific language).

Provide default behavior: Concrete methods in an ABC are often used to provide common or default functionality that 
many subclasses can utilize. This reduces code duplication and promotes reusability.

Why include concrete methods in an ABC?
Shared functionality: When multiple subclasses will share a common behavior, defining it as a concrete method in 
the ABC centralizes the logic and avoids redundant implementations.

Default implementations: Concrete methods can provide a sensible default implementation that subclasses can either 
accept or override if they need different behavior.

Template Method Pattern: Concrete methods in an ABC can be used in conjunction with abstract methods to implement the 
Template Method design pattern, where the ABC defines the overall algorithm (template) with some steps being concrete
and others left to subclasses to implement.

"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):  # Concrete method
        print("Moving...")

    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
dog.move()  # Uses concrete method from Animal
print(dog.make_sound())

cat = Cat()
cat.move()  # Uses concrete method from Animal
print(cat.make_sound())
# In this example, Animal is an ABC with a concrete method move() and an abstract method make_sound(). Both Dog and Cat inherit the move() method and provide their specific implementation for make_sound().

"""
we will explore general algorithms for traversing a tree that can be used to provide
concrete implementations of the positions and iter methods within the Tree class. The
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



    def depth(self, p):  # Return the number of levels separating Position p from the root.”””
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))


    def height1(self): # works, but O(nˆ2) worst-case time .Return the height of the tree.”””
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))


"""
We can compute the height of a tree more efficiently, in O(n) worst-case time,
by relying instead on the original recursive definition. To do this, we will param￾eterize a function based on a 
position within the tree, and calculate the height of the subtree rooted at that position. Algorithm height2, 
shown as nonpublic method height2 in Code Fragment 8.5, computes the height of tree T in this way.
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

Although we do not yet have a concrete implementation of children(p), we assume that such an iteration 
is generated in O(cp +1) time, where cp denotes the number of children of p. Algorithm height2 spends 
O(cp +1) time at each position p to compute the maximum, and its overall running time is O(∑p(cp + 1)) = O(n+ ∑p cp).
"""
def height(self, p=None): # Return the height of the subtree rooted at Position p.
    #If p is None, return the height of the entire tree.
    if p is None:
        p = self.root( )
    return self._height2(p) # start height2 recursion
"""
                Binary Trees
A binary tree is an ordered tree with the following properties:
1. Every node has at most two children.
2. Each child node is labeled as being either a left child or a right child.
3. A left child precedes a right child in the order of children of a node.

The subtree rooted at a left or right child of an internal node v is called a left subtree
or right subtree, respectively, of v. A binary tree is proper if each node has either
zero or two children. Some people also refer to such trees as being full binary
trees

 An important class of binary trees arises in contexts where we wish
to represent a number of different outcomes that can result from answering a series
of yes-or-no questions.
Each internal node is associated with a question. Starting at
the root, we go to the left or right child of the current node, depending on whether
the answer to the question is “Yes” or “No.” With each decision, we follow an
edge from a parent to a child, eventually tracing a path in the tree from the root
to a leaf.
Such binary trees are known as decision trees, because a leaf position p
in such a tree represents a decision of what to do if the questions associated with
p’s ancestors are answered in a way that leads to p. A decision tree is a proper
binary tree


An arithmetic expression can be represented by a binary tree whose leaves are associated 
with variables or constants, and whose internal nodes are associated with one of the operators 
+, −, ×, and /. (See Figure 8.8.) Each node in such a tree has a value associated with it.
• If a node is leaf, then its value is that of its variable or constant.
• If a node is internal, then its value is defined by applying its operation to the
values of its children.

                              -
                /                           +
        *             +             *             6
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

The new sibling method is derived from the combination of left, right, and parent. Typ￾ically, 
we identify the sibling of a position p as the “other” child of p’s parent.However, if p 
is the root, it has no parent, and thus no sibling. Also, p may be the only child of its 
parent, and thus does not have a sibling.

method; this method is abstract in the Tree class. Although we have still not speci-
fied how the children of a node will be stored, we derive a generator for the ordered
children based upon the implied behavior of abstract methods left and right.

In a binary tree - level 0 has at most one node (the root), level 1 has at most two 
nodes (the children of the root), level 2 has at most four nodes, and so on. In general, 
level d has at most 2d nodes grows exponentially as we go down the tree.

Let T be a nonempty binary tree, and let n, nE, nI and h denote the number of nodes, 
number of external nodes, number of internal nodes, and height of T, respectively. 
Then T has the following properties:
1. h+1 ≤ n ≤ 2^(h+1) −1
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
    def sibling(self, p):  # Return a Position representing p's sibling (or None if no sibling).”””
        parent = self.parent(p)
        if parent is None: # p must be the root
            return None # root has no sibling
        else:
            if p == self.left(parent): # if position is at left
                return self.right(parent) # sibling is the right of parent
            else:
                return self.left(parent) # p is right so sibling is left
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
nE = nI +1.

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

We have not yet defined key imple￾mentation details for how a tree will be represented 
internally, and how we can effectively navigate between parents and children. Specifically,
a concrete imple￾mentation of a tree must provide methods root, parent, num children, 
children, len , and in the case of BinaryTree, the additional accessors left and right

 Linked Structure for Binary Trees
A natural way to realize a binary tree T is to use a linked structure, with a node
(see Figure 8.11a) that maintains references to the element stored at a position p
and to the nodes associated with the children and parent of p. If p is the root of
T, then the parent field of p is None. Likewise, if p does not have a left child
(respectively, right child), the associated field is None. The tree itself maintains an
instance variable storing a reference to the root node (if any), and a variable, called
size, that represents the overall number of nodes of T

                                    parent
                l-child ref          ref to ele at p           r-child ref      

                   parent                                          parent
                                                l-child ref   ref to ele at p  r-child ref 
l-child ref   ref to ele at p  r-child ref 

Python Implementation of a Linked Binary Tree Structure
We define a simple, nonpublic Node class to represent a node, and a public Position class that wraps a node. 
We provide a validate utility for robustly checking the validity of a given position instance when 
unwrapping it, and a make position utility for wrapping a node as a position to return to a caller.
-------------------
In Python, __ne__ is a special method, also known as a "dunder" or "magic" method, that implements the "not
 equal to" (!=) operator for objects. When you use object1 != object2, Python internally calls object1.__ne__(object2).
Key aspects of __ne__:
Operator Overloading: It allows you to define how the != operator behaves for instances of your custom classes.
Comparison Logic: The method should return True if the two objects are considered not equal and False otherwise.
Signature: It typically takes two arguments: self (the instance on which the method is called) and other (the object 
being compared to).
Default Behavior: If __ne__ is not explicitly defined in a class, Python's default implementation will typically 
delegate to __eq__ (the equality method) and return the negation of its result. This means if object1 == object2 
is True, then object1 != object2 will be False by default, and vice versa.
Consistency with __eq__: It is generally recommended to ensure that __ne__ and __eq__ are consistent, 
meaning a != b should be the logical negation of a == b.

"""
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
"""

with a constructor and with concrete implementations for the methods that remain abstract in the Tree and
BinaryTree classes. The constructor creates an empty tree by initializing root to
None and size to zero. These accessor methods are implemented with careful use
of the validate and make position utilities to safeguard against boundary case

Operations for Updating a Linked Binary Tree 

We chose not to declare update methods as part of the Tree or BinaryTree ab￾stract base classes for 
several reasons.For linked binary trees, update methods to support for gen￾eral usage are 

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

T.attach(p, T1, T2): Attach the internal structure of trees T1 and T2, respec￾tively, as the left and right 
subtrees of leaf position p of T, and reset T1 and T2 to empty trees; an error condition
occurs if p is not a leaf.

We have specifically chosen this collection of operations because each can be
implemented in O(1) worst-case time with our linked representation.
The most complex of these are delete and attach, due to the case analyses involving the
various parent-child relationships and boundary conditions, yet there remains only
a constant number of operations to perform-  if we used a tree representation with a sentinel node,
akin to our treatment of positional lists

To avoid the problem of undesirable update methods being inherited by sub￾classes of LinkedBinaryTree,
we have chosen an implementation in which none of the above methods are publicly supported. Instead, 
we provide nonpublic ver￾sions of each, for example, providing the underscored delete in lieu of a 
public delete

------------------------
The __slots__ attribute in Python classes is used to explicitly declare the data members (attributes) 
that an instance of the class will possess. This declaration has several significant implications: 

Memory Optimization: By default, Python instances store their attributes in a dictionary (__dict__). 
This dictionary provides flexibility, allowing new attributes to be added dynamically at runtime. 
However, a dictionary for each instance can consume significant memory, especially when dealing with 
a large number of instances. When __slots__ is defined, Python instead allocates a fixed amount of 
space for the specified attributes, often in a more compact structure like a hidden array of 
references, thereby reducing memory consumption per instance.

Attribute Access Speed: Storing attributes in a fixed-size structure can also lead to faster attribute 
lookup times compared to dictionary lookups.
Preventing Dynamic Attribute Creation: When __slots__ is defined, instances of that class cannot have 
new attributes added to them at runtime unless those attributes are explicitly listed in __slots__. 
Attempting to add an unlisted attribute will result in an AttributeError. This can be beneficial for 
enforcing a fixed structure and preventing typos or unintended attribute creation.

How to use __slots__:
To use __slots__, define a class attribute named __slots__ and assign it an iterable (e.g., a tuple or list) 
containing the names of the allowed instance attributes as strings.
Python
"""

class MyClass:
    __slots__ = ('attribute1', 'attribute2', 'attribute3')

    def __init__(self, val1, val2, val3):
        self.attribute1 = val1
        self.attribute2 = val2
        self.attribute3 = val3

# Example usage
obj = MyClass(10, 20, 30)
print(obj.attribute1)  # Output: 10

class SEcclass:
    __slots__ =("a","n","j","l")

    def __init__(self,val1,va2,va3,va4):
        self.a = val1
        self.n = va2
        self.j = va3
        self.l = va4

obj2 = SEcclass(1,2,3,4)
print(obj2.a)
"""
# Attempting to add a new attribute not in __slots__ will raise an AttributeError
# obj.new_attribute = 40 
Important Considerations:
Inheritance: If a class with __slots__ inherits from another class, all classes in the inheritance hierarchy 
must also define __slots__ (or inherit from object in Python 3, which handles __slots__ implicitly for its base 
classes) to fully benefit from the memory and speed optimizations. If a parent class does not define __slots__ 
and therefore has a __dict__, then the child class instances will still have a __dict__, negating some of the 
benefits.
No __dict__ or __weakref__: Instances of classes using __slots__ will typically not have a __dict__ attribute 
or a __weakref__ attribute (unless explicitly included in __slots__). This means they cannot be directly used 
with functions or mechanisms that rely on these attributes, such as weakref.ref.
Flexibility Trade-off: While __slots__ offers performance benefits, it reduces the dynamic flexibility of adding 
attributes to instances at runtime. This trade-off should be considered based on the specific needs of the 
application.

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
    def parent(self, p): #Return the Position of p's parent (or None if p is root).”””
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p): # Return the Position of p's left child (or None if no left child).”””
        node = self._validate(p)
        return self._make_position(node._left)
    def right(self, p): # Return the Position of p's right child (or None if no right child).”””
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
        node._parent = node #  node is empty or null by default -convention for deprecated node
        return node._element
    def delete1(self,p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size += 1
        node._parent = node # node is empty or null -convention for deprecated node
        return node._element

    def attach1(self,p,lefttr,righttr):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(lefttr) is type(righttr):
            raise TypeError('All tree must be of same type')
        self._size = len(lefttr) + len(righttr)
        if not lefttr.is_empty():
            lefttr._root._parent = node  # parrent and root also of ths subtree
            node._left = lefttr._root
            lefttr._root = None  # set lefttr instance is empty
            lefttr,_size = 0
        if not righttr.is_empty():
            righttr._root._parent = node  # parrent and root also of ths subtree
            node._right = righttr._root
            righttr._root = None  # set lefttr instance is empty
            righttr,_size = 0


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


    def heightn(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.heightn(c) for c in self.children(p))
    def heit(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def deth(self,p):
        if self.is_root(p):
            return 0
        else:
            return  1 + self.deth(self.parent(p))  # moving up
"""
The len method, implemented in LinkedBinaryTree, uses an instance variable(self.size)
storing the number of nodes of T and takes O(1) time root, left, right, parent, and num 
children are imple￾mented directly in LinkedBinaryTree and take O(1) time and all other
methods also
The depth method at position p runs in O(dp +1) time where dp is its depth; the height
method on the root of the tree runs in O(n) time
The various update methods add root, add left, add right, replace, delete, and attach 
(that is, their nonpublic implementations) each run in O(1) time,as they involve relinking
 only a constant number of nodes per operation.
-----------
    Array-Based Representation of a Binary Tree
An alternative representation of a binary tree T is based on a way of 'numbering' the
positions of T. For every position p of T, let f(p) be the integer defined as follows.
• If p is the root of T, then f(p) = 0.
• If p is the left child of position q, then f(p) = 2 f(q) +1.
• If p is the right child of position q, then f(p) = 2 f(q) +2.


from left to right. (See Figure 8.12.) Note well that the level numbering is based on 'potential 
positions' within the tree, not actual positions of a given tree,so they are not necessarily consecutive

One advantage of an array-based representation of a binary tree is that a posi￾tion p can be represented
by the single integer f(p), and that position-based meth￾ods such as root, parent, left, and right can 
be implemented using simple arithmetic operations on the number f(p).Based on our formula for the level 
numbering, the left child of p has index 2 f(p) + 1, the right child of p has index 2 f(p) + 2, and
the parent of p has index (f(p)− 1)/2

deleting a node and promoting its child takes O(n) time because it is not just the child that moves 
locations  within the array, but all descendants of that child.

When representing a binary tree with a linked structure, each node explicitly maintains fields left 
and right as references to individual children. For a general tree,there is no a priori limit on the 
number of children that a node may have. A natural way to realize a general tree T as a linked structure 
is to have each node store a single container of references to its children. For example,a children 
field of anode can be a Python list of references to the children of the node

by using a collection to store the children of each position p, we can implement
children(p) by simply iterating that collection.
Operation                               Running Time
len, is empty                           O(1)
root, parent, is root, is leaf          O(1)
children(p)                             O(cp +1)
depth(p)                                O(dp +1)
height                                  O(n)
Running times of the accessor methods of an n-node general tree im￾plemented with a  linked 
structure.We let cp denote the number of children of a position p. The space usage is O(n)

        Tree Traversal Algorithms
    Preorder and Postorder Traversals of General Trees
In a preorder traversal of a tree T, the root of T is visited first and then the sub￾trees rooted
at its children are traversed recursively. If the tree is ordered, then the subtrees are traversed 
according to the order of the children
"""
def preorder(T, p): #  perform the “visit” action for position p
    for  c in T.children(p):
       preorder(T, c)                      # {recursively traverse the subtree rooted at c}
"""
        Postorder Traversal
it recursively traverses the subtrees rooted at the children of the root first, and then visits the 
root (hence, the name “postorder”)
"""
def postorder(T, p):
    for  c in T.children(p):
       postorder(T, c)
"""
    BFS
we visit all the positions at depth d before we visit the positions at depth d + 1. Such an
algorithm is known as a breadth-first traversal.

A breadth-first traversal is a common approach used in software for playing games. A 'game tree'
represents the possible choices of moves that might be made by a player (or computer) during a 
game, with the root of the tree being the initial configuration for the game. For example,
Tic-Tac-Toe.
A breadth-first traversal of such a game tree is often performed because a computer may be unable 
to explore a complete game tree in a limited amount of time. So the computer will consider all 
moves, then responses to those moves, going as deep as computational time allows

The process is not recursive, since we are not traversing entire subtrees at once. We use a queue 
to produce a FIFO (i.e., first-in first-out) semantics for the order in which we visit nodes. The 
overall running time is O(n), due to the n calls to enqueue and n calls to dequeue

"""
def breadthfirst(T): # Initialize queue Q to contain T.root( )
    Q = T.root()
    while Q:
        p = Q.dequeue( )  # {p is the oldest entry in the queue}
        for  c in T.children(p):   #perform the “visit” action for position p
            Q.enqueue(c)    # {add p’s children to the end of the queue for later visits}
"""
The standard preorder, postorder, and breadth-first traversals that were introduced for 
general trees, can be directly applied to binary trees
    Inorder Traversal of a Binary Tree

During an inorder traversal, we visit a position between the recursive traver￾sals of its left and right 
subtrees. The inorder traversal of a binary tree T can beinformally viewed as visiting the nodes of T “from 
left to right.” Indeed, for everyposition p, the inorder traversal visits p after all the positions in the 
left subtree of p and before all the positions in the right subtree of p starts from botom extreme left 

def inorder(p):
   if p has a left child lc then
       inorder(lc)             {recursively traverse the left subtree of p}
   perform the “visit” action for position p
   if p has a right child rc then
       inorder(rc)            {recursively traverse the right subtree of p}
       
                            12

              6                              18
         /          \                    /       \
       4              10               14           19
    2        5         8      11      13      16
 /   \               /  \                   /   \
1       3           7     9                 15   17
Algorithm inorder(p):
if p has a left child lc then inorder(lc) {recursively traverse the left subtree of p} perform the “visit” 
action for position p if p has a right child rc then inorder(rc) {recursively traverse the right subtree of p}

the inorder traversal visits positions in a consistent order with the standard representation of
the expression, as in 3+1×3/9−5+2... (albeit without parentheses).

            Binary Search Trees
An important application of the inorder traversal algorithm arises when we store an
ordered sequence(sorted) of elements in a binary tree, defining a structure we call a binary
search tree. Let S be a set whose unique elements have an order relation. For
example, S could be a set of integers. A binary search tree for S is a binary tree T
such that, for each position p of T:
• Position p stores an element of S, denoted as e(p).
• Elements stored in the left subtree of p (if any) are less than e(p).
• Elements stored in the right subtree of p (if any) are greater than e(p).
                            12

              6                              18
        /            \                    /       \
      4               10               14           19
  2        5         8      11      13      16
2    4    5   6    8  10  11  12  13  14  16  18  19

by traversing a path down the tree T, starting at the root. At each internal position p 
encountered, we compare our search value v with the element e(p) stored at p. If v < e(p), 
then the search continues in the left subtree of p.If v = e(p), then the search terminates 
successfully. If v > e(p), then the search continues in the right subtree of p. Finally, if
we reach an empty subtree, the search terminates unsuccessfully.running time - height of T

height of a binary tree with n nodes can be as small as log(n+1)−1 or as large as n−1

Implementing Tree Traversals in Python
 tree T should include support for the following methods:
 
T.positions( ): Generate an iteration of all positions of tree T.
iter(T): Generate an iteration of all elements stored within tree T. 

the order in which these iterations report their results. - tree traversal algorithms we have
introduced could be used to produce these iterations. it is easy to produce an iteration of all 
elements of a tree, if we rely on a presumed iteration of all positions. Therefore, support for 
the iter(T) syntax can be formally provided by a concrete implementation of the special method 
iter within the abstract base class Tree. We rely on Python’s generator syntax as the mechanism 
for producing iterations. 
"""
def __iter__(self): #Generate an iteration of the tree s elements
    for p in self.positions( ):  # use same order as positions()
        yield p.element( ) # but yield each element
"""
 # Preorder Traversal

"""
def preorder1(self): # Generate a preorder iteration of positions in the tree.”””
    if not self.is_empty( ):
        for p in self._subtree_preorder(self.root( )): # start recursion
            yield p
def subtree_preorder(self, p):  # Generate a preorder iteration of positions in subtree rooted at p.”””
    yield p # visit p before its subtrees
    for c in self.children(p): # for each child c
        for other in self._subtree_preorder(c): # do preorder of c’s subtree ,if c has subtree
            yield other # yielding each to our caller
"""
A user of the class can therefore write code such as - for p in T.preorder( ):
Rather than loop over the results returned by the preorder call,we return the entire iteration
as an object.
"""
def positions(self): # Generate an iteration of the tree s positions.
    return self.preorder( ) # return entire preorder iteration
"""
Postorder Traversal
t within the recursive utility for a postorder we wait to yield position p until 
after we have recursively yield the positions in its subtrees. 
"""
def postorder1(self): # Generate a postorder iteration of positions in the tree.”””
    if not self.is_empty( ):
        for p in self._subtree_postorder(self.root( )): # start recursion
            yield p
def _subtree_postorder(self, p): # Generate a postorder iteration of positions in subtree rooted at p.”””
    for c in self.children(p): # for each child c
        for other in self._subtree_postorder(c): # do postorder of c’s subtree
            yield other # yielding each to our caller
    yield p # visit p after its subtrees
"""
e breadth-first traversal algorithm is not recursive; it relies on a queue of positions to 
manage the traver￾sal process
                    Inorder Traversal for Binary Trees
The preorder, postorder, and breadth-first traversal algorithms are applicable to all trees,
Those methods are inherited by the abstract BinaryTree class, the concrete LinkedBinaryTree
 class,etc.
Inorder traversal algorithm, because it - explicitly relies on the notion of a left and right
child of a node, only applies to binary trees. We therefore include its definition within 
the body of the BinaryTree class. 

"""
def breadthfirst1(self): # Generate a breadth-first iteration of the positions of the tree.
    if not self.is_empty( ):
        fringe = LinkedQueue() # known positions not yet yielded
        fringe.enqueue(self.root( )) # starting with the root
        while not fringe.is_empty( ):
            p = fringe.dequeue( ) # remove from front of the queue
            yield p # report this position
            for c in self.children(p):
                fringe.enqueue(c) # add children to back of queue

def inorder(self): # Generate an inorder iteration of positions in the tree.”””
    if not self.is_empty( ):
        for p in self._subtree_inorder(self.root( )):
            yield p  # will give every point ie a root of a subtree
def _subtree_inorder(self, p): # Generate an inorder iteration of positions in subtree rooted at p.”””
    if self.left(p) is not None: # if left child exists, traverse its subtree
        for other in self._subtree_inorder(self.left(p)):
            yield other
    yield p # visit p between its subtrees
    if self.right(p) is not None: # if right child exists, traverse its subtree
        for other in self._subtree_inorder(self.right(p)):
            yield other
# override inherited version to make inorder the default
def positions(self): # Generate an iteration of the tree s positions.”””
    return self.inorder( ) # make inorder the default
""" 
Applications of Tree Traversals

Table of Contents
When using a tree to represent the hierarchical structure of a document, a preorder
traversal of the tree can naturally be used to produce a table of contents for the doc￾ument

The unindented version of the table of contents, given a tree T, can be produced
with the following code:
"""
def contents(T):
    for p in T.preorder( ):
        print(p.element( ))
"""

A preferred approach to producing an indented table of contents is to redesign a top-down 
recursion that includes the current depth as an additional parameter. This implementation 
runs in worst-case O(n) 

"""
def preorder_indent(T, p, d): #Print preorder representation of subtree of T rooted at p at depth d.”””
    print(2*d* ' ' + str(p.element( ))) # use depth for indentation
    for c in T.children(p):
        preorder_indent(T, c, d+1) # child depth is d+1
#  On a complete tree T, the recursion should be started with form preorder indent(T, T.root( ), 0).

#Tree Traversal Algorithms
def preorder_label(T, p, d, path): # Print labeled representation of subtree of T rooted at p at depth d.”””
    label = '.'.join(str(j+1) for j in path) # displayed labels are one-indexed
    print(2*d*' ' + label, p.element())
    path.append(0) # path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path) # child depth is d+1
        path[-1] += 1
    path.pop()
#Efficient recursion for printing an indented and labeled pre￾sentation of a preorder traversal

def parenthesize(T, p): #Print parenthesized representation of subtree of T rooted at p.”””
    print(p.element( ), end= '') # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' ('if first_time else ','  # determine proper separator
            print(sep, end='' )
            first_time = False              # any future passes will not be the first
            parenthesize(T, c)              # recur on child
        print(')' , end= '')                # include closing parenthesis

"""
Recursive computation of disk space  - is emblematic of a postorder traversal,as we cannot
effectively compute the total space used by a directory until after we know the space that
is used by its children directories. As it visits the position of a directory, there is no
easy way to discern which of the previous positions represent children of that directory,
nor how much recursive disk space was allocated.

We would like to have a mechanism for children to return information to the parent as part
of the traversal process. A custom solution to the disk space prob￾lem, with each level of 
recursion providing a return value to the (parent) caller,
"""
def disk_space(T, p): # Return total disk space for subtree of T rooted at p.”””
    subtotal = p.element( ).space( )   # space used at position p
    for c in T.children(p):
        subtotal += disk_space(T, c)   # add child’s space to subtotal
    return subtotal
#We assume that a space( ) method of each tree element reports the local space used at
# that position.
"""
Euler Tours and the Template Method Pattern 
recursive tree traversals.are not general enough to capture the range of computations 
we desire.

In some cases, we need more of a blending of the ap￾proaches, with initial work performed
before recurring on subtrees, additional work performed after those recursions, and in the
case of a binary tree, work performed between the two possible recursions. Furthermore, in
some contexts it was impor￾tant to know the depth of a position, or the complete path from
the root to that position, or to return information from one level of the recursion to 
another. 
The Euler tour traversal of a general tree T can be informally defined as a “walk” around T, 
where we start by going from the root toward its leftmost child, viewing the edges of T as
being “walls” that we always keep to our left. 

The complexity of the walk is O(n), because it progresses exactly two times along each of 
the n−1 edges of the tree—once going downward(left “pre visit”))along the edge, and later 
going upward(right “post visit”) along the edge. To unify the concept of preorder and 
postorder traversals, we can think of there being two notable “visits” to each position p:
"""
def eulertour1(T, p): # perform the “pre visit” action for position p
    for  c in T.children(p):
        eulertour1(T, c) # {recursively tour the subtree rooted at c}
    # perform the “post visit” action for position p
"""
The Template Method Pattern
To provide a framework that is reusable and adaptable, we rely on an interesting object-oriented
software design pattern, the template method pattern. The template method pattern describes 
a generic computation mechanism that can be specialized for a particular application by 
redefining certain steps. To allow customization, the primary algorithm calls auxiliary 
functions known as hooks at designated steps of the process.

In the context of an Euler tour traversal, we define two separate hooks, a pre￾visit hook 
that is called before the subtrees are traversed, and a postvisit hook that is called after
the completion of the subtree traversals. Our implementation will take the form of an EulerTour
class that manages the process, and defines trivial defi-nitions for the hooks 

Tree Traversal Algorithms
"""
class EulerTour: # Abstract base class for performing Euler tour of a tree.
    # hook previsit and hook postvisit may be overridden by subclasses.

    def __init__(self, tree): # Prepare an Euler tour template for given tree.
        self._tree = tree
    def tree(self): # Return reference to the tree being traversed.
        return self._tree

    def execute(self): # Perform the tour and return any result from post visit of root.”””
        if len(self._tree) > 0:
            return self._tour(self._tree.root( ), 0, [ ]) # start the recursion
    def tour(self, p, d, path): # Perform tour of subtree rooted at Position p.
        #path list of indices of children on path from root to p
        self._hook_previsit(p, d, path) # ”pre visit” p
        results = [ ]
        path.append(0) # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path)) # recur on child s subtree
            path[-1] += 1 # increment index
        path.pop( ) # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results) # ”post visit” p
        return answer
    def _hook_previsit(self, p, d, path): # can be overridden
        pass
    def _hook_postvisit(self, p, d, path, results): # can be overridden
        pass
# An EulerTour base class providing a framework for perform￾ing Euler tour traversals of a tree.
"""
method hook previsit(p, d, path)
This function is called once for each position, immediately before its subtrees(if any) 
are traversed. Parameter p is a position in the tree, d is the depth of that position, and 
path is a list of indices
method hook postvisit(p, d, path, results)
This function is called once for each position, immediately after its subtrees(if any) are 
traversed. The first three parameters use the same convention as did hook previsit. The final
parameter is a list of objects that were provided as return values from the post visits of 
the respective subtrees of p. Any value returned by this call will be available to the 
parent of p during its postvisi

A labeled version of an indented, preorder presentation

"""
class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.' .join(str(j+1) for j in path) # labels are one-indexed
        print(2*d*' ' + label, p.element( ))
"""
To produce the parenthetic string representation, we define a subclass that overrides 
both the previsit and postvisit hooks.(that prints a parenthetic string repre￾sentation 
of a tree)
"""
class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0: # p follows a sibling
            print( ', ' , end= '') # so preface with comma
        print(p.element( ), end='' ) # then print element
        if not self.tree( ).is_leaf(p): # if p has children
            print( '(' , end= '') # print opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree( ).is_leaf(p): # if p has children
            print( ')' , end='' ) # print closing parenthesis
"""
we need to invoke a method on the tree instance that is being traversed from within the 
hooks. The public tree( ) method of the EulerTour class serves as an accessor for that tree.
Finally the task of computing disk space, as originally implemented ,can be performed quite 
easily with the EulerTour subclass 
"""
class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results): # we simply add space associated with p to that of its subtrees
        return p.element( ).space( ) + sum(results)
"""
The Euler Tour Traversal of a Binary Tree
In Section 8.4.6, we introduced the concept of an Euler tour traversal of a general graph, using the 
template method pattern in designing the EulerTour class. That class provided methods hook previsit and hook
postvisit that could be overrid￾den to customize a tour. In Code Fragment 8.33 we provide a BinaryEulerTour 
specialization that includes an additional hook invisit that is called once for each position—after its left 
subtree is traversed, but before its right subtree is traversed.

Our implementation of BinaryEulerTour replaces the original tour utility to
specialize to the case in which a node has at most two children. If a node has only
one child, a tour differentiates between whether that is a left child or a right child,
with the “in visit” taking place after the visit of a sole left child, but before the visit
of a sole right child

#Abstract base class for performing Euler tour of a binary tree.
This version includes an additional hook invisit that is called after the tour
of the left subtree (if any), yet before the tour of the right subtree (if any).
 Note: Right child is always assigned index 1 in path, even if no left sibling.
"""
class BinaryEulerTour(EulerTour):
    """
    Abstract base class for performing Euler tour of a binary tree.
    This version includes an additional hook invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).
    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def _tour(self, p, d, path):
        results = [None, None] # will update with results of recursions
        self._hook_previsit(p, d, path) # ”pre visit” for p
        if self._tree.left(p) is not None: # consider left child
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop( )
        self._hook_invisit(p, d, path) # ”in visit” for p
        if self._tree.right(p) is not None: # consider right child
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop( )
        answer = self._hook_postvisit(p, d, path, results)   # ”post visit” p
        return answer

    def _hook_invisit(self, p, d, path):
        pass # can be overridden
"""
0                            12

1                  6                         18
             /         \                 /       \
2        4              10            14           19
3    2        5                   13      16
4          a     b     
    0   1  2  3  4  5   6    7    8   9   10   11  12
The geometry is determined by an algorithm that assigns x- and y-coordinates to each
position p of a binary tree T using the following two rules:
• x(p) is the number of positions visited before p in an inorder traversal of T.
• y(p) is the depth of p in T
convention common in computer graphics that x￾coordinates increase left to right and 
y-coordinates increase top to bottom.assigning (x,y) coordinates
"""
class BinaryLayout(BinaryEulerTour): # Class for computing (x,y) coordinates for each node of a binary tree.”””
    def __init__(self, tree):
        super( ).__init__(tree) # must call the parent constructor
        self._count = 0 # initialize count of processed nodes
    def _hook_invisit(self, p, d, path):
        p.element( ).setX(self._count) # x-coordinate serialized by count
        p.element( ).setY(d) # y-coordinate is depth
        self._count += 1

"""
Case Study: An Expression Tree
we define a new ExpressionTree class that provides support for constructing such trees, and 
for displaying and evaluating the arithmetic expression that such a tree represents.Our 
ExpressionTree class is de-fined as a subclass of LinkedBinaryTree, and we rely on the 
nonpublic mutators to construct such trees. Each internal node must store a string that 
defines a binary op￾erator (e.g., + ), and each leaf must store a numeric value (or a string
representinga numeric value).

two basic forms of initialization:
ExpressionTree(value): Create a tree storing the given value at the root.
ExpressionTree(op,E1,E2): Create a tree storing string op at the root (e.g., +),and with the 
structures of existing ExpressionTree instances E1 and E2 as the left and right subtrees of
the root, respectively.
We use add root to cre￾ate an initial root of the tree storing the token provided as the 
first parameter. Then we perform run-time checking of the parameters to determine whether
the caller invoked the one-parameter version of the constructor (in which case, we are done),
or the three-parameter form. In that case, we use the inherited attach method to
incorporate the structure of the existing trees as subtrees of the root

Composing a Parenthesized String Representation
"""
class ExpressionTree(LinkedBinaryTree): # An arithmetic expression tree
    def __init__(self, token, left=None, right=None): # Create an expression tree.
        """In a single parameter form, token should be a leaf value (e.g., 42 ),
        8 and the expression tree will have that value at an isolated node.
        In a three-parameter version, token should be an operator,
         and left and right should be existing ExpressionTree instances
         that become the operands for the binary operator."""

        super( ).__init__( ) # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError( 'Token must be a string' )
        self._add_root(token) # use inherited, nonpublic method
        if left is not None: # presumably three-parameter form
            if token not in '+-*x/' :
                raise ValueError( 'token must be valid operator' )
            self._attach(self.root( ), left, right) # use inherited, nonpublic method
    def __str__(self): # Return string representation of the expression.
        pieces = [ ] # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root( ), pieces)
        return  ''.join(pieces)

    def _parenthesize_recur(self, p, result): # Append piecewise representation of p s subtree to resulting list.”””
        if self.is_leaf(p):
            result.append(str(p.element( ))) # leaf value as a string
        else:
            result.append( '(' ) # opening parenthesis
            self._parenthesize_recur(self.left(p), result) # left subtree
            result.append(p.element( )) # operator
            self._parenthesize_recur(self.right(p), result) # right subtree
            result.append( ')' ) # closing parenthesis"""

        """
        Expression Tree Evaluation
        The numeric evaluation of an expression tree can be accomplished with a simple application of a postorder 
        traversal. If we know the values represented by the two subtrees of an internal position, we can calculate 
        the result of the computation that position designates. Pseudo-code for the recursive evaluation of the value 
        repre￾sented by a subtree rooted at position p is given in Code Fragment 8.36.
        """

        #   we provide a public evaluate method that is invoked on instance T as T.evaluate( ).
    def evaluate(self): # Return the numeric result of the expression.”””
        return self._evaluate_recur(self.root( ))
    def _evaluate_recur(self, p): # Return the numeric result of subtree rooted at p.”””
        if self.is_leaf(p):
            return float(p.element( )) # we assume element is numeric
        else:
            op = p.element( )
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op =='+' : return left_val + right_val
            elif op =='-' : return left_val - right_val
            elif op == '/' : return left_val / right_val
            else: return left_val * right_val # treat x or as multiplication
        #Support for evaluating an ExpressionTree instance
        """
        Building an Expression Tree
        The constructor for the ExpressionTree class, from Code Fragment 8.35, provides basic functionality for 
        combining existing trees to build larger expression trees.However, the question still remains how to 
        construct a tree that represents an ex￾pression for a given string, such as (((3+1)x4)/((9-5)+2)) .
        To automate this process, we rely on a bottom-up construction algorithm, as￾suming that a string can first be 
        tokenized so that multidigit numbers are treated atomically (see Exercise R-8.30), and that the expression is 
        fully parenthesized.The algorithm uses a stack S while scanning tokens of the input expression E to
        find values, operators, and right parentheses. (Left parentheses are ignored.)
        • When we see an operator ◦, we push that string on the stack.
        • When we see a literal value v, we create a single-node expression tree T storing v, and push T on the stack.
        • When we see a right parenthesis, ) , we pop the top three items from the stack S, which represent a 
        subexpression (E1 ◦ E2). We then construct a tree T using trees for E1 and E2 as subtrees of the root 
        storing ◦, and push the resulting tree T back on the stack.We repeat this until the expression E has been 
        processed, at which time the top element on the stack is the expression tree for E. The total running time is O(n).
        An implementation of this algorithm is given in Code Fragment 8.38 in the form of a stand-alone function named 
        build expression tree, which produces and returns an appropriate ExpressionTree instance, assuming the input has 
        been tokenized.
        """

    def build_expression_tree(tokens):  #Returns an ExpressionTree based upon by a tokenized expression.”””
        S=[] # we use Python list as stack
        for t in tokens:
            if t in ['+','-','x','*','/ ']: # t is an operator symbol
                S.append(t) # push the operator symbol
            elif t not in '()' : # consider t to be a literal
                S.append(ExpressionTree(t)) # push trivial tree storing value
            elif t == ')' : # compose a new tree from three constituent parts
                right = S.pop( ) # right subtree as per LIFO
                op = S.pop( ) # operator symbol
                left = S.pop( ) # left subtree
                S.append(ExpressionTree(op, left, right)) # repush tree
             # we ignore a left parenthesis
        return S.pop( )
        """Implementation of a build expression tree that produces an
            ExpressionTree from a sequence of tokens representing an arithmetic expression."""


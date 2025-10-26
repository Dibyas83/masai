
"""
The idea is to do Level order traversal of the partially built Binary Tree using queue and traverse
the linked list at the same time. At every step, we take the parent node from queue, make next two
nodes of linked list as children of the parent node, and push the next two nodes to queue.
"""
# Python program to create a Complete Binary tree
# from its Linked List Representation

from collections import deque


class Lnode:
    def __init__(self, value):
        self.data = value
        self.next = None


class Tnode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Converts a given linked list (10 12 15 25 30 36 ) representing a complete
# binary tree into the linked representation of a binary tree.
def convert(head):
    if not head:
        return None

    # Queue to store the parent nodes
    q = deque()

    # The first node is always the root node,
    # and add it to the queue
    root = Tnode(head.data) # 10
    q.append(root)  # [10]

    # Move the pointer to the next node
    head = head.next

    # Until the end of the linked list is reached,
    # do the following steps
    while head: # 12 - > 25  ->36

        # Take the parent node from the queue
        # and remove it from the queue
        parent = q.popleft()   # 10 ->  12  ->15

        leftChild = None
        rightChild = None

        # Create left child
        if head:
            leftChild = Tnode(head.data) # 12  -> 25  ->36(final)
            q.append(leftChild) # [12]   -> [15,25]  -> [25, 36]
            head = head.next # 15  -> 30  -> none

        # Create right child
        if head:
            rightChild = Tnode(head.data) # 15  -> 30
            q.append(rightChild) # [12,15]  -> [15,25, 30]
            head = head.next # 25  ->36

        # Assign the left and right children of the parent
        parent.left = leftChild
        parent.right = rightChild
        """
                        10
                12             15
            25     30
                            36
        """
    return root


# Level Order Traversal of the binary tree
def levelOrderTraversal(root):
    if not root:
        return

    # Queue to hold nodes at each level
    q = deque()
    q.append(root) # head.data [10]

    while q:
        currNode = q.popleft() # [10] 12

        # Print the current node's data
        print(currNode.data, end=" ")

        # Push the left and right children
        # of the current node to the queue
        if currNode.left:
            q.append(currNode.left) # [ 15] ..... [ 15,25]
        if currNode.right:
            q.append(currNode.right) # [12 15]....... [ 15,25,30]


if __name__ == "__main__":
    # Create linked list : 10->12->15->25->30->36
    head = Lnode(10)
    head.next = Lnode(12)
    head.next.next = Lnode(15)
    head.next.next.next = Lnode(25)
    head.next.next.next.next = Lnode(30)
    head.next.next.next.next.next = Lnode(36)

    root = convert(head)
    levelOrderTraversal(root)

















"""

Circular Linked List
• All nodes are connected to form a circle
• There is no NULL at the end: Last node points back to the first node

head - 10|1000 - 11|2000 - 12|3000 - 13|4800->
       |                                      |
        <------------------------------------

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):#Adds a new node at the end of the circular linked list.
        new_node = Node(data)
        if not self.head: # If the list is empty, initialize head.
            self.head = new_node
            new_node.next = new_node # Points to itself, making it circular
        else:
            current = self.head
            # Traverse until the last node that points back to head
            while current.next != self.head: # one complete round ,stops at end
                current = current.next
            # Link the last node to the new node
            current.next = new_node # added
            # The new node now points back to head
            new_node.next = self.head

    def traverse(self):#Prints the elements in the circular linked list once.
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")



"""
Doubly Linked List Representation
• prev: Location (pointer) to the previous node
• next: Location (pointer) to the next node
• key: Information

        prev key next
head  - NULL 55 715 <=> 600 56 220 <=> 715 57 910 <=> 220 58 NULL
600          600          715          220          910

Advantages

• Node will not only have the reference (pointer) to the next node but also to the
previous node
    • Given a node, we can navigate in both directions

• In doubly linked list, a node can be deleted even if we don’t have previous
node’s address
    • In singly linked list, a node cannot be removed unless we have pointer to the predecessor

• Disadvantages
• Each node requires an extra pointer, requiring more space
• The insertion or deletion of a node takes a bit longer time (more pointer
operations)


"""

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # Adds a new node at the end of the doubly linked list.
        new_node = DNode(data)
        if not self.head: # no self.head
            self.head = new_node
        else:
            current = self.head

            # Traverse to the last node
            while current.next: # not null or none
                current = current.next # reached none
            current.next = new_node
            new_node.prev = current

    def traverse_forward(self): # Prints elements from head to tail.

        current = self.head
        while current: # current.next is not none
            print(current.data, end=" <-> ")
            last = current # Keep track of the last node
            current = current.next
        print("None (end)")
    def traverse_backward(self): # Prints elements from tail to head.

        # First find the tail
        current = self.head
        while current and current.next:
            current = current.next
        # Now traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None (start)")


def main():
    # 1. Work with CircularLinkedList
    cll = CircularLinkedList()
    for value in [10, 20, 30, 40, 50]:
        cll.append(value)
    print("Circular Linked List Traversal:")
    cll.traverse()
    # 2. Work with DoublyLinkedList
    dll = DoublyLinkedList()
    for value in [10, 20, 30, 40, 50]:
        dll.append(value)
    print("\nDoubly Linked List Traversal (Forward):")
    dll.traverse_forward()
    print("Doubly Linked List Traversal (Backward):")
    dll.traverse_backward()
if __name__ == "__main__":
    main()





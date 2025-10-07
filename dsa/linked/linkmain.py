

"""
 Linked lists are widely used in real-world applications such as:
Music or video playlists (where each track links to the next)
Operating systems (for scheduling tasks)
Undo/redo functionality in text editors

 Limitations of Arrays (or Python Lists)
1. Insertion/Deletion at Arbitrary Positions: Inserting or deleting an element in the middle of a Python
list typically requires shifting elements, which can be costly (O(n) time).
2. Memory Constraints (Lower-Level Languages): In lower-level contexts (like C), arrays require
contiguous memory blocks. While Python lists do handle resizing dynamically, they can still suffer
from performance hits if the array must expand frequently.
3. Frequent Insertions: If you often insert in the front or middle, it can be more efficient to maintain a
linked structure than to rely on list insertions that shift elements.

2.2 How Linked Lists Help
1. Efficient Insertions/Deletions: Adding or removing nodes typically involves just changing a few
pointers (or references in Python).
2. Flexible Size: You can grow or shrink the list as needed.
3. Non-Contiguous Memory: In languages like C, nodes can be allocated anywhere. In Python, the
concept of “contiguous memory” is abstracted away, but the linked-list structure still offers clarity and
efficiency for certain operations.

A Singly Linked List is a sequence of elements (called nodes) where each node contains:
1. Data (key): The actual information to store (e.g., an integer, a student’s name, etc.).
2. Pointer (next): The reference to the next node in the sequence.

A special pointer (often called head) references the first node. The last node’s next reference is set to
None , indicating the end of the list.
[ Data | next ] → [ Data | next ] → [ Data | next ] → None
^
|
head

Typical operations:
1. Traverse – Visit and read each node’s data.
2. Search – Find a node containing a certain key.
3. Insert – Add a new node at the beginning, at the end, or after a given position.
4. Delete – Remove a node from the beginning, from the end, or at a specified position

If we have 10 nodes, how many next references do we follow to traverse from the first to the last node?
A: We follow 9 next pointers to get from the first node to the last (the 10th).

To search for a key k , start at head and check each node until you find the key or reach the end ( None )
No random access in a singly linked list. You can’t jump to a middle node in O(1) time as you might
with an array index

Why can’t we perform binary search (which is O(log n)) on a singly linked list?
A: Binary search requires direct (index-based) access to the middle of the list. Singly linked lists only allow
sequential traversal, so you can’t jump in constant time.

Traverse: O(n)
Search: O(n) worst case, O(1) best case
Insert or Delete:
At Head: O(1)
At Tail (in a singly list with no tail pointer): O(n) to find last node
In Middle: O(n) to find the spot + O(1) to adjust pointers


Step-by-Step Algorithm: recursive traverse

Firstly, we define a recursive method to traverse the singly linked list, which takes a node as a parameter.
In this function, the base case is that if the node is null then we will return from the recursive method.
We then pass the head node as the parameter to this function.
After that, we access and print the data of the current node.
At last, we will make a recursive call to this function with the next node as the parameter.
"""



class Node:
    def __init__(self,data):
        self.data = data  # Assign data
        self.next = None # last or single node # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, no nodes in the list

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head # 3. Make next of new Node as head
        self.head = new_node # 4. Move the head to point to new Node

    def insertat_end(self, data): # new data to be inserted

        new_node = Node(data) # data fed to a node# If the list is empty, the new node becomes the head
        if self.head is None: # empty linked list
            self.head = new_node
            return
        current = self.head
        while current.next is not None: # traverse to the end
            current = current.next
        current.next = new_node# curr.next which had none now has link to newnode


    def insert_after(self, data,pos): # new data to be inserted

        if pos < 1:
            print("Position must be >= 1.")
            return self.head

        new_node = Node(data) # data fed to a node# If the list is empty, the new node becomes the head
        if self.head is None: # empty linked list
            return new_node
        i = 1
        current = self.head
        while i < pos: # traverse to the pos before pos
            if current is None:
                return self.head
            current = current.next
            i += 1
        if current is None:
            print("Position out of range.")
            return self.head
        print("current.next = ",current.next)
        new_node.next = current.next # first create link to existing list from new
        current.next = new_node  # then from list to new
        return self.head


    def search(self,k):
        current = self.head
        i = 0
        while current is not None:
            if current.data == k:
                print(f"{k} found at position {i}.")
                return True
            current = current.next
            i += 1
        print(f"{k} not found in the list.")
        return False

    def present(self, x):

        # Initialize current to head
        current = self.head

        # Loop till current not equal to None
        while current != None:
            if current.data == x:  # if the current node's value is equal to key
                # Data found
                return True

            current = current.next # increment

        # Data Not found
        return False

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return None

        va = self.head.data
        deleted_node = self.head # Store the current head in a temporary variable
        print("del",va)
        self.head = self.head.next # Move the head pointer to the next node
        deleted_node = None  # Free the memory of the old head node
        return self.head

    def delete_from_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return None
        # If there's only one node
        if self.head.next is None:
            val = self.head.data
            self.head = None
            return val

        # Otherwise, traverse to the second-last node
        current = self.head
        while current.next.next is not None:  #   head - curr - curr.next - (None)
            current = current.next
        val = current.next.data  # Last node's data
        print("val",val)
        current.next = None  # Remove last node
        return self.head

    def delete_at_pos(self,j):
        if j<1 or self.head is None:
            print("invalid")
            return None

        current = self.head
        # if we are deleting the first node
        if j == 1:
            val = current.data
            self.head = current.next
            return val
        # find j-1 th node,Traverse to the node before the one to be deleted
        count = 1
        while current is not None and count < (j-1):
            current = current.next # when co = j-1 current is to be deleted
            count += 1 # curr  -  curr.next - curr.next.next
                       #  j-1  -     j      - j.next
        val = current.next.data # data of jth point
        print("posval",val)
        current.next = current.next.next
        return self.head

def traverseList(head):
    # base condition is when the head is None
    if head is None:
        print()
        return

    # printing the current node data
    print(head.data, end="")

    # print arrow if not the last node
    if head.next is not None:
        print(" -> ", end="")

    # moving to the next node
    traverseList(head.next)

def delete_from_beginning(head):
    if head is None:
        print("List is empty, nothing to delete.")
        return None

    va = head.data
    deleted_node = head  # Store the current head in a temporary variable
    print("del", va)
    head = head.next  # Move the head pointer to the next node
    deleted_node = None  # Free the memory of the old head node
    return head


def main():
    # 1. Work with CircularLinkedList
    lili1 = LinkedList()
    lili2 = LinkedList()
    lili3 = LinkedList()
    for value in [10, 20, 30, 40, 50]:
        lili1.insert_at_beginning(value)
        lili1.insert_after(value,2)
        lili3.insertat_end(value)
    print(" Linked List Traversal:")
    lili1.traverse()
    lili3.traverse()
    print(lili1.search(30))
    traverseList(lili1.head)
    lili1.insert_after(100,5)
    lili1.traverse()
    lili1.delete_at_pos(4)
    lili1.traverse()




if __name__ == "__main__":
    main()

# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Link the fourth node
head.next.next.next = Node(40)

# printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
head = delete_from_beginning(head)
traverseList(head)
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Delete the head node and return the new head
def deleteHead(head):

    # Check if the list is empty
    if head is None:
        return None

    # Store the current head in a
    # temporary variable
    temp = head

    # Move the head pointer to the next node
    head = head.next

    # Free the memory of the old head node
    # (Python garbage collector will handle it)
    temp = None

    return head


# Function to print the linked list
def printList(curr):
    while curr is not None:
        print(curr.data, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 8 -> 2 -> 3 -> 1 -> 7
    head = Node(8)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(7)

    head = deleteHead(head)  
    printList(head)
"""


"""
if __name__ == "__main__":
    head = None
    head = insert(head, 10)
    head = insert(head, 20)
    head = insert(head, 5)
    head = insert(head, 44)

    print("Linked List:")
    traverse(head)
    # Search for a value
    k = 15
    found_node = search(head, k)
    if found_node:
        print(f"Value {k} found in the list!")
    else:
        print(f"Value {k} not found in the list.")


 Delete at a Specific Position (j-th node)
1. Traverse to the j-th node (keeping track of the (j-1)-th node).
2. Remove the j-th node by adjusting pointers.
3. Return the data of the removed node.




. Q: If this was the only node in the list, what happens next?
A: After head = head.next , head becomes None . So the list becomes empty
"""
"""
5.1 Stack Using Linked List
A stack follows Last-In-First-Out (LIFO).
Push: Insert a new node at the beginning of the linked list (O(1)).
Pop: Delete a node from the beginning of the linked list (O(1)).
"""
# Using our LinkedList structure
class StackLL:
    def __init__(self):
        self.ll = LinkedList() # internally use a LinkedList

    def push(self, data):
        self.ll.insert_at_beginning(data)


    def pop(self):
        return self.ll.delete_from_beginning()

    def peek(self):
        return self.ll.head.data if self.ll.head else None

"""
 Queue Using Linked List
A queue follows First-In-First-Out (FIFO).
Enqueue: Insert a new node at the end of the list.
Dequeue: Remove from the front (head) of the list
"""
class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None # keep track of the last node

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node # update tail

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None # If empty after removal
        return val

"""
Implement a function to reverse a singly linked list.
1. Create or use a singly linked list structure in Python.
2. Populate it with some integer values.
3. Write a reverse() method that reverses the list in-place.

We keep a prev pointer that initially is None .
We iterate through the list, detaching each node and hooking it to prev .
At the end, prev is the new head.
"""
def reverse(self):
    prev = None
    current = self.self.head
    while current is not None: # curr stops before none  #  head -> node -> curr -> cuur.next(none or prev)
        nxt = current.next
        current.next = prev  # change direction of pointer     head <- node <- curr <- prev(head))<-
        prev = current # make prev = cuur
        current = nxt # go to next step or increment
    self.self.head = prev



"""
# a linked list node
class Node:
    def __init__(self, data):
        # constructor to initialize a new node with data
        self.data = data
        self.next = None

# function to traverse and print the singly linked list
def traverseList(head):
    # base condition is when the head is None
    if head is None:
        print()
        return

    # printing the current node data
    print(head.data, end="")

    # print arrow if not the last node
    if head.next is not None:
        print(" -> ", end="")

    # moving to the next node
    traverseList(head.next)

if __name__ == "__main__":
    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList(head)
"""
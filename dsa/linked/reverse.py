

#------iteratively

class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def reverseList(head):

    curr = head
    prev = None

    # traverse all the nodes of Linked List
    while curr is not None:

        # store next
        nextNode = curr.next

        # reverse current node's next pointer
        curr.next = prev

        # move pointers one position ahead
        prev = curr
        curr = nextNode

    return prev


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = reverseList(head)
    printList(head)





#------------------ recursively
"""
The idea is to use recursion to reach the last node of the list, which becomes the new head after reversal.
As the recursion starts returning, each node makes its next node point back to itself, effectively reversing
the links one by one until the entire list is reversed.
"""

class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def reverseList(head):
    if head is None or head.next is None:
        return head

    # reverse the rest of linked list and put the
    # first element at the end
    rest = reverseList(head.next)

    # make the current head as last node of
    # remaining linked list
    head.next.next = head

    # update next of current head to NULL
    head.next = None

    return rest


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)
    printList(head)



"""
Using Stack - O(n) Time and O(n) Space
The idea is to traverse the linked list and push all nodes except the last node into the stack.
 Make the last node as the new head of the reversed linked list. Now, start popping the element and append
  each node to the reversed Linked List. Finally, return the head of the reversed linked list.
"""

class Node:
    def __init__(self, new_data):

        self.data = new_data
        self.next = None


def reverseList(head):

    stack = []

    temp = head

    # push all nodes except the last node into stack
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    head = temp

    # pop all the nodes and append to the linked list
    while stack:

        # append the top value of stack in list
        temp.next = stack.pop()

        temp = temp.next

    temp.next = None

    return head


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

if __name__ == "__main__":
    # create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)
    printList(head)



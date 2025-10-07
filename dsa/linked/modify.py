

"""

Given a Singly linked list.- The task is to modify the value of the first half of nodes such that
1st node's new value is equal to the value of the last node minus the first node's current value,
2nd node's new valueis equal to the second last node's value minus 2nd nodes current value,
likewise for first half nodes, then replace the second half of nodes with the initial values of
the first half of nodes (values before modifying the nodes).

Note: If the size of it is odd then the value of the middle node remains unchanged.

"""



# Python program to modify a singly linked list
# By transferring it to an array
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodes(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count

def linkedListToArray(head, arr, n):
    curr = head

    for i in range(n):
        arr[i] = curr.data
        curr = curr.next

def arrayToLinkedList(arr, head, n):
    curr = head

    for i in range(n):
        curr.data = arr[i]
        curr = curr.next

def modifyArray(arr, n):

    # Modify the array
    for i in range(n // 2):
        x = arr[i]
        arr[i] = arr[n - i - 1] - x
        arr[n - i - 1] = x

def modifyTheList(head):
    if head.next is None:
        return None

    # Count the number of nodes
    n = countNodes(head)

    # Create an array
    arr = [0] * n

    # Convert linked list to array
    linkedListToArray(head, arr, n)

    # Modify the array
    modifyArray(arr, n)

    # Convert array back to linked list
    arrayToLinkedList(arr, head, n)

    return head

def printList(node):
    curr = node
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list
    # 10 -> 4 -> 5 -> 3 -> 6
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(6)

    head = modifyTheList(head)

    printList(head)























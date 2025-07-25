
# Python program to implement Recursive insertion and
# traversal in a linked list

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to insert a new node at the
# end of linked list using recursion.
def insert_end(head, data):

    # If linked list is empty, create a new node
    if head is None:
        return Node(data)     # when head becomes none data is added to list

    # If we have not reached the end,
    # keep traversing recursively
    head.next = insert_end(head.next, data)
    return head

# Function to traverse and print the linked list
# starting from the head node, recursively
def traverse(head):
    if head is None:
        return

    print(head.data, end=" ")

    # Recur for the remaining list
    traverse(head.next)

def func(head):
    if head == None:
        return 'empty'

    pos = 0
    while head != None:
        if pos == head:
            if head.next.next != None:
                print(head.data, " ", end='')
                return func(head.next)
            print(head.data, " ", end='')
        head = head.next
        pos += 1
    return head

if __name__ == "__main__":

    # Insert nodes with data 1, 2, 3, 4, 5
    head = None
    head = insert_end(head, 1)  # making head a list in which data is added to end
    head = insert_end(head, 2)
    head = insert_end(head, 3)
    head = insert_end(head, 4)
    head = insert_end(head, 5)

    traverse(head)
    print(func(head))










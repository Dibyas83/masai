

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListRecursive(head: ListNode) -> ListNode:
    """
    Recursively reverses a singly linked list.
    """
    # Base case: If the list is empty or has only one node, it's already reversed.
    if not head or not head.next:
        return head

    # Recursive step: Reverse the rest of the list.
    # new_head will be the new head of the *reversed* sub-list.
    new_head = reverseListRecursive(head.next)

    # Link the current node (head) to the end of the reversed sub-list.
    # head.next is the node that was originally *after* head.
    # After the recursive call, head.next points to the *tail* of the reversed sub-list.
    # We make that tail point back to the original head.
    head.next.next = head

    # Set the current node's next pointer to None, as it becomes the new tail.
    head.next = None

    # Return the new head of the completely reversed list.
    return new_head

# Example Usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Reverse the list
reversed_head = reverseListRecursive(head)

print("Reversed List:")
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")











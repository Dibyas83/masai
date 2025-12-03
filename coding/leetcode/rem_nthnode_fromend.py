
# given linked list rem nth node from end, using two pointer p1 p2 separated by n nodes,
# when p2 is at end pi is at nth pos from end , by making prev.next= curr.next or
# if p1 starts before 1st node and both separated by  n+1 nodes

class ListNode:  # list f intervals as object(two member start and end)
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solut:

    def rem_nthnode(self,head: ListNode, n: int) ->  ListNode: # l1 and l2 are pointer of  nodes of lists
        dummy = ListNode(0, head) # it is before head
        left = dummy
        right = head

        while n > 0 and right: # take right to nth pos
            right =right.next
            n += 1

        while  right: # take right to nth pos
            left = left.next
            right =right.next

        left.next = left.next.next
        return  dummy.next  # head








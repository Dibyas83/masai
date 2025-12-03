
#merge sorted linked list
#  list1 = 1    2    4  list2 = 1   3   4

class ListNode:  # list f intervals as object(two member start and end)
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solut:

    def mergelinklist(self,l1: ListNode, l2: ListNode) ->  ListNode: # l1 and l2 are pointer of  nodes of lists
        res = ListNode()  # dummy starting node of new linkedlist
        tail = res

        while l1 and l2: # not null
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next # move to next node in list of l1
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return res.next














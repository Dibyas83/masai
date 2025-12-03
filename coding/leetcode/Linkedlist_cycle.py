
# given head of a linked list  determine if it has a cycle in it ie next goes to node which
# is already traversed and dont reach None
# by using hashmap or hashset and visited list. take every node and it self to set
# using slow and fast ponter if they mmet at a point
#  1, 2, 3, 4, 5, 6, 7 , 8, 9, 11, 12, 13 ,ater 3 steps it becomes
# s,f    s           f
# slow anf fast pointer slow moves gap increases ,fast moves gap dec by 2 steps
class ListNode:  # list f intervals as object(two member start and end)
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solut:

    def ifcycliclist(self,head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next: # both not null
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


        return False # if null














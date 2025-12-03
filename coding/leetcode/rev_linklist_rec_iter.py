
# null   -  1(head)   -   2   -   3   -  none
# prev      curr
# rev a singly linked list. using two pointer iteratively ,curr = head and prev = null

# for _  in range(len):  x = curr.next , curr.next = prev , prev = curr, curr = x
# at last curr = null , head = prev

class ListNode:  # list f intervals as object(two member start and end)
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solut:

    def revlist(self,head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr: # not null
            x = curr.next
            curr.next = prev
            prev = curr # move fwd
            curr = x # move fwd
        return prev # got head
# O(n), mem O(1)
# recursively it becomes O(n), mem O(n)

# it is done rec by breaking it to sub problems
# null   -  1(head)   -   2   -   3   -  none
# by reversing every except 1 and make 1 head, then reverse rest except 2 and make 2 head, ....

# when cur = 2 , cur.next = 3 .  rev by making cur.next.next = curr, curr = prev



class Solutrec:

    def revlist(self,head: ListNode) -> ListNode:

        if not head: # base case - if head is null - going to last or end
            return None
        new_head  = head  #  when not null. curr position becomes head and newhead is that head
        if head.next:  # head.next is not null
            new_head = self.revlist(head.next)  # as rev_list returns head
            head.next.next = head
        head.next = None  # (1)
        return  new_head

# head = 1,head.next = 2 not null, revlist(2)  (1)linked to None. head = 2, head.next = 3 not null, revlist(3) linked to 1 . head = 3, head.next =  null, newhead remain as of prev = 3 linked to 2
#  null   -  1(head)   -   2   -   3   -  none






# given a head of linked list.change the order. by meging ist to last of 2nd half pairs
# by reversing 2nd half. by using fast and slow pointer to reacg half

# 1  2  3  4  5   ,   1  ->  2 -> 3 -> null     5 -> 4

class ListNode:  # list f intervals as object(two member start and end)
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solut:

    def reorder(self,head: ListNode) ->  None: # l1 and l2 are pointer of  nodes of lists
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        send_half = slow.next
        prev = slow.next = None # last node
        while send_half:
            tmp = send_half.next # saving before deleting link.  4.next = 5
            send_half.next = prev # reversing  4 .next = none
            prev = send_half  # now at  prev it is 4
            send_half = tmp  # at  4 it is 5

        first, send_half = head, prev  # last node
        while send_half:
            tmp1, tmp2 = first.next, send_half.next
            first.next = send_half
            send_half.next = tmp1
            first = tmp1
            send_half  = tmp2
            first, send_half = tmp1, tmp2













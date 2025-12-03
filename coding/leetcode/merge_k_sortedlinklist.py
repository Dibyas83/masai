
#merge sorted linked list
#  list1 = 1    list2 =  4  list3 =   3   list4 = 6
# compare l1,l2 then res with l3 then res with l4 by iterating val in res not effiicient


class ListNode:  # list f intervals as object(two member start and end)
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solut:

    def merge_k_linklist(self,l1sts: list[ListNode]) ->  ListNode: # l1 and l2 are pointer of  nodes of lists
        if not l1sts or len(l1sts) == 0:
            return None

        while len(l1sts) > 1:
            mergdlist = []

            for i in range(0, len(l1sts), 2):
                l1 = l1sts[i]
                l2 = l1sts[i+1] if (i+1) < len(l1sts) else None
                mergdlist.append(self.merge_k_linklist(l1,l2)) # mergesort first two list
            l1sts = mergdlist # lists is half the size of total lists
        return  l1sts[0] # the last list

    def mergelinklist(self, l1, l2):
        res = ListNode()  # dummy starting node of new linkedlist
        tail = res

        while l1 and l2:  # not null
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next  # move to next node in list of l1
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next # tail is the next val

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return res.next


















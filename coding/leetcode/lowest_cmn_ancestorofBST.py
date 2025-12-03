
"""
         3
    1          7
 7     2     8    3
    5    3

find the root of the  lowest subtree which  has  3 and 7 ans is 1
check if p& q are small than root then on left side or bigger than root on right side, if p or q is same as root then root itself
"""
# DOING ITERATIVELY using stack = 3 to 1 to null |3,1| to 1(revisit=k=1) to 2|3,#,2| to null(k=1,2) to 2 to 1 to 3|#,#,#|(k=1,2,3) to 4|#,#,#,4| to null to 4 |#,#,#,#|(k=1,2,3,4) after left of 4 we go to right of 4 which is also null but there is nothing to pop so we know it is empty now
# if from 1 to null we pop 1 , all was popped orderly

class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def lowest_cmn_ancestor(self, root: Treenode,p: Treenode, q: Treenode) -> Treenode:

        curr = root # pintr

        while curr: # curr is not null and stack is not empty
            while curr:
                if p.val and q.val > curr.val:
                    curr = curr.right
                elif p.val and q.val < curr.val:
                    curr = curr.left
                elif (p.val < curr.val and q.val > curr.val) or (p.val == curr.val or q.val == curr.val) or (p.val > curr.val and q.val < curr.val):
                    return  curr










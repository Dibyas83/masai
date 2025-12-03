
"""
        3
    1       4
      2
"""
# DOING ITERATIVELY using stack = 3 to 1 to null |3,1| to 1(revisit=k=1) to 2|3,#,2| to null(k=1,2) to 2 to 1 to 3|#,#,#|(k=1,2,3) to 4|#,#,#,4| to null to 4 |#,#,#,#|(k=1,2,3,4) after left of 4 we go to right of 4 which is also null but there is nothing to pop so we know it is empty now
# if from 1 to null we pop 1 , all was popped orderly

class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def kthsmallest(self, root: Treenode,k: int) -> int:
        n = 0 # no ok elements visited ,when it reaches k
        stack = []
        curr = 0 # pintr

        while curr and stack: # curr is not null and stack is not empty
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right







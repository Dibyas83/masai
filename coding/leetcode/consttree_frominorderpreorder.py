
# given two lists of traversals

"""
        5               5
    4       3       4       3       not same
         6    7           6    7

preorder - root - leftsub - rightsub  = 5,4,3,6,7  got 3 as root and as 20 is in rightsub from inorder and 20 comes first so it is root of that sub
                                      - 1 -  -  3  -  from inorder
inorder - leftsub - root - rightsub   = 4, 5, 6,3,7  left of 5 is leftsub and right is rightsub
                                      - 1 -  -  3  -

"""

class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def builtree(self, preorder: list[int], inorder: list[int]) -> Treenode:
        if not preorder or not inorder:
            return None
        root = Treenode(preorder[0])
        mid = inorder.index(preorder[0]) # index of root in inorder
        root.left = self.builtree(preorder[1:mid+1], inorder[:mid])
        root.right = self.builtree(preorder[mid+1:], inorder[mid+1:])
        return  root












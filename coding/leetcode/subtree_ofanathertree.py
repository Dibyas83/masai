
# to check if a given subtree is a subtree of anather tree,or same tree or totally diff check by starting from root,then from its child
"""
        5               5
    4       3       4       3       not same
                               7
"""


class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def issubtree(self, s: Treenode, t: Treenode) -> bool:
        if not t:
            return True
        if not s:
            return False
        if self.sametree(s,t): # s.left or right are compared
            return True
        return self.issubtree(s.left, t) or self.issubtree(s.right, t)

    def sametree(self, s, t) -> bool:

        if not s and not t: # both tree are empty s and t are roots
            return True
        if not s or not t: # one tree is empty
            return False
        if s.val != t.val: # if val are diff
            return False
        if s and t and s.val == t.val:
            return self.sametree(s.left, t.left) and self.sametree(s.right, t.right)
            # rec calling left side of p and q trees andrec calling right side of p and q trees



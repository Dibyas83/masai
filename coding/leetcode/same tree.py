
# check if the struc and val are same

# using dfs , for recursively if root and root of subtrees are same

from  collections import  deque

class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def sametree(self, p: Treenode,q: Treenode) -> bool:
        if not p and not q: # both tree are empty pand q are roots
            return True
        if not p or not q: # one tree is empty
            return False
        if p.val != q.val: # if val are diff
            return False
        return self.sametree(p.left, q.left) and self.sametree(p.right, q.right)
        # rec calling left side of p and q trees andrec calling right side of p and q trees







"""
            4                    4
        2       3            3       2
    5       6       7    7      6       5

"""
class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def inverttree(self, root: Treenode,) -> Treenode:
        if not root: # both tree are empty pand q are roots
            return None
        tmp = root.left # left ele stored in var
        root.left = root.right
        root.right=tmp

        self.inverttree(root.left)
        self.inverttree(root.right)
        return root









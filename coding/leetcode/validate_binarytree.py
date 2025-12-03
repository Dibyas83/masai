
"""
left child should be small than root and right bigger
            4
        2       5
          3   4     7    not subytree as root !< 4 in right subtree

"""
# calculation is done from bot,recursively


class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def validtree(self, root: Treenode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.va< right and node.val > left):
                return False

            return valid(node.left,left,node.val) and valid(node.right,node.val,right) # (node, should be
            # greater than this, should be < this) ,3 is smaller than 4(root) in left subtree - node.val is parent
        return valid(root, float("-inf"), float("inf"))









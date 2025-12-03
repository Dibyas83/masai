
"""
            4
        2       3
             6     7

"""
# calculation is done from bot,recursively


class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def maxpathsum(self, root: Treenode,) -> int:
        res = [root.val] # global var ,it will absorb changes

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            leftmax = dfs(root.left)
            righttmax = dfs(root.right)
            leftmax =max(leftmax ,0)
            righttmax = max(righttmax ,0)

            # compute max path sum with split
            res[0] =max(res[0], root.val + leftmax, righttmax)

            return root.val + max(leftmax,righttmax)

        dfs(root)
        return res[0]










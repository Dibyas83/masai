
# given a root, a binary trees max depth is the no of nodes along the longest path to leaf node

# 3 ways dfs,rec and iter dfs,bfs

# 1 + max(dfs(left) ,dfs(right))
from  collections import  deque

class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def maxdep(self, root: Treenode) -> int:
        if not root:
            return 0
        return  1 + max(self.maxdep(root.left), self.maxdep(root.right))

    # bfs - counting levels using que (replace the root with childrens) stop when no child
    def maxdepbfs(self, root: Treenode) -> int:
        if not root:
            return 0
        level =1
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: # not empty and has ele
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return level

    def iterdfs(self, root: Treenode):  # using stack and add child
       
        stack = [[root, 1]] # root and depth
        res = 0
        while stack:
            node, depth = stack.pop()

            if node: # not none
                res = max(res, depth)
                stack.append([node.left, depth+1]) # adding child
                stack.append([node.right, depth+1])
            return  res








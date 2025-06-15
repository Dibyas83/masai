

class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
    def __str__(self):
        return str(self.val)


class Sol:
    def isbst(self,root):
        if root is None:
            return True
        if root.left is not None and root.val <= root.left.val:
            return False
        if root.right is not None and root.val >= root.right.val:
            return False
        return (self.isbst(root.left) and self.isbst(root.right))
r = Sol()
n = int(input())
arr = list(map(int,input().split(" ")))
root = None
for i in range(n):
    root = Node(arr[i])
print(r.isbst(root))

#-----------------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def isBST(self, root):

        if root is None:
            return True
        if root.left is not None and root.val <= root.left.val:
            return False
        if root.right is not None and root.val >= root.right.val:
            return False
        else:
            return self.isBST(root.left) and self.isBST(root.right)


solve = Solution()
t = int(input())
A = []
for j in range(t):
    A.append(int(input()))
print(A)
root = None
for i in range(t):
    root = Node(A[i])
print(solve.isBST(root))








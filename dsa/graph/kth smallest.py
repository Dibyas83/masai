"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

"""
#------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthsmall(root1,k):
    res = []
    get_val(root1,res)
    res.sort()
    return res[k-1]

def get_val(root1,res):
    if root1 is None:
        return
    else:
        get_val(root1.left,res)
        res.append(root1.val)
        get_val(root1.right,res)
        print(res)
        return


k = int(input())
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
root1 = None
for i in range(n):
    root1 = Node(arr[i])
    print(root1.val)
print(kthsmall(root1,k))








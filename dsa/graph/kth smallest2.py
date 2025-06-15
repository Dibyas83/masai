
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        return


k = int(input())
n = int(input())
arr = list(map(int,input().split(" ")))
root1 = None
for i in range(n+1):
    root1 = Node(arr[i])
    print(root1.val)
print(kthsmall(root1,k))








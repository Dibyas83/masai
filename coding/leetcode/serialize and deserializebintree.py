

# dfs using que,remove root and replace with children


class Treenode:  # list f intervals as object(two member start and end)
    def __init__(self, val =0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solu:
    def serialize (self, root):
        res = []
        def dfs(node):
            if not node: # empty
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return  ",".join(res)
    def deserialize (self, data):
        vals = data.split(",") # a list
        self.i = 0 # member var of this class,global pointer.0 means starting from first val from list

        def dfs(): # rec func
            if vals[self.i] == "N": # base case
                self.i += 1 # move pointer ,as end of road
                return None
            node = Treenode(int(vals[self.i]))  # root of the tree created
            self.i += 1
            node.left = dfs()
            node.right  =dfs()
            return node
        return dfs() # returning tree



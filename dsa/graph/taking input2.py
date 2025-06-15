class Node:
    def __init__(self, key):
        self.key = key
        self.leftBranch = None
        self.rightBranch = None


def insert(root, key):
    if root is None:
        root = Node(key)
        return
    else:
        if root.key == key:
            return

        if key < root.key:
            if root.leftBranch:
                insert(root.leftBranch, key)
                return
            root.leftBranch = Node(key)
            return

        if root.rightBranch:
            insert(root.rightBranch, key)
            return
        root.rightBranch = Node(key)


def preorder(root):
    if root:
        print(root.key)
        preorder(root.leftBranch)
        preorder(root.rightBranch)


keys = list(map(int, input('Enter data to construct a BST (numbers divided by a space): ').split()))
print(keys)

root = Node(keys[0])

for key in keys:
    insert(root, key)

preorder(root)






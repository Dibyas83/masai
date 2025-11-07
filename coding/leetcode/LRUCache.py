
"""
lru cache stores value with fixed size ,with get( key value pairs) trturn it if present else return -1
put(key value) or update the val if key already exists,if it exceeds size evect the least used key val pair.
this is how browser works
"""
#   put - add in order,get value that has key as 1 using hashmap,
# if val be a pointer to node itself,using double linked list and pointer left(least used)
# and right(most used) we swap
# node has key,val and for prev and next node we need two  pointer -      left   [1,5]   [2,6]   right    >(Nodes)

class Node:
    def __init__(self,key, val):
        self.key,self.val = key, val
        self.prev = self.next = None


class Lrucache:
    def __init__(self, capacity: int):
        self.cap = capacity # storing capacity in a attribute
        self.cache = {} # map key to node
        self.left, self.right = Node(0,0), Node(0,0) # couple of dummy pointer to dummy node to
        # show which are the most recent val added with 0 as def val. these node are linked
        self.left.next, self.right.prev =  self.right, self.left

     # these helper func need to be applied to linked list
     # remove from list
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next,nxt.prev = nxt, prev

      #insert at right
    def insert(self, node):
        prev, nxt = self.right.prev,  self.right
        prev.next = nxt.prev = node
        node.next,node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # this tells us node, each key is maped to a node
        return -1
    # everytime we get a val we need to update it to most recent val

    def put(self,key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the lru from the hashmap
            lru =  self.left.next
            self.remove(lru)
            del self.cache[lru.key]














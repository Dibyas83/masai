


# it is linear ,like an array,it is a collection of nodes.nodes object have two component data and address
# of mem of next node.first node is called head and last node is called tail(address pointing to null or none . next = none)

# array needs right or left shift during insertion or del needs n time.linked list dont need shifting so tc is constant

# using linked list we can more data structures like stack , queue,doubly and circular linked list.no mem wastage like arrays

# linked list read(searching) operation in which we require to fetch will have tc of n,as we move from head - address to address
# 3 main operations are insert(from head ,middle(insert),tail(append)),traverse(print),delete(from head,tail(pop),using val(pos unknown=remove),using index),search(using val,index)

# lets create  nodes first
# in array read operations(traverse,indexing) but writing works(insert,delete) are slow ,its opposite in linklist
class Node:

    def __init__(self,value):
        self.data = value # attributes
        self.next = None  # address(next) one node is also the last node ,none is in address

class Linkedlist:

    def __init__(self):
        self.head = None  # create empty linked list . so head is none is condition for empty linked list
        self.n = 0  # n = count of nodes(length of linklist)

    def __len__(self):
        return self.n

# insert from head
    def insert_head(self,value):

        new_node = Node(value) # create new node by giving value
        new_node.next = self.head # create connection to current head
        self.head = new_node # reassign head to new node
        self.n = self.n + 1

    # to insert at tail we first traverse from head to tail and set tails next as new node address
    def append(self,val):  # same as insert_tail

        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return  # it will not process further

        curr = self.head  # marking the start point
        while curr.next != None:  # asks if currents next is none
            curr = curr.next # this is not processed when curr.next = none

        curr.next = new_node # new nodes next is none  and also in empty list heads value is none so if curr = head,curr = none and it has no next attribute
        self.n = self.n + 1

    def insert_after(self,after,val): # traverse  to pos,make link from new node to cur.next nad then cur to new node
        new_node = Node(val)
        curr = self.head
        while curr != None:
            if curr.data == after: # after is the value in the pos req
                break # curr stops here
            curr = curr.next # looping untill curr.data= none.if not found it goes to end and curr is none

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'not found' # if curr=none
    # delete by - clear,del from head,tail(pop),by value(remove)
    def clear(self):
        self.head = None
        self.n = 0

    def delfromhead(self):
        if self.head == None:
            return 'empty list'
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):  # cur!= none(stops at none), cur.next != none(stops at tail), cur.nex.nex != none
        if self.head == None: # if empty
            return 'empty'

        curr = self.head

        # if there is only 1 item in linllist
        if curr.next == None: # its head , so delete head
            return self.delfromhead()

        while curr.next.next != None:
            curr = curr.next  # keep moving fwd untill none
        curr.next = None # jumps tail
        self.n = self.n -1


    def remove(self,val):
        #if empty
        if self.head == None:
            return 'empty list'
        # we stop before the item to be deleted,but if the no is ist item
        if self.head.data==val:
            return self.delfromhead()


        curr = self.head
        while curr.next != None:
            if curr.next.data == val:
                break # now curr is before the val
            curr = curr.next # move
        if curr.next == None:
            return  "not found"
        else:
            curr.next = curr.next.next # answer

    def seach(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'not found'

    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return 'out of range'

    def func(self,head):
        if head == None:
            return 'empty'

        pos = 0
        while head != None:
            if pos == head:
                if head.next.next != None:
                    print(head.data, " ", end='')
                    return self.func(head.next)
                print(head.data, " ", end='')
            head = head.next
            pos += 1
        return 'out of range'

    def __str__(self):

        curr = self.head
        result = ""


        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]
"""
    def traverse(self):
        curr = self.head

        while curr != None:
            print(curr.data)
            curr = curr.next
"""




l = Linkedlist()
print(len(l))
print("---------------------")
a = Node(1)
b = Node(2)
c = Node(3)
print(a) # printing objects gives its address
print(a.data) # printing attributes
print(b.data) # printing attributes
print(c.data) # printing attributes
print(a.next)
print(b.next)
print(c.next)
"""
<__main__.Node object at 0x0000010E39CD6F90>
1
2
3
None
None
None
3 nodes created with no link
"""
print(id(a))
print(id(b))
print(id(c))
"""
2052895829904
2052898442768
2052898443088
"""
a.next = b  # linked list created by connection
b.next = c
print(a.next)
print(b.next)
print(c.next)
l.insert_head(11)  #
l.insert_head(22)
l.insert_head(33)
l.insert_head(44)  # insserted from head so latest head is 44
print(len(l))
print(l)
"""
44  
33
22
11
None now ccurr is none

"""
l.append(56)
l.append("True")
l.append(True)
print(l)

l.insert_after(22,222)  # 22 is value not position
l.insert_after(44,223)
l.insert_after(6,212)
print(l)
list_empty = Linkedlist()
list_empty.insert_after(22,222)
print(list_empty.insert_after(22,222))
l.delfromhead()
print(l)

l.pop()
print(l)


lin = Linkedlist()
lin.append(1)
lin.append(2)
lin.append(3)
lin.append(4)
lin.append(5)

print(lin,"lin")
print(lin.func(head),"lin")


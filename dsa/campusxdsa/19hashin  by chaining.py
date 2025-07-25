


"""
index remains same we form a linked list from that cur pos of index
"""
from operator import delitem
from os import remove

import select

cat = ord("c") + ord("a") + ord("t")
print(cat)
print(cat%10//2)
dog = ord("d") + ord("o") + ord("g")
print(dog)
print(dog%10//2)
rat = ord("r") + ord("a") + ord("t")
print(rat)
print(rat%10//2)

"""collison - two item with same index.solved by 
1-closed addressing technique -or chaining-duplicate will stay in the same address
by using node which has all items of same index is chained to same adress by creating nodes with
item in it and next pointed to other item address 

31,47,16,21,36 
l[1] = 31%5 = 1,l[2] = 47%5 = 2, 16%2 = 1,21%5 = 1,36%5= 1
this is not a int array but a node array(data,next)
if asked for 36 index 1  - we go to 1 compare if not there we traverse next by next    
When linked list created becomes bigger than array, there is no benifit
a - rehashing technique -if load factor crossed array size is increased,and hashing size inc and 
rehashing happens and items are placed in new places
b - chaining is long , we create balanced tree(logn)
--------------
an array of linked list
an array in which each item is an linked list not node  1 2 3 4 5 6 7 8 9
                                                            4
                                                            6
                                                            8
in python there is no built in link list, so we have to create one                                   
added from tail


"""
class Node:

    def __init__(self,key,value):
        self.key = key # attributes
        self.value = value  # attributes
        self.next = None  # address(next) one node is also the last node ,none is in address

class LL:

    def __init__(self):
        self.head = None  # create empty linked list . so head is none is condition for empty linked list
        self.n = 0  # n = count of nodes(length of linklist)

    def __len__(self):
        return self.n

    # to insert at tail we first traverse from head to tail and set tails next as new node address
    def add(self,key,value):  # same as insert_tail

        new_node = Node(key,value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return  # it will not process further

        curr = self.head  # marking the start point
        while curr.next != None:  # asks if currents next is none
            curr = curr.next # this is not processed when curr.next = none

        curr.next = new_node # new nodes next is none  and also in empty list heads value is none so if curr = head,curr = none and it has no next attribute
        self.n = self.n + 1

    # delete by - clear,del from head,tail(pop),by value(remove)
    def clear(self):
        self.head = None
        self.n = 0

    def delfromhead(self):
        if self.head == None:
            return 'empty list'
        self.head = self.head.next
        self.n = self.n - 1

    def remove(self,key):
        #if empty
        if self.head == None:
            return 'empty list'
        # we stop before the item to be deleted,but if the no is ist item
        if self.head.key == key:
            return self.delfromhead()

        curr = self.head
        while curr.next != None:
            if curr.next.key == key:
                break # now curr is before the val
            curr = curr.next # move
        if curr.next == None:
            return  "not found"
        else:
            curr.next = curr.next.next #  as it is before the value to del curr points next to next.next deleting link to next
            self.n = self.n - 1
    def traverse(self):
        curr = self.head

        while curr != None:
            print(curr.key, "-->", curr.value, " ", end=" ")
            curr = curr.next

    def size(self):

        curr = self.head
        counter = 0

        while curr != None:
            counter += 1
            curr = curr.next
        return counter

    def search(self,key):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.key == key:
                return pos
            curr = curr.next
            pos += 1
        return -1

    def get_node_atindex(self,index):
        curr = self.head
        conte=0
        while curr is not None:
            if conte == index:
                return curr
            curr = curr.next
            conte +=1

    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return 'out of range'



    def __str__(self):

        curr = self.head
        result = ""

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

class Diction: # using hash ,using two array one for keys one for values

    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.make_array(self.capacity)  # array of linkedlist.each linked list is a
        # bucket with bucket index.but in the chain each key is a node

    def make_array(self,capacity):
        l = []
        for i in range(capacity):
            l.append(LL())
        return l

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value): # it will call put and pass key,value to it,so can make dict like input
        self.put(key,value)

    def __delitem__(self, key):  # del from object so object.__delitem__

        bucket_index = self.hash_functions(key)

        self.buckets[bucket_index].remove(key)
        self.size -= 1

    def __str__(self):
        for i in self.buckets:
           i.traverse() # traversing the link list i in buckets
        return ""    # prints object

    def __len__(self):   # self is the object as input
        return self.size # gives length of object

    def get(self, key):

        bucket_index = self.hash_functions(key) # tells in which bucket key is in

        res = self.buckets[bucket_index].search(key)

        if res == -1:
            return "Not Present"
        else:
            node = self.buckets[bucket_index].get_node_atindex(res)
            return node.value

    def put(self, key, value):

        bucket_index = self.hash_functions(key)

        node_index = self.get_node_index(bucket_index, key)

        if node_index == -1:
            # insert
            self.buckets[bucket_index].add(key, value)
            self.size += 1

            load_factor = self.size / self.capacity  # size is no of nodes in all of linked lists and capacity is no of linkedlist specified in array
            print(load_factor) # also called lambda

            if (load_factor >= 2):
                self.rehash() # then all nodes place changes according to rehashed value and placed into new resized array(doubled)
        else:
            # update
            node = self.buckets[bucket_index].get_node_at_index(node_index) # gives node  at node_index of linked list at arrays[index]
            node.value = value # node already present

    def rehash(self):
        self.capacity = self.capacity * 2
        old_buckets = self.buckets # buckets or linked list placed to old buckets
        self.size = 0 # currently no nodes,start again from 0
        self.buckets = self.make_array(self.capacity) # array size doubled

        for i in old_buckets: # i is a linked lists
            for j in range(i.size()):  # size or nodes in that linked list
                node = i.get_node_atindex(j)
                key_item = node.key
                value_item = node.value
                self.put(key_item, value_item)


    def get_node_index(self,bucket_index,key):

        node_index = self.buckets[bucket_index].search(key) # linnkedlist object
        return  node_index

    def hash_functions(self,key): # gives index
        #return key %self.size  # but will not working on string
        return abs(hash(key)) % self.capacity  # will work on string ,int,unmutable objects like tuple not list,
        # sometimes they are negetive so use abs


j = LL()
j.add(2,4)
j.add(7,8)
j.add(11,55)
j.traverse()

print(j.get_node_atindex(1).key)
# print(j.get_node_atindex(4).key)  'NoneType' object has no attribute 'key'
d1 = Diction(2)
"""
when 4
0.25
0.5
0.75
1.0
1.25
when 2
0.5
1.0
1.5
2.0
0.25
0.5
0.75
1.0
1.25
"""
d1.put("python",34) # forming buckets or linked lists according to hash value
d1.put("java",56)
d1.put("c",86)
d1.put("c++",200)
d1.put("r",201)
#print(d1.buckets)
#print(d1.buckets[0].traverse())
#print(d1.buckets[1].traverse())
#print(d1.buckets[2].traverse())
#print(d1.buckets[3].traverse())

print(len(d1))

print(str(d1))
d1.__delitem__("c")
print(len(d1))



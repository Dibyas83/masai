
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

    def __str__(self):

        curr = self.head
        result = ""


        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

def fun(head):
    if head == None:
        return
    if head.next.next != None:  # head.next.next = 3.when on 4 head it will stop or return and not go to fun()
        print(head.data," ",end='') # it will print data of 1st node,=1- and no line change then 2,3,4 .till now fun() is not completed
        fun(head.next)
    print(head.data," ",end='') # it will be executed when fun() call will be completed.when completed
    # it print 4(where fun stops),the each return none to the prev func which are pending and they also print
    # head.data and returns none so head =none condition satisfy and goes to previous fun(call),so print 3,2,1
"""
1->2->3->4->5
1  2  3  4  3  2  1
"""
# first create a linked list then fun(head)
lk = Linkedlist()
lk.insert_head(5)
lk.insert_head(4)
lk.insert_head(3)
lk.insert_head(2)
lk.insert_head(1)
print(lk)
fun(lk.head) # gave it the head of lk





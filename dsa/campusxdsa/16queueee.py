


# fifo
# insertion or enque is from tail or rear,pop or deletion or deque  from head .like standing for
# tickets.head is called front
# in que it does not have to traverse to tail for addition, as two pointers are taken from front and rear

class Node:
    def __init__(self,value1):
        self.data = value1
        self.next = None

class Queue:
    def __init__(self):
        self.front = None # head initially none
        self.rear = None # tail

    def enqueue(self,value1):
        new_node = Node(value1) # a node is created but not linked

        if self.rear == None: # que empty
            self.front = new_node # insertion done and link created
            self.rear = self.front  # both front and rear having same value of newnode
        else: # que not empty
            self.rear.next = new_node # self.rear.next was  None
            self.rear = new_node # rear pointer sent to new node and now rear.next is pointing to none

    def deque(self):
        if self.front == None:
            return "empty"
        else:
            x1 = self.front.data

            self.front = self.front.next  # front pointer moved to next  7->8->9->none.now front is 8
            return x1


    def is_empty(self):
        return self.front == None # Tru or falkse

    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next  # or self.front.next
        return counter
    def front_item(self):
        if self.front == None:
            return "empty"
        else:
            return self.front.data

    def rear_item(self):
        if self.front == None:
            return "empty"
        else:
            return self.rear.data

    def traverse(self):
        temp = self.front

        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next # or self.front.next


q = Queue()
qu = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q.deque(),"deq")
#q.deque()
q.traverse()
print(q.front_item())
print(q.rear_item())
print(qu.is_empty())

def fun(num):
    if num == 0:
        return 0
    else:
        q.enqueue(num%10)
        res = fun(num//10)
        res = res*10 + q.deque()
        return res
"""
    num%10 = 3,num//10 =12 ,now num = 12
    12%10 = 2,12//10 = 1 ,num = 1
    1%10 = 1,1//10= 0,num=0 ,return 0 to res
    res*10 + 3 =3
    3*10 +2 = 32
    32*10 + 1 = 321
"""
q = Queue()
print(fun(123))












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

    def seach(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'not found'

    def replace_max(self,value):
        temp = self.head
        max = temp # current data

        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next # for fwding

        max.data = value

    def sum_odd_nodes(self):
        temp = self.head
        counter = 0
        result = 0
        while temp != None:
            if counter % 2 != 0:
                result = result + temp.data

            counter += 1
            temp = temp.next
        print(result)

lk = Linkedlist()
lk.insert_head(5)
lk.insert_head(4)
lk.insert_head(13)
lk.insert_head(2)
lk.insert_head(1)
lk.insert_head(11)
lk.insert_head(10)
print(lk)
lk.replace_max(15)
print(lk.sum_odd_nodes())
print(lk)













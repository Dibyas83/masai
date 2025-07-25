
# if there is only * or / replace with space ,if both present replace with space and next char bold
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
            result = result + str(curr.data) + " "
            curr = curr.next

        return result[::]

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

    def reverse(self):
        prev_node = None  # tail
        curr_node = self.head


        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node # moving prev
            curr_node = next_node # moving prev

        self.head = prev_node

    def change(self):
        temp = self.head
        while temp != None:
            if temp.data == "*" or temp.data == "/":
                temp.data = " "
                if temp.next.data == "*" or temp.next.data == "/":
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next  # jumping the next * or / .so shifting of whole linklist
                    # instead of two spaces
            temp = temp.next

lk = Linkedlist()
lk.insert_head("a")
lk.insert_head("c")
lk.insert_head("*")
lk.insert_head("/")
lk.insert_head("n")
lk.insert_head("o")
lk.insert_head("t")
lk.insert_head("*")
lk.insert_head("r")
lk.insert_head("u")
lk.insert_head("n")
print(lk)
lk.reverse()
lk.change()
print(lk)















"""
can be implemented using arrays,and linked list

1 by linked list   -push,pop,peek,empty,size
starts or inserted from head and deleted from head

"""
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # like head ,initially none ie empty
        self.size = 0

    def isempty(self):
        return self.top == None # will return true as self.top is none

    def push(self,val):
        newnode = Node(val)
        newnode.next = self.top
        self.top = newnode
        self.size += 1

    def peek(self):
        if self.isempty():
            return "empty"
        else:
            return self.top.data

    def pop(self):
        if self.isempty():
            return "emoty"
        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data

    def poped(self):
        if self.isempty():
            return "emoty"
        else:
            return self.top

    def traverse(self):
         temp = self.top
         while temp != None:
             print(temp.data)
             temp = temp.next

    def size_of(self):
         return self.size

    def reverse(self,string):
        for i in string:
            newnode = Node(i)
            newnode.next = self.top
            self.top = newnode

s = Stack()
st = Stack()
print(s.isempty())
s.push(2)
s.push(4)
s.push(6)
s.push(8)
s.push(10)
print(s.isempty())
print(s.traverse())
print(s.peek())
print(s.pop())
print(s.traverse())
st.reverse("help")
print(st.traverse())

def rev_string(text):
    stri = Stack()

    for i in text:
        stri.push(i)

    resultst = ""
    while  not stri.isempty(): # isempty is false. not false means true.when not true it will stop
        resultst += stri.pop()

    print(resultst)

rev_string("smile")

# undo(stack1) redo(stack2) using two stack.sting is in stack1 during undo 1 pops and pushed into 2.in redo 2 pops and rtored in 1

def undo_redo(): # or def undo_redo(pattern,condition):
    un = Stack()
    re = Stack()
    pattern = input()
    condition = input("u or r")

    for i in pattern:
        un.push(i)

    for i in condition:
        if i == "u":
            data = un.pop()
            re.push(data)
        else:
            data = re.pop()
            un.push(data)

    res = ""
    while not un.isempty():
        res = un.pop() + res # this will print in rev

    print(res)

undo_redo()  # or def undo_redo(pattern=input(),condition=input()):

# celebrity problem we get a 4*4 matrix as input we need to return a single value between 0 - n(colmn),celebrity is one who knos nobody and other knows him ,
# news = ([] * 4) * 4

cele = [[0,0,1,1],[0,0,1,0],[0,0,0,0],[0,0,1,0]] # = [[a],[b],[c],[d]] d is celebrity no 1

def find_the_celeb(cele):
    s1 = Stack()
    for i in range(len(cele)):
        s1.push(i)
    print(s1.traverse())
    while s1.size_of() >= 2:
        i = s1.pop() # 3
        j = s1.pop() # 2
        if cele[i][j] == 0: # j is not a celebrity
            s1.push(i)
        else: # i is not a celeb
            s1.push(j)

    celeb  = s1.pop()  # 2 ,checking 2
    for i in range(len(cele)):
        if i != celeb: #  2 on 2 intersection
            if cele[i][celeb] == 0 or cele[celeb][i] == 1: # [row][col] checking if col 2 has 0 or row 2 has 1 except  [2][2]
                print(" no one is calebrity")
                return
    print("the celeb is ",celeb)

# so a matrix was solved in order of n

print("-----------------------------")
"""
# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
    
d = {'a': 1, 'b': 2, 'c': 3}
tar = 2

# Find the first key for the value 2
for key, val in d.items():
    if val == tar:
        print(key)  
        break
"""
# parenthesis balance check  - push opening brackets and pop matching closing brackets

brks = {
    "(" :")",
    "{" :"}",
    "[" :"]"
}
word = "(dg{fgh[gg]}gh)]"
def match(brks,word):
    bracket = " "
    bracketsin = " "
    res = Stack()
    for keys in brks:
        bracket += keys
    print(bracket)
    for value in brks.values():
        bracketsin += value
    print(bracketsin)
    print(word)
    for i in range(len(word)):

        if word[i] in  bracket:
            res.push(word[i])
    for j in range(len(word)):

        if word[j] in bracketsin and  not res.isempty(): #  value = my_dict["name"]
            print(word[j],"1")
            print(res.peek(),"2")
            d= res.peek()

            if brks[res.peek()] == word[j]:
                res.pop()
            else:
                print("unbalanced")

        else:
            print("unba")
            print(word[j])
    print(res.traverse())

match(brks,word)



















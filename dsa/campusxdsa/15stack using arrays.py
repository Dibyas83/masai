

l = [1,2,3,4,5,6]
l.append(7)
l.append(9)
l.pop()
print(l)

class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None]* self.size # array created with a fixed size - name of array
        self.top = -1 # a variable.as everything will be from top

    def push(self,value):
        if self.top == self.size - 1: # 2 = 3-1
            return "overflow"
        else:
            self.top += 1
            self.stack[self.top] = value  # adding by index

    def pop(self):
        if self.top == -1:
            return "empty"
        else:
            data = self.stack(self.top)
            self.top -= 1 # moving top
            print(data)

    def traverse(self):
        for i in range(self.top + 1):
            print(self.stack[i],end=' ')

















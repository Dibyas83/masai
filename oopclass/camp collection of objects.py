


class Customer:
    def __init__(self,name,age):
        #print("hello")
        self.name = name
        self.age = age

    def intro(self):
        print('i am',self.name,'and i am',self.age)

c1 = Customer('nit',34)
c2 = Customer('nites',32)
c3 = Customer('nitin',38)

l = [c1,c2,c3]
for i in l:
    print(i.name,i.age) # if only i it will print address of object i
    i.intro()





























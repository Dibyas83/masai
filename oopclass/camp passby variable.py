


class Customer:
    def __init__(self,name):
        #print("hello")
        self.name = name



def greet(customer):  # a func is created outside class
    print(id(customer))
    customer.name = "nitish" # earlier customer was pointing to siksha ,now changed to nitish as if siksha was global
    print(customer.name)
    print(id(customer))

cust = Customer("siksha") # cust ia ref here to object Customer("name")
print(id(cust))
greet(cust)# customer asks cust where you pointing,then both variables or references are points to same
# object, but if customer changed original object address changes.so class objects are mutable like lists,dict and sets
"""
1574910062480
1574910062480
"""
print(cust.name)

print("------------------")

def change(l,lc):
    print(id(l),"l")
    #l.append(5)
    l = l + (5,6)
    lc = l + (5,6)
    print(l,"l")
    print(id(l),"append")
    print(lc,"append")

l1 =[1,2,3,4]
lc =()
l4 =(1,2,3,4)
print(id(l1),"l1")
# change(l1[:]) # cloning so no change
change(l4,lc)

print(id(l4),"l4")





























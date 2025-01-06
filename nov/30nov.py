


d= {}  # empty dictionary
d[1] = "a"
b={}
b[1.0] = "b"
print(d)
print(b)

d = {True:1,1:"r",1.0:"rt",1:6}  # 1 and 1.0 have same hash value True is also 1
g = {"gt": 1, 1: "r" , 1.0: "rt",4:6}  # rt is latest value

print(g.items())
print(g.values())
print(g.keys())
g.update(d)
g.update({"ass": "oo","o":b}) # b is anather dict
print(g)
coop = d.copy() # shallow copy
print(d)
print(coop)
student = {"stud1":{"name":"alice","age":25},"stud2":{"name":"bob","age":67}}
print(student["stud2"]["name"])
"a"
print("a")
print(type("a"))
lam_dict = {1: lambda x:x**2,2: lambda x: x**3}
print(lam_dict[1](2))
print(lam_dict[2](3))

f = lambda x: x**5
j = {}
j[f] = 32
j[f(2)] = 100
print(j)

coordinates =(1,2,3)
a,b,c = coordinates
print(a,b,c)


t=(5,10,3,5,55)
minval = t[0]
max_val = t[0]
for val in t:
    if val >max_val:
        max_val = val
    if val < minval:
        minval = val
print(minval)
print(max_val)


"""
tuple is ordered,immutable ,can use index,set cant use index
tuples are hashable and can be used as keys
memory efficient ,fast operations
"""

mset = set([1,2,5,7,4,3,9,6])
print(mset)
mset.discard(2)
print(mset)
# emptyset =set()
# dictionary = {}

tuple1 = (3,4,5,6,3,7)
tuple2 = tuple([1,2,6,9]) # tupl constructor
empty_tuple = ()
print(tuple1[2])
print(tuple1.count(2))
print(tuple1.index(7))
print(tuple1.count(3))

coordinates = (1,2,3)
coord = (1,2,3)
#x,y = coordinates
x,y,z = coordinates
print(x,y,z)
r,t,o = coord
print(r,t,o)
"""
sets used in membership check  O(1)  ,list and tuple O(n)
"""
set1 = set(range(10))
print(5 in set1)
#g={4,5,6,7,[8]}
g={4,5,6,7}# create set
g = set([4,5,6,1,2,4,3, 22,33]) # create set with constructor ,it will not add,no idexes or sorting,pop willrandomly remove
g.add(11)
g.discard(6)
print(g)
h=g.pop()
# h=g.pop(5)  set.pop() takes no arguments (1 given)
print(g)
print("==========444444")

h={6,7,4,3}
print(h)
print(g & h)  # intersection common to both
print(g | h)  # union
print(g - h)  # g only
print(g ^ h)  # symmetric difference union -intersection
print(len(h))


u = print("as")
m = print("asd")
print(u,m)
print(id(u),id(m))
e = {u:1,m:6}
print(e)


"ws" == "fg"
c = {"as":2, "fg":2}
print(c)


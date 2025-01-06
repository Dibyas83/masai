mylist=[1,2,3,'hey'] # not stored in contiguous
print(mylist[0])
print(mylist[-3])
# list methods 1-append() add an alement to the end of list like update
mylist.append("end element")
print(mylist)
#removes an element
mylist.remove(3)
print(mylist)
# pop() removes at specified location,if imdex is more last is removed
mylist.pop(2)
print(mylist)
mylist.insert(1,6)
print(mylist)
mylist.reverse()
print(mylist)
mylist.pop(0)
print(mylist)
mylist.sort(reverse=True) # should have no strings
print(mylist)
# list comprehension
mylist = [x for x in range(10)]
print(mylist)
mylist2=[u**3 for u in range(10)]
print(mylist.extend(mylist2))

mylist=[]
for x in range(10):
    mylist.append(x**3)
print(mylist)

names=["alice","asd","sdasd"]
init =[na[0] for na in names]
print(init)
print(names[1])
list1=list((list(("we","are","gone")),list(("far","away"))))
print(list1)

h =[3,5,7,8,33,44]
h.remove(5)
h.append(0)
print(h)











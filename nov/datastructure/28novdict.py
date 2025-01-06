
"""
binary search and sort is for list ,not for dictionary

"""

li =[3,4,5,6,7]
dicto ={3:2,4:3,"name":"alice",6:3,"courses":["math","phy"]} # 4 items
dicto3 =dict( i = 2,l=3,name_a = "alice",courses=["math","phy"]) # 4 items dict constructor for creating dicttonary only string keys can be used

dicto2 ={3:2,4:3,5:7,6:3,4:8} # 4 items
print(dicto3)
print(li[3])
print(li[0])
print(dicto.keys())
print(dicto2)
print(dicto.values())
print(dicto[3])
# print(dicto(3))
# print(dicto[0]) KeyError: 0
print(dicto["name"])
dicto[4] = 1 # to change
dicto[1] = 1 # to add
dicto["c"] = 1
print(dicto)
print(dicto[4])
print(dicto3.get("name_a"))
print(dicto3.get(0)) # raises none not key error if key doesnot exist
print(dicto3.items())
print("=====================================")
g = dicto2.pop(5) # 5 is key g takes value
dicto.popitem() # pops last item
# g = dicto2.pop[5]
print(g)

for i in dicto2.items():
    print(i)
for j in dicto3.items():
    print(j)


for i in range(200):
    print(i,chr(i))

mysent = ""
for i in range(97,97 + 26):
    mysent += chr(i)
print(mysent)

mydict = {}
cnt = 97
for let in mysent:
    mydict[let] = cnt
    cnt += 1
print(mydict)

# methods keys(),values(),items(),update()(adds anather dict , iterable of key-value pairs),copy()(returns a shallow copy)
# keys cannot be list,dictionary as it is mutable,can be immutable types ex strings no,tuples


s="abcdefgh"
g = {}
for i in s:
    if i in g:
        g[i] += 1
    else:
        g[i]=1
print(g)

#for i in range(len(s):
    #print(i)
    #print([i])

print("------------------------------45656")
dict4 ={"a":0,"b":0,"a":4,"d":0}
print(dict4)
print(dict4.items())
dict4.update({2:4,"u":7})
print(dict4)


num12 = input("enter no=")
print(num12*3)


data = input("enter nos sep by comas =")
nos = data.split(",")
tot = 0
for n in nos:
    tot += int(n)
print("sum",tot)

d = {'1,1':1}
d.get('1,1',0) # sets default value
d.get('1,2',0)
d.get('1,3',0)
d.get('1,4',0)
print(d)
# update() the dictionary with another dictionary or iterable of key-value pairs
# copy() returns a shallow copy of the dictionary.

# fabinoci series
f0 = 1
f1 = 2
flist = [f0,f1]
for i in range(10):
    flist.append(flist[i-1] + flist[i-2])
print(flist)








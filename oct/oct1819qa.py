for i in range(1,4):
    for j in range(1,11):
        print(f"{i}*{j} ={i*j}")

classes = [["a","b","c"],["v","n","m"]]
for groups in classes:
    for student in groups:
        print(student,end=" ")
    print()

print("1111111111111111111111111")

x = 1
while True:
    x += 1
    print("looping for ", x)
    if x>5:
        break
    x += 1

for i in range(1,5):
    for j in range(1,10):
        if j > 2:
            break
        print(i,j)
    print()
print("============1")
for i in range(1,5):
    for j in range(1,3):
        if j > 2:
            continue
        print(i*j,end=" ")
    print()

for i in range(1,5):
    for j in range(1,6):
        if j > i:
            break
        print("*",end=" ")
    print()
m=0
for i in range(1,5):
    for j in range(1,6):
        if j > 6//2-m & j < 6//2+m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        m += 1
    print()
result = []
for i in range(1,5):
    for j in range(1,6):
        result.append(i*j)
print(result)

o=list(range(5))
print(o)
o.remove(3)
o.remove(0)
o.insert(1,4)
print(o)
list3 = [x**3 for x in range(7)]
print(list3)

names = ["fsdf","rtyrty","ryrtyrt"]
initial = [name[0] for name in names]
print(initial)

q,w,e = 2,5,7
if q>w and q>e: print(q)
else: print(e)

print("============================55")

left=2
right=18
key=6
count=0

for i in range(left, right + 1):
    while i%key == 0:
      i += 1
      print(i)
      count +=1
print(count)
# range is an object

zen = "aei"
v ="aeiou"
for char in zen:
    if char not in v:
        print(char,end=' ')
else:
    print("not found")


gun ={10:"ten",20:"567",3:"tuy"}
for x in gun:
    print(x," ",gun[x])

ct = 0
while ct < 5:

    ct += 1
    print("ctct",ct)
else:
    print("rtyu", ct)
print("ghjk", ct)

mt = 0
rt = 0
ct = 0
while ct < 5 and rt < 100:
    rt += 1
    ct += 1
    print("kkkk",rt)
else:
    while mt < ct + 10 and rt < 100:
        rt += 1
        mt += 1
        print("more than 5",rt)
        ct = 0

mt = 0
rt = 0
ct = 0
for i in range(100):
    while ct < 5 and rt < 100:
        rt += 1
        ct += 1
        print("kkkk", rt)
    while ct < 10 and rt < 100:
        rt += 1
        ct += 1
        print("more than 5", rt)
    ct = 0


i =2
while(i<25):
    j = 2
    while(j<=(i/j)):
        if not (i%j): break # not 1 or more or true
        j = j+1
    if(j > i/j):print(i, "prime")
    i = i+1

print("good bye")












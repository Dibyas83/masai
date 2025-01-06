x=0
print("pos") if x>0 else print("neg")


x=1
while x<10:
    x += 1
    print("looping")
    if x>10:
        break
    x += 1


for i in range(3):
    if i == 1:
        continue
    print(i)
print("==============1")

for i in range(3):
    if i == 1:
        i=i+3
        pass
    print(i)
print("================2")

for i in range(3):
    if i == 1:
        break
    print(i)

for i in range(6):
    if i%2 != 0:
        continue
    for j in range(5):
        if j>2:
            break

        print(i,j,end=" ")
    print()
print("=============")

for i in range(5):
    for j in range(i+2):
        if i == j:
            break
    print(i,j)

for i in range(4,6):
    print("Table of ", i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

for i in range(1,3):
    for j in range(1,4):
        print(i,"*",j,"=",i*j)

for i in range(1,11):
        print(5,"*",i,"=",i*5)

for i in range(5):
    for j in range(5):
        if i < j:
            break
        print("*",end=" ") # by default \n is at end in print,end="" gives space insame line and dont go to new line.
    print()

for i in range(5):
    for j in range(5):
        if i == j:
            break
        print("*",end=" ")
    print()
N=6
for i in range(N):
    print(i)
    for j in range(N+1):
        if i < j:
            break
        print("*",end=" ")
print()

mlist=[1,2,3,1,"hey","you"]
mlist[1:3]="hello"
print(mlist)
mlist[1]="hello"
print(mlist)
mlist[6]=[3,4]
print(mlist)
mlist[8]=range(1,10)
print(mlist)
print("=========================1233423234")
print(list(mlist[8]))
l=list(mlist[8])
mlist[8]=list(mlist[8])
print(mlist[8])
print(l)
mlist.remove("l")
mlist.append("mm")
print(mlist)
mlist.pop(2)
mlist.insert(2,20)
print(mlist)
mlist.reverse()
print(mlist)
print("=========================55")

n=[1,4,3,78,6,4]
op=[x for x in n if x%2 == 0]
opp=[x for x in n if x&1 == 0]
print(op)
print(opp)
n.sort(reverse=True)
n.extend([2,3,1])
n.extend("rat")
n.extend([i for i in range(6)])
print(n)
d=[x**3 for x in range(10)]
print(d)
#or
g=[]
for x in range(2,5):
    for y in range(1,4):
        g.append(x**y)
print(g)
print("------------------------app")
names=["alice",'hjk',"jhkh"]
initials=[names[0] for name in names]
initial=[name[0] for name in names]
print(initials)
print(initial)
print("=======================")

for i in range(5):
    for j in range(5):
        if i < j:
            break
        print(j+1,end=" ")
    print(end="\n")

l1=[1,2,44]
l2=[4,5]
l3=l1 + l2
print(l3*2)

n=431
for i in range(2,n):
    if n%i == 0:
        print("not prime")
        break
    else:
        print("prime")
        break

v = 12345
o = 0
while v % (10**o) != v:
    o += 1
print(o)
rev_no=0
prev_digit = 0
for j in range(o):
    po10 = (10**(o-j-1))
    g = (v%(10**(j+1))-prev_digit)/10**j
    prev_digit = g
    rev_no += int(g)*po10
    print(int(g),po10)
print(rev_no)
y=[[1,2,3],[5,6,4],[4,6,7]]
print("[",end=" ")
for innrr in y:
    print(innrr)
print("]",end=" ")




my = [2,3,5,6,7]
my[4] = range(1,10)
print(my)
# my[5] = list(range(1,10))
my[3] = list(range(1,10))
my.remove(3)
my.append(11)
print(my)
my.insert(2,6)
my.pop(3)
myl=[3,5,7,4,9]
myl.sort(reverse=True)
myl.reverse()
myl.extend([2,5,6])
print(myl)
print(my)
l3 = my + myl
print(l3)

n=4567
h = 0
while n%(10**h) != n:

    h += 1
print(h) # length
print(n%(10**3))
print(n%(10**4))

r = [[3,4],[6,7],[8,9]]
for i in r:
    print(i)







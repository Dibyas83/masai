#d=int(float("10,5"))
myfloat = float("10.5")
m= "d"
#h=int(m)
e=int(myfloat)
print(e)
print("-----------------")
#print(my)
ch='f'
intvalue = ord(ch) - ord('8')#ascival ues
print(ord(ch))
print(ord("8"))
# print(ord(8))
print(intvalue)
print(ord(ch))
print(ord('8'))

print(True & False | True)
print(True & False & True)
print(bool(""))
print('----------------------------23')
print(bool("0"))
print(bool("1"))
print(bool(0))

a = 10
if(a>20):
    d=30
    g=60
    print(d,g)

r=66
if r>33:
    h=67
    r=67
else:
    i=68
    r=65
print(r)
print("====================================================88")
t=56
if (t%2 == 0):print("even")
   # print("again")
else:print("odd")

a = 11
b = 22
if (a == 11) & (b == 22):
    print("yes")

myno = 10
if(myno%2 == 0):
    if(myno % 3 == 0):
        print("div by 2 3")
    print("div by 2")


c=0
d,h = 11,23
if (d == 11):
    print("hhhhhhhhhhhh")
    if (d%2==1):
        c+=1
else:print("ggggg")
print(d,c)

d,h = 11,22
if (a == 11)  & (b == 22): print("aaaaa")

age = 13
elidibility = "eligible" if age >= 18 else "not eligible" #ternary operato
print(elidibility)
print(type(elidibility))
order = "pizza" if elidibility == "eligible" else "saga pakhal"
print(order)
eligibility="vote" if a >9 else "go home"
eligibility=True if a >9 else False
print(eligibility)

h=55
print("even" if (h%2 == 0) else "odd") # elif not allowed

for i in range(3,31,3):
    print(i)
for i in range(-10,3,2*2):
    print(i)

#b=4
#for i in range(-11,0,b/2): floating
for i in range(-11,0,b//2):
    print("u")



l = 1
for h in range(2,4,l):
    l = l + 2
for i in range(2, 100, l):

    print(i,end=" ")

m=0
while m<5:
    print(m)
    m += 1

for i in range(7):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 4:
        continue
    print(i)


for c in range(100):
    if c % 5 == 0:
        continue
    if c%3 == 0:
        continue
    print(c,end=" ")

print("==============================56")

for d in range(100):
    if (d%5 == 0) or (d%3 == 0):
        continue
    print(d,end=" ")


count =0
while count<5:
    print(count)
    count += 1



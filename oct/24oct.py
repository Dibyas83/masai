list=[10,20,30]
for x in range(1,4):
    for j in range(1,3):
        print(x*j,end=" ")
    print()

list=[10,20,30]
for x in range(1,4):
    for j in range(1,3):
        print(x*j)
    print()

list=[10,20,30]
for x in list:
    for j in range(1,3):
        print(x*j,end=" ")
    print()
print("-----------------------")
list=[10,20,30]
for x in range(1,4):
    for j in range(1,3):
        print(x+j,end=" ,")
    print()

list=[10,20,30]
for x in range(1,4):
    for j in range(1,3):
        print(x+j)
    print()

list=[10,20,30]
for x in range(1,4):
    for j in range(1,3):
        print(x+j)

print("-----------------------1")
list=[10,20,30]
for x in range(1,4):
    for j in range(1,3):
        print(x,j, end = ", ")
    print()

numbers=[5,10,15]
for num in numbers:
    for i in range(num//5):
        print(num,end=" ")
    print()
print("-------------------2")

numbers = [5,10,15]
for num in numbers:
    for i in range(1+ num//5):  # 0 0,1 0,1,2
        print(num*i,end=" ")
    print()
print("-------------------3")
numbers=[5,10,15]
for num in numbers:
    for _ in range(1,3):
        print(num*_,end=" ")
    print()
print("------------7")

numbers4=[10,20,30,40]
reversed_list = []
for i in range(len(numbers4)-1,-1,-1): # (4-1)3 to 0
    reversed_list.append(numbers4[i])
print(reversed_list)

#def print_characters(N, string):
N=6
string="ganesh"
for i in range(1,N+1):
    print(string[-i],end=" ")

print("------------666")


strg='hi'
sd=strg.upper()
strg =strg.replace("h","H")

print(strg[0])

s='pyt hon'
s[0:3]
print(s[:4])
print(s[3:5])
print(s[-1::-1])
print(s.count(""))

numbers=[5,10,15]
i=0
while(i < len(numbers)):
    print(numbers[i],end=" ")
    i += 1
    print(i,i < len(numbers))
print("---------------------------------------6666")

K=12
string="rhondarousey"
for i in range(1,K):
    if i%2==0:
        u=string[-i]
        print(u,end="")

print(("hello"+" "+"world. ")*2)
s="programming"
print(s[1], s[-2], s[3:6])
print(s.find("gr"))
print("--------------------------------------8")
for i in range(1,len(s),2):
    print(s[i],end=" ")

j=" \t hi \n"
g=j.strip()
print(g)
i=g.replace("h","p")
print(i)
b="he is a_liar ,he is good"
b.split()
print(b.split("_"))
print(b.split())
print(b)
print("____________________8")
print(" ".join(b))
print(" ".join(b.split()))
print(b.count(""))
print(len(b))
print(b.replace("he","she",2))


























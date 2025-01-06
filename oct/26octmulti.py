s="hello"
s1=s.replace("h","b")
print(s1)
s += " " "world"
print(s)

print("hello"[2:])
print(s.split()[1])

print(s[:5] + s[-4:-100:-1])
print(s[:5] + s[-4::-1])


vowels =["a","e","i","o","u"]
l="hello"
if l in vowels:
    print("l has vowels")
else:
    print("consonants")
print(len(l))
di =s1.replace("b","y")
print(di)

di += " " "tyu" # new assignment not modification
print(di)
print(di[1:10])
print(di.split()[0])
print(di.split()[1])
print("----------------============================8")
fg="the fight begins"
print(fg[:2] + fg[-4::-1])# modifier
print(fg.split()[1])
print(fg)
print(fg[::-1]) # 3rd col is step,-1 is start from end,+1 means start from start
print(fg[::1])
name = "Alice"
age = 25.56789
print(f"my name is{name} my age is{age}")
print("my name is %s and i am %d years ," %(name,age))
print("my name is {} and i am {} years ," .format(name,age))
print("my name is %s and i am %.2f years ," %(name,age))
print("my name is %s and i am %10f years ," %(name,age))  # 10f gives one space
print("my name is %s and i am %1000f years \n," %(name,age)) #1000 gives 3 spaces
print("my name is %s and i am %-1000f years ," %(name,age)) #1000 gives 3 spaces after no
# multidimensional list where elements themselves as list
shape:(4,3,2) # row 4,col 3,depth 2
#2d list  l2d=
l2d =[[1,2],[3,4],[7,8]]
print(l2d[0][1])
print(l2d[1][0])
print(l2d[2])
for row in l2d:
    print(row,end=" ")
    for element in row:
        print(element,end=" ")
print("--------------------------------------------------------------------7")

e2d =[[1,2],[3,4],[7,8]]
for i in range(len(e2d)):   # 0-2
    for j in range(len(e2d[i])): # length = 2 of [1,2] (0-1)
        if i == j:
            print(e2d[i][j],end=" \n") # matches only at 0 & 1 ie 1 & 4
print("--------------------------------================")
# 3d list
di = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(di[0])
print(di[0][0])
print(di[0][0][0])
di.append([10,11])
di.append([14,21])
print(di[2][1])
di[1].append([7,4])
di[2].pop(0)
print(di)
matrix1 = [[i for i in range(3)] for j in range(4)]
matrix2 = [[i + j for i in range(3)] for j in range(4)] # when j=0[0,1] when j=1[0+1,1+1}
matrix3 = [[i + j for i in range(3)] for j in range(3)]
matrix4 = [[i + j for i in range(3)] for j in range(0)]
print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)
print("-------------------6")

mat = []
for j in range(4):
    mat.append([j])
    for i in range(3):
        mat.append([i])

        print(mat)
    print(i+j)
#print(mat)
print("----------------------------------=============================123")


def greet(name="guest"):
    print(f"hello,{name}")
    print(f"hello {name}")

print(greet("paban"))


def add(x,y):
    return x+y
print(add(7,8))


def add_sub(x,y):
    return x+y,x-y
print(add_sub(7,8))

lamda_add = lambda x,y:x+y
print(lamda_add(2,1))
lambda_dist = lambda x1,y1,x2,y2:((x2-x1)**2 + (y2-y1)**2)**0.5
print(lambda_dist(3,4,5,6))
lambda_greet = lambda name1: f"hello {name1}"
print(lambda_greet("rt"))
fa = lambda t,r:t  * r
print(fa(4,6))
multiply =lambda x:x*5
print(multiply(5))
print("------------------------------------123")
greet = lambda name:f"hello {name}"
print(greet("ram"))
l="785567"
print(len(l))
print(l.count(""))

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a.append([5, 10, 15, 20, 25])
print(a)

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[0].extend([12, 14, 16, 18])
print(a)

# Reversing a sublist

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[2].reverse()
print(a)










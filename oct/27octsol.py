g=4
count = 0
for i in range(1,4):
    for j in range(1,4):
        print(count,end=" ")
        count += 1
    print()

g=4
count = 0
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")

    print()



g = 4
count = 0
for i in range(5):
    for j in range(5):
        if j<i:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print("------------------------2")
g=4
count = 0
for i in range(1,5):
    for j in range(1,i+1):

        print("*",end=" ")
    print()
print("-----------------------------------3")

g=4
for i in range(1,g+1):
    for j in range(1,g+1):
        if j == 1:
            print("*", end=" ")
        if i == 1 or i == g :
            print("*",end=" ")

    print()
"""
 else:
    print("*",end="")
     break
"""
g=6
for i in range(1,g+1):
    for j in range(1,g+1):
        if j == 1 or 2:
            print("*",end=" ")
        else:
            print("*",end=" ")
            break

    print()



print("==============1")
g = 4
for i in range(1,g+1):
    for j in range(1,g+1):
        if i == g:

            print("*",end=" ")
        elif  j == 1 or j == g:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("============2")
g = 4
for i in range(0, g + 1):
    for j in range(0, g + 1-i):
        print("*", end=" ")
    print()
print("=============")
g = 4
for i in range(g,0,-1):
    for j in range(1, g + 1):
        if j <= i:
            if j == g:
                print("*",end="")
            else:
                print("*", end="_")
        else:
            if j == g:
                print("_",end="")
            else:
                print("_",end=" ")
    print()




print("==========///////////")
g = 4
for i in range(g):
    for j in range(g):
        if j <= i:
            if j % 2 == 0:
                print("1",end=" ")
            else:
                print("0", end=" ")
    print()

print("=================")
N=5
for i in range(1,N):
    bag = " "
    for j in range(1,N*4+1):
        if i == j or j == N*2+i:
            bag += "\\"
        else:
            bag += " "
print(bag.rstrip())

l=2
str2 = "abcd"
for i in str2:
    print(i*l)
    l += 1


















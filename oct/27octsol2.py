
for k in range(1,5):
    for l in range(1,5):
        print(l,end=" ")

for k in range(1,5):
    for l in range(1,5):
        print(k,l,end=" ")

for k in range(1,5):
    for l in range(1,5):
        print(l,end=" ")
    print()
print("================")
dont = 1
for g in range(1,4):
    for h in range(1,4):
        print(dont,end=" ")
        dont += 1
    print()

for k in range(1,5):
    for l in range(1,k+1):
        print("*",end="")
    print()

for e in range(1,5):
    for r in range(1,5):
        if e == 1 or e == 4:
            print("*",end=" ")
        else:
            print("*",end=" ")
            break
    print()

for e in range(1,5):
    for r in range(1,5):
        if e == 4:
            print("*",end=" ")
        elif r == 1 or r == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

N=5
for row in range(N,0,-1):
    for col in range(1, N+1):
        if col <= row:
            if col == N:
                print("*", end="")
            else:
                print("*", end=" ")
        else:
            if col == N:
                print(" ", end="")
            else:
                print(" ", end=" ")

    print()
print("----------------------666")
s = 6
arr =[1,2,3,4,5,6]
for i in range(s-1,-1,-1):
    print(arr[i],end=" ")


B=5
for t in range(B):
    for y in range(B):
        if y <= t:
            if y%2 == 0:
                print("1",end=" ")
            else:
                print("0",end=" ")
    print()

if 0%2 == 0:
    print(1)

o=7
for row in range(1,o+1):
    for col in range(1,o+1):
        if row == 1 or row == o:
            print("*",end=" ")
        elif col == o - row + 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


u = 5
for row in range(1,u+1):
    bag = ""
    for col in range(1,u*4+1):

        if row == col or col == u*2+row:
            bag += "\\"
        elif col == u*2-row+1:
            bag += "/"
        elif col == u*4-row+1:
            bag += "/"
        else:
            bag += " "


    print(bag.rstrip())


#5




















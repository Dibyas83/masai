for i in range(5,1,-1):
    count = 1
    for j in range(i,-1,-1):
        print(count ,end="")
        count +=1
    print()


for i in range(6,1,-1):
    for j in range(1,i+i):
        print("*", end=" ")
    print()

for i in range(5,1,-1):
    for j in range(i,-1,-1):
        print([i],[j] ,end="")
    print()


for i in range(5):
    for j in range(5):
        # print(i%j,end="")
        print([i],[j],end="")
    print()
print("===============2")
for i in range(5):
    for j in range(5):
        # print(i%j,end="")
        print(i*j,end="")
    print()
print("=================")
for i in range(5):
    for j in range(4,-1,-1):
        # print(i%j,end="")
        print(i*j,end="")
    print()
print("===================2")

for i in range(4,-1,-1):
    for j in range(4,-1,-1):
        # print(i%j,end="")
        print(i*j,end="")
    print()

print("/////////////////////")
count = 1
for i in range(4,-1,-1):
    for j in range(4,-1,-1):
        # print(i%j,end="")
        print(j*count,end="")
        count += 1
    print()
print("=====================1")
for i in range(1,5):
    for j in range(5,10):
        # print(i%j,end="")
        print(i*j,end="")
        print([i],[j],end="")
    print()







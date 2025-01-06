for i in range(4,6):
    for j in range(1,11):
        if j%2==0:

        #print(i,"*",j,"=",i*j*"*")
            print(i*j*"*")
    print()

#q = "*"
#for i in range(1,3):
 #   for q in range(1,11):
  #      print(i,"*",q,"=",i*q)
   #     print("i*q","=",i*"q")
    #print()
print("----------------------------1")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("========================88")
for i in range(1,6):
    for j in range(1,6-i+1):
        print("*",end=" ")
    print()
print("===================")
for i in range(5,0,-1):
    for j in range(1,i+1):

        print("*",end=" ") # 5(1 to 5(5+1))  ,4(1 to 4(4+1=5)
    print()


list=[1,"dhgg","fghf",45]
print(list[2])
list.append(56)
print(list)

N=3
ct = 0
for h in range(1,N+1):
    for j in range(ct+1,ct+N+1):
        print(j,end=" ")
    ct += 1
    print()
print("========================")
N=3
ct = 0
for h in range(1,N+1):
    for j in range(ct+1,ct+N+1):
        print(j,end=" ")
        ct += 1
    print()











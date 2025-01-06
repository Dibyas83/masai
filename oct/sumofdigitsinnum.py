sum =1
N = 3
X = int(input("entr ; ",))
next = X
for i in range(1,N):
    if i == 1:

        sum += X
    else:

        next *= X
        sum += next
print(sum)



g = 34567
sum = 0
while g>0:
    sum +=g%10
    g =g//10
print(sum)
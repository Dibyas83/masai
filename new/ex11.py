count =0
while count<5:
    print("come".format(count))
    count +=1
else:
    print("or")
print("go")


for letter in 'python':
    if letter == 'h' :
        break
    print("curremt letter ;",letter)
print("bye")


# while:
   #  while:

# while:
 #   if

j=0
print("pos") if j >=0 else print("neg")

e=1
while True:
    e += 1
    print("looping",e)
    if e >10:
        break
    e += 1
left=2
right=99
key=6
count=0
if left&right >1  & key <10000:
    for i in range(left,right+1):
        if i%key == 0:
            print("count=",count)
            count +=1


        print(count)

for i in range(4):
    print("in",i,"th iteration of outer loop")
    for dg in range(4):
        print("in", dg , "th iteration of inner loop")
        if dg >2:
            break
        print(i,dg)

for q in range(5):

    for w in range(1):

        if(q==w): break
        print(q,w)


for i in range(4):
    for j in range(5):
        if j >i:
            break
        print("*", end=" ")
    print()


for i in range(4):
    for j in range(5):
        if j >i:
            break
        print(j+1, end=" ")
    print(end= "\n")

numbers=[1,2,3,4,5]
result=[]
for m in numbers:
    for k in numbers:
        result.append(m*k)
print(result)









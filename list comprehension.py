
l1 = ["a","b","c","d","e","f","g"]
l3=[1,3,46,33,88]
l2 = []
for i in l3:
    if i > 44:

        l2.append(i)
print(l1,"\n",l2)

l4 = [i for i in l3 if i >2]
print(l4)

mul1 = 1
for i in l3:
    mul1 *= i
print(mul1)











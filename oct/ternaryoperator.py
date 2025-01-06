x=0
print(("pos") if x > 0 else print("neg or o"))
i=0
while True:
    print("looping",i)
    if x > 10:
        break
    x += 1
    i+=1
print(x)

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i,j)
















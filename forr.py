
v=1
for i in range(0,10,2):
    print(i,"i")
    v*=2
    for j in range(0,100,v):

        print(i,j,v,"i" "j" "v")

"""
i changes but no of steps in range adjusts and remain same.
steps can only change inside range parenthesis

"""
print("--------------------------")


for u in range(0,10,2):
    start = 1
    stop = 100
    step = 1

    i = start
    while i < stop:
        print(i)
        i += step
        step *= 2









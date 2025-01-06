N = int(input())
X = int(input())
coun = 0
age = []
for i in range(N):

    age += input()

    if int(age[i] )>= X:
        coun += 1
print(coun)
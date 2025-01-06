set1 = {4,5,6,8,9}


set2 = {4,5,1,6,7,3}


set1 = list(set1)
set2 = list(set2)
set1.extend(set2)
set1 = set(set1)
set1 = list(set1)
print(set1)
for i in range(len(set1)):
    print(set1[i], end="")
print("-------------------------------------")

a = [1, 2, 3]
b = [1, 5, 6]

# Initialize an empty list to store the merged elements
res = []


for val in a:
    res.append(val)



for val in b:
    res.append(val)

print(res)

a = [1, 2, 3]
b = [4, 3, 6]

# Use list comprehension to create a new merged list
c = [item for item in a] + [item for item in b]

print(c)
# print(stream[i-1])


def merge1(n, A, m, B):

    u = []
    A1 = list(A)
    B1 = list(B)
    u = [item for item in A1] + [item for item in B1]
    d = set(u)
    v = list(d)
    print(" ".join(map(str,v)))
n=4
m=4
A =[1,2,3,6]
B = [4,5,7,8]
merge1(n,A,m,B)
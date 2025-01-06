x=5
y=10
print(x > y or x == 5)
print(len("Hello World"))
print(bool(0))
z=2.456
print(int(z))
list_m=[1,2,3]
list_m.insert(1,4)
print(list_m)
print(len(list_m))
print((list_m))

mystr = "Hello world"
mystr = mystr.split(" ")
for wo in mystr:
    bag = ""
    for i in range(len(wo)-1,-1,-1):
        bag += wo[i]
    print(bag,end=" ")

arr1 =[4,5,6,5,8]
arr2 = [5,6,7,3,9]
n=5
for i in range(n):
    for j in range(n):
        if arr1[i] == arr2[j]:
            print(arr2[j])

bag = ""
v="aeiou"
s="adefghii"
for i in range(n):
    for j in v:
        if s[i] != j:
            bag += s[i]
            if s[i] == j & s[i+1] != j:
                bag += s[i+i]
                if s[i] == j & s[i+1] == j:
                    bag += s[i]
                    print(bag)
















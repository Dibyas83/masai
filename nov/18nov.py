zen ="ahmad"
for char in zen:
    if char in "aeiou":
        print(char,end=' ')

no=(34,32,45,56,64,67,54,74,23)
total = 0
for nom in no:
    if nom%2 == 0:
        print(nom,end=" ")
    total += nom
print(total)


i = {10:"ten",20:"twenty",30:"th"} # dictionary key:value pairs
for pairs in i:

    print(i[pairs])
    print(pairs)
    print(pairs,":",i[pairs])

for count in range(2):
    print("iteration no. {}".format(count))
else:
    print(2)
print(3)

for i in ["iit","mandi"]:
    print(i)
    break
else:
    print("loop")
print("====================")
#for i in range (1,["iit","mandi","rear"]):
 #   print(i)

#else:
 #   print("loop")

for i in ["iit","mandi"]:
    print(i)

else:
    print("loop")

#range is object
#pass = ...
count =0
while count<=8:
    count += 1
    print("jk")
print("end")
print("=====================")
for letter in "python":
    if letter == "h":
        break
    print(letter,end="")
print("\tgood")


n=2
while(n<25):
    j = 2
    while(j <= (n/j)):
        print(j)
        print(n%j)
        if not (n%j):break
        j=j+1
    if (j>n/j):print("special")
    n=n+1
print("bye")






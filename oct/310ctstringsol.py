string1 = "angryd"
N = len(string1)
for i in range(N-1,-1,-1):
    print(string1[i],end="")
    if i%2 == 0:
        print("*",end="")
print("-----------------------------1")
st = string1[-1::-1]
print(st)

a = " i am gonna sleep"
b =a.isalpha()
count = 0
to_avoid ='aeiouAEIOU'
for char in a:
    if char.isalpha() and char not  in to_avoid:
        count += 1
print(count)
print("===========")
str12 ="sky"
bag = ""
N= len(str12)
for i in range(N-1,-1,-1):
    bag += str12[i] # palendrome  is eq to rev
print(bag)
if str12 == bag:

    print("yes")
else:
    print("n")

r = 4205678
g = str(r)
if '420' in g:
    print("caugh")










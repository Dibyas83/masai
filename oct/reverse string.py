

f= [3,4,2,7,1]
u = len(f)
for i in range(u-1,-1,-1):
    print(f[i],end=" ")



mystr = "Hello"
bag = ""
for i in range(len(mystr)-1,-1,-1):
    bag += mystr[i]
print(bag)
#return bag

print("-----------------1")
s="fuj io fgh as"
list1 = ""
rev = ""
for i in s:
    if i != " ":
        list1 += i
        print(list1)
    else: # when space comes
        rev += list1[::-1] # reverse the stored string
        rev += " "
        list1 = ""
rev +=list1[::-1] # for the last no
print(rev)
print("-------------------------------------11")

u="asfg hj kl"
u = u[::-1]
print(u)


st = "all of world"


def rev_str(st):
    print(" ".join(word[::-1] for word in st.split(" ")))


print(rev_str(st))

print("------------------")






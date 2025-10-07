
n= int(input())
stri = input()
v = "aeiou"
c= 0
for i in range(0,n-1):
    if stri[i] in v:
        if stri[i+1] not in v:
            c += 1
print(c)












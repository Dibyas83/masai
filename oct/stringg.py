stream="abbcd"
count = ""
c=0
for i in range(len(stream)):

    for j in stream:

        if stream[i] == j and c < 2:
            c += 1
            count += stream[i]
        elif c == 2:
            count += "-1"
        else:
            count += stream[i-1]
    print(count)

test_string ="fgjfjrutur"

eq = "="
add_string = "grtutrirtu"
# add_string = [x for x in range(1,11)]

# Using join()
# adding one string to another
for i in range(len(test_string)):
    res = "=".join((test_string[i], add_string[i]))
    print(res,end=" ")

# print result
print("The concatenated string is : " + res)

ans = "".join((res,"!"))

#print after adding character
print(ans)


def multi(res=""):
    res += "q"
    res = " ".join((res, "a"))
    return res

print(multi())
print(multi())

# string is a palindrome if ada rev = ada

s= "aasdfgertiii"
v = "aeiou"
newsr = ""
flag =False
for i in range(1,11):
    if s[i]  in v:
        for j in range(i, 11):
            if s[j + 1] in v:
                flag = True
            else:
                flag = False
                break
    if flag == True:
        newsr += s[i]+s[i+1]

    if s[i] not in v:
        newsr += s[i]
print(newsr)


g="aaaaaa"
g=g[0:5]
print(g)







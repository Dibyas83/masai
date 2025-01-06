
s= "aasdfgertiii"
v = "aeiou"
newsr = ""
for i in range(1,11):
    if s[i] in v:
        for j in range(i, 11):
            while s[j + 1] in v:
                j=j+1
                pass
            newsr += s[i]
    else:
        newsr += s[i]




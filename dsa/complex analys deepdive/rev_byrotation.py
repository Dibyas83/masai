str1 = input()
str2 = input()
flag = False
for i in range(len(str1)):
    str1 = str1[-1] + str1[0:-1]
    if str1 == str2:
        flag = True
if flag:
    print("yes")
else:
    print("No")










myeq = "(2+[3+4])"
open_brack = ["(","[","{"]
cl_brack = [")","]","}"]
liopbrack = []
#traverse letters in myeq
for letter in myeq:
    if letter in open_brack:
        liopbrack.append(letter)
        print(liopbrack)
    elif letter in cl_brack:
        v = liopbrack.pop() # = liopbrack.pop
        print("----------------------")
        print(v)
        print(liopbrack)
        if open_brack.index(v) == cl_brack.index(letter):
            continue
        else:
            print("unbalanced equation")
    else:pass # if no is encountered
if len(liopbrack) == 0:
    print(liopbrack)
    print("balanced")


j =[4,5,6,7,8,4,5]
j.pop()
k=j.pop()

print(j)

mydict = {"(":")","[":"]","{":"]"}
myeqn = "(2+3)"
openbr =""
for letter in myeqn:
    if letter in mydict.keys():
        openbr = letter
    elif letter in mydict.values():
        if mydict[openbr] == letter:
            print("balanced")



























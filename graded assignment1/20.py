#m =([i+j for j in range(2)] for i in range(2))
#print(m[][])

n=5
str = "momon"
if str[::] == str[-1::-1]:
    print(str[::])
    print("y")
else:
    print("no")


#for x in range(9):
tot = [0]
numbers =[2,3,4,7,8,9,22,14,45,32,24,16]
result = list(map(lambda x: x**2,filter(lambda x:x%2 == 0 and x>5,numbers)))
tot += result
print(tot)
print("---------------------------------------------")
print(tot.sort)
print("--------------------------------================")
# rint(tot.sort(-1))
print("-=================================-")
print(sorted(tot))

let = "ashello worldlo"
print(let.strip("as"))
print(let.strip("lo"))
print(let.strip("lo"))

m=10
name = aa if m > 10 else "pavan" if m<15 else "gh"
print(name)
flag = False
arr=[2,3,4,5,6]
c = 0
n=5
for i in range(n):
    for j in range(n):
        if arr[i] == 2*arr[j]:
            if arr[i] != 0:
                c += 1
                flag = True
if flag == True:print("Yes")
else:print("no")
print(c)


myDict = {"name": "John", "country": "Norway"}
mySeparator = " TEST "

x = mySeparator.join(myDict)
print(x)


def myfunc(a, b):
  return a + b


x = map(myfunc, (('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
print(x)

arr=(12,15,18,16,11,14,5,10,14)
targ = 30
cout = 0
seen = {}
for num in arr:
    compliment = targ - num
    if compliment in seen:
        cout += seen[compliment]
        print(seen[compliment])
    if num in seen:
        seen[num] += 1
        print(seen[num])
    else:
        seen[num]= 1
print(cout)
print("-------------111111111111")

cot = 0
n =len(arr)
for i in range(n):
    if i ==0 and arr[i]> arr[i+1]:
        cot += 1
    if i == n-1 and arr[i] > arr[i-1]:
        cot += 1
    elif 0 < i<n-1 and arr[i] > arr[i-1] and arr[i] >arr[i+1]:
        cot += 1
print(cot)

resul = []
ct = 1
s="aaabbccccad"
m = len(s)
for i in range(1,m):
    if s[i] == s[i-1]:
        ct += 1
    else:
        resul.append(f"{s[i-1]}{ct}")
        ct = 1
#resul.append(f"{s[-1]}{ct}")
resul.append(f"{s[i]}{ct}")
print("".join(resul))
print("--------------------------22222")

S= "i love ndia lol"
li = S.split(" ")
cnt = 0
n = len(li)
for i in range(n):
    for j in range(n-1):
        if li[i][0] == li[j+1][0]:

            cnt += 1
            print(li[i],cnt)
            break
        else:
            cnt = cnt

print(li[i][0])
print(li[j+1][0])

print(n)
print("--------3333333333333333------------")
sentence = "A Transformation in education"
words = []
word = []
for char in sentence:
    if char == ' ':
        if word:
            words.append("".join(word))
            word = []

        else:
            word.append(char)
if word:
    words.append("".join(word))
reversed_sentence = []
while words:

    reversed_sentence.append(words.pop())
print(" ".join(reversed_sentence))





s= "abcdefghi"
def new_string(s):
    l = len(s)
    if l % 2 == 0:
        mid = l // 2
        low = 0
        high = l // 2 - 1
        str1 = s[high::-1]
        str2 = s[-1:-(mid + 1):-1]

        print(str1 + str2)
    else:
        mid = l // 2
        low = 0
        high = l // 2 - 1
        str1 = s[high::-1]
        str2 = s[-1:-(mid + 1):-1]
        str3 = s[mid]
        print(str1 + str3 + str2)

new_string("asdfghj")


print("---------------------------22")


def new_string(S):
    l = len(S)
    if l % 2 == 0:
        mid = l // 2
        low = 0
        high = l // 2 - 1
        str1 = S[high::-1]
        str2 = S[-1:-(mid + 1):-1]
        print(str1 + str2)
    else:
        mid = l // 2
        low = 0
        high = l // 2 - 1
        str1 = S[high::-1]
        str2 = S[-1:-(mid + 1):-1]
        str3 = S[mid]
        print(str1 + str3 + str2)
S="gsrdhdhdjd"
new_string(S)

print("---------------------3")
S = input()
l = len(S)
if l % 2 == 0:
    mid = l // 2
    low = 0
    high = l // 2 - 1
    str1 = S[high::-1]
    str2 = S[-1:-(mid + 1):-1]
    print(str1 + str2)
else:
    mid = l // 2
    low = 0
    high = l // 2 - 1
    str1 = S[high::-1]
    str2 = S[-1:-(mid + 1):-1]
    str3 = S[mid]
    print(str1 + str3 + str2)



s1 ="asdfg"
l = len(s1)
s2 ="fgaid"

for i in range(l):
    if s1 == s2[i:l:1] + s2[0:i:1]:
        print("Yes")
        break
else:
    print("No")


# def solve(N,M,arr):
arr = [[1,2,3],[4,5,6],[7,8,9]]
N = 3
M = 3
sum = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] % 2 != 0:
            # print(arr[i][j])

            sum += arr[i][j]
    print(sum)
    sum = 0
print("--------------------13")
N = 26
a = [i for i in range(30,30+N)]
b = [chr(j) for j in range(97,97+N)]
print(a)
print(b)
res = map(lambda y, x: y + "=" + str(x), b, a)
print(list(res))
new = " ".join(res)
p = list(new)
print(p)


"""

ty= [i for i in range(30,30+N)]
yu = [chr(j) for j in range(97,97+N)]
m ='-'.join(map(ty,yu))

"""
print("-----------------14")

sentence = "a ass hole"
news= sentence.split(" ")

print(" ".join(news[-1::-1]))



n = int(input())
li = []
for i in range(n):
    li.append(input())
print(li)



m = int(input())
li = [input() for j in range(m)]
we = 0
for i in range(m-1):
    we += int(li[i])

print(we*int(li[m-1]) + m)

t = int(input())
for c in range(t):

    n = int(input())
    A = [input() for j in range(n)]
    we = 0
    for i in range(n - 1):
        we += int(A[i])
    print(we * int(A[n - 1]) + n)




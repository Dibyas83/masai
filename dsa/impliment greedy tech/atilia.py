
def solve(n,st,dict):
    mx = float("-inf")
    for i in range(n):
        if dict[st[i]] > mx:
            mx = dict[st[i]]
    print(mx)

def inp():
    dict ={}
    char = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(char)):
        dict[char[i]] = i + 1
    print(dict)

    t = int(input())
    for _ in range(t):
        n = int(input())
        st = str(input())
        print(dict[st[-1]]) # st -1 is last letter "g" whose value in dict is 7
        print(dict["z"])
        solve(n,st,dict)
inp()

















"""

5
1
a
4
down
11
masaischool
3
bcf
5
zzzzz


----------------
1
23
19
6
26
"""
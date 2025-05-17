
def gen_sub(s,ans,index):
    if ans:
        print("".join(ans))
    if index == len(s):
        return
    for i in range(index,len(s)): # index i=0,0+1,(0+1)+1
        ans.append(s[i])
        print(ans)
        gen_sub(s,ans, i + 2) # from 0-4 then i+1=5=len ,return to prev =asdf,pop f
        # and i is 3+1=4 append g.after this seq finishes it start from 0+1
        ans.pop()

def inpt():
    n = int(input())
    s = input()
    ans = []
    gen_sub(s,ans,0)
inpt()














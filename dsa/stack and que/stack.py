


def solve(s):


    dic = {
        ')': '(',
        '}': '{'
    }
    stk = []
    for char in s:
        if char == "(" or char == "{":
            stk.append(char)
        else:
            if len(stk):

                if dic[char] == stk[-1] or dic[char] == stk[-1]:
                    stk.pop()
            else:
                return "n"
    if len(stk):
        return "n"
    return "yes"

def inpt():
    n = int(input())
    for i in range(n):
        s = input()
        a = solve(s)
        print(a)
inpt()

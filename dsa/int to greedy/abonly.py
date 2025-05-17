

def solve(s):
    n = list(s)
    for  i in range(len(n)):
        if i == len(n) - 1:
            if n[i] == "?":
                if n[i-1] == "a":
                    n[i] = "b"
                else:
                    n[i] ="a"
            else:
                n[i] = n[i]
        else:
            if n[i] == "?":
                if n[i+1]=="a" or n[i-1] == "a":
                    n[i] = "b"
                else:
                    n[i] = "a"
            else:
                n[i] = n[i]
    print(*n,sep = "")

s= input()
solve(s)






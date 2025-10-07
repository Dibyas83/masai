
def power(n, r, ans):
    if n == 0:
        return ans
    ans = ans * r
    return power(n - 1, r, ans)


def main():
    t = int(input())
    for _ in range(t):

        a,b = list(map(int,input().split(" ")))
        print(power(a,b,1)) # initial value of ans

if __name__== "__main__":
    main()




def tothepow(n,base):
    if n == 0:
        return 1

    return base * tothepow(n-1, base)

print(tothepow(4,2))




def power(n,r,expo):
    if n == 0:
        return expo
    expo = expo*r
    return power(n-1,r,expo)


def main():
    t = int(input())
    for _ in range(t):

        a,b = list(map(int,input().split(" ")))
        print(power(a,b,1)) # initial value of expo

if __name__== "__main__":
    main()










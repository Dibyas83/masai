
def gcd(a,b):
    if b != 0:
        return gcd(b,a%b) # 5,7%5=2 -> 2,5%2=1 ->1,1
    return a  # if b =0 and b < a

def main():
    t = int(input())
    for _ in range(t):

        a,b = list(map(int,input().split(" ")))
        print(gcd(a,b))

if __name__== "__main__":
    main()

def gcd2(a,b):
    if a%b != 0:
        return 1
    else:
        if a>b:
            if a != 0:
                return gcd(a%b,b) # 5,7%5=2 -> 2,5%2=1 ->1,1

        return b   # if b =0 and b < a

print(gcd2(18,3))
print(gcd2(9,2))
print(gcd2(16,8))
print(gcd(50,25))
print(gcd(36,18))

#5,13%5=3 -> 3,5%3=2 ->2,3%2 ->1,2%1 -> 1,1
# 10,20%10=0 ->0,10
#
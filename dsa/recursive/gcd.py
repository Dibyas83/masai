
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


# print(2%5)  == 2
print(5%3)

#5,13%5=3 -> 3,5%3=2 ->2,3%2 ->1,2%1 -> 1,1
# 10,20%10=0 ->0,10
#
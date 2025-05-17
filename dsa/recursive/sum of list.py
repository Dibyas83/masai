

def sumlistele(arr,n):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        return arr[n-1] + sumlistele(arr[:n-1],n-1)

n = int(input())
arr = list(map(int,input().split(" ")))
print(sumlistele(arr,n))

#---------
print("-----------------")

def solve(a):
    return sum(a)
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split(" ")))
        print(solve(a))

if __name__== "__main__":
    main()






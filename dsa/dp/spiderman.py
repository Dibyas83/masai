
def jump(n,arre):
    prev1 = 0   # stores prev values
    prev2 = 0
    for i in range(1,n):
        take1 = prev1 + abs(arre[i] - arre[i-1])
        take2 = float("inf")
        if i > 1:
            take2 = prev2 + abs(arre[i] - arre[i-2])
        curr = min(take1,take2)
        prev2 = prev1
        prev1 =curr
    return prev1

def inpt():
    n = int(input())
    arre = list(map(int,input().strip().split(" ")))
    #dp = [float("inf")] * (n+1)
    print(jump(n,arre))

inpt()















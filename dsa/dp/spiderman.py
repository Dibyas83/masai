
def jump(n,arre):
    prev1 = 0   # stores prev values
    prev2 = 0
    for i in range(1,n):
        take1 = prev1 + abs(arre[i] - arre[i-1])
        take2 = float("inf")
        print(prev1 ,take1,"p1"+"t1",end=" ")
        if i > 1:
            take2 = prev2 + abs(arre[i] - arre[i-2])

            print(prev2 ,take2,"p2"+"t2",end=" ")
        curr = min(take1,take2)
        print(curr,"c")
        prev2 = prev1
        prev1 =curr
        print(prev1,end=" ")
    return prev1

def inpt():
    n = int(input())
    arre = list(map(int,input().strip().split(" ")))
    #dp = [float("inf")] * (n+1)
    print(jump(n,arre))

inpt()

#-------------
def fly(n1,arr):
    prev11 = 0
    prev22 = 0
    for i in range(1,n1):
        takeone = prev11 + abs(arr[i] - arr[i-1])
        taketwo = float('inf')
        if i>1:
            taketwo = prev22 + abs(arr[i] - arr[i-2])

        curri = min(takeone,taketwo)
        prev22 = prev11
        prev11 = curri
    return prev11

def inpt1():
    n1 = int(input())
    arr = list(map(int,input().split(" ")))
    #dp = [float('inf')]* (n1+1)
    print(fly(n1,arr))
inpt1()















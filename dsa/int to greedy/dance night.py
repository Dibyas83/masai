from sys import flags

t = int(input())
for i in range(t):
    m,n =map(int,input().split(" "))
    li = sorted(list(map(int,input().split(" "))))
    l2 = sorted(list(map(int,input().split(" "))))
    print(li)
    print(l2)
    flag  = False
    if m > n:
        print("no")
    else:
        for i in range(m):
            if li[i] > l2[i]:
                flag = True
                print(flag,"flag")
                continue
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")










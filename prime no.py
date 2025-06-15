
n=int(input())
if n<=1:
    print("not")
else:
    for i in range(2,n): # if n+1 it will divide and give ans yes
        if n%i == 0:
            print("not")
            break

    else:
        print("prime")








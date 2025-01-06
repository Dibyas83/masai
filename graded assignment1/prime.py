def check_prime(num):
    count = 0
    for i in range(1,num +1):
        if num%i == 1:
            count += 1
    if count == 2:
        return  True
    return False


def solve(N,M,arr):
    count =0
    for i in range(N):
        for j in range(M):
            if check_prime(arr[i][j]) == True:
                count += 1
    print(count)


# rev prime

d = int(input("entr ; ",))
if d == 0 or d == 1:
    print("not prime")
elif d>1:
    for i in range(2,d): # or d**0.5 + 1
        if d%i == 0:
            print("not")
            break
    else:
        print("prime")










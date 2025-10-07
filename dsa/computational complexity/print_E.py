
n = int(input())
for i in range(n):
    if i == 0 or i == n-1:
        print("* " * n)
    elif i == n//2:  # n/2 wrong == 1
        print("*" * n)
    else:
        print("*")


















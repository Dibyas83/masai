

def big_matrix():
    n, m = map(int,input().split(" "))

    A = []
    B = []
    sum1 = 0
    sum2 = 0
    for i in range(n):
        Ar = list(map(int, input().split(" ")))
        A.append(Ar)
    for a in range(n):
        for b in range(m):
            sum1 += A[a][b]
    i, j = map(int, input().split(" "))
    for x in range(i):
        Br = list(map(int, input().split(" ")))
        B.append(Br)
    for r in range(i):
        for t in range(j):
            sum2 += B[r][t]
    if sum1 > sum2:
        print(sum1)
    else:
        print(sum2)

big_matrix()
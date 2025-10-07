def merge1(n,A,m,B):
    c = []
    for i in range(1, n):
        for j in range(1, m):
            if A[i - 1] < B[j - 1]:
                c.append(A[i - 1])
                if A[i] < B[j - 1]:
                    c.append(A[i])
                else:
                    c.append(B[j - 1])
            else:
                c.append(B[j - 1])
                if B[j] < A[i - 1]  and B[j] < A[j]:

                    c.append(B[j])
                else:
                    c.append(A[i - 1])


def merge1(n, A, m, B):
    c = []
    A = [1,3,55,77]
    B = [2,4,6,9]
    n = len(A)
    m = len(B)
    for i in range(1, n):
        for j in range(1, m+1):
            if A[i - 1] < B[j - 1]:
                c.append(A[i - 1])
                if A[i] < B[j-1]:
                    c.append(A[i])
                else:
                    c.append(B[j-1])

            else:
                c.append(B[j - 1])
                if B[j] < A[i]:
                    c.append(B[j])
                else:
                    c.append(A[i])

    d = set(c)
    v = list(d)
    print(" ".join(map(str,v)))

n=4
A =[11,44,77,99]
m = 4
B = [22,55,77,99]
merge1(4,A,4,B)


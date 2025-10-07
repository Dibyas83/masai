arrA = [5, 3, 4, 2, 6]
ct = [6,4]
print(arrA[arrA.index(ct[-1])-1])


def trnsform_arr():
    T = int(input())

    for _ in range(T):
        res =[]
        N = int(input())
        A = list(map(int, input().split(" ")))
        e = min(A)
        for x in A:
            if x == e:
                res.append(-1)
            else:
                res.append(x)

        result1 = [-1 ]
        # print(result1)
        print(" ".join(map(str, res)))




trnsform_arr()














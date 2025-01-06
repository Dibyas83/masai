def distinct():
    N = int(input())
    A = list(input().split(" "))
    K = int(input())
    u = False
    ct = 0

    if len(A) <= K:
        for ele in A:

            for x in ele:
                ele.remove(x)
                if x not in ele:
                    u = True
                else:
                    u = False

        if u == True:
            print("True")
        else:
            print("False")

distinct()
















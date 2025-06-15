def combin(amnt, k):
    res1 = []

    def backtrack1(start, comb):
        if len(comb) == k:
            res1.append(comb.copy())
            return
        # (start,amnt-(k-len(comb))+1)
        for i in range(start,amnt-(k-len(comb))+1):
            comb.append(i)
            backtrack1(i + 1, comb)
            comb.pop()

    backtrack1(1, [])
    return res1

amnt = 10
k = 3
print(combin(amnt, k))







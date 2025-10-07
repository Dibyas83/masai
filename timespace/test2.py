def tricky_sum(n):
    co = 0
    for i in range(n):
        for j in range(i):
            co += 1
            print(co)
    return co

print(tricky_sum(100))
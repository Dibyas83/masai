def permutation(n,k):
    k =[3,2,1]
    l =len(k)
    ct = 0

    for i in range(l):
        times = n // k[i]
        if (n % k[i]) in k:
            ct += 1
            return k[i]*(times-1) + k








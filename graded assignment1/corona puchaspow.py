
cost = "k"
rupees_have = "M"
# price inc by doub,triple.... i

def solve(k,m):
    count = 1
    i = 1
    remaining = m
    while(i*k <= remaining):
        count += 1
        remaining -= i*k
        i += 1
    print(count)
    print(remaining)


solve(20,50)


















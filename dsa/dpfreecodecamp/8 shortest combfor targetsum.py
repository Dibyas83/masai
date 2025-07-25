
# 7,(5,3,4,7) = [3,4],[7]

"""
8,(2,3,5)
                            8

            6(2)            5(3)             3(5)

        4    3    1     3    2    0      1   0    -

    2   1  1  0       1  0   0

    0
"""
def bestsum(targ, arr):
    if targ == 0:
        return []
    if targ < 0:
        return None

    shortestcomb = None

    for num in arr:
        rem = targ - num
        remcomb = bestsum(rem, arr)
        if remcomb is not None:
            comb = remcomb + [num]
            if shortestcomb is None or len(comb) < len(shortestcomb):
                shortestcomb = comb

    return shortestcomb

print(bestsum(7, [5, 3, 4, 7]))
# [7]
# tc n**m * m, n**n
#------------------------------------memo

def memo_bestsum(targ, arr,memo):
    if targ in memo:
        return memo[targ]
    if targ == 0:
        return []
    if targ < 0:
        return None

    shortestcomb = None

    for num in arr:
        rem = targ - num
        remcomb = memo_bestsum(rem, arr,memo)
        if remcomb is not None:
            comb = remcomb + [num]
            if shortestcomb is None or len(comb) < len(shortestcomb):
                shortestcomb = comb

    memo[targ] = shortestcomb
    return shortestcomb
memo = {}
print(memo_bestsum(100, [5, 3, 4, 25],memo))
print(memo_bestsum(10, [5, 3, 4, 25],memo))
"""

[25, 25, 25, 25]
[5, 5]
"""
# tc n *m ** 2, n**2

















def ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return ways(n-1) + ways(n-2) + ways(n-3)

n = 10
print(ways(n))
"""

def ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return ways(n-1) + ways(n-2) + ways(n-3)


ans = ways(5)
print(ans)

"""






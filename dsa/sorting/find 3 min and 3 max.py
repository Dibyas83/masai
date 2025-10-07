
def solve(n,arr):
    if n == 0:
        return
    uniq_val = sorted(set(arr))
    if len(uniq_val) >= 3:
        min_val = uniq_val[:3]
        print(" ".join(map(str,min_val)))
        max_val = uniq_val[-1:-4:-1]
        # max_val = uniq_val[-3:]
        print(" ".join(map(str, max_val)))
    else:
        print("not possible")

n = int(input())
arr = list(map(int,input().split(" ")))
solve(n,arr)

"""
5
2 4 6 1 7
1 2 4
7 6 4
"""
"""
5
2 4 6 1 7
1 2 4
4 6 7
"""
